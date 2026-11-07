import unittest
import csv
import io
import runpy
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from decimal import Decimal

from calculadora import (
    ler_cenarios_csv,
    calcular_cenario,
    calcular_consumo_cenario,
    calcular_custo_ia_cenario,
    calcular_custo_infra_cenario,
    calcular_custo_anual,
    calcular_custo_servico,
    calcular_custo_tokens,
    calcular_feedbacks_mensais,
    calcular_real,
    calcular_respostas_mensais,
    calcular_tokens_mensais,
)


class TestCalcularRespostasMensais(unittest.TestCase):
    def test_calcula_respostas_do_cenario_didatico(self):
        resultado = calcular_respostas_mensais(100, 40)
        self.assertEqual(resultado, 4000)

    def test_zero_usuarios_retorna_zero(self):
        resultado = calcular_respostas_mensais(0, 40)
        self.assertEqual(resultado, 0)

    def test_usuarios_negativos_geram_erro(self):
        with self.assertRaises(ValueError):
            calcular_respostas_mensais(-1, 40)

    def test_usuarios_fracionarios_geram_erro(self):
        with self.assertRaises(TypeError):
            calcular_respostas_mensais(1.5, 40)

    def test_usuarios_como_texto_geram_erro(self):
        with self.assertRaises(TypeError):
            calcular_respostas_mensais("100", 40)

    def test_respostas_por_usuario_como_texto_geram_erro(self):
        with self.assertRaises(TypeError):
            calcular_respostas_mensais(100, "40")

    def test_usuarios_com_infinito_positivo_geram_erro(self):
        with self.assertRaises(TypeError):
            calcular_respostas_mensais(float("inf"), 40)

    def test_usuarios_com_infinito_negativo_geram_erro(self):
        with self.assertRaises(TypeError):
            calcular_respostas_mensais(float("-inf"), 40)

    def test_usuarios_com_nan_geram_erro(self):
        with self.assertRaises(TypeError):
            calcular_respostas_mensais(float("nan"), 40)

    def test_respostas_por_usuario_com_infinito_positivo_geram_erro(self):
        with self.assertRaises(ValueError):
            calcular_respostas_mensais(100, float("inf"))

    def test_respostas_por_usuario_com_infinito_negativo_geram_erro(self):
        with self.assertRaises(ValueError):
            calcular_respostas_mensais(100, float("-inf"))

    def test_respostas_por_usuario_com_nan_geram_erro(self):
        with self.assertRaises(ValueError):
            calcular_respostas_mensais(100, float("nan"))


class TestCalcularFeedbacksMensais(unittest.TestCase):
    def test_calcula_feedbacks_do_cenario_didatico(self):
        resultado = calcular_feedbacks_mensais(4000, 0.6, 0.25)
        self.assertEqual(resultado, (2400, 1600, 600, 2200))

    def test_taxa_acerto_zero_gera_feedback_para_todos_os_erros(self):
        resultado = calcular_feedbacks_mensais(100, 0, 0.25)
        self.assertEqual(resultado, (0, 100, 0, 100))

    def test_taxa_acerto_um_gera_feedback_apenas_nos_acertos_selecionados(self):
        resultado = calcular_feedbacks_mensais(100, 1, 0.25)
        self.assertEqual(resultado, (100, 0, 25, 25))

    def test_proporcao_zero_gera_feedback_apenas_nos_erros(self):
        resultado = calcular_feedbacks_mensais(100, 0.6, 0)
        self.assertEqual(resultado, (60, 40, 0, 40))

    def test_proporcao_um_gera_feedback_em_todas_as_respostas(self):
        resultado = calcular_feedbacks_mensais(100, 0.6, 1)
        self.assertEqual(resultado, (60, 40, 60, 100))

    def test_taxa_acerto_negativa_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, -0.1, 0.25)

    def test_taxa_acerto_maior_que_um_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, 1.1, 0.25)

    def test_proporcao_negativa_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, 0.6, -0.1)

    def test_proporcao_maior_que_um_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, 0.6, 1.1)

    def test_respostas_mensais_como_texto_gera_erro(self):
        with self.assertRaises(TypeError):
            calcular_feedbacks_mensais("100", 0.6, 0.25)

    def test_respostas_mensais_com_booleano_gera_erro(self):
        with self.assertRaises(TypeError):
            calcular_feedbacks_mensais(True, 0.6, 0.25)

    def test_respostas_mensais_com_infinito_positivo_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(float("inf"), 0.6, 0.25)

    def test_respostas_mensais_com_infinito_negativo_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(float("-inf"), 0.6, 0.25)

    def test_respostas_mensais_com_nan_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(float("nan"), 0.6, 0.25)

    def test_taxa_acerto_como_texto_gera_erro(self):
        with self.assertRaises(TypeError):
            calcular_feedbacks_mensais(100, "0.6", 0.25)

    def test_taxa_acerto_com_booleano_gera_erro(self):
        with self.assertRaises(TypeError):
            calcular_feedbacks_mensais(100, True, 0.25)

    def test_taxa_acerto_com_infinito_positivo_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, float("inf"), 0.25)

    def test_taxa_acerto_com_infinito_negativo_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, float("-inf"), 0.25)

    def test_taxa_acerto_com_nan_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, float("nan"), 0.25)

    def test_proporcao_como_texto_gera_erro(self):
        with self.assertRaises(TypeError):
            calcular_feedbacks_mensais(100, 0.6, "0.25")

    def test_proporcao_com_booleano_gera_erro(self):
        with self.assertRaises(TypeError):
            calcular_feedbacks_mensais(100, 0.6, True)

    def test_proporcao_com_infinito_positivo_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, 0.6, float("inf"))

    def test_proporcao_com_infinito_negativo_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, 0.6, float("-inf"))

    def test_proporcao_com_nan_gera_erro(self):
        with self.assertRaises(ValueError):
            calcular_feedbacks_mensais(100, 0.6, float("nan"))


class TestCalcularTokensMensais(unittest.TestCase):
    def test_calcula_tokens_do_cenario_didatico(self):
        resultado = calcular_tokens_mensais(500, 300, 2200)
        self.assertEqual(resultado, (1_100_000, 660_000))

    def test_aceita_estimativas_fracionarias(self):
        resultado = calcular_tokens_mensais(2.5, 1.5, 2.5)
        self.assertEqual(resultado, (6.25, 3.75))

    def test_aceita_zero_em_cada_argumento(self):
        self.assertEqual(calcular_tokens_mensais(0, 300, 2200), (0, 660_000))
        self.assertEqual(calcular_tokens_mensais(500, 0, 2200), (1_100_000, 0))
        self.assertEqual(calcular_tokens_mensais(500, 300, 0), (0, 0))

    def test_recusa_tipos_invalidos_nos_tres_argumentos(self):
        for valor in ("500", True, False, None, Decimal("500"), 1j, []):
            with self.subTest(argumento="tokens_entrada", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_tokens_mensais(valor, 300, 2200)
            with self.subTest(argumento="tokens_saida", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_tokens_mensais(500, valor, 2200)
            with self.subTest(argumento="feedbacks_mensais", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_tokens_mensais(500, 300, valor)

    def test_recusa_negativos_nos_tres_argumentos(self):
        for valor in (-1, -0.5):
            with self.subTest(argumento="tokens_entrada", valor=valor):
                with self.assertRaises(ValueError):
                    calcular_tokens_mensais(valor, 300, 2200)
            with self.subTest(argumento="tokens_saida", valor=valor):
                with self.assertRaises(ValueError):
                    calcular_tokens_mensais(500, valor, 2200)
            with self.subTest(argumento="feedbacks_mensais", valor=valor):
                with self.assertRaises(ValueError):
                    calcular_tokens_mensais(500, 300, valor)

    def test_recusa_infinito_e_nan_nos_tres_argumentos(self):
        for valor in (float("inf"), float("-inf"), float("nan")):
            with self.subTest(argumento="tokens_entrada", valor=valor):
                with self.assertRaises(ValueError):
                    calcular_tokens_mensais(valor, 300, 2200)
            with self.subTest(argumento="tokens_saida", valor=valor):
                with self.assertRaises(ValueError):
                    calcular_tokens_mensais(500, valor, 2200)
            with self.subTest(argumento="feedbacks_mensais", valor=valor):
                with self.assertRaises(ValueError):
                    calcular_tokens_mensais(500, 300, valor)


class TestCalcularCustoTokens(unittest.TestCase):
    def test_calcula_custos_do_cenario_didatico(self):
        entrada = calcular_custo_tokens(1_100_000, Decimal("0.10"))
        saida = calcular_custo_tokens(660_000, Decimal("0.50"))
        self.assertEqual(entrada, Decimal("0.11"))
        self.assertEqual(saida, Decimal("0.33"))
        self.assertEqual(entrada + saida, Decimal("0.44"))
        self.assertIsInstance(entrada, Decimal)
        self.assertIsInstance(saida, Decimal)

    def test_aceita_zero_tokens_e_preco_gratuito(self):
        self.assertEqual(calcular_custo_tokens(0, Decimal("0.10")), Decimal("0"))
        self.assertEqual(calcular_custo_tokens(500, Decimal("0")), Decimal("0"))

    def test_aceita_tokens_fracionarios(self):
        resultado = calcular_custo_tokens(2.5, Decimal("0.10"))
        self.assertEqual(resultado, Decimal("0.00000025"))

    def test_recusa_tipos_invalidos_dos_tokens(self):
        for valor in ("500", True, False, None, Decimal("500"), 1j, []):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_tokens(valor, Decimal("0.10"))

    def test_recusa_tokens_negativos_infinito_e_nan(self):
        for valor in (-1, -0.5, float("inf"), float("-inf"), float("nan")):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    calcular_custo_tokens(valor, Decimal("0.10"))

    def test_preco_exige_decimal(self):
        for valor in ("0.10", 1, 0.1, True, False, None, 1j, []):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_tokens(500, valor)

    def test_recusa_preco_negativo_infinito_e_nan(self):
        for valor in (Decimal("-0.10"), Decimal("Infinity"), Decimal("-Infinity"),
                      Decimal("NaN"), Decimal("sNaN")):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    calcular_custo_tokens(500, valor)


class TestCalcularReal(unittest.TestCase):
    def test_converte_com_os_tres_tipos_de_cotacao_permitidos(self):
        for cotacao in (5, 5.0, Decimal("5.00")):
            with self.subTest(cotacao=cotacao, tipo=type(cotacao).__name__):
                resultado = calcular_real(Decimal("0.44"), cotacao)
                self.assertEqual(resultado, Decimal("2.20"))
                self.assertIsInstance(resultado, Decimal)

    def test_aceita_custo_zero(self):
        self.assertEqual(calcular_real(Decimal("0"), 5), Decimal("0"))

    def test_custo_exige_decimal(self):
        for valor in ("0.44", 1, 0.44, True, False, None, 1j, []):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_real(valor, 5)

    def test_recusa_custo_negativo_infinito_e_nan(self):
        for valor in (Decimal("-0.44"), Decimal("Infinity"), Decimal("-Infinity"),
                      Decimal("NaN"), Decimal("sNaN")):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    calcular_real(valor, 5)

    def test_recusa_tipos_invalidos_da_cotacao(self):
        for valor in ("5.00", True, False, None, 1j, []):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_real(Decimal("0.44"), valor)

    def test_recusa_cotacao_zero_negativa_infinita_e_nan(self):
        for valor in (0, 0.0, Decimal("0"), -1, -0.5, Decimal("-5"),
                      float("inf"), float("-inf"), float("nan"),
                      Decimal("Infinity"), Decimal("-Infinity"),
                      Decimal("NaN"), Decimal("sNaN")):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    calcular_real(Decimal("0.44"), valor)


class TestCalcularCustoAnual(unittest.TestCase):
    def test_calcula_custos_anuais_do_cenario_didatico(self):
        custo_usd = calcular_custo_anual(Decimal("0.44"))
        custo_brl = calcular_custo_anual(Decimal("2.20"))
        self.assertEqual(custo_usd, Decimal("5.28"))
        self.assertEqual(custo_brl, Decimal("26.40"))
        self.assertIsInstance(custo_usd, Decimal)
        self.assertIsInstance(custo_brl, Decimal)

    def test_aceita_custo_zero(self):
        self.assertEqual(calcular_custo_anual(Decimal("0")), Decimal("0"))

    def test_custo_mensal_exige_decimal(self):
        for valor in ("0.44", 1, 0.44, True, False, None, 1j, []):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_anual(valor)

    def test_recusa_custo_negativo_infinito_e_nan(self):
        for valor in (Decimal("-0.44"), Decimal("Infinity"), Decimal("-Infinity"),
                      Decimal("NaN"), Decimal("sNaN")):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    calcular_custo_anual(valor)



class TestCalcularCustoServico(unittest.TestCase):
    # Preços inventados para aprendizado, sem representar planos pesquisados.
    def test_calcula_backend_didatico(self):
        resultado = calcular_custo_servico(Decimal("5.00"), 2)
        self.assertEqual(resultado, Decimal("10.00"))
        self.assertIsInstance(resultado, Decimal)

    def test_calcula_banco_didatico(self):
        resultado = calcular_custo_servico(Decimal("3.00"), 1)
        self.assertEqual(resultado, Decimal("3.00"))
        self.assertIsInstance(resultado, Decimal)

    def test_zero_unidades_retorna_zero(self):
        resultado = calcular_custo_servico(Decimal("5.00"), 0)
        self.assertEqual(resultado, Decimal("0"))
        self.assertIsInstance(resultado, Decimal)

    def test_preco_gratuito_retorna_zero(self):
        resultado = calcular_custo_servico(Decimal("0"), 2)
        self.assertEqual(resultado, Decimal("0"))
        self.assertIsInstance(resultado, Decimal)

    def test_preco_exige_decimal(self):
        for valor in ("5.00", 5, 5.0, True, False, None, 1j, []):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_servico(valor, 2)

    def test_recusa_preco_negativo_infinito_e_nan(self):
        for valor in (Decimal("-5.00"), Decimal("Infinity"), Decimal("-Infinity"),
                      Decimal("NaN"), Decimal("sNaN")):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    calcular_custo_servico(valor, 2)

    def test_quantidade_exige_inteiro(self):
        for valor in (1.5, 2.0, "2", True, False, None, Decimal("2"), 1j, [],
                      float("inf"), float("-inf"), float("nan")):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_servico(Decimal("5.00"), valor)

    def test_recusa_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            calcular_custo_servico(Decimal("5.00"), -1)


class TestCalcularConsumoCenario(unittest.TestCase):
    def criar_hipoteses(self):
        # Cada chamada cria um dicionário independente para o teste.
        return {
            "usuarios_ativos": 100,
            "respostas_por_usuario": 40,
            "taxa_acerto": 0.6,
            "proporcao_acertos_com_feedback": 0.25,
            "tokens_entrada": 500,
            "tokens_saida": 300,
        }

    def test_calcula_cenario_didatico(self):
        resultado = calcular_consumo_cenario(self.criar_hipoteses())
        esperado = {
            "respostas_mensais": 4000,
            "acertos_mensais": 2400,
            "erros_mensais": 1600,
            "feedbacks_nos_acertos": 600,
            "feedbacks_mensais": 2200,
            "tokens_entrada_total": 1_100_000,
            "tokens_saida_total": 660_000,
        }
        self.assertEqual(resultado, esperado)

    def test_zero_usuarios_produz_consumo_zero(self):
        hipoteses = self.criar_hipoteses()
        hipoteses["usuarios_ativos"] = 0
        resultado = calcular_consumo_cenario(hipoteses)
        for campo, valor in resultado.items():
            with self.subTest(campo=campo):
                self.assertEqual(valor, 0)

    def test_zero_respostas_produz_consumo_zero(self):
        hipoteses = self.criar_hipoteses()
        hipoteses["respostas_por_usuario"] = 0
        resultado = calcular_consumo_cenario(hipoteses)
        for campo, valor in resultado.items():
            with self.subTest(campo=campo):
                self.assertEqual(valor, 0)

    def test_exige_dicionario(self):
        for valor in (None, [], "cenario", 100, True):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_consumo_cenario(valor)

    def test_recusa_chaves_ausentes(self):
        with self.assertRaises(ValueError):
            calcular_consumo_cenario({})
        for chave in self.criar_hipoteses():
            hipoteses = self.criar_hipoteses()
            del hipoteses[chave]
            with self.subTest(chave=chave):
                with self.assertRaises(ValueError) as erro:
                    calcular_consumo_cenario(hipoteses)
                self.assertIn(chave, str(erro.exception))

    def test_propaga_erros_de_tipo_dos_campos(self):
        for chave in self.criar_hipoteses():
            for valor in ("100", True, False, None, Decimal("1")):
                hipoteses = self.criar_hipoteses()
                hipoteses[chave] = valor
                with self.subTest(chave=chave, valor=valor):
                    with self.assertRaises(TypeError):
                        calcular_consumo_cenario(hipoteses)
        for valor in (1.5, 100.0, float("inf"), float("-inf"), float("nan")):
            hipoteses = self.criar_hipoteses()
            hipoteses["usuarios_ativos"] = valor
            with self.subTest(chave="usuarios_ativos", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_consumo_cenario(hipoteses)

    def test_propaga_erros_de_negativos_e_taxas_acima_de_um(self):
        for chave in self.criar_hipoteses():
            hipoteses = self.criar_hipoteses()
            hipoteses[chave] = -1
            with self.subTest(chave=chave):
                with self.assertRaises(ValueError):
                    calcular_consumo_cenario(hipoteses)
        for chave in ("taxa_acerto", "proporcao_acertos_com_feedback"):
            hipoteses = self.criar_hipoteses()
            hipoteses[chave] = 1.1
            with self.subTest(chave=chave, valor=1.1):
                with self.assertRaises(ValueError):
                    calcular_consumo_cenario(hipoteses)

    def test_propaga_erros_de_infinito_e_nan_nos_campos_float(self):
        for chave in ("respostas_por_usuario", "taxa_acerto",
                      "proporcao_acertos_com_feedback", "tokens_entrada", "tokens_saida"):
            for valor in (float("inf"), float("-inf"), float("nan")):
                hipoteses = self.criar_hipoteses()
                hipoteses[chave] = valor
                with self.subTest(chave=chave, valor=valor):
                    with self.assertRaises(ValueError):
                        calcular_consumo_cenario(hipoteses)

    def test_nao_altera_as_hipoteses(self):
        hipoteses = self.criar_hipoteses()
        copia = hipoteses.copy()
        resultado = calcular_consumo_cenario(hipoteses)
        self.assertEqual(hipoteses, copia)
        self.assertIsNot(resultado, hipoteses)

    def test_aceita_chave_adicional_sem_mudar_o_consumo(self):
        hipoteses = self.criar_hipoteses()
        esperado = calcular_consumo_cenario(hipoteses)
        hipoteses["nome"] = "Cenário didático"
        self.assertEqual(calcular_consumo_cenario(hipoteses), esperado)
        self.assertEqual(hipoteses["nome"], "Cenário didático")


class TestCalcularCustoIaCenario(unittest.TestCase):
    def criar_entradas(self):
        consumo = {"tokens_entrada_total": 1_100_000, "tokens_saida_total": 660_000}
        precos = {
            "entrada_por_milhao_usd": Decimal("0.10"),
            "saida_por_milhao_usd": Decimal("0.50"),
        }
        cotacao = {"brl_por_usd": Decimal("5.00")}
        return consumo, precos, cotacao

    def test_calcula_custos_do_cenario_didatico(self):
        consumo, precos, cotacao = self.criar_entradas()
        resultado = calcular_custo_ia_cenario(consumo, precos, cotacao)
        esperado = {
            "custo_entrada_usd": Decimal("0.11"),
            "custo_saida_usd": Decimal("0.33"),
            "custo_ia_mensal_usd": Decimal("0.44"),
            "custo_entrada_br": Decimal("0.55"),
            "custo_saida_br": Decimal("1.65"),
            "custo_ia_mensal_br": Decimal("2.20"),
            "custo_ia_anual_usd": Decimal("5.28"),
            "custo_ia_anual_br": Decimal("26.40"),
        }
        self.assertEqual(resultado, esperado)
        for campo, valor in resultado.items():
            with self.subTest(campo=campo):
                self.assertIsInstance(valor, Decimal)

    def test_zero_tokens_em_cada_canal_e_nos_dois(self):
        for entrada, saida, esperado in ((0, 660_000, "0.33"),
                                        (1_100_000, 0, "0.11"), (0, 0, "0")):
            consumo, precos, cotacao = self.criar_entradas()
            consumo["tokens_entrada_total"] = entrada
            consumo["tokens_saida_total"] = saida
            with self.subTest(entrada=entrada, saida=saida):
                resultado = calcular_custo_ia_cenario(consumo, precos, cotacao)
                self.assertEqual(resultado["custo_ia_mensal_usd"], Decimal(esperado))

    def test_precos_gratuitos_em_cada_canal_e_nos_dois(self):
        for entrada, saida, esperado in (("0", "0.50", "0.33"),
                                        ("0.10", "0", "0.11"), ("0", "0", "0")):
            consumo, precos, cotacao = self.criar_entradas()
            precos["entrada_por_milhao_usd"] = Decimal(entrada)
            precos["saida_por_milhao_usd"] = Decimal(saida)
            with self.subTest(entrada=entrada, saida=saida):
                resultado = calcular_custo_ia_cenario(consumo, precos, cotacao)
                self.assertEqual(resultado["custo_ia_mensal_usd"], Decimal(esperado))

    def test_aceita_tokens_fracionarios(self):
        consumo, precos, cotacao = self.criar_entradas()
        consumo["tokens_entrada_total"] = 0.5
        consumo["tokens_saida_total"] = 0.5
        resultado = calcular_custo_ia_cenario(consumo, precos, cotacao)
        self.assertEqual(resultado["custo_ia_mensal_usd"], Decimal("0.00000030"))

    def test_cotacao_aceita_tres_tipos_e_altera_apenas_os_valores_em_reais(self):
        for taxa in (5, 5.0, Decimal("5.00"), Decimal("6.00")):
            consumo, precos, cotacao = self.criar_entradas()
            cotacao["brl_por_usd"] = taxa
            with self.subTest(taxa=taxa, tipo=type(taxa).__name__):
                resultado = calcular_custo_ia_cenario(consumo, precos, cotacao)
                self.assertEqual(resultado["custo_ia_mensal_usd"], Decimal("0.44"))
                self.assertEqual(resultado["custo_ia_mensal_br"],
                                 Decimal("0.44") * Decimal(str(taxa)))

    def test_exige_dicionarios_nos_tres_argumentos(self):
        for valor in (None, [], "cenario", 100, True):
            consumo, precos, cotacao = self.criar_entradas()
            with self.subTest(argumento="consumo_cenario", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_ia_cenario(valor, precos, cotacao)
            with self.subTest(argumento="precos_ia", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_ia_cenario(consumo, valor, cotacao)
            with self.subTest(argumento="cotacao", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_ia_cenario(consumo, precos, valor)

    def test_recusa_cada_chave_obrigatoria_ausente(self):
        consumo, precos, cotacao = self.criar_entradas()
        for grupo, dicionario in (("consumo", consumo), ("precos", precos), ("cotacao", cotacao)):
            for chave in dicionario.copy():
                copia = dicionario.copy()
                del dicionario[chave]
                with self.subTest(grupo=grupo, chave=chave):
                    with self.assertRaises(ValueError) as erro:
                        calcular_custo_ia_cenario(consumo, precos, cotacao)
                    self.assertIn(chave, str(erro.exception))
                dicionario[chave] = copia[chave]

    def test_propaga_erros_dos_tokens(self):
        consumo, precos, cotacao = self.criar_entradas()
        for chave in consumo.copy():
            for tipo_erro, valores in ((TypeError, ("100", True, False, None, Decimal("100"), [], 1j)),
                                      (ValueError, (-1, -0.5, float("inf"), float("-inf"), float("nan")))):
                for valor in valores:
                    consumo, precos, cotacao = self.criar_entradas()
                    consumo[chave] = valor
                    with self.subTest(chave=chave, valor=valor, erro=tipo_erro.__name__):
                        with self.assertRaises(tipo_erro):
                            calcular_custo_ia_cenario(consumo, precos, cotacao)

    def test_propaga_erros_dos_precos(self):
        consumo, precos, cotacao = self.criar_entradas()
        for chave in precos.copy():
            for tipo_erro, valores in ((TypeError, ("0.10", 1, 0.1, True, False, None, [], 1j)),
                                      (ValueError, (Decimal("-0.1"), Decimal("Infinity"), Decimal("-Infinity"), Decimal("NaN"), Decimal("sNaN")))):
                for valor in valores:
                    consumo, precos, cotacao = self.criar_entradas()
                    precos[chave] = valor
                    with self.subTest(chave=chave, valor=valor, erro=tipo_erro.__name__):
                        with self.assertRaises(tipo_erro):
                            calcular_custo_ia_cenario(consumo, precos, cotacao)

    def test_propaga_erros_dos_cotacao(self):
        consumo, precos, cotacao = self.criar_entradas()
        for chave in cotacao.copy():
            for tipo_erro, valores in ((TypeError, ("5", True, False, None, [], 1j)),
                                      (ValueError, (0, 0.0, Decimal("0"), -1, -0.5, Decimal("-1"), float("inf"), float("-inf"), float("nan"), Decimal("Infinity"), Decimal("-Infinity"), Decimal("NaN"), Decimal("sNaN")))):
                for valor in valores:
                    consumo, precos, cotacao = self.criar_entradas()
                    cotacao[chave] = valor
                    with self.subTest(chave=chave, valor=valor, erro=tipo_erro.__name__):
                        with self.assertRaises(tipo_erro):
                            calcular_custo_ia_cenario(consumo, precos, cotacao)

    def test_nao_altera_as_tres_entradas(self):
        consumo, precos, cotacao = self.criar_entradas()
        antes = (consumo.copy(), precos.copy(), cotacao.copy())
        resultado = calcular_custo_ia_cenario(consumo, precos, cotacao)
        self.assertEqual((consumo, precos, cotacao), antes)
        for entrada in (consumo, precos, cotacao):
            self.assertIsNot(resultado, entrada)

    def test_aceita_chaves_adicionais_sem_alterar_os_custos(self):
        consumo, precos, cotacao = self.criar_entradas()
        esperado = calcular_custo_ia_cenario(consumo, precos, cotacao)
        consumo["feedbacks_mensais"] = 2200
        precos["modelo"] = "Modelo de referência"
        cotacao["origem"] = "Didática"
        self.assertEqual(calcular_custo_ia_cenario(consumo, precos, cotacao), esperado)


class TestCalcularCustoInfraCenario(unittest.TestCase):
    def criar_entradas(self):
        precos = {
            "backend_mensal_por_unidade_usd": Decimal("5.00"),
            "banco_mensal_por_unidade_usd": Decimal("3.00"),
        }
        capacidade = {"quantidade_backend": 2, "quantidade_banco": 1}
        cotacao = {"brl_por_usd": Decimal("5.00")}
        return precos, capacidade, cotacao

    def test_calcula_custos_do_cenario_didatico(self):
        precos, capacidade, cotacao = self.criar_entradas()
        resultado = calcular_custo_infra_cenario(precos, capacidade, cotacao)
        esperado = {
            "custo_backend_mensal_usd": Decimal("10.00"),
            "custo_banco_mensal_usd": Decimal("3.00"),
            "custo_infra_mensal_usd": Decimal("13.00"),
            "custo_backend_mensal_br": Decimal("50.00"),
            "custo_banco_mensal_br": Decimal("15.00"),
            "custo_infra_mensal_br": Decimal("65.00"),
            "custo_infra_anual_usd": Decimal("156.00"),
            "custo_infra_anual_br": Decimal("780.00"),
        }
        self.assertEqual(resultado, esperado)
        for campo, valor in resultado.items():
            with self.subTest(campo=campo):
                self.assertIsInstance(valor, Decimal)

    def test_zero_unidades_em_cada_servico_e_nos_dois(self):
        for backend, banco, esperado in ((0, 1, "3"), (2, 0, "10"), (0, 0, "0")):
            precos, capacidade, cotacao = self.criar_entradas()
            capacidade["quantidade_backend"] = backend
            capacidade["quantidade_banco"] = banco
            with self.subTest(backend=backend, banco=banco):
                resultado = calcular_custo_infra_cenario(precos, capacidade, cotacao)
                self.assertEqual(resultado["custo_infra_mensal_usd"], Decimal(esperado))
                if backend == 0 and banco == 0:
                    for valor in resultado.values():
                        self.assertEqual(valor, Decimal("0"))

    def test_preco_gratuito_em_cada_servico_e_nos_dois(self):
        for backend, banco, esperado in (("0", "3", "3"), ("5", "0", "10"), ("0", "0", "0")):
            precos, capacidade, cotacao = self.criar_entradas()
            precos["backend_mensal_por_unidade_usd"] = Decimal(backend)
            precos["banco_mensal_por_unidade_usd"] = Decimal(banco)
            with self.subTest(backend=backend, banco=banco):
                resultado = calcular_custo_infra_cenario(precos, capacidade, cotacao)
                self.assertEqual(resultado["custo_infra_mensal_usd"], Decimal(esperado))

    def test_cotacao_aceita_tres_tipos_e_altera_apenas_os_valores_em_reais(self):
        for taxa in (5, 5.0, Decimal("5.00"), Decimal("6.00")):
            precos, capacidade, cotacao = self.criar_entradas()
            cotacao["brl_por_usd"] = taxa
            with self.subTest(taxa=taxa, tipo=type(taxa).__name__):
                resultado = calcular_custo_infra_cenario(precos, capacidade, cotacao)
                self.assertEqual(resultado["custo_infra_mensal_usd"], Decimal("13"))
                self.assertEqual(resultado["custo_infra_mensal_br"],
                                 Decimal("13") * Decimal(str(taxa)))

    def test_exige_dicionarios_nos_tres_argumentos(self):
        for valor in (None, [], "cenario", 100, True):
            precos, capacidade, cotacao = self.criar_entradas()
            with self.subTest(argumento="precos_infraestrutura", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_infra_cenario(valor, capacidade, cotacao)
            with self.subTest(argumento="hipoteses_capacidade", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_infra_cenario(precos, valor, cotacao)
            with self.subTest(argumento="cotacao", valor=valor):
                with self.assertRaises(TypeError):
                    calcular_custo_infra_cenario(precos, capacidade, valor)

    def test_recusa_cada_chave_obrigatoria_ausente(self):
        precos, capacidade, cotacao = self.criar_entradas()
        for grupo, dicionario in (("precos", precos), ("capacidade", capacidade), ("cotacao", cotacao)):
            for chave in dicionario.copy():
                copia = dicionario.copy()
                del dicionario[chave]
                with self.subTest(grupo=grupo, chave=chave):
                    with self.assertRaises(ValueError) as erro:
                        calcular_custo_infra_cenario(precos, capacidade, cotacao)
                    self.assertIn(chave, str(erro.exception))
                dicionario[chave] = copia[chave]

    def test_propaga_erros_de_precos(self):
        precos, capacidade, cotacao = self.criar_entradas()
        for chave in precos.copy():
            for tipo_erro, valores in ((TypeError, ("5", 5, 5.0, True, False, None, [], 1j)),
                                      (ValueError, (Decimal("-1"), Decimal("Infinity"), Decimal("-Infinity"), Decimal("NaN"), Decimal("sNaN")))):
                for valor in valores:
                    precos, capacidade, cotacao = self.criar_entradas()
                    precos[chave] = valor
                    with self.subTest(chave=chave, valor=valor, erro=tipo_erro.__name__):
                        with self.assertRaises(tipo_erro):
                            calcular_custo_infra_cenario(precos, capacidade, cotacao)

    def test_propaga_erros_de_quantidades(self):
        precos, capacidade, cotacao = self.criar_entradas()
        for chave in capacidade.copy():
            for tipo_erro, valores in ((TypeError, (1.5, 2.0, "2", True, False, None, Decimal("2"), [], 1j, float("inf"), float("-inf"), float("nan"))),
                                      (ValueError, (-1, -2))):
                for valor in valores:
                    precos, capacidade, cotacao = self.criar_entradas()
                    capacidade[chave] = valor
                    with self.subTest(chave=chave, valor=valor, erro=tipo_erro.__name__):
                        with self.assertRaises(tipo_erro):
                            calcular_custo_infra_cenario(precos, capacidade, cotacao)

    def test_propaga_erros_de_cotacao(self):
        precos, capacidade, cotacao = self.criar_entradas()
        for chave in cotacao.copy():
            for tipo_erro, valores in ((TypeError, ("5", True, False, None, [], 1j)),
                                      (ValueError, (0, 0.0, Decimal("0"), -1, -0.5, Decimal("-1"), float("inf"), float("-inf"), float("nan"), Decimal("Infinity"), Decimal("-Infinity"), Decimal("NaN"), Decimal("sNaN")))):
                for valor in valores:
                    precos, capacidade, cotacao = self.criar_entradas()
                    cotacao[chave] = valor
                    with self.subTest(chave=chave, valor=valor, erro=tipo_erro.__name__):
                        with self.assertRaises(tipo_erro):
                            calcular_custo_infra_cenario(precos, capacidade, cotacao)

    def test_nao_altera_as_tres_entradas(self):
        precos, capacidade, cotacao = self.criar_entradas()
        antes = (precos.copy(), capacidade.copy(), cotacao.copy())
        resultado = calcular_custo_infra_cenario(precos, capacidade, cotacao)
        self.assertEqual((precos, capacidade, cotacao), antes)
        for entrada in (precos, capacidade, cotacao):
            self.assertIsNot(resultado, entrada)

    def test_aceita_chaves_adicionais_sem_alterar_os_custos(self):
        precos, capacidade, cotacao = self.criar_entradas()
        esperado = calcular_custo_infra_cenario(precos, capacidade, cotacao)
        precos["origem"] = "Didática"
        capacidade["nome"] = "Cenário didático"
        cotacao["origem"] = "Manual"
        self.assertEqual(calcular_custo_infra_cenario(precos, capacidade, cotacao), esperado)


class TestCalcularCenario(unittest.TestCase):
    def criar_entradas(self):
        # A lista segue a ordem dos cinco argumentos de calcular_cenario.
        return [
            {
                "usuarios_ativos": 100, "respostas_por_usuario": 40,
                "taxa_acerto": 0.6, "proporcao_acertos_com_feedback": 0.25,
                "tokens_entrada": 500, "tokens_saida": 300,
            },
            {"quantidade_backend": 2, "quantidade_banco": 1},
            {"entrada_por_milhao_usd": Decimal("0.10"), "saida_por_milhao_usd": Decimal("0.50")},
            {"backend_mensal_por_unidade_usd": Decimal("5.00"),
             "banco_mensal_por_unidade_usd": Decimal("3.00")},
            {"brl_por_usd": Decimal("5.00")},
        ]

    def test_calcula_cenario_didatico_completo(self):
        resultado = calcular_cenario(*self.criar_entradas())
        esperado = {
            "consumo": {
                "respostas_mensais": 4000,
                "acertos_mensais": 2400,
                "erros_mensais": 1600,
                "feedbacks_nos_acertos": 600,
                "feedbacks_mensais": 2200,
                "tokens_entrada_total": 1_100_000,
                "tokens_saida_total": 660_000,
            },
            "custos_ia": {
                "custo_entrada_usd": Decimal("0.11"),
                "custo_saida_usd": Decimal("0.33"),
                "custo_ia_mensal_usd": Decimal("0.44"),
                "custo_entrada_br": Decimal("0.55"),
                "custo_saida_br": Decimal("1.65"),
                "custo_ia_mensal_br": Decimal("2.20"),
                "custo_ia_anual_usd": Decimal("5.28"),
                "custo_ia_anual_br": Decimal("26.40"),
            },
            "custos_infraestrutura": {
                "custo_backend_mensal_usd": Decimal("10"),
                "custo_banco_mensal_usd": Decimal("3"),
                "custo_infra_mensal_usd": Decimal("13"),
                "custo_backend_mensal_br": Decimal("50"),
                "custo_banco_mensal_br": Decimal("15"),
                "custo_infra_mensal_br": Decimal("65"),
                "custo_infra_anual_usd": Decimal("156"),
                "custo_infra_anual_br": Decimal("780"),
            },
            "totais": {
                "custo_total_mensal_usd": Decimal("13.44"),
                "custo_total_mensal_br": Decimal("67.20"),
                "custo_total_anual_usd": Decimal("161.28"),
                "custo_total_anual_br": Decimal("806.40"),
            },
        }
        self.assertEqual(resultado, esperado)
        for grupo in ("custos_ia", "custos_infraestrutura", "totais"):
            for campo, valor in resultado[grupo].items():
                with self.subTest(grupo=grupo, campo=campo):
                    self.assertIsInstance(valor, Decimal)

    def test_zero_usuarios_ou_respostas_mantem_infraestrutura(self):
        for campo in ("usuarios_ativos", "respostas_por_usuario"):
            entradas = self.criar_entradas()
            entradas[0][campo] = 0
            with self.subTest(campo=campo):
                resultado = calcular_cenario(*entradas)
                for valor in resultado["consumo"].values():
                    self.assertEqual(valor, 0)
                for valor in resultado["custos_ia"].values():
                    self.assertEqual(valor, Decimal("0"))
                self.assertEqual(resultado["totais"], {
                    "custo_total_mensal_usd": Decimal("13"),
                    "custo_total_mensal_br": Decimal("65"),
                    "custo_total_anual_usd": Decimal("156"),
                    "custo_total_anual_br": Decimal("780"),
                })

    def test_zero_unidades_mantem_apenas_custos_de_ia(self):
        entradas = self.criar_entradas()
        entradas[1]["quantidade_backend"] = 0
        entradas[1]["quantidade_banco"] = 0
        resultado = calcular_cenario(*entradas)
        for valor in resultado["custos_infraestrutura"].values():
            self.assertEqual(valor, Decimal("0"))
        self.assertEqual(resultado["totais"]["custo_total_mensal_usd"], Decimal("0.44"))
        self.assertEqual(resultado["totais"]["custo_total_anual_br"], Decimal("26.40"))

    def test_precos_gratuitos_zeram_custos_sem_zerar_consumo(self):
        entradas = self.criar_entradas()
        for indice in (2, 3):
            for chave in entradas[indice]:
                entradas[indice][chave] = Decimal("0")
        resultado = calcular_cenario(*entradas)
        self.assertEqual(resultado["consumo"]["feedbacks_mensais"], 2200)
        for grupo in ("custos_ia", "custos_infraestrutura", "totais"):
            for valor in resultado[grupo].values():
                self.assertEqual(valor, Decimal("0"))

    def test_mudar_cotacao_preserva_consumo_e_totais_em_dolares(self):
        entradas = self.criar_entradas()
        entradas[4]["brl_por_usd"] = Decimal("6")
        resultado = calcular_cenario(*entradas)
        self.assertEqual(resultado["consumo"]["feedbacks_mensais"], 2200)
        self.assertEqual(resultado["totais"], {
            "custo_total_mensal_usd": Decimal("13.44"),
            "custo_total_mensal_br": Decimal("80.64"),
            "custo_total_anual_usd": Decimal("161.28"),
            "custo_total_anual_br": Decimal("967.68"),
        })

    def test_propaga_tipo_invalido_em_cada_argumento(self):
        for indice in range(5):
            for valor in (None, [], "cenario", 100, True):
                entradas = self.criar_entradas()
                entradas[indice] = valor
                with self.subTest(argumento=indice, valor=valor):
                    with self.assertRaises(TypeError):
                        calcular_cenario(*entradas)

    def test_propaga_ausencia_de_cada_chave_obrigatoria(self):
        for indice, dicionario in enumerate(self.criar_entradas()):
            for chave in dicionario:
                entradas = self.criar_entradas()
                del entradas[indice][chave]
                with self.subTest(argumento=indice, chave=chave):
                    with self.assertRaises(ValueError) as erro:
                        calcular_cenario(*entradas)
                    self.assertIn(chave, str(erro.exception))

    def test_propaga_erros_numericos_de_cada_grupo(self):
        casos = (
            (0, "usuarios_ativos", 1.5, TypeError),
            (0, "taxa_acerto", 1.1, ValueError),
            (0, "tokens_entrada", float("nan"), ValueError),
            (1, "quantidade_backend", -1, ValueError),
            (1, "quantidade_banco", True, TypeError),
            (2, "entrada_por_milhao_usd", 0.1, TypeError),
            (2, "saida_por_milhao_usd", Decimal("-1"), ValueError),
            (3, "backend_mensal_por_unidade_usd", Decimal("Infinity"), ValueError),
            (3, "banco_mensal_por_unidade_usd", "3", TypeError),
            (4, "brl_por_usd", 0, ValueError),
            (4, "brl_por_usd", float("inf"), ValueError),
        )
        for indice, chave, valor, tipo_erro in casos:
            entradas = self.criar_entradas()
            entradas[indice][chave] = valor
            with self.subTest(argumento=indice, chave=chave, valor=valor):
                with self.assertRaises(tipo_erro):
                    calcular_cenario(*entradas)

    def test_nao_altera_as_cinco_entradas(self):
        entradas = self.criar_entradas()
        copias = []
        for entrada in entradas:
            copias.append(entrada.copy())
        resultado = calcular_cenario(*entradas)
        self.assertEqual(entradas, copias)
        for grupo in resultado.values():
            for entrada in entradas:
                self.assertIsNot(grupo, entrada)

    def test_resultados_de_execucoes_sao_independentes(self):
        entradas = self.criar_entradas()
        primeiro = calcular_cenario(*entradas)
        primeiro["consumo"]["respostas_mensais"] = -1
        segundo = calcular_cenario(*entradas)
        self.assertEqual(segundo["consumo"]["respostas_mensais"], 4000)
        self.assertEqual(entradas[0]["usuarios_ativos"], 100)

    def test_chaves_adicionais_nao_alteram_resultado(self):
        entradas = self.criar_entradas()
        esperado = calcular_cenario(*entradas)
        for entrada in entradas:
            entrada["observacao"] = "Cenário didático"
        self.assertEqual(calcular_cenario(*entradas), esperado)


class TestLerCenariosCsv(unittest.TestCase):
    colunas = [
        "cenario", "usuarios_ativos", "respostas_por_usuario", "taxa_acerto",
        "proporcao_acertos_com_feedback", "tokens_entrada", "tokens_saida",
    ]

    def setUp(self):
        temporario = TemporaryDirectory(prefix="liteart_cenarios_")
        self.addCleanup(temporario.cleanup)
        self.caminho = Path(temporario.name) / "cenarios.csv"
        self.registro = ["Cenário de teste", "100", "40", "0.60", "0.25", "500", "300"]

    def escrever(self, registros, colunas=None, encoding="utf-8"):
        with self.caminho.open("w", encoding=encoding, newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(self.colunas if colunas is None else colunas)
            escritor.writerows(registros)
        return self.caminho

    def test_leitura_valida_tipos_e_estrutura(self):
        self.escrever([self.registro])
        esperado = [{
            "nome": "Cenário de teste",
            "hipoteses_consumo": {
                "usuarios_ativos": 100, "respostas_por_usuario": 40.0,
                "taxa_acerto": 0.6, "proporcao_acertos_com_feedback": 0.25,
                "tokens_entrada": 500.0, "tokens_saida": 300.0,
            },
        }]
        for caminho in (self.caminho, str(self.caminho)):
            with self.subTest(caminho=caminho):
                resultado = ler_cenarios_csv(caminho)
                self.assertEqual(resultado, esperado)
                hipoteses = resultado[0]["hipoteses_consumo"]
                self.assertIs(type(hipoteses["usuarios_ativos"]), int)
                for coluna in self.colunas[2:]:
                    self.assertIs(type(hipoteses[coluna]), float)

    def test_exemplo_ordem_e_feedbacks_dos_dois_cenarios(self):
        caminho = Path(__file__).resolve().parent / "dados" / "cenarios_exemplo.csv"
        cenarios = ler_cenarios_csv(caminho)
        self.assertEqual([c["nome"] for c in cenarios], [
            "Cenário didático: 100 usuários", "Cenário didático: 500 usuários",
        ])
        self.assertEqual([c["hipoteses_consumo"]["usuarios_ativos"] for c in cenarios], [100, 500])
        self.assertEqual([
            calcular_consumo_cenario(c["hipoteses_consumo"])["feedbacks_mensais"]
            for c in cenarios
        ], [2200, 11000])

    def test_dicionarios_independentes(self):
        self.escrever([self.registro, ["Outro cenário", *self.registro[1:]]])
        primeiro, segundo = ler_cenarios_csv(self.caminho)
        self.assertIsNot(primeiro, segundo)
        self.assertIsNot(primeiro["hipoteses_consumo"], segundo["hipoteses_consumo"])
        primeiro["hipoteses_consumo"]["usuarios_ativos"] = 999
        self.assertEqual(segundo["hipoteses_consumo"]["usuarios_ativos"], 100)

    def test_remove_espacos_externos(self):
        self.escrever([[f"  {valor}  " for valor in self.registro]])
        resultado = ler_cenarios_csv(self.caminho)[0]
        self.assertEqual(resultado["nome"], "Cenário de teste")
        self.assertEqual(resultado["hipoteses_consumo"]["usuarios_ativos"], 100)

    def test_utf8_com_e_sem_bom(self):
        for encoding in ("utf-8", "utf-8-sig"):
            with self.subTest(encoding=encoding):
                self.escrever([self.registro], encoding=encoding)
                self.assertEqual(ler_cenarios_csv(self.caminho)[0]["nome"], "Cenário de teste")

    def test_colunas_em_outra_ordem(self):
        self.escrever([list(reversed(self.registro))], list(reversed(self.colunas)))
        self.assertEqual(ler_cenarios_csv(self.caminho)[0]["hipoteses_consumo"]["usuarios_ativos"], 100)

    def test_arquivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            ler_cenarios_csv(self.caminho)

    def test_arquivo_vazio(self):
        for conteudo in ("", "\ufeff"):
            with self.subTest(conteudo=conteudo):
                self.caminho.write_text(conteudo, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "CSV vazio"):
                    ler_cenarios_csv(self.caminho)

    def test_somente_cabecalho(self):
        self.escrever([])
        with self.assertRaisesRegex(ValueError, "sem registros"):
            ler_cenarios_csv(self.caminho)

    def test_colunas_ausentes_e_inesperadas(self):
        casos = [
            (self.colunas[:-1], "tokens_saida"),
            ([*self.colunas, "preco"], "preco"),
            (["nome", *self.colunas[1:]], "cenario"),
            ([*self.colunas, "taxa_acerto"], "taxa_acerto"),
        ]
        for colunas, nome in casos:
            with self.subTest(colunas=colunas):
                self.escrever([], colunas)
                with self.assertRaises(ValueError) as erro:
                    ler_cenarios_csv(self.caminho)
                self.assertIn(nome, str(erro.exception))
                self.assertIn("Colunas incorretas", str(erro.exception))

    def test_campos_vazios_identificam_registro_e_coluna(self):
        for indice, coluna in enumerate(self.colunas):
            for vazio in ("", "   "):
                with self.subTest(coluna=coluna, vazio=vazio):
                    registro = self.registro.copy()
                    registro[indice] = vazio
                    self.escrever([self.registro, registro])
                    with self.assertRaises(ValueError) as erro:
                        ler_cenarios_csv(self.caminho)
                    self.assertIn("Registro 2", str(erro.exception))
                    self.assertIn(coluna, str(erro.exception))
                    self.assertIn("vazio", str(erro.exception))

    def test_textos_numericos_invalidos(self):
        for indice, coluna in enumerate(self.colunas[1:], start=1):
            with self.subTest(coluna=coluna):
                registro = self.registro.copy()
                registro[indice] = "abc"
                self.escrever([registro])
                with self.assertRaises(ValueError) as erro:
                    ler_cenarios_csv(self.caminho)
                self.assertIn("Registro 1", str(erro.exception))
                self.assertIn(coluna, str(erro.exception))

    def test_negativos_em_todas_as_hipoteses(self):
        for indice, coluna in enumerate(self.colunas[1:], start=1):
            with self.subTest(coluna=coluna):
                registro = self.registro.copy()
                registro[indice] = "-1"
                self.escrever([registro])
                with self.assertRaises(ValueError) as erro:
                    ler_cenarios_csv(self.caminho)
                self.assertIn("Registro 1", str(erro.exception))
                self.assertIn(coluna, str(erro.exception))

    def test_infinito_nan_e_overflow(self):
        for indice, coluna in enumerate(self.colunas[1:], start=1):
            for invalido in ("inf", "-inf", "Infinity", "NaN", "1e999"):
                with self.subTest(coluna=coluna, invalido=invalido):
                    registro = self.registro.copy()
                    registro[indice] = invalido
                    self.escrever([registro])
                    with self.assertRaises(ValueError) as erro:
                        ler_cenarios_csv(self.caminho)
                    self.assertIn("Registro 1", str(erro.exception))
                    self.assertIn(coluna, str(erro.exception))

    def test_usuarios_fracionarios_nao_sao_truncados(self):
        for invalido in ("100.5", "100.0"):
            with self.subTest(invalido=invalido):
                registro = self.registro.copy()
                registro[1] = invalido
                self.escrever([registro])
                with self.assertRaisesRegex(ValueError, "Registro 1.*usuarios_ativos.*inteiro"):
                    ler_cenarios_csv(self.caminho)

    def test_taxas_acima_de_um(self):
        for indice in (3, 4):
            with self.subTest(coluna=self.colunas[indice]):
                registro = self.registro.copy()
                registro[indice] = "1.01"
                self.escrever([registro])
                with self.assertRaisesRegex(ValueError, f"Registro 1.*{self.colunas[indice]}.*entre 0 e 1"):
                    ler_cenarios_csv(self.caminho)

    def test_zero_usuarios_e_taxas_nos_limites(self):
        for taxa in ("0", "1"):
            with self.subTest(taxa=taxa):
                self.escrever([["Limites", "0", "0", taxa, taxa, "0", "0"]])
                hipoteses = ler_cenarios_csv(self.caminho)[0]["hipoteses_consumo"]
                self.assertEqual(hipoteses["usuarios_ativos"], 0)
                self.assertEqual(hipoteses["taxa_acerto"], float(taxa))
                self.assertEqual(hipoteses["proporcao_acertos_com_feedback"], float(taxa))
                self.assertEqual(calcular_consumo_cenario(hipoteses)["feedbacks_mensais"], 0)

    def test_medias_fracionarias_validas(self):
        self.escrever([["Frações", "100", "40.5", "0.60", "0.25", "500.5", "300.25"]])
        hipoteses = ler_cenarios_csv(self.caminho)[0]["hipoteses_consumo"]
        self.assertEqual(hipoteses["respostas_por_usuario"], 40.5)
        self.assertEqual(hipoteses["tokens_entrada"], 500.5)
        self.assertEqual(hipoteses["tokens_saida"], 300.25)
        self.assertEqual(calcular_consumo_cenario(hipoteses)["respostas_mensais"], 4050)

    def test_campos_extras_nao_viram_indice_nem_sao_descartados(self):
        for registros in (
            [[*self.registro, "extra"]],
            [self.registro, [*self.registro, "extra"]],
            [[*self.registro, ""]],
        ):
            with self.subTest(registros=registros):
                self.escrever(registros)
                with self.assertRaisesRegex(ValueError, "CSV malformado"):
                    ler_cenarios_csv(self.caminho)

    def test_registro_com_campos_faltando(self):
        self.escrever([self.registro, self.registro[:-1]])
        with self.assertRaisesRegex(ValueError, "Registro 2.*tokens_saida.*vazio"):
            ler_cenarios_csv(self.caminho)

    def test_aspas_malformadas(self):
        self.escrever([])
        with self.caminho.open("a", encoding="utf-8") as arquivo:
            arquivo.write('"Nome sem fechar,100,40,0.6,0.25,500,300\n')
        with self.assertRaisesRegex(ValueError, "CSV malformado"):
            ler_cenarios_csv(self.caminho)

    def test_registro_em_branco_nao_e_descartado(self):
        self.escrever([self.registro, [], self.registro])
        with self.assertRaisesRegex(ValueError, "Registro 2.*cenario.*vazio"):
            ler_cenarios_csv(self.caminho)

    def test_numero_de_registro_independe_de_linhas_fisicas(self):
        primeiro = ["Nome com vírgula,\ne quebra de linha", *self.registro[1:]]
        segundo = ["Segundo", "abc", *self.registro[2:]]
        self.escrever([primeiro, segundo])
        with self.assertRaisesRegex(ValueError, "Registro 2.*usuarios_ativos"):
            ler_cenarios_csv(self.caminho)

    def test_nao_imprime_nem_altera_o_arquivo(self):
        self.escrever([self.registro])
        antes = self.caminho.read_bytes()
        arquivos_antes = list(self.caminho.parent.iterdir())
        with redirect_stdout(io.StringIO()) as saida:
            ler_cenarios_csv(self.caminho)
        self.assertEqual(saida.getvalue(), "")
        self.assertEqual(self.caminho.read_bytes(), antes)
        self.assertEqual(list(self.caminho.parent.iterdir()), arquivos_antes)

    def test_importacao_nao_le_csv_nem_cria_arquivos(self):
        script = Path(__file__).resolve().parent / "calculadora.py"
        with patch("pandas.read_csv", side_effect=AssertionError("leitura na importação")), \
                patch("pandas.DataFrame.to_csv", side_effect=AssertionError("exportação na importação")), \
                patch.object(Path, "mkdir", side_effect=AssertionError("mkdir na importação")), \
                redirect_stdout(io.StringIO()) as saida:
            estado = runpy.run_path(str(script), run_name="calculadora_importada")
        self.assertEqual(saida.getvalue(), "")
        self.assertIn("ler_cenarios_csv", estado)
        self.assertNotIn("tabela_cenarios", estado)


if __name__ == "__main__":
    unittest.main()
