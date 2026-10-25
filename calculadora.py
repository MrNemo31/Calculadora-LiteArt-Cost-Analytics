from decimal import Decimal

def calcular_respostas_mensais(usuarios_ativos, respostas_por_usuario):
    """Retorna o volume mensal estimado de respostas."""
    return usuarios_ativos * respostas_por_usuario


def calcular_feedbacks_mensais(respostas_mensais, taxa_acerto, proporcao_acertos_com_feedback):
    """Retorna acertos, erros, feedbacks nos acertos e total de feedbacks."""
    acertos_mensais = respostas_mensais * taxa_acerto
    erros_mensais = respostas_mensais - acertos_mensais
    feedbacks_nos_acertos = acertos_mensais * proporcao_acertos_com_feedback
    feedbacks_mensais = erros_mensais + feedbacks_nos_acertos
    return acertos_mensais, erros_mensais, feedbacks_nos_acertos, feedbacks_mensais


def calcular_custo_tokens(tokens_total, preco_por_milhao_usd):
    """Retorna o custo em USD; a tarifa deve ser informada como Decimal."""
    tokens_decimal = Decimal(str(tokens_total))
    return tokens_decimal / 1_000_000 * preco_por_milhao_usd


def calcular_tokens_mensais(tokens_entrada, tokens_saida, feedbacks_mensais):
    tokens_entrada_total = tokens_entrada * feedbacks_mensais
    tokens_saida_total = tokens_saida * feedbacks_mensais
    return tokens_entrada_total, tokens_saida_total

def calcular_real(custo_usd, taxa_cambio):
    return custo_usd * Decimal(str(taxa_cambio))

def calcular_custo_anual(custo_mensal):
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