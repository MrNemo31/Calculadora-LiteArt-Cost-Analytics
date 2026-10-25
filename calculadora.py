from decimal import Decimal
from math import isfinite

def calcular_respostas_mensais(usuarios_ativos, respostas_por_usuario):
    """Recebe usuários int e média int ou float finita, ambos não negativos."""
    if type(usuarios_ativos) is not int:
        raise TypeError("A quantidade de usuários deve ser um número inteiro (int).")

    if type(respostas_por_usuario) not in (int, float):
        raise TypeError("A média de respostas por usuário deve ser um número (int ou float).")

    if type(respostas_por_usuario) is float and not isfinite(respostas_por_usuario):
        raise ValueError("A média de respostas por usuário deve ser finita (sem infinito ou NaN).")

    if usuarios_ativos < 0:
        raise ValueError("A quantidade de usuários não pode ser negativa.")

    if respostas_por_usuario < 0:
        raise ValueError("A média de respostas por usuário não pode ser negativa.")

    return usuarios_ativos * respostas_por_usuario


def calcular_feedbacks_mensais(respostas_mensais, taxa_acerto, proporcao_acertos_com_feedback):
    """Recebe int ou float; respostas finitas e não negativas e taxas entre 0 e 1."""
    if type(respostas_mensais) not in (int, float):
        raise TypeError("O total de respostas mensais deve ser um número (int ou float).")

    if type(taxa_acerto) not in (int, float):
        raise TypeError("A taxa de acerto deve ser um número (int ou float).")

    if type(proporcao_acertos_com_feedback) not in (int, float):
        raise TypeError("A proporção dos acertos com feedback deve ser um número (int ou float).")

    if type(respostas_mensais) is float and not isfinite(respostas_mensais):
        raise ValueError("O total de respostas mensais deve ser finito (sem infinito ou NaN).")

    if respostas_mensais < 0:
        raise ValueError("O total de respostas mensais não pode ser negativo.")

    if not 0 <= taxa_acerto <= 1:
        raise ValueError("A taxa de acerto deve estar entre 0 e 1.")

    if not 0 <= proporcao_acertos_com_feedback <= 1:
        raise ValueError("A proporção dos acertos com feedback deve estar entre 0 e 1.")

    acertos_mensais = respostas_mensais * taxa_acerto
    erros_mensais = respostas_mensais - acertos_mensais
    feedbacks_nos_acertos = acertos_mensais * proporcao_acertos_com_feedback
    feedbacks_mensais = erros_mensais + feedbacks_nos_acertos
    return acertos_mensais, erros_mensais, feedbacks_nos_acertos, feedbacks_mensais


def calcular_custo_tokens(tokens_total, preco_por_milhao_usd):
    """Recebe tokens int ou float e preço Decimal, finitos e não negativos."""
    if type(tokens_total) not in (int, float):
        raise TypeError("O total de tokens deve ser um número (int ou float).")

    if type(preco_por_milhao_usd) is not Decimal:
        raise TypeError("O preço por milhão de tokens deve ser informado como Decimal.")

    if type(tokens_total) is float and not isfinite(tokens_total):
        raise ValueError("O total de tokens deve ser finito (sem infinito ou NaN).")

    if not preco_por_milhao_usd.is_finite():
        raise ValueError("O preço por milhão de tokens deve ser finito (sem infinito ou NaN).")

    if tokens_total < 0:
        raise ValueError("O total de tokens não pode ser negativo.")

    if preco_por_milhao_usd < 0:
        raise ValueError("O preço por milhão de tokens não pode ser negativo.")

    tokens_decimal = Decimal(str(tokens_total))
    return tokens_decimal / 1_000_000 * preco_por_milhao_usd


def calcular_tokens_mensais(tokens_entrada, tokens_saida, feedbacks_mensais):
    """Retorna os tokens mensais; recebe int ou float finitos e não negativos."""
    if type(tokens_entrada) not in (int, float):
        raise TypeError("A média de tokens de entrada por feedback deve ser um número (int ou float).")

    if type(tokens_saida) not in (int, float):
        raise TypeError("A média de tokens de saída por feedback deve ser um número (int ou float).")

    if type(feedbacks_mensais) not in (int, float):
        raise TypeError("O total de feedbacks mensais deve ser um número (int ou float).")

    if type(tokens_entrada) is float and not isfinite(tokens_entrada):
        raise ValueError("A média de tokens de entrada por feedback deve ser finita (sem infinito ou NaN).")

    if type(tokens_saida) is float and not isfinite(tokens_saida):
        raise ValueError("A média de tokens de saída por feedback deve ser finita (sem infinito ou NaN).")

    if type(feedbacks_mensais) is float and not isfinite(feedbacks_mensais):
        raise ValueError("O total de feedbacks mensais deve ser finito (sem infinito ou NaN).")

    if tokens_entrada < 0:
        raise ValueError("A média de tokens de entrada por feedback não pode ser negativa.")

    if tokens_saida < 0:
        raise ValueError("A média de tokens de saída por feedback não pode ser negativa.")

    if feedbacks_mensais < 0:
        raise ValueError("O total de feedbacks mensais não pode ser negativo.")

    tokens_entrada_total = tokens_entrada * feedbacks_mensais
    tokens_saida_total = tokens_saida * feedbacks_mensais
    return tokens_entrada_total, tokens_saida_total

def calcular_real(custo_usd, taxa_cambio):
    """Converte custo Decimal não negativo com cotação numérica finita e positiva."""
    if type(custo_usd) is not Decimal:
        raise TypeError("O custo em dólares deve ser informado como Decimal.")

    if type(taxa_cambio) not in (int, float, Decimal):
        raise TypeError("A cotação deve ser um número (int, float ou Decimal).")

    if not custo_usd.is_finite():
        raise ValueError("O custo em dólares deve ser finito (sem infinito ou NaN).")

    taxa_cambio_decimal = Decimal(str(taxa_cambio))
    if not taxa_cambio_decimal.is_finite():
        raise ValueError("A cotação deve ser finita (sem infinito ou NaN).")

    if custo_usd < 0:
        raise ValueError("O custo em dólares não pode ser negativo.")

    if taxa_cambio_decimal <= 0:
        raise ValueError("A cotação deve ser maior que zero.")

    return custo_usd * taxa_cambio_decimal

def calcular_custo_anual(custo_mensal):
    """Projeta 12 meses constantes a partir de um custo Decimal finito e não negativo."""
    if type(custo_mensal) is not Decimal:
        raise TypeError("O custo mensal deve ser informado como Decimal.")

    if not custo_mensal.is_finite():
        raise ValueError("O custo mensal deve ser finito (sem infinito ou NaN).")

    if custo_mensal < 0:
        raise ValueError("O custo mensal não pode ser negativo.")

    return custo_mensal * Decimal("12")

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