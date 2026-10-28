from decimal import Decimal
from math import isfinite

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


if __name__ == "__main__":
    # Cenário didático: hipóteses de consumo, não dados reais do LiteArt.
    usuarios_ativos = 100
    respostas_por_usuario = 40
    taxa_acerto = 60 / 100
    proporcao_acertos_com_feedback = 25 / 100
    tokens_entrada = 500
    tokens_saida = 300

    # Cotação didática em reais por dólar, não uma cotação pesquisada.
    taxa_cambio = Decimal("5.00")

    # Cada erro gera feedback; apenas parte dos acertos recebe feedback.
    respostas_mensais = calcular_respostas_mensais(usuarios_ativos, respostas_por_usuario)
    acertos_mensais, erros_mensais, feedbacks_nos_acertos, feedbacks_mensais = calcular_feedbacks_mensais(
        respostas_mensais, taxa_acerto, proporcao_acertos_com_feedback
    )
    tokens_entrada_total, tokens_saida_total = calcular_tokens_mensais(tokens_entrada, tokens_saida, feedbacks_mensais)

    # Preços pesquisados: GPT-6 Luna, Standard, entrada sem cache.
    # Fonte: https://developers.openai.com/api/docs/models/gpt-6-luna
    # Consulta: 2026-10-23. Sem adicionais regionais, ferramentas ou cache.
    preco_entrada_por_milhao_usd = Decimal("0.10")
    preco_saida_por_milhao_usd = Decimal("0.50")

    # Custos mensais estimados de IA, em dólares.
    # A conversão para Decimal acontece dentro de calcular_custo_tokens.
    custo_entrada_usd = calcular_custo_tokens(tokens_entrada_total, preco_entrada_por_milhao_usd)
    custo_saida_usd = calcular_custo_tokens(tokens_saida_total, preco_saida_por_milhao_usd)
    custo_ia_mensal_usd = custo_entrada_usd + custo_saida_usd

    # Custo mensal estimado de IA, em reais (BRL), usando uma taxa de câmbio hipotética.
    custo_entrada_br = calcular_real(custo_entrada_usd, taxa_cambio)
    custo_saida_br = calcular_real(custo_saida_usd, taxa_cambio)
    custo_ia_mensal_br = calcular_real(custo_ia_mensal_usd, taxa_cambio)

    # Custos anuais estimados de IA, em dólares e reais (BRL).
    custo_ia_anual_usd = calcular_custo_anual(custo_ia_mensal_usd)
    custo_ia_anual_br = calcular_custo_anual(custo_ia_mensal_br)


    # Exibição dos resultados para conferência manual.
    print("Respostas no mês:", respostas_mensais)
    print("Acertos estimados:", acertos_mensais)
    print("Erros estimados:", erros_mensais)
    print("Feedbacks nos acertos:", feedbacks_nos_acertos)
    print("Total de feedbacks no mês:", feedbacks_mensais)
    print("Total de tokens de entrada no mês:", tokens_entrada_total)
    print("Total de tokens de saída no mês:", tokens_saida_total)

    print(f"Custo mensal estimado de entrada (USD): US$ {custo_entrada_usd:.2f}")
    print(f"Custo mensal estimado de saída (USD): US$ {custo_saida_usd:.2f}")
    print(f"Custo mensal estimado de IA (USD): US$ {custo_ia_mensal_usd:.2f}")
    print(f"Custo mensal estimado de entrada (BRL): R$ {custo_entrada_br:.2f}")
    print(f"Custo mensal estimado de saída (BRL): R$ {custo_saida_br:.2f}")
    print(f"Custo mensal estimado de IA (BRL): R$ {custo_ia_mensal_br:.2f}")

    print("Custo anual ignorando a variação de preços e câmbio, apenas para conferência didática.")
    print(f"Custo anual estimado de IA (USD): US$ {custo_ia_anual_usd:.2f}")
    print(f"Custo anual estimado de IA (BRL): R$ {custo_ia_anual_br:.2f}")
