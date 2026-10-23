# Cenário didático: hipóteses de consumo, não dados reais do LiteArt.
usuarios_ativos = 100
respostas_por_usuario = 40
taxa_acerto = 60 / 100
proporcao_acertos_com_feedback = 25 / 100

# Cada erro gera feedback; apenas parte dos acertos recebe feedback.
respostas_mensais = usuarios_ativos * respostas_por_usuario
acertos_mensais = respostas_mensais * taxa_acerto
erros_mensais = respostas_mensais - acertos_mensais
feedbacks_nos_acertos = acertos_mensais * proporcao_acertos_com_feedback
feedbacks_mensais = erros_mensais + feedbacks_nos_acertos

# Exibição dos resultados para conferência manual.
print("Respostas no mês:", respostas_mensais)
print("Acertos estimados:", acertos_mensais)
print("Erros estimados:", erros_mensais)
print("Feedbacks nos acertos:", feedbacks_nos_acertos)
print("Total de feedbacks no mês:", feedbacks_mensais)
