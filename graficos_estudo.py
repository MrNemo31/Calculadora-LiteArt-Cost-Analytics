"""Gráficos do estudo a partir dos resultados existentes, sem executar a análise."""

import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from html import escape
from math import isfinite
from pathlib import Path

import pandas as pd
import plotly.express as px

from analise_estudo import (
    CAMPOS_DATAS, CAMPOS_FINANCEIROS, COLUNAS_CONDICOES, COLUNAS_HIPOTESES,
    ler_csv_texto,
)
from calculadora import formatar_moeda_br


PASTA = Path(__file__).resolve().parent
COLUNAS_CONSUMO = (
    "respostas_mensais", "acertos_mensais", "erros_mensais", "feedbacks_nos_acertos",
    "feedbacks_mensais", "tokens_entrada_total", "tokens_saida_total",
)
COLUNAS_CUSTOS = (
    "custo_entrada_usd", "custo_saida_usd", "custo_ia_mensal_usd", "custo_entrada_br",
    "custo_saida_br", "custo_ia_mensal_br", "custo_ia_anual_usd", "custo_ia_anual_br",
)
COLUNAS_RESULTADOS = (
    "id_cenario", "cenario", *COLUNAS_HIPOTESES, *COLUNAS_CONSUMO,
    *COLUNAS_CUSTOS, *COLUNAS_CONDICOES,
)
ESCALAS = ("100", "500", "1.000")
POLITICAS = ("Somente nos erros", "Erros + 25% dos acertos", "Todas as respostas")
PROPORCOES = (Decimal("0"), Decimal("0.25"), Decimal("1"))
COLUNAS_SENSIBILIDADE = (
    "id_cenario", "id_referencia", "campo_alterado", "usuarios_ativos",
    "tokens_entrada_referencia", "tokens_saida_referencia", "tokens_entrada_cenario",
    "tokens_saida_cenario", "custo_referencia_mensal_br", "custo_cenario_mensal_br",
    "variacao_mensal_br", "variacao_percentual", *COLUNAS_CONDICOES,
)


def _decimal(valor, identificador, campo, permitir_negativo=False):
    """Reconstrói Decimal de texto; rejeita floats para não esconder perda de precisão."""
    try:
        if not isinstance(valor, (str, Decimal)):
            raise ValueError("informe texto decimal ou Decimal, sem float intermediário.")
        numero = Decimal(valor)
        if not numero.is_finite():
            raise ValueError("informe número finito.")
        if not permitir_negativo and numero < 0:
            raise ValueError("informe número não negativo.")
    except (InvalidOperation, ValueError) as erro:
        raise ValueError(f"{identificador}, campo '{campo}': {erro}") from erro
    return numero


def validar_dados_grafico(dados):
    """Retorna cópia ordenada C01–C09, validando a matriz e condições desta edição."""
    if not dados.columns.is_unique:
        raise ValueError("Gráfico: colunas duplicadas.")
    ausentes = set(COLUNAS_RESULTADOS) - set(dados.columns)
    if ausentes:
        raise ValueError(f"Gráfico: colunas ausentes: {sorted(ausentes)}.")
    if dados["id_cenario"].duplicated().any():
        raise ValueError("Gráfico: identificador duplicado.")
    esperados = [f"C{i:02d}" for i in range(1, 10)]
    ausentes = set(esperados) - set(dados["id_cenario"])
    if ausentes:
        raise ValueError(f"Gráfico: identificadores ausentes: {sorted(ausentes)}.")
    selecionados = dados.set_index("id_cenario").loc[esperados].reset_index().copy(deep=True)
    registros = selecionados.to_dict("records")
    for posicao, registro in enumerate(registros):
        id_ = registro["id_cenario"]
        for campo in COLUNAS_RESULTADOS:
            valor = registro[campo]
            if valor is None or (isinstance(valor, str) and not valor.strip()):
                raise ValueError(f"{id_}, campo '{campo}': obrigatório vazio.")
        try:
            usuarios = int(registro["usuarios_ativos"])
            if isinstance(registro["usuarios_ativos"], (float, Decimal)):
                raise ValueError("use inteiro sem parte decimal.")
        except (ValueError, TypeError) as erro:
            raise ValueError(f"{id_}, campo 'usuarios_ativos': informe um inteiro.") from erro
        registro["usuarios_ativos"] = usuarios
        for campo in (*COLUNAS_HIPOTESES[1:], *COLUNAS_CONSUMO,
                      *COLUNAS_CUSTOS, *CAMPOS_FINANCEIROS):
            registro[campo] = _decimal(registro[campo], id_, campo)
        for campo in CAMPOS_FINANCEIROS:
            if registro[campo] <= 0:
                raise ValueError(f"{id_}, campo '{campo}': deve ser positivo neste estudo.")
        for campo in CAMPOS_DATAS:
            try:
                if date.fromisoformat(registro[campo]).isoformat() != registro[campo]:
                    raise ValueError("formato ISO obrigatório")
            except (TypeError, ValueError) as erro:
                raise ValueError(f"{id_}, campo '{campo}': data ISO inválida.") from erro
        esperado = (100, 500, 1000)[posicao // 3]
        hipoteses = (usuarios, registro["respostas_por_usuario"], registro["taxa_acerto"],
                     registro["proporcao_acertos_com_feedback"], registro["tokens_entrada"],
                     registro["tokens_saida"])
        if hipoteses != (esperado, Decimal("40"), Decimal("0.60"),
                         PROPORCOES[posicao % 3], Decimal("500"), Decimal("300")):
            raise ValueError(f"{id_}: hipóteses incompatíveis com a matriz principal do estudo.")
        if any(registro[c] != registros[0][c] for c in COLUNAS_CONDICOES):
            raise ValueError(f"{id_}: condições comerciais ou referências incompatíveis.")
    return pd.DataFrame.from_records(registros, coerce_float=False)


def ler_resultados_grafico(caminho):
    """Lê o CSV completo como texto, sem alterar o arquivo ou executar os cálculos."""
    try:
        registros = ler_csv_texto(caminho, COLUNAS_RESULTADOS)
        return validar_dados_grafico(pd.DataFrame.from_records(registros))
    except FileNotFoundError as erro:
        raise FileNotFoundError(
            f"Resultados não encontrados: {caminho}. Gere-os primeiro executando "
            "analise_estudo.py com o Python da .venv-win."
        ) from erro


def criar_figura(dados):
    """Cria barras agrupadas; somente a altura usa float em uma cópia de visualização."""
    visualizacao = validar_dados_grafico(dados)
    visualizacao["escala"] = [ESCALAS[i // 3] for i in range(9)]
    visualizacao["politica"] = [POLITICAS[i % 3] for i in range(9)]
    visualizacao["custo_texto"] = visualizacao["custo_ia_mensal_br"].map(
        lambda valor: f"R$ {formatar_moeda_br(valor)}"
    )
    visualizacao["feedbacks_texto"] = visualizacao["feedbacks_mensais"].map(
        lambda valor: format(valor, "f").rstrip("0").rstrip(".") if valor % 1
        else str(int(valor))
    )
    visualizacao["custo_grafico_br"] = visualizacao["custo_ia_mensal_br"].map(float)
    if not all(isfinite(v) for v in visualizacao["custo_grafico_br"]):
        raise ValueError("Custo fora da faixa representável no gráfico de ponto flutuante.")
    figura = px.bar(
        visualizacao, x="escala", y="custo_grafico_br", color="politica",
        pattern_shape="politica", barmode="group", text="custo_texto",
        category_orders={"escala": list(ESCALAS), "politica": list(POLITICAS)},
        color_discrete_sequence=["#0072B2", "#D55E00", "#009E73"],
        pattern_shape_sequence=["", "/", "."],
        custom_data=["id_cenario", "usuarios_ativos", "politica", "feedbacks_texto", "custo_texto"],
        labels={"escala": "Usuários ativos por mês", "custo_grafico_br": "Custo mensal estimado de IA (BRL)",
                "politica": "Política de feedback"},
        title="Custo mensal estimado de IA por escala e política de feedback",
    )
    figura.update_traces(
        textposition="outside", cliponaxis=False,
        hovertemplate=("<b>%{customdata[0]}</b><br>Usuários: %{customdata[1]}"
                       "<br>Política: %{customdata[2]}<br>Feedbacks/mês: %{customdata[3]}"
                       "<br>Custo mensal de IA: %{customdata[4]}<extra></extra>"),
    )
    condicoes = visualizacao.iloc[0]
    legenda_condicoes = (
        f"Cenários hipotéticos · {escape(condicoes['modelo'])} · {escape(condicoes['modalidade'])}"
        f" · tarifas e câmbio fixos<br>"
        f"Entrada: US$ {formatar_moeda_br(condicoes['preco_entrada_por_milhao_usd'])}/milhão"
        f" · saída: US$ {formatar_moeda_br(condicoes['preco_saida_por_milhao_usd'])}/milhão"
        f" · BRL/USD: {str(condicoes['brl_por_usd']).replace('.', ',')}"
    )
    figura.update_layout(
        template="plotly_white", height=650, separators=",.",
        title={"x": 0.04, "font": {"size": 21}},
        font={"family": "Arial, sans-serif", "size": 14},
        margin={"l": 90, "r": 35, "t": 160, "b": 130},
        legend={"orientation": "h", "y": -0.23, "x": 0, "title_text": "Política de feedback"},
        annotations=[{"text": legenda_condicoes, "xref": "paper", "yref": "paper",
                      "x": 0, "y": 1.19, "showarrow": False, "align": "left", "xanchor": "left",
                      "font": {"size": 13}}],
    )
    figura.update_xaxes(type="category", categoryorder="array", categoryarray=list(ESCALAS))
    maximo = max(visualizacao["custo_grafico_br"])
    figura.update_yaxes(range=[0, maximo * 1.20 if maximo else 1], tickprefix="R$ ", tickformat=",.2f")
    return figura


def exportar_html(figura, caminho):
    """Exporta HTML completo e offline, sem abrir navegador."""
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    figura.write_html(caminho, full_html=True, include_plotlyjs=True, auto_open=False)
    return caminho


def validar_sensibilidade_grafico(dados):
    """Valida a base comum C05 e retorna cópia C10–C13, sem inventar percentuais."""
    if not dados.columns.is_unique:
        raise ValueError("Sensibilidade: colunas duplicadas.")
    ausentes = set(COLUNAS_SENSIBILIDADE) - set(dados.columns)
    if ausentes:
        raise ValueError(f"Sensibilidade: colunas ausentes: {sorted(ausentes)}.")
    if dados["id_cenario"].duplicated().any():
        raise ValueError("Sensibilidade: identificador duplicado.")
    ids = ["C10", "C11", "C12", "C13"]
    if set(dados["id_cenario"]) != set(ids):
        raise ValueError("Sensibilidade: exija exatamente C10, C11, C12 e C13, sem identificadores ausentes.")
    registros = dados.set_index("id_cenario").loc[ids].reset_index().to_dict("records")
    numericos = (
        "tokens_entrada_referencia", "tokens_saida_referencia", "tokens_entrada_cenario",
        "tokens_saida_cenario", "custo_referencia_mensal_br", "custo_cenario_mensal_br",
        "variacao_mensal_br", "variacao_percentual", *CAMPOS_FINANCEIROS,
    )
    for posicao, registro in enumerate(registros):
        id_ = registro["id_cenario"]
        if registro["variacao_percentual"] is None or registro["variacao_percentual"] == "":
            raise ValueError(
                f"{id_}: percentual não aplicável; sem base válida para representar as quatro comparações."
            )
        for campo in COLUNAS_SENSIBILIDADE:
            valor = registro[campo]
            if valor is None or (isinstance(valor, str) and not valor.strip()):
                raise ValueError(f"{id_}, campo '{campo}': obrigatório vazio.")
        if registro["id_referencia"] != "C05":
            raise ValueError(f"{id_}: referência deve ser C05.")
        for campo in numericos:
            registro[campo] = _decimal(
                registro[campo], id_, campo,
                permitir_negativo=campo in ("variacao_mensal_br", "variacao_percentual"),
            )
        for campo in ("custo_referencia_mensal_br", *CAMPOS_FINANCEIROS):
            if registro[campo] <= 0:
                raise ValueError(f"{id_}, campo '{campo}': base deve ser positiva para o gráfico.")
        try:
            usuarios = registro["usuarios_ativos"]
            if isinstance(usuarios, (float, Decimal)) or int(usuarios) < 0:
                raise ValueError("inteiro não negativo obrigatório")
            registro["usuarios_ativos"] = int(usuarios)
        except (ValueError, TypeError) as erro:
            raise ValueError(f"{id_}, campo 'usuarios_ativos': inteiro inválido.") from erro
        for campo in CAMPOS_DATAS:
            try:
                if date.fromisoformat(registro[campo]).isoformat() != registro[campo]:
                    raise ValueError("formato ISO obrigatório")
            except (ValueError, TypeError) as erro:
                raise ValueError(f"{id_}, campo '{campo}': data ISO inválida.") from erro
        fixos = (
            "usuarios_ativos", "tokens_entrada_referencia", "tokens_saida_referencia",
            "custo_referencia_mensal_br", *COLUNAS_CONDICOES,
        )
        if any(registro[c] != registros[0][c] for c in fixos):
            raise ValueError(f"{id_}: condições, custo ou tokens da referência incompatíveis.")
        alterado = "tokens_entrada" if posicao < 2 else "tokens_saida"
        inalterado = "tokens_saida" if posicao < 2 else "tokens_entrada"
        if registro["campo_alterado"] != alterado:
            raise ValueError(f"{id_}: campo alterado deve ser {alterado}.")
        if registro[f"{inalterado}_cenario"] != registro[f"{inalterado}_referencia"]:
            raise ValueError(f"{id_}: {inalterado} deve permanecer igual à referência.")
        if registro[f"{alterado}_cenario"] == registro[f"{alterado}_referencia"]:
            raise ValueError(f"{id_}: {alterado} deve mudar em relação à referência.")
    return pd.DataFrame.from_records(registros, coerce_float=False)


def ler_sensibilidade_grafico(caminho):
    """Lê texto; percentual vazio é não aplicável e impede criar barras fictícias."""
    caminho = Path(caminho)
    try:
        with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
            leitor = csv.reader(arquivo, strict=True)
            if next(leitor, None) != list(COLUNAS_SENSIBILIDADE):
                raise ValueError(f"{caminho}: cabeçalho da sensibilidade incorreto.")
            registros = []
            for numero, valores in enumerate(leitor, 1):
                if len(valores) != len(COLUNAS_SENSIBILIDADE):
                    raise ValueError(f"{caminho}, registro {numero}: quantidade incorreta de campos.")
                registros.append(dict(zip(COLUNAS_SENSIBILIDADE, (v.strip() for v in valores), strict=True)))
    except FileNotFoundError as erro:
        raise FileNotFoundError(f"{caminho}: gere os resultados primeiro com analise_estudo.py.") from erro
    except (csv.Error, UnicodeError) as erro:
        raise ValueError(f"{caminho}: CSV inválido: {erro}") from erro
    if not registros:
        raise ValueError(f"{caminho}: sensibilidade sem registros.")
    return validar_sensibilidade_grafico(pd.DataFrame.from_records(registros))


def _texto_tokens(valor):
    """Quantidade sem símbolo monetário, com agrupamento brasileiro e fração preservada."""
    inteiro, _, fracao = format(valor, ",f").partition(".")
    fracao = fracao.rstrip("0")
    return inteiro.replace(",", ".") + ("," + fracao if fracao else "")


def criar_figura_sensibilidade(dados):
    """Retorna quatro barras horizontais; só as coordenadas da cópia usam float."""
    visualizacao = validar_sensibilidade_grafico(dados)
    rotulos, percentuais = [], []
    for registro in visualizacao.to_dict("records"):
        campo = registro["campo_alterado"]
        nome = "Entrada" if campo == "tokens_entrada" else "Saída"
        antes = _texto_tokens(registro[f"{campo}_referencia"])
        depois = _texto_tokens(registro[f"{campo}_cenario"])
        rotulos.append(f"{registro['id_cenario']} — {nome}: {antes} → {depois} tokens")
        # Os dados já são percentuais: não multiplicar por 100 outra vez.
        percentuais.append(f"{registro['variacao_percentual']:+.1f}%".replace(".", ","))
    visualizacao["rotulo"] = rotulos
    visualizacao["percentual_texto"] = percentuais
    visualizacao["variacao_grafica"] = visualizacao["variacao_percentual"].map(float)
    if not all(isfinite(v) for v in visualizacao["variacao_grafica"]):
        raise ValueError("Percentual fora da faixa representável no gráfico de ponto flutuante.")
    visualizacao["direcao"] = visualizacao["variacao_percentual"].map(
        lambda valor: "Redução" if valor < 0 else "Aumento" if valor > 0 else "Sem variação"
    )
    for campo in ("custo_referencia_mensal_br", "custo_cenario_mensal_br", "variacao_mensal_br"):
        visualizacao[f"{campo}_texto"] = visualizacao[campo].map(
            lambda valor: f"R$ {formatar_moeda_br(valor)}"
        )
    for campo in ("tokens_entrada_referencia", "tokens_saida_referencia",
                  "tokens_entrada_cenario", "tokens_saida_cenario"):
        visualizacao[f"{campo}_texto"] = visualizacao[campo].map(_texto_tokens)
    figura = px.bar(
        visualizacao, x="variacao_grafica", y="rotulo", orientation="h", color="direcao",
        text="percentual_texto", category_orders={"rotulo": rotulos},
        color_discrete_map={"Redução": "#0072B2", "Aumento": "#D55E00", "Sem variação": "#666666"},
        custom_data=[
            "id_cenario", "id_referencia", "campo_alterado", "tokens_entrada_referencia_texto",
            "tokens_saida_referencia_texto", "tokens_entrada_cenario_texto", "tokens_saida_cenario_texto",
            "custo_referencia_mensal_br_texto", "custo_cenario_mensal_br_texto",
            "variacao_mensal_br_texto", "percentual_texto",
        ],
        labels={"variacao_grafica": "Variação do custo mensal de IA contra C05 (%)", "rotulo": "", "direcao": "Efeito"},
        title="Sensibilidade do custo mensal de IA em relação a C05",
    )
    figura.update_traces(
        textposition="outside", cliponaxis=False,
        hovertemplate=("<b>%{customdata[0]} contra %{customdata[1]}</b>"
                       "<br>Campo alterado: %{customdata[2]}"
                       "<br>Entrada/feedback: %{customdata[3]} → %{customdata[5]} tokens"
                       "<br>Saída/feedback: %{customdata[4]} → %{customdata[6]} tokens"
                       "<br>Referência mensal: %{customdata[7]}<br>Cenário mensal: %{customdata[8]}"
                       "<br>Diferença mensal: %{customdata[9]}<br>Variação: %{customdata[10]}<extra></extra>"),
    )
    limite = max(1, max(abs(v) for v in visualizacao["variacao_grafica"]) * 1.25)
    figura.update_xaxes(type="linear", range=[-limite, limite], ticksuffix="%", tickformat="+.1f")
    figura.update_yaxes(type="category", categoryorder="array", categoryarray=rotulos, autorange="reversed")
    figura.add_vline(x=0, line_width=2, line_color="#333333")
    custo_base = formatar_moeda_br(visualizacao.iloc[0]["custo_referencia_mensal_br"])
    figura.update_layout(
        template="plotly_white", height=600, separators=",.",
        title={"x": 0.03, "font": {"size": 21}}, font={"family": "Arial, sans-serif", "size": 14},
        margin={"l": 340, "r": 70, "t": 140, "b": 115},
        legend={"orientation": "h", "y": -0.20, "x": 0},
        annotations=[{"text": f"Referência C05: R$ {custo_base}/mês · hipóteses, tarifas e câmbio fixos"
                      "<br>Estimativas; sem comprovação de qualidade pedagógica equivalente.",
                      "xref": "paper", "yref": "paper", "x": 0, "y": 1.16, "xanchor": "left",
                      "showarrow": False, "align": "left", "font": {"size": 13}}],
    )
    return figura


def executar_grafico(caminho_entrada=None, caminho_saida=None,
                     caminho_sensibilidade=None, caminho_saida_sensibilidade=None):
    pasta = PASTA / "resultados" / "estudo_de_caso"
    entrada = pasta / "resultados_cenarios.csv" if caminho_entrada is None else caminho_entrada
    saida = pasta / "custo_mensal_por_escala_politica.html" if caminho_saida is None else caminho_saida
    dados = ler_resultados_grafico(entrada)
    figura = criar_figura(dados)
    entrada_sensibilidade = (
        Path(entrada).parent / "sensibilidade_tokens.csv"
        if caminho_sensibilidade is None else caminho_sensibilidade
    )
    saida_sensibilidade = (
        Path(saida).parent / "sensibilidade_tokens.html"
        if caminho_saida_sensibilidade is None else caminho_saida_sensibilidade
    )
    sensibilidade = ler_sensibilidade_grafico(entrada_sensibilidade)
    figura_sensibilidade = criar_figura_sensibilidade(sensibilidade)
    # Nenhuma gravação começa antes de ambas as entradas e figuras estarem válidas.
    destino = exportar_html(figura, saida)
    destino_sensibilidade = exportar_html(figura_sensibilidade, saida_sensibilidade)
    print(f"Gráfico salvo: {destino}")
    print(f"Gráfico salvo: {destino_sensibilidade}")
    print("Para visualizar, abra o HTML manualmente no navegador; ele funciona offline.")
    return figura


if __name__ == "__main__":
    try:
        executar_grafico()
    except (OSError, ValueError) as erro:
        raise SystemExit(f"Gráfico não gerado: {erro}") from erro
