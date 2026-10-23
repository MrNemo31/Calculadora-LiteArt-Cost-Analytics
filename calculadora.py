from decimal import Decimal

# Cenário didático: hipóteses de consumo, não dados reais do LiteArt.
usuarios_ativos = 100
respostas_por_usuario = 40
taxa_acerto = 60 / 100
proporcao_acertos_com_feedback = 25 / 100
tokens_entrada = 500
tokens_saida = 300

# Cada erro gera feedback; apenas parte dos acertos recebe feedback.
respostas_mensais = usuarios_ativos * respostas_por_usuario
acertos_mensais = respostas_mensais * taxa_acerto
erros_mensais = respostas_mensais - acertos_mensais
feedbacks_nos_acertos = acertos_mensais * proporcao_acertos_com_feedback
feedbacks_mensais = erros_mensais + feedbacks_nos_acertos
tokens_entrada_total = tokens_entrada * feedbacks_mensais
tokens_saida_total = tokens_saida * feedbacks_mensais

# Preços pesquisados: GPT-6 Luna, Standard, entrada sem cache.
# Fonte: https://developers.openai.com/api/docs/models/gpt-6-luna
# Consulta: 2026-10-23. Sem adicionais regionais, ferramentas ou cache.
preco_entrada_por_milhao_usd = Decimal("0.10")
preco_saida_por_milhao_usd = Decimal("0.50")

# Conversão dos totais para Decimal antes dos cálculos monetários.
tokens_entrada_decimal = Decimal(str(tokens_entrada_total))
tokens_saida_decimal = Decimal(str(tokens_saida_total))

# Custos mensais estimados de IA, em dólares.
custo_entrada_usd = tokens_entrada_decimal / 1_000_000 * preco_entrada_por_milhao_usd
custo_saida_usd = tokens_saida_decimal / 1_000_000 * preco_saida_por_milhao_usd
custo_ia_mensal_usd = custo_entrada_usd + custo_saida_usd


# Exibição dos resultados para conferência manual.
print("Respostas no mês:", respostas_mensais)
print("Acertos estimados:", acertos_mensais)
print("Erros estimados:", erros_mensais)
print("Feedbacks nos acertos:", feedbacks_nos_acertos)
print("Total de feedbacks no mês:", feedbacks_mensais)
print("Total de tokens de entrada no mês:", tokens_entrada_total)
print("Total de tokens de saída no mês:", tokens_saida_total)

print(f"Custo mensal estimado de entrada (USD): {custo_entrada_usd:.2f}")
print(f"Custo mensal estimado de saída (USD): {custo_saida_usd:.2f}")
print(f"Custo mensal estimado de IA (USD): {custo_ia_mensal_usd:.2f}")
