"""Validação e cálculo reproduzíveis do estudo, sem alterar o fluxo do MVP."""

import csv
from datetime import date
from decimal import Decimal, InvalidOperation
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


def executar_estudo(caminho_cenarios=None, caminho_condicoes=None, caminho_saida=None):
    """Valida tudo e calcula antes de exportar; aceita caminhos temporários nos testes."""
    entrada = PASTA / "dados" / "estudo_de_caso"
    cenarios = ler_cenarios_estudo(
        entrada / "cenarios.csv" if caminho_cenarios is None else caminho_cenarios
    )
    condicoes = ler_condicoes_fixas(
        entrada / "condicoes_fixas.csv" if caminho_condicoes is None else caminho_condicoes
    )
    tabela = calcular_resultados(cenarios, condicoes)
    destino = exportar_resultados(
        tabela, PASTA / "resultados" / "estudo_de_caso" / "resultados_cenarios.csv"
        if caminho_saida is None else caminho_saida,
    )
    apresentar_resultados(tabela)
    print(f"Arquivo salvo: {destino}")
    return tabela


def main():
    try:
        executar_estudo()
    except (OSError, ValueError) as erro:
        raise SystemExit(f"Estudo não executado: {erro}") from erro


if __name__ == "__main__":
    main()
