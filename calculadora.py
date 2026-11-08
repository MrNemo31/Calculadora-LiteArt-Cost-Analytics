from decimal import Decimal
from math import isfinite
from pathlib import Path
from warnings import catch_warnings, simplefilter

import pandas as pd

#Funções auxuliares de validação
def validar_numero_nao_negativo(valor, nome, tipos_permitidos=(int, float)):
    """Valida o tipo permitido, valor finito e não negativo; não converte o valor."""
    if type(valor) not in tipos_permitidos:
        raise TypeError(f"{nome}: tipo não permitido para este campo.")

    if type(valor) is float and not isfinite(valor):
        raise ValueError(f"{nome}: informe um número finito (sem infinito ou NaN).")

    if type(valor) is Decimal and not valor.is_finite():
        raise ValueError(f"{nome}: informe um número finito (sem infinito ou NaN).")

    if valor < 0:
        raise ValueError(f"{nome}: o valor não pode ser negativo.")


# Funções de cálculo de consumo e custo de IA

def calcular_respostas_mensais(usuarios_ativos, respostas_por_usuario):
    """Recebe usuários int e média int ou float finita, ambos não negativos."""
    if type(usuarios_ativos) is not int:
        raise TypeError("A quantidade de usuários deve ser um número inteiro (int).")

    validar_numero_nao_negativo(usuarios_ativos, "Quantidade de usuários")
    validar_numero_nao_negativo(respostas_por_usuario, "Média de respostas por usuário")

    return usuarios_ativos * respostas_por_usuario


def calcular_feedbacks_mensais(respostas_mensais, taxa_acerto, proporcao_acertos_com_feedback):
    """Recebe int ou float; respostas finitas e não negativas e taxas entre 0 e 1."""
    validar_numero_nao_negativo(respostas_mensais, "Respostas mensais")
    validar_numero_nao_negativo(taxa_acerto, "Taxa de acerto")
    validar_numero_nao_negativo(proporcao_acertos_com_feedback, "Proporção dos acertos com feedback")

    if taxa_acerto > 1:
        raise ValueError("A taxa de acerto deve estar entre 0 e 1.")

    if proporcao_acertos_com_feedback > 1:
        raise ValueError("A proporção dos acertos com feedback deve estar entre 0 e 1.")

    acertos_mensais = respostas_mensais * taxa_acerto
    erros_mensais = respostas_mensais - acertos_mensais
    feedbacks_nos_acertos = acertos_mensais * proporcao_acertos_com_feedback
    feedbacks_mensais = erros_mensais + feedbacks_nos_acertos
    return acertos_mensais, erros_mensais, feedbacks_nos_acertos, feedbacks_mensais


def calcular_custo_tokens(tokens_total, preco_por_milhao_usd):
    """Recebe tokens int ou float e preço Decimal, finitos e não negativos."""
    validar_numero_nao_negativo(tokens_total, "Total de tokens")
    validar_numero_nao_negativo(preco_por_milhao_usd, "Preço por milhão de tokens", (Decimal,))

    tokens_decimal = Decimal(str(tokens_total))
    return tokens_decimal / 1_000_000 * preco_por_milhao_usd


def calcular_tokens_mensais(tokens_entrada, tokens_saida, feedbacks_mensais):
    """Retorna os tokens mensais; recebe int ou float finitos e não negativos."""
    validar_numero_nao_negativo(tokens_entrada, "Tokens de entrada por feedback")
    validar_numero_nao_negativo(tokens_saida, "Tokens de saída por feedback")
    validar_numero_nao_negativo(feedbacks_mensais, "Feedbacks mensais")

    tokens_entrada_total = tokens_entrada * feedbacks_mensais
    tokens_saida_total = tokens_saida * feedbacks_mensais
    return tokens_entrada_total, tokens_saida_total


def calcular_real(custo_usd, taxa_cambio):
    """Converte custo Decimal não negativo com cotação numérica finita e positiva."""
    validar_numero_nao_negativo(custo_usd, "Custo em dólares", (Decimal,))
    validar_numero_nao_negativo(taxa_cambio, "Cotação", (int, float, Decimal))

    if taxa_cambio <= 0:
        raise ValueError("A cotação deve ser maior que zero.")

    return custo_usd * Decimal(str(taxa_cambio))


def calcular_custo_anual(custo_mensal):
    """Projeta 12 meses constantes a partir de um custo Decimal finito e não negativo."""
    validar_numero_nao_negativo(custo_mensal, "Custo mensal", (Decimal,))
    return custo_mensal * Decimal("12")


def calcular_custo_servico(preco_mensal_por_unidade, quantidade):
    """Calcula a mensalidade na moeda do preço; recebe Decimal e quantidade int."""
    validar_numero_nao_negativo(preco_mensal_por_unidade, "Preço mensal por unidade", (Decimal,))

    if type(quantidade) is not int:
        raise TypeError("A quantidade de unidades deve ser um número inteiro (int).")

    validar_numero_nao_negativo(quantidade, "Quantidade de unidades")
    return preco_mensal_por_unidade * quantidade


def calcular_consumo_cenario(hipoteses_consumo):
    """Recebe as seis hipóteses e retorna o consumo estimado sem alterar a entrada."""
    if type(hipoteses_consumo) is not dict:
        raise TypeError("As hipóteses de consumo devem ser um dicionário (dict).")

    chaves_obrigatorias = (
        "usuarios_ativos",
        "respostas_por_usuario",
        "taxa_acerto",
        "proporcao_acertos_com_feedback",
        "tokens_entrada",
        "tokens_saida",
    )
    for chave in chaves_obrigatorias:
        if chave not in hipoteses_consumo:
            raise ValueError(f"Hipóteses de consumo: chave obrigatória ausente: {chave}.")

    respostas_mensais = calcular_respostas_mensais(
        hipoteses_consumo["usuarios_ativos"],
        hipoteses_consumo["respostas_por_usuario"],
    )
    acertos_mensais, erros_mensais, feedbacks_nos_acertos, feedbacks_mensais = calcular_feedbacks_mensais(
        respostas_mensais,
        hipoteses_consumo["taxa_acerto"],
        hipoteses_consumo["proporcao_acertos_com_feedback"],
    )
    tokens_entrada_total, tokens_saida_total = calcular_tokens_mensais(
        hipoteses_consumo["tokens_entrada"],
        hipoteses_consumo["tokens_saida"],
        feedbacks_mensais,
    )

    return {
        "respostas_mensais": respostas_mensais,
        "acertos_mensais": acertos_mensais,
        "erros_mensais": erros_mensais,
        "feedbacks_nos_acertos": feedbacks_nos_acertos,
        "feedbacks_mensais": feedbacks_mensais,
        "tokens_entrada_total": tokens_entrada_total,
        "tokens_saida_total": tokens_saida_total,
    }


def calcular_custo_ia_cenario(consumo_cenario, precos_ia, cotacao):
    """Retorna os custos de IA em Decimal, sem alterar os três dicionários."""
    if type(consumo_cenario) is not dict:
        raise TypeError("O consumo do cenário deve ser um dicionário (dict).")
    if type(precos_ia) is not dict:
        raise TypeError("Os preços de IA devem ser um dicionário (dict).")
    if type(cotacao) is not dict:
        raise TypeError("A cotação deve ser um dicionário (dict).")

    for chave in ("tokens_entrada_total", "tokens_saida_total"):
        if chave not in consumo_cenario:
            raise ValueError(f"Consumo do cenário: chave obrigatória ausente: {chave}.")
    for chave in ("entrada_por_milhao_usd", "saida_por_milhao_usd"):
        if chave not in precos_ia:
            raise ValueError(f"Preços de IA: chave obrigatória ausente: {chave}.")
    if "brl_por_usd" not in cotacao:
        raise ValueError("Cotação: chave obrigatória ausente: brl_por_usd.")

    custo_entrada_usd = calcular_custo_tokens(
        consumo_cenario["tokens_entrada_total"], precos_ia["entrada_por_milhao_usd"]
    )
    custo_saida_usd = calcular_custo_tokens(
        consumo_cenario["tokens_saida_total"], precos_ia["saida_por_milhao_usd"]
    )
    custo_ia_mensal_usd = custo_entrada_usd + custo_saida_usd

    custo_entrada_br = calcular_real(custo_entrada_usd, cotacao["brl_por_usd"])
    custo_saida_br = calcular_real(custo_saida_usd, cotacao["brl_por_usd"])
    custo_ia_mensal_br = calcular_real(custo_ia_mensal_usd, cotacao["brl_por_usd"])

    custo_ia_anual_usd = calcular_custo_anual(custo_ia_mensal_usd)
    custo_ia_anual_br = calcular_custo_anual(custo_ia_mensal_br)

    return {
        "custo_entrada_usd": custo_entrada_usd,
        "custo_saida_usd": custo_saida_usd,
        "custo_ia_mensal_usd": custo_ia_mensal_usd,
        "custo_entrada_br": custo_entrada_br,
        "custo_saida_br": custo_saida_br,
        "custo_ia_mensal_br": custo_ia_mensal_br,
        "custo_ia_anual_usd": custo_ia_anual_usd,
        "custo_ia_anual_br": custo_ia_anual_br,
    }


def calcular_custo_infra_cenario(precos_infraestrutura, hipoteses_capacidade, cotacao):
    """Retorna os custos fixos em Decimal, sem alterar os três dicionários."""
    if type(precos_infraestrutura) is not dict:
        raise TypeError("Os preços de infraestrutura devem ser um dicionário (dict).")
    if type(hipoteses_capacidade) is not dict:
        raise TypeError("As hipóteses de capacidade devem ser um dicionário (dict).")
    if type(cotacao) is not dict:
        raise TypeError("A cotação deve ser um dicionário (dict).")

    for chave in ("backend_mensal_por_unidade_usd", "banco_mensal_por_unidade_usd"):
        if chave not in precos_infraestrutura:
            raise ValueError(f"Preços de infraestrutura: chave obrigatória ausente: {chave}.")
    for chave in ("quantidade_backend", "quantidade_banco"):
        if chave not in hipoteses_capacidade:
            raise ValueError(f"Hipóteses de capacidade: chave obrigatória ausente: {chave}.")
    if "brl_por_usd" not in cotacao:
        raise ValueError("Cotação: chave obrigatória ausente: brl_por_usd.")

    custo_backend_mensal_usd = calcular_custo_servico(
        precos_infraestrutura["backend_mensal_por_unidade_usd"],
        hipoteses_capacidade["quantidade_backend"],
    )
    custo_banco_mensal_usd = calcular_custo_servico(
        precos_infraestrutura["banco_mensal_por_unidade_usd"],
        hipoteses_capacidade["quantidade_banco"],
    )
    custo_infra_mensal_usd = custo_backend_mensal_usd + custo_banco_mensal_usd

    custo_backend_mensal_br = calcular_real(custo_backend_mensal_usd, cotacao["brl_por_usd"])
    custo_banco_mensal_br = calcular_real(custo_banco_mensal_usd, cotacao["brl_por_usd"])
    custo_infra_mensal_br = calcular_real(custo_infra_mensal_usd, cotacao["brl_por_usd"])
    custo_infra_anual_usd = calcular_custo_anual(custo_infra_mensal_usd)
    custo_infra_anual_br = calcular_custo_anual(custo_infra_mensal_br)

    return {
        "custo_backend_mensal_usd": custo_backend_mensal_usd,
        "custo_banco_mensal_usd": custo_banco_mensal_usd,
        "custo_infra_mensal_usd": custo_infra_mensal_usd,
        "custo_backend_mensal_br": custo_backend_mensal_br,
        "custo_banco_mensal_br": custo_banco_mensal_br,
        "custo_infra_mensal_br": custo_infra_mensal_br,
        "custo_infra_anual_usd": custo_infra_anual_usd,
        "custo_infra_anual_br": custo_infra_anual_br,
    }


def calcular_cenario(
    hipoteses_consumo, hipoteses_capacidade, precos_ia, precos_infraestrutura, cotacao
):
    """Calcula consumo, IA, infraestrutura e totais, sem alterar as entradas."""
    consumo = calcular_consumo_cenario(hipoteses_consumo)
    custos_ia = calcular_custo_ia_cenario(consumo, precos_ia, cotacao)
    custos_infraestrutura = calcular_custo_infra_cenario(
        precos_infraestrutura, hipoteses_capacidade, cotacao
    )

    custo_total_mensal_usd = (
        custos_ia["custo_ia_mensal_usd"] + custos_infraestrutura["custo_infra_mensal_usd"]
    )
    custo_total_mensal_br = (
        custos_ia["custo_ia_mensal_br"] + custos_infraestrutura["custo_infra_mensal_br"]
    )

    return {
        "consumo": consumo,
        "custos_ia": custos_ia,
        "custos_infraestrutura": custos_infraestrutura,
        "totais": {
            "custo_total_mensal_usd": custo_total_mensal_usd,
            "custo_total_mensal_br": custo_total_mensal_br,
            "custo_total_anual_usd": calcular_custo_anual(custo_total_mensal_usd),
            "custo_total_anual_br": calcular_custo_anual(custo_total_mensal_br),
        },
    }


def formatar_moeda_br(valor):
    """Retorna texto com milhares, vírgula decimal e duas casas, sem alterar o Decimal."""
    texto = f"{valor:,.2f}"
    return texto.translate(str.maketrans(",.", ".,"))


def converter_hipotese_consumo(texto, coluna):
    """Converte uma hipótese textual e valida as regras compartilhadas das entradas."""
    if not texto:
        raise ValueError("Campo obrigatório vazio. Digite um valor.")
    try:
        valor = int(texto) if coluna == "usuarios_ativos" else float(texto)
    except ValueError as erro:
        formato = (
            "um inteiro sem parte decimal (ex.: 100)" if coluna == "usuarios_ativos"
            else "um número com ponto decimal, sem separadores de milhares (ex.: 40.5)"
        )
        raise ValueError(f"Informe {formato}.") from erro

    validar_numero_nao_negativo(valor, coluna)
    if coluna in ("taxa_acerto", "proporcao_acertos_com_feedback") and valor > 1:
        raise ValueError("A taxa deve estar entre 0 e 1, inclusive. Use 0.60 para 60%.")
    return valor


def ler_cenario_terminal():
    """Solicita um cenário, repetindo somente entradas inválidas."""
    print("Use ponto decimal para frações (ex.: 40.5), sem separadores de milhares.")
    print("As taxas são proporções entre 0 e 1: 0.60 corresponde a 60%.")
    while True:
        nome = input("Nome do cenário (ex.: Turma de revisão): ").strip()
        if nome:
            break
        print("O nome do cenário é obrigatório. Digite um nome antes de continuar.")

    perguntas = (
        ("usuarios_ativos", "Usuários ativos (inteiro, usuários/mês; ex.: 100): "),
        ("respostas_por_usuario", "Respostas por usuário (respostas/usuário/mês; ex.: 40): "),
        ("taxa_acerto", "Taxa de acerto (proporção de 0 a 1; ex.: 0.60): "),
        ("proporcao_acertos_com_feedback", "Acertos com feedback (proporção de 0 a 1; ex.: 0.25): "),
        ("tokens_entrada", "Tokens de entrada (média de tokens/feedback; ex.: 500): "),
        ("tokens_saida", "Tokens de saída faturáveis (média de tokens/feedback; ex.: 300): "),
    )
    hipoteses = {}
    for coluna, pergunta in perguntas:
        while True:
            texto = input(pergunta).strip()
            try:
                valor = converter_hipotese_consumo(texto, coluna)
            except ValueError as erro:
                print(f"Corrija {coluna}: {erro}")
            else:
                hipoteses[coluna] = valor
                break
    return {"nome": nome, "hipoteses_consumo": hipoteses}


def ler_cenarios_csv(caminho):
    """Lê hipóteses de consumo em UTF-8, sem executar os cenários."""
    colunas = (
        "cenario", "usuarios_ativos", "respostas_por_usuario", "taxa_acerto",
        "proporcao_acertos_com_feedback", "tokens_entrada", "tokens_saida",
    )
    try:
        # Não permitir que campos extras sejam descartados ou usados como índice.
        with catch_warnings():
            simplefilter("error", pd.errors.ParserWarning)
            tabela = pd.read_csv(
                caminho, dtype=str, keep_default_na=False, encoding="utf-8-sig",
                sep=",", index_col=False, on_bad_lines="error", skip_blank_lines=False,
            )
    except pd.errors.EmptyDataError as erro:
        raise ValueError("CSV vazio: informe o cabeçalho e pelo menos um cenário.") from erro
    except (pd.errors.ParserError, pd.errors.ParserWarning) as erro:
        raise ValueError(f"CSV malformado: {erro}") from erro

    ausentes = [coluna for coluna in colunas if coluna not in tabela.columns]
    inesperadas = [coluna for coluna in tabela.columns if coluna not in colunas]
    if ausentes or inesperadas:
        raise ValueError(
            f"Colunas incorretas: ausentes={ausentes}; inesperadas={inesperadas}."
        )
    if tabela.empty:
        raise ValueError("CSV sem registros de dados: informe pelo menos um cenário.")

    cenarios = []
    for numero, registro in enumerate(tabela.to_dict(orient="records"), start=1):
        valores = {}
        for coluna in colunas:
            texto = registro[coluna]
            if not isinstance(texto, str) or not texto.strip():
                raise ValueError(f"Registro {numero}, coluna '{coluna}': campo obrigatório vazio.")
            texto = texto.strip()
            if coluna == "cenario":
                valores[coluna] = texto
                continue
            try:
                valor = converter_hipotese_consumo(texto, coluna)
            except ValueError as erro:
                raise ValueError(f"Registro {numero}, coluna '{coluna}': {erro}") from erro
            valores[coluna] = valor
        cenarios.append({
            "nome": valores["cenario"],
            "hipoteses_consumo": {coluna: valores[coluna] for coluna in colunas[1:]},
        })
    return cenarios


if __name__ == "__main__":
    try:
        while True:
            print("\nComo deseja informar os cenários?")
            print("1 — Importar dados/cenarios_exemplo.csv.")
            print("2 — Preencher um único cenário pelo terminal.")
            opcao = input("Digite 1 ou 2: ").strip()
            if opcao in ("1", "2"):
                break
            print("Opção inválida. Digite 1 para importar o CSV ou 2 para preencher pelo terminal.")

        if opcao == "1":
            caminho_cenarios = Path(__file__).resolve().parent / "dados" / "cenarios_exemplo.csv"
            try:
                # Validar o arquivo inteiro antes de calcular ou escrever resultados.
                cenarios_didaticos = ler_cenarios_csv(caminho_cenarios)
            except (OSError, ValueError) as erro:
                raise SystemExit(f"Erro ao ler cenários de '{caminho_cenarios}': {erro}") from erro
        else:
            cenarios_didaticos = [ler_cenario_terminal()]
    except (KeyboardInterrupt, EOFError) as erro:
        raise SystemExit("\nEntrada cancelada. Nenhum resultado foi gerado ou sobrescrito.") from erro

    # Cotação didática em reais por dólar, não uma cotação pesquisada.
    cotacao = {
        "brl_por_usd": Decimal("5.00"),
    }

    # Preços pesquisados: GPT-6 Luna, Standard, entrada sem cache.
    # Fonte: https://developers.openai.com/api/docs/models/gpt-6-luna
    # Consulta: 2026-10-23. Sem adicionais regionais, ferramentas ou cache.
    precos_ia = {
        "entrada_por_milhao_usd": Decimal("0.10"),
        "saida_por_milhao_usd": Decimal("0.50"),
    }

    resumos_cenarios = []
    for cenario in cenarios_didaticos:
        consumo = calcular_consumo_cenario(cenario["hipoteses_consumo"])
        custos_ia = calcular_custo_ia_cenario(consumo, precos_ia, cotacao)
        resumos_cenarios.append({
            "cenario": cenario["nome"],
            "usuarios_ativos": cenario["hipoteses_consumo"]["usuarios_ativos"],
            "feedbacks_mensais": consumo["feedbacks_mensais"],
            "tokens_entrada_total": consumo["tokens_entrada_total"],
            "tokens_saida_total": consumo["tokens_saida_total"],
            "custo_ia_mensal_usd": custos_ia["custo_ia_mensal_usd"],
            "custo_ia_mensal_br": custos_ia["custo_ia_mensal_br"],
            "custo_ia_anual_usd": custos_ia["custo_ia_anual_usd"],
            "custo_ia_anual_br": custos_ia["custo_ia_anual_br"],
        })

    tabela_cenarios = pd.DataFrame.from_records(resumos_cenarios, coerce_float=False)
    formatadores_monetarios = {
        "custo_ia_mensal_usd": lambda valor: f"US$ {formatar_moeda_br(valor)}",
        "custo_ia_mensal_br": lambda valor: f"R$ {formatar_moeda_br(valor)}",
        "custo_ia_anual_usd": lambda valor: f"US$ {formatar_moeda_br(valor)}",
        "custo_ia_anual_br": lambda valor: f"R$ {formatar_moeda_br(valor)}",
    }
    titulos_colunas = [
        "Cenário", "Usuários ativos", "Feedbacks/mês", "Tokens entrada/mês", "Tokens saída/mês",
        "IA mensal (USD)", "IA mensal (BRL)", "IA anual (USD)", "IA anual (BRL)",
    ]

    print("\nEstimativa de custos de IA")
    print("Modelo de referência: GPT-6 Luna (gpt-6-luna)")
    print(f"Entrada sem cache: US$ {formatar_moeda_br(precos_ia['entrada_por_milhao_usd'])} por milhão de tokens")
    print(f"Saída faturável: US$ {formatar_moeda_br(precos_ia['saida_por_milhao_usd'])} por milhão de tokens")
    print(f"Cotação utilizada: R$ {formatar_moeda_br(cotacao['brl_por_usd'])} por US$ 1,00 (didática)")
    print("Estimativas baseadas nas hipóteses informadas; não representam despesas medidas.")
    print("Infraestrutura e demais despesas estão fora do escopo desta versão.")
    print("O anual pressupõe 12 meses com consumo, preços e câmbio constantes.\n")
    print(tabela_cenarios.to_string(
        index=False, header=titulos_colunas, formatters=formatadores_monetarios,
    ))

    if len(tabela_cenarios) > 1:
        menor_custo_mensal_br = tabela_cenarios["custo_ia_mensal_br"].min()
        maior_custo_mensal_br = tabela_cenarios["custo_ia_mensal_br"].max()
        diferenca_custos_mensais_br = maior_custo_mensal_br - menor_custo_mensal_br
        print("\nResumo da IA mensal em BRL:")
        print(f"Menor custo de IA: R$ {formatar_moeda_br(menor_custo_mensal_br)}")
        print(f"Maior custo de IA: R$ {formatar_moeda_br(maior_custo_mensal_br)}")
        print(f"Diferença: R$ {formatar_moeda_br(diferenca_custos_mensais_br)}")

    caminho_csv = Path(__file__).resolve().parent / "resultados" / "cenarios.csv"
    caminho_csv.parent.mkdir(parents=True, exist_ok=True)
    tabela_cenarios.to_csv(
        caminho_csv,
        header=True,
        index=False,
        encoding="utf-8",
        sep=",",
        decimal=".",
        mode="w",
    )
    print(f"\nCSV salvo em: {caminho_csv}")

