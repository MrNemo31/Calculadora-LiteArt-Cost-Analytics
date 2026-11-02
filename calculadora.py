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


if __name__ == "__main__":
    # Cenário didático: hipóteses de consumo, não dados reais do LiteArt.
    hipoteses_consumo = {
        "usuarios_ativos": 100,
        "respostas_por_usuario": 40,
        "taxa_acerto": 60 / 100,
        "proporcao_acertos_com_feedback": 25 / 100,
        "tokens_entrada": 500,
        "tokens_saida": 300,
    }

    # Cotação didática em reais por dólar, não uma cotação pesquisada.
    cotacao = {
        "brl_por_usd": Decimal("5.00"),
    }

    # Infraestrutura didática em USD: preços inventados, não planos pesquisados.
    precos_infraestrutura = {
        "backend_mensal_por_unidade_usd": Decimal("5.00"),
        "banco_mensal_por_unidade_usd": Decimal("3.00"),
    }

    # Hipóteses de capacidade: quantidades contratadas, não preços.
    hipoteses_capacidade = {
        "quantidade_backend": 2,
        "quantidade_banco": 1,
    }

    # Preços pesquisados: GPT-6 Luna, Standard, entrada sem cache.
    # Fonte: https://developers.openai.com/api/docs/models/gpt-6-luna
    # Consulta: 2026-10-23. Sem adicionais regionais, ferramentas ou cache.
    precos_ia = {
        "entrada_por_milhao_usd": Decimal("0.10"),
        "saida_por_milhao_usd": Decimal("0.50"),
    }

    # Executar o cenário completo antes de apresentar os resultados.
    resultado_cenario = calcular_cenario(
        hipoteses_consumo, hipoteses_capacidade, precos_ia, precos_infraestrutura, cotacao
    )
    consumo_cenario = resultado_cenario["consumo"]
    custos_ia_cenario = resultado_cenario["custos_ia"]
    custos_infra_cenario = resultado_cenario["custos_infraestrutura"]
    totais_cenario = resultado_cenario["totais"]

    respostas_mensais = consumo_cenario["respostas_mensais"]
    acertos_mensais = consumo_cenario["acertos_mensais"]
    erros_mensais = consumo_cenario["erros_mensais"]
    feedbacks_nos_acertos = consumo_cenario["feedbacks_nos_acertos"]
    feedbacks_mensais = consumo_cenario["feedbacks_mensais"]
    tokens_entrada_total = consumo_cenario["tokens_entrada_total"]
    tokens_saida_total = consumo_cenario["tokens_saida_total"]

    custo_entrada_usd = custos_ia_cenario["custo_entrada_usd"]
    custo_saida_usd = custos_ia_cenario["custo_saida_usd"]
    custo_ia_mensal_usd = custos_ia_cenario["custo_ia_mensal_usd"]
    custo_entrada_br = custos_ia_cenario["custo_entrada_br"]
    custo_saida_br = custos_ia_cenario["custo_saida_br"]
    custo_ia_mensal_br = custos_ia_cenario["custo_ia_mensal_br"]
    custo_ia_anual_usd = custos_ia_cenario["custo_ia_anual_usd"]
    custo_ia_anual_br = custos_ia_cenario["custo_ia_anual_br"]

    custo_backend_mensal_usd = custos_infra_cenario["custo_backend_mensal_usd"]
    custo_banco_mensal_usd = custos_infra_cenario["custo_banco_mensal_usd"]
    custo_infra_mensal_usd = custos_infra_cenario["custo_infra_mensal_usd"]
    custo_backend_mensal_br = custos_infra_cenario["custo_backend_mensal_br"]
    custo_banco_mensal_br = custos_infra_cenario["custo_banco_mensal_br"]
    custo_infra_mensal_br = custos_infra_cenario["custo_infra_mensal_br"]
    custo_infra_anual_usd = custos_infra_cenario["custo_infra_anual_usd"]
    custo_infra_anual_br = custos_infra_cenario["custo_infra_anual_br"]

    custo_total_mensal_usd = totais_cenario["custo_total_mensal_usd"]
    custo_total_mensal_br = totais_cenario["custo_total_mensal_br"]
    custo_total_anual_usd = totais_cenario["custo_total_anual_usd"]
    custo_total_anual_br = totais_cenario["custo_total_anual_br"]

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

    print("Infraestrutura com preços didáticos, sem comprovação de capacidade dos planos.")
    print(f"Custo mensal estimado de backend (USD): US$ {custo_backend_mensal_usd:.2f}")
    print(f"Custo mensal estimado de backend (BRL): R$ {custo_backend_mensal_br:.2f}")
    print(f"Custo mensal estimado de banco (USD): US$ {custo_banco_mensal_usd:.2f}")
    print(f"Custo mensal estimado de banco (BRL): R$ {custo_banco_mensal_br:.2f}")
    print(f"Custo mensal estimado de infraestrutura (USD): US$ {custo_infra_mensal_usd:.2f}")
    print(f"Custo mensal estimado de infraestrutura (BRL): R$ {custo_infra_mensal_br:.2f}")
    print(f"Custo anual estimado de infraestrutura (USD): US$ {custo_infra_anual_usd:.2f}")
    print(f"Custo anual estimado de infraestrutura (BRL): R$ {custo_infra_anual_br:.2f}")

    print("Total do cenário: infraestrutura e IA, com as hipóteses e exclusões do planejamento.")
    print(f"Custo total mensal estimado (USD): US$ {custo_total_mensal_usd:.2f}")
    print(f"Custo total mensal estimado (BRL): R$ {custo_total_mensal_br:.2f}")
    print(f"Custo total anual estimado (USD): US$ {custo_total_anual_usd:.2f}")
    print(f"Custo total anual estimado (BRL): R$ {custo_total_anual_br:.2f}")

    # Cópias independentes: alterar o consumo de um cenário não altera o outro.
    consumo_100_usuarios = hipoteses_consumo.copy()
    consumo_500_usuarios = hipoteses_consumo.copy()
    consumo_500_usuarios["usuarios_ativos"] = 500

    cenarios_didaticos = [
        {
            "nome": "Cenário didático: 100 usuários",
            "hipoteses_consumo": consumo_100_usuarios,
            "hipoteses_capacidade": hipoteses_capacidade.copy(),
        },
        {
            "nome": "Cenário didático: 500 usuários",
            "hipoteses_consumo": consumo_500_usuarios,
            "hipoteses_capacidade": hipoteses_capacidade.copy(),
        },
    ]

    # Preços e cotação compartilhados; a capacidade é uma hipótese, não uma garantia.
    comparacao_cenarios = []
    print("\nComparação de cenários didáticos")
    print("Mesmos preços, cotação e unidades contratadas; capacidade não validada.")
    for cenario in cenarios_didaticos:
        resultado_comparacao = calcular_cenario(
            cenario["hipoteses_consumo"],
            cenario["hipoteses_capacidade"],
            precos_ia,
            precos_infraestrutura,
            cotacao,
        )
        comparacao_cenarios.append({
            "nome": cenario["nome"],
            "usuarios_ativos": cenario["hipoteses_consumo"]["usuarios_ativos"],
            "resultado": resultado_comparacao,
        })

        print(f"\n{cenario['nome']}")
        print("Usuários ativos:", cenario["hipoteses_consumo"]["usuarios_ativos"])
        print("Feedbacks mensais:", resultado_comparacao["consumo"]["feedbacks_mensais"])
        print(f"IA mensal: R$ {resultado_comparacao['custos_ia']['custo_ia_mensal_br']:.2f}")
        print(f"Infraestrutura mensal: R$ {resultado_comparacao['custos_infraestrutura']['custo_infra_mensal_br']:.2f}")
        print(f"Total mensal: R$ {resultado_comparacao['totais']['custo_total_mensal_br']:.2f}")
        print(f"Total anual: R$ {resultado_comparacao['totais']['custo_total_anual_br']:.2f}")

