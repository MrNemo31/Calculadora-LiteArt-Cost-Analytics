"""Validação e cálculo reproduzíveis do estudo, sem alterar o fluxo do MVP."""

import csv
from datetime import date
from decimal import Decimal, InvalidOperation, localcontext
from numbers import Integral
from pathlib import Path

import pandas as pd

from calculadora import (
    calcular_consumo_cenario,
    calcular_custo_ia_cenario,
    converter_hipotese_consumo,
    formatar_moeda_br,
    validar_numero_nao_negativo,
)


PASTA = Path(__file__).resolve().parent
COLUNAS_HIPOTESES = (
    "usuarios_ativos", "respostas_por_usuario", "taxa_acerto",
    "proporcao_acertos_com_feedback", "tokens_entrada", "tokens_saida",
)
COLUNAS_CENARIOS = ("id_cenario", "cenario", *COLUNAS_HIPOTESES)
CAMPOS_FINANCEIROS = (
    "preco_entrada_por_milhao_usd", "preco_saida_por_milhao_usd", "brl_por_usd",
)
CAMPOS_DATAS = (
    "data_consulta_precos", "data_referencia_cambio", "data_consulta_cambio",
)
COLUNAS_CONDICOES = (
    "provedor", "modelo", "modalidade", *CAMPOS_FINANCEIROS,
    "fonte_modelo", "fonte_precos", "data_consulta_precos", "fonte_cambio",
    "data_referencia_cambio", "data_consulta_cambio",
)
COLUNAS_BASE_INDICADORES = (
    "id_cenario", "cenario", "usuarios_ativos", "custo_entrada_usd", "custo_saida_usd",
    "custo_ia_mensal_usd", "custo_ia_mensal_br",
)
COLUNAS_INDICADORES = (
    "participacao_entrada_percentual", "participacao_saida_percentual",
    "custo_ia_mensal_por_usuario_usd", "custo_ia_mensal_por_usuario_br",
)


def ler_csv_texto(caminho, colunas):
    """Lê texto UTF-8 (com ou sem BOM), sem inferência numérica ou perda de campos."""
    caminho = Path(caminho)
    try:
        with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
            leitor = csv.reader(arquivo, strict=True)
            cabecalho = next(leitor, None)
            if cabecalho is None:
                raise ValueError(f"{caminho}: arquivo vazio.")
            if cabecalho != list(colunas):
                ausentes = [c for c in colunas if c not in cabecalho]
                extras = [c for c in cabecalho if c not in colunas]
                raise ValueError(
                    f"{caminho}: colunas incorretas; ausentes={ausentes}; "
                    f"inesperadas={extras}. Confira também ordem e duplicidades."
                )
            registros = []
            for numero, valores in enumerate(leitor, start=1):
                if len(valores) != len(colunas):
                    raise ValueError(
                        f"{caminho}, registro {numero}: esperado(s) {len(colunas)} "
                        f"campos, recebido(s) {len(valores)}."
                    )
                registro = dict(zip(colunas, (v.strip() for v in valores), strict=True))
                for campo, texto in registro.items():
                    if not texto:
                        raise ValueError(
                            f"{caminho}, registro {numero}, campo '{campo}': obrigatório vazio."
                        )
                registros.append(registro)
    except (csv.Error, UnicodeError) as erro:
        raise ValueError(f"{caminho}: CSV inválido: {erro}") from erro
    if not registros:
        raise ValueError(f"{caminho}: arquivo sem registros de dados.")
    return registros


def ler_cenarios_estudo(caminho):
    """Valida esta edição com C01 a C13; conserva a ordem recebida e os nomes."""
    registros = ler_csv_texto(caminho, COLUNAS_CENARIOS)
    identificadores = set()
    combinacoes = set()
    cenarios = []
    for numero, registro in enumerate(registros, start=1):
        identificador = registro["id_cenario"]
        if identificador in identificadores:
            raise ValueError(
                f"{caminho}, registro {numero}, campo 'id_cenario': "
                f"identificador duplicado: {identificador}."
            )
        identificadores.add(identificador)
        hipoteses = {}
        for campo in COLUNAS_HIPOTESES:
            try:
                hipoteses[campo] = converter_hipotese_consumo(registro[campo], campo)
            except ValueError as erro:
                raise ValueError(
                    f"{caminho}, registro {numero}, campo '{campo}': {erro}"
                ) from erro
        combinacao = tuple(hipoteses.values())
        if combinacao in combinacoes:
            raise ValueError(f"{caminho}, registro {numero}: combinação de hipóteses duplicada.")
        combinacoes.add(combinacao)
        cenarios.append({
            "id_cenario": identificador, "cenario": registro["cenario"],
            "hipoteses_consumo": hipoteses,
        })
    esperados = {f"C{numero:02d}" for numero in range(1, 14)}
    if identificadores != esperados:
        raise ValueError(
            f"{caminho}, campo 'id_cenario': exija cobertura C01 a C13; "
            f"ausentes={sorted(esperados - identificadores)}; "
            f"inesperados={sorted(identificadores - esperados)}."
        )
    return cenarios


def ler_condicoes_fixas(caminho):
    """Converte somente tarifas e câmbio para Decimal; preserva as referências."""
    registros = ler_csv_texto(caminho, COLUNAS_CONDICOES)
    if len(registros) != 1:
        raise ValueError(f"{caminho}: informe exatamente uma linha de condições fixas.")
    condicoes = registros[0]
    for campo in CAMPOS_FINANCEIROS:
        try:
            valor = Decimal(condicoes[campo])
            validar_numero_nao_negativo(valor, campo, (Decimal,))
            if valor <= 0:
                raise ValueError("o valor deve ser estritamente positivo.")
        except (InvalidOperation, ValueError) as erro:
            raise ValueError(f"{caminho}, registro 1, campo '{campo}': {erro}") from erro
        condicoes[campo] = valor
    for campo in CAMPOS_DATAS:
        try:
            valor = date.fromisoformat(condicoes[campo])
            if valor.isoformat() != condicoes[campo]:
                raise ValueError("utilize AAAA-MM-DD.")
        except ValueError as erro:
            raise ValueError(
                f"{caminho}, registro 1, campo '{campo}': data ISO inválida (AAAA-MM-DD)."
            ) from erro
    return condicoes


def calcular_resultados(cenarios, condicoes):
    """Adapta os dados às duas funções do MVP, sem modificar os dicionários recebidos."""
    precos = {
        "entrada_por_milhao_usd": condicoes["preco_entrada_por_milhao_usd"],
        "saida_por_milhao_usd": condicoes["preco_saida_por_milhao_usd"],
    }
    cotacao = {"brl_por_usd": condicoes["brl_por_usd"]}
    resultados = []
    for cenario in cenarios:
        hipoteses = cenario["hipoteses_consumo"]
        consumo = calcular_consumo_cenario(hipoteses)
        custos = calcular_custo_ia_cenario(consumo, precos, cotacao)
        resultados.append({
            "id_cenario": cenario["id_cenario"], "cenario": cenario["cenario"],
            **hipoteses, **consumo, **custos, **condicoes,
        })
    return pd.DataFrame.from_records(resultados, coerce_float=False)


def _indexar_comparacoes(tabela, necessarios):
    """Indexa registros por ID e verifica o contrato necessário às comparações."""
    obrigatorias = {
        "id_cenario", *COLUNAS_HIPOTESES, *COLUNAS_CONDICOES, "custo_ia_mensal_br",
    }
    if not tabela.columns.is_unique:
        raise ValueError("Comparações: colunas duplicadas na tabela de resultados.")
    ausentes = obrigatorias - set(tabela.columns)
    if ausentes:
        raise ValueError(f"Comparações: colunas obrigatórias ausentes: {sorted(ausentes)}.")
    por_id = {}
    for registro in tabela.to_dict("records"):
        identificador = registro["id_cenario"]
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("Comparações: id_cenario deve ser um texto preenchido.")
        if identificador in por_id:
            raise ValueError(f"Comparações: identificador duplicado: {identificador}.")
        por_id[identificador] = registro
    ausentes = set(necessarios) - set(por_id)
    if ausentes:
        raise ValueError(f"Comparações: cenários necessários ausentes: {sorted(ausentes)}.")
    for identificador in necessarios:
        registro = por_id[identificador]
        validar_numero_nao_negativo(
            registro["custo_ia_mensal_br"], f"{identificador}: custo mensal BRL", (Decimal,),
        )
        for campo in CAMPOS_FINANCEIROS:
            validar_numero_nao_negativo(
                registro[campo], f"{identificador}: {campo}", (Decimal,),
            )
    return por_id


def _validar_par(cenario, referencia, campo_alterado):
    """Exige hipóteses fixas e condições idênticas; não compara nomes ou consumos derivados."""
    campos_fixos = (
        *(campo for campo in COLUNAS_HIPOTESES if campo != campo_alterado),
        *COLUNAS_CONDICOES,
    )
    divergentes = [campo for campo in campos_fixos if cenario[campo] != referencia[campo]]
    if divergentes:
        raise ValueError(
            f"{cenario['id_cenario']} contra {referencia['id_cenario']}: "
            f"cenários não comparáveis; campos divergentes: {', '.join(divergentes)}."
        )
    if cenario[campo_alterado] == referencia[campo_alterado]:
        raise ValueError(
            f"{cenario['id_cenario']} contra {referencia['id_cenario']}: "
            f"a hipótese '{campo_alterado}' deve ser diferente da referência."
        )


def comparar_politicas(tabela):
    """Redução de IA = referência menos política; percentual usa a referência da mesma escala."""
    pares = (
        ("C01", "C03"), ("C02", "C03"), ("C04", "C06"),
        ("C05", "C06"), ("C07", "C09"), ("C08", "C09"),
    )
    por_id = _indexar_comparacoes(tabela, {id_ for par in pares for id_ in par})
    comparacoes = []
    for id_cenario, id_referencia in pares:
        cenario, referencia = por_id[id_cenario], por_id[id_referencia]
        _validar_par(cenario, referencia, "proporcao_acertos_com_feedback")
        proporcao = cenario["proporcao_acertos_com_feedback"]
        validar_numero_nao_negativo(proporcao, f"{id_cenario}: proporção de acertos com feedback")
        if referencia["proporcao_acertos_com_feedback"] != 1 or proporcao > 1:
            raise ValueError(
                f"{id_cenario} contra {id_referencia}: a referência deve usar proporção 1 "
                "e a política deve estar entre 0 e 1."
            )
        custo_referencia = referencia["custo_ia_mensal_br"]
        reducao = custo_referencia - cenario["custo_ia_mensal_br"]
        # A divisão segue a precisão Decimal vigente; referência zero não tem percentual.
        percentual = None if custo_referencia == 0 else reducao / custo_referencia * Decimal("100")
        comparacoes.append({
            "id_cenario": id_cenario,
            "id_referencia": id_referencia,
            "usuarios_ativos": cenario["usuarios_ativos"],
            "proporcao_acertos_com_feedback": proporcao,
            "custo_politica_mensal_br": cenario["custo_ia_mensal_br"],
            "custo_referencia_mensal_br": custo_referencia,
            "reducao_mensal_br": reducao,
            "reducao_percentual": percentual,
            **{campo: referencia[campo] for campo in COLUNAS_CONDICOES},
        })
    return pd.DataFrame.from_records(comparacoes, coerce_float=False)


def analisar_sensibilidade(tabela):
    """Variação de IA = cenário menos C05; somente o token previsto pode mudar."""
    variacoes = (
        ("C10", "tokens_entrada"), ("C11", "tokens_entrada"),
        ("C12", "tokens_saida"), ("C13", "tokens_saida"),
    )
    por_id = _indexar_comparacoes(tabela, {"C05", *(id_ for id_, _ in variacoes)})
    referencia = por_id["C05"]
    custo_referencia = referencia["custo_ia_mensal_br"]
    comparacoes = []
    for id_cenario, campo_alterado in variacoes:
        cenario = por_id[id_cenario]
        _validar_par(cenario, referencia, campo_alterado)
        validar_numero_nao_negativo(cenario[campo_alterado], f"{id_cenario}: {campo_alterado}")
        variacao = cenario["custo_ia_mensal_br"] - custo_referencia
        percentual = None if custo_referencia == 0 else variacao / custo_referencia * Decimal("100")
        comparacoes.append({
            "id_cenario": id_cenario,
            "id_referencia": "C05",
            "campo_alterado": campo_alterado,
            "usuarios_ativos": cenario["usuarios_ativos"],
            "tokens_entrada_referencia": referencia["tokens_entrada"],
            "tokens_saida_referencia": referencia["tokens_saida"],
            "tokens_entrada_cenario": cenario["tokens_entrada"],
            "tokens_saida_cenario": cenario["tokens_saida"],
            "custo_referencia_mensal_br": custo_referencia,
            "custo_cenario_mensal_br": cenario["custo_ia_mensal_br"],
            "variacao_mensal_br": variacao,
            "variacao_percentual": percentual,
            **{campo: referencia[campo] for campo in COLUNAS_CONDICOES},
        })
    return pd.DataFrame.from_records(comparacoes, coerce_float=False)


def calcular_indicadores(tabela):
    """Deriva indicadores dos custos existentes, sem recalcular ou alterar a entrada."""
    if not tabela.columns.is_unique:
        raise ValueError("Indicadores: colunas duplicadas.")
    ausentes = set(COLUNAS_BASE_INDICADORES) - set(tabela.columns)
    if ausentes:
        raise ValueError(f"Indicadores: colunas obrigatórias ausentes: {sorted(ausentes)}.")
    if tabela.empty:
        raise ValueError("Indicadores: tabela sem cenários.")
    identificadores = set()
    resultados = []
    # Herda a precisão e o arredondamento atuais, sem alterar o contexto global ou seus flags.
    with localcontext():
        for registro in tabela[list(COLUNAS_BASE_INDICADORES)].to_dict("records"):
            id_ = registro["id_cenario"]
            if not isinstance(id_, str) or not id_.strip():
                raise ValueError("Indicadores: id_cenario deve ser um texto preenchido.")
            if id_ in identificadores:
                raise ValueError(f"Indicadores: identificador duplicado: {id_}.")
            identificadores.add(id_)
            nome = registro["cenario"]
            if not isinstance(nome, str) or not nome.strip():
                raise ValueError(f"{id_}: nome do cenário obrigatório.")
            usuarios = registro["usuarios_ativos"]
            if isinstance(usuarios, bool) or not isinstance(usuarios, Integral) or usuarios < 0:
                raise ValueError(f"{id_}: usuarios_ativos deve ser inteiro não negativo, sem booleano.")
            for campo in COLUNAS_BASE_INDICADORES[3:]:
                validar_numero_nao_negativo(registro[campo], f"{id_}: {campo}", (Decimal,))
            entrada = registro["custo_entrada_usd"]
            saida = registro["custo_saida_usd"]
            total_usd = registro["custo_ia_mensal_usd"]
            total_br = registro["custo_ia_mensal_br"]
            if entrada + saida != +total_usd:
                raise ValueError(f"{id_}: componentes e total mensal USD incoerentes na precisão vigente.")
            # As duas bases são independentes: total zero não implica usuários zero, ou vice-versa.
            usuarios_decimal = Decimal(int(usuarios))
            resultados.append({
                **registro,
                "participacao_entrada_percentual": None if total_usd == 0 else entrada / total_usd * Decimal("100"),
                "participacao_saida_percentual": None if total_usd == 0 else saida / total_usd * Decimal("100"),
                "custo_ia_mensal_por_usuario_usd": None if usuarios == 0 else total_usd / usuarios_decimal,
                "custo_ia_mensal_por_usuario_br": None if usuarios == 0 else total_br / usuarios_decimal,
            })
    return pd.DataFrame.from_records(resultados, coerce_float=False)


def apresentar_indicadores(indicadores):
    """Mostra participações e oito casas por usuário; não substitui os dados por textos."""
    def por_usuario(valor, moeda):
        if valor is None:
            return "Não aplicável"
        texto = f"{valor:,.8f}".translate(str.maketrans(",.", ".,"))
        return f"{moeda} {texto}"

    print("\nIndicadores — participações e custo de IA por usuário ativo/mês")
    exibicao = indicadores[["id_cenario", "usuarios_ativos", *COLUNAS_INDICADORES]].copy()
    formatos = {
        "participacao_entrada_percentual": formatar_percentual,
        "participacao_saida_percentual": formatar_percentual,
        "custo_ia_mensal_por_usuario_usd": lambda valor: por_usuario(valor, "US$"),
        "custo_ia_mensal_por_usuario_br": lambda valor: por_usuario(valor, "R$"),
    }
    # to_string pode ignorar formatadores para None; preparar esses textos só na cópia.
    for campo, formatador in formatos.items():
        exibicao[campo] = exibicao[campo].map(formatador)
    print(exibicao.to_string(
        index=False, na_rep="Não aplicável",
        header=["Cenário", "Usuários", "Entrada (%)", "Saída (%)",
                "USD/usuário ativo/mês", "BRL/usuário ativo/mês"],
    ))
    print("Somente IA; custo por usuário não comprova economia de escala ou viabilidade financeira.")


def formatar_percentual(valor):
    """Retorna texto com sinal; None significa percentual não aplicável, nunca zero."""
    if valor is None:
        return "Não aplicável"
    sinal = "+" if valor > 0 else ""
    return f"{sinal}{formatar_moeda_br(valor)}%"


def apresentar_comparacoes(politicas, sensibilidade):
    """Formata cópias de apresentação, sem arredondar os dados das comparações."""
    formatos = {
        campo: lambda valor: f"R$ {formatar_moeda_br(valor)}"
        for campo in (
            "custo_politica_mensal_br", "custo_referencia_mensal_br",
            "custo_cenario_mensal_br", "reducao_mensal_br", "variacao_mensal_br",
        )
    }
    formatos.update(reducao_percentual=formatar_percentual, variacao_percentual=formatar_percentual)
    print("\nPolíticas — redução do custo mensal de IA contra feedback em todas as respostas")
    print(politicas[[
        "id_cenario", "id_referencia", "usuarios_ativos", "proporcao_acertos_com_feedback",
        "custo_politica_mensal_br", "custo_referencia_mensal_br",
        "reducao_mensal_br", "reducao_percentual",
    ]].to_string(
        index=False, formatters=formatos, na_rep="Não aplicável",
        header=["Cenário", "Referência", "Usuários", "Proporção nos acertos",
                "IA/mês BRL", "Referência BRL", "Redução BRL", "Redução (%)"],
    ))
    print("Redução = referência menos política; percentual usa a referência da mesma escala.")
    print("\nTokens — variação do custo mensal de IA em relação a C05")
    print(sensibilidade[[
        "id_cenario", "id_referencia", "campo_alterado",
        "tokens_entrada_cenario", "tokens_saida_cenario", "custo_cenario_mensal_br",
        "variacao_mensal_br", "variacao_percentual",
    ]].to_string(
        index=False, formatters=formatos, na_rep="Não aplicável",
        header=["Cenário", "Referência", "Hipótese", "Entrada/feedback", "Saída/feedback",
                "IA/mês BRL", "Variação BRL", "Variação (%)"],
    ))
    print("Variação = cenário menos C05; sinal negativo indica redução e positivo indica aumento.")
    print("Referência zero: percentual não aplicável (campo vazio no CSV).")
    print("Relações das fórmulas sob hipóteses; não comprovam aprendizagem ou qualidade equivalente.")

def apresentar_resultados(tabela):
    """Formata apenas a apresentação; os valores da tabela continuam numéricos."""
    colunas = [
        "id_cenario", "usuarios_ativos", "feedbacks_mensais",
        "custo_ia_mensal_usd", "custo_ia_mensal_br",
    ]
    print("Estudo de caso — estimativas de IA sob hipóteses, tarifas e câmbio fixos")
    print(tabela[colunas].to_string(
        index=False, header=["Cenário", "Usuários", "Feedbacks/mês", "IA/mês USD", "IA/mês BRL"],
        formatters={
            "custo_ia_mensal_usd": lambda valor: f"US$ {formatar_moeda_br(valor)}",
            "custo_ia_mensal_br": lambda valor: f"R$ {formatar_moeda_br(valor)}",
        },
    ))
    print("Valores calculados por fórmulas; não são evidências empíricas sobre estudantes.")


def exportar_resultados(tabela, caminho):
    """Substitui o CSV com os valores completos, sem formatadores de exibição."""
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    tabela.to_csv(caminho, index=False, encoding="utf-8", sep=",", decimal=".")
    return caminho


def executar_estudo(
    caminho_cenarios=None, caminho_condicoes=None, caminho_saida=None,
    caminho_politicas=None, caminho_sensibilidade=None, caminho_indicadores=None,
):
    """Valida e compara tudo antes de exportar; aceita caminhos temporários nos testes."""
    entrada = PASTA / "dados" / "estudo_de_caso"
    cenarios = ler_cenarios_estudo(
        entrada / "cenarios.csv" if caminho_cenarios is None else caminho_cenarios
    )
    condicoes = ler_condicoes_fixas(
        entrada / "condicoes_fixas.csv" if caminho_condicoes is None else caminho_condicoes
    )
    tabela = calcular_resultados(cenarios, condicoes)
    politicas = comparar_politicas(tabela)
    sensibilidade = analisar_sensibilidade(tabela)
    indicadores = calcular_indicadores(tabela)
    destino = Path(
        PASTA / "resultados" / "estudo_de_caso" / "resultados_cenarios.csv"
        if caminho_saida is None else caminho_saida
    )
    destino_politicas = (
        destino.parent / "comparacao_politicas.csv"
        if caminho_politicas is None else Path(caminho_politicas)
    )
    destino_sensibilidade = (
        destino.parent / "sensibilidade_tokens.csv"
        if caminho_sensibilidade is None else Path(caminho_sensibilidade)
    )
    destino_indicadores = (
        destino.parent / "indicadores_cenarios.csv"
        if caminho_indicadores is None else Path(caminho_indicadores)
    )
    for dados, caminho in (
        (tabela, destino), (politicas, destino_politicas), (sensibilidade, destino_sensibilidade),
        (indicadores, destino_indicadores),
    ):
        exportar_resultados(dados, caminho)
    apresentar_resultados(tabela)
    apresentar_comparacoes(politicas, sensibilidade)
    apresentar_indicadores(indicadores)
    for caminho in (destino, destino_politicas, destino_sensibilidade, destino_indicadores):
        print(f"Arquivo salvo: {caminho}")
    return tabela

def main():
    try:
        executar_estudo()
    except (OSError, ValueError) as erro:
        raise SystemExit(f"Estudo não executado: {erro}") from erro


if __name__ == "__main__":
    main()
