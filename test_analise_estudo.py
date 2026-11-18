"""Testes isolados da rotina do estudo; não escrevem nos resultados do projeto."""

from contextlib import redirect_stdout
from copy import deepcopy
import csv
from decimal import Decimal
import io
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import pandas as pd
from pandas.testing import assert_frame_equal

import analise_estudo as estudo


class TestAnaliseEstudo(unittest.TestCase):
    def setUp(self):
        temporario = TemporaryDirectory(prefix="liteart_estudo_")
        self.addCleanup(temporario.cleanup)
        self.raiz = Path(temporario.name).resolve()
        self.cenarios = self.raiz / "cenarios.csv"
        self.condicoes = self.raiz / "condicoes.csv"
        self.saida = self.raiz / "resultados" / "resultados_cenarios.csv"
        origem = Path(__file__).resolve().parent / "dados" / "estudo_de_caso"
        self.cenarios.write_bytes((origem / "cenarios.csv").read_bytes())
        self.condicoes.write_bytes((origem / "condicoes_fixas.csv").read_bytes())

    def ler_texto(self, caminho):
        with caminho.open(encoding="utf-8", newline="") as arquivo:
            return list(csv.DictReader(arquivo))

    def escrever(self, caminho, registros, colunas=None, encoding="utf-8"):
        if colunas is None:
            colunas = estudo.COLUNAS_CENARIOS if caminho == self.cenarios else estudo.COLUNAS_CONDICOES
        with caminho.open("w", encoding=encoding, newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)
            escritor.writeheader()
            escritor.writerows(registros)

    def alterar(self, caminho, campo, valor, numero=0):
        registros = self.ler_texto(caminho)
        registros[numero][campo] = valor
        self.escrever(caminho, registros)

    def executar(self):
        with redirect_stdout(io.StringIO()) as texto:
            tabela = estudo.executar_estudo(self.cenarios, self.condicoes, self.saida)
        return tabela, texto.getvalue()

    def test_leitura_valida_tipos_ordem_e_dicionarios_independentes(self):
        cenarios = estudo.ler_cenarios_estudo(str(self.cenarios))
        self.assertEqual([c["id_cenario"] for c in cenarios], [f"C{i:02d}" for i in range(1, 14)])
        self.assertIn("usuários", cenarios[0]["cenario"])
        self.assertIn("referência", cenarios[4]["cenario"])
        for cenario in cenarios:
            hipoteses = cenario["hipoteses_consumo"]
            self.assertIs(type(hipoteses["usuarios_ativos"]), int)
            for campo in estudo.COLUNAS_HIPOTESES[1:]:
                self.assertIs(type(hipoteses[campo]), float)
        cenarios[0]["hipoteses_consumo"]["usuarios_ativos"] = 999
        self.assertEqual(cenarios[1]["hipoteses_consumo"]["usuarios_ativos"], 100)

    def test_condicoes_validas_preservam_precisao_fontes_e_datas(self):
        condicoes = estudo.ler_condicoes_fixas(self.condicoes)
        originais = self.ler_texto(self.condicoes)[0]
        for campo in estudo.COLUNAS_CONDICOES:
            if campo in estudo.CAMPOS_FINANCEIROS:
                self.assertIsInstance(condicoes[campo], Decimal)
                self.assertEqual(condicoes[campo].as_tuple(), Decimal(originais[campo]).as_tuple())
            else:
                self.assertEqual(condicoes[campo], originais[campo])

    def test_utf8_bom_e_espacos_externos(self):
        for caminho, leitor in ((self.cenarios, estudo.ler_cenarios_estudo),
                                (self.condicoes, estudo.ler_condicoes_fixas)):
            registros = self.ler_texto(caminho)
            esperado = leitor(caminho)
            for registro in registros:
                for campo in registro:
                    registro[campo] = f"  {registro[campo]}  "
            self.escrever(caminho, registros, encoding="utf-8-sig")
            self.assertEqual(leitor(caminho), esperado)

    def test_colunas_ausentes_inesperadas_duplicadas_e_fora_de_ordem(self):
        for caminho, colunas, leitor in (
            (self.cenarios, estudo.COLUNAS_CENARIOS, estudo.ler_cenarios_estudo),
            (self.condicoes, estudo.COLUNAS_CONDICOES, estudo.ler_condicoes_fixas),
        ):
            for cabecalho in (colunas[:-1], (*colunas, "extra"),
                              (*colunas[:-1], colunas[0]), tuple(reversed(colunas))):
                with self.subTest(caminho=caminho, cabecalho=cabecalho):
                    caminho.write_text(
                        ",".join(cabecalho) + "\n", encoding="utf-8"
                    )
                    with self.assertRaisesRegex(ValueError, "colunas incorretas"):
                        leitor(caminho)

    def test_arquivos_vazios_ou_somente_cabecalho(self):
        for caminho, colunas, leitor in (
            (self.cenarios, estudo.COLUNAS_CENARIOS, estudo.ler_cenarios_estudo),
            (self.condicoes, estudo.COLUNAS_CONDICOES, estudo.ler_condicoes_fixas),
        ):
            for conteudo in ("", ",".join(colunas) + "\n"):
                with self.subTest(caminho=caminho, conteudo=conteudo):
                    caminho.write_text(conteudo, encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, str(caminho).replace("\\", "\\\\")):
                        leitor(caminho)

    def test_arquivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            estudo.ler_cenarios_estudo(self.raiz / "inexistente.csv")

    def test_campos_obrigatorios_vazios_identificam_arquivo_registro_e_campo(self):
        for caminho, colunas, leitor in (
            (self.cenarios, estudo.COLUNAS_CENARIOS, estudo.ler_cenarios_estudo),
            (self.condicoes, estudo.COLUNAS_CONDICOES, estudo.ler_condicoes_fixas),
        ):
            original = caminho.read_bytes()
            for campo in colunas:
                with self.subTest(campo=campo):
                    caminho.write_bytes(original)
                    self.alterar(caminho, campo, "  ")
                    with self.assertRaises(ValueError) as erro:
                        leitor(caminho)
                    self.assertIn(str(caminho), str(erro.exception))
                    self.assertIn("registro 1", str(erro.exception))
                    self.assertIn(f"'{campo}'", str(erro.exception))

    def test_identificador_duplicado(self):
        self.alterar(self.cenarios, "id_cenario", "C01", numero=1)
        with self.assertRaisesRegex(ValueError, "registro 2.*id_cenario.*duplicado"):
            estudo.ler_cenarios_estudo(self.cenarios)

    def test_cobertura_ausente_ou_identificador_inesperado(self):
        registros = self.ler_texto(self.cenarios)
        for alterados in (registros[:-1], [{**registros[0], "id_cenario": "C14"}, *registros[1:]]):
            with self.subTest(quantidade=len(alterados)):
                self.escrever(self.cenarios, alterados)
                with self.assertRaisesRegex(ValueError, "cobertura C01 a C13"):
                    estudo.ler_cenarios_estudo(self.cenarios)

    def test_combinacoes_duplicadas(self):
        registros = self.ler_texto(self.cenarios)
        for campo in estudo.COLUNAS_HIPOTESES:
            registros[1][campo] = registros[0][campo]
        self.escrever(self.cenarios, registros)
        with self.assertRaisesRegex(ValueError, "registro 2.*combinação.*duplicada"):
            estudo.ler_cenarios_estudo(self.cenarios)

    def test_usuarios_fracionarios_nao_sao_truncados(self):
        for valor in ("100.5", "100.0"):
            with self.subTest(valor=valor):
                self.alterar(self.cenarios, "usuarios_ativos", valor)
                with self.assertRaisesRegex(ValueError, "registro 1.*usuarios_ativos.*inteiro"):
                    estudo.ler_cenarios_estudo(self.cenarios)

    def test_hipoteses_nao_numericas_negativas_infinito_e_nan(self):
        original = self.cenarios.read_bytes()
        for campo in estudo.COLUNAS_HIPOTESES:
            for valor in ("texto", "-1", "Infinity", "NaN"):
                with self.subTest(campo=campo, valor=valor):
                    self.cenarios.write_bytes(original)
                    self.alterar(self.cenarios, campo, valor)
                    with self.assertRaisesRegex(ValueError, f"registro 1.*{campo}"):
                        estudo.ler_cenarios_estudo(self.cenarios)

    def test_taxas_fora_do_intervalo(self):
        original = self.cenarios.read_bytes()
        for campo in ("taxa_acerto", "proporcao_acertos_com_feedback"):
            for valor in ("-0.1", "1.01"):
                with self.subTest(campo=campo, valor=valor):
                    self.cenarios.write_bytes(original)
                    self.alterar(self.cenarios, campo, valor)
                    with self.assertRaisesRegex(ValueError, f"registro 1.*{campo}"):
                        estudo.ler_cenarios_estudo(self.cenarios)

    def test_zero_limites_das_taxas_e_medias_fracionarias(self):
        registros = self.ler_texto(self.cenarios)
        registros[0].update(usuarios_ativos="0", respostas_por_usuario="40.5",
                            taxa_acerto="0", proporcao_acertos_com_feedback="1",
                            tokens_entrada="250.5", tokens_saida="150.5")
        self.escrever(self.cenarios, registros)
        hipoteses = estudo.ler_cenarios_estudo(self.cenarios)[0]["hipoteses_consumo"]
        self.assertEqual(hipoteses, dict(zip(estudo.COLUNAS_HIPOTESES,
                                           (0, 40.5, 0.0, 1.0, 250.5, 150.5))))

    def test_condicoes_com_multiplas_linhas(self):
        registro = self.ler_texto(self.condicoes)[0]
        self.escrever(self.condicoes, [registro, registro])
        with self.assertRaisesRegex(ValueError, "exatamente uma linha"):
            estudo.ler_condicoes_fixas(self.condicoes)

    def test_financeiros_exigem_decimal_finito_positivo(self):
        original = self.condicoes.read_bytes()
        for campo in estudo.CAMPOS_FINANCEIROS:
            for valor in ("texto", "0", "-0.1", "Infinity", "NaN", "sNaN"):
                with self.subTest(campo=campo, valor=valor):
                    self.condicoes.write_bytes(original)
                    self.alterar(self.condicoes, campo, valor)
                    with self.assertRaisesRegex(ValueError, f"registro 1.*{campo}"):
                        estudo.ler_condicoes_fixas(self.condicoes)

    def test_datas_invalidas_e_formato_iso_estrito(self):
        original = self.condicoes.read_bytes()
        for campo in estudo.CAMPOS_DATAS:
            for valor in ("2026-02-30", "18/11/2026", "20261118", "2026-W47-3"):
                with self.subTest(campo=campo, valor=valor):
                    self.condicoes.write_bytes(original)
                    self.alterar(self.condicoes, campo, valor)
                    with self.assertRaisesRegex(ValueError, f"registro 1.*{campo}.*ISO"):
                        estudo.ler_condicoes_fixas(self.condicoes)

    def test_csv_malformado_campos_extras_ausentes_e_linha_vazia(self):
        cabecalho = ",".join(estudo.COLUNAS_CENARIOS) + "\n"
        for linha in ("C01,nome,100,40,0.60,0,500,300,extra\n", "C01,nome\n",
                      "\n", 'C01,"nome sem fechamento\n'):
            with self.subTest(linha=linha):
                self.cenarios.write_text(cabecalho + linha, encoding="utf-8")
                with self.assertRaises(ValueError):
                    estudo.ler_cenarios_estudo(self.cenarios)

    def test_codificacao_invalida(self):
        self.cenarios.write_bytes(b"\xff\xfe")
        with self.assertRaisesRegex(ValueError, "CSV inválido"):
            estudo.ler_cenarios_estudo(self.cenarios)

    def test_calculos_do_estudo_formula_independente_e_decimal(self):
        tabela, _ = self.executar()
        self.assertEqual(tabela.shape, (13, 35))
        self.assertEqual(list(tabela["id_cenario"]), [f"C{i:02d}" for i in range(1, 14)])
        por_id = tabela.set_index("id_cenario")
        for identificador, esperado in (
            ("C02", (2200, 1100000, 660000, Decimal("0.44"))),
            ("C05", (11000, 5500000, 3300000, Decimal("2.20"))),
        ):
            linha = por_id.loc[identificador]
            self.assertEqual(tuple(linha[c] for c in (
                "feedbacks_mensais", "tokens_entrada_total", "tokens_saida_total",
                "custo_ia_mensal_usd")), esperado)
            self.assertEqual(linha["custo_ia_mensal_br"], esperado[-1] * Decimal("5.8102"))
        # Fórmulas independentes em Decimal: não chamam as funções de cálculo do MVP.
        for linha in tabela.to_dict("records"):
            respostas = Decimal(str(linha["usuarios_ativos"])) * Decimal(str(linha["respostas_por_usuario"]))
            taxa = Decimal(str(linha["taxa_acerto"]))
            proporcao = Decimal(str(linha["proporcao_acertos_com_feedback"]))
            feedbacks = respostas * ((1 - taxa) + taxa * proporcao)
            entrada = feedbacks * Decimal(str(linha["tokens_entrada"]))
            saida = feedbacks * Decimal(str(linha["tokens_saida"]))
            usd = (entrada * Decimal("0.10") + saida * Decimal("0.50")) / Decimal("1000000")
            self.assertEqual(Decimal(str(linha["feedbacks_mensais"])), feedbacks)
            self.assertEqual(Decimal(str(linha["tokens_entrada_total"])), entrada)
            self.assertEqual(Decimal(str(linha["tokens_saida_total"])), saida)
            self.assertEqual(linha["custo_ia_mensal_usd"], usd)
            self.assertEqual(linha["custo_ia_mensal_br"], usd * Decimal("5.8102"))
            self.assertEqual(linha["custo_ia_anual_usd"], usd * 12)
            self.assertEqual(linha["custo_ia_anual_br"], usd * Decimal("5.8102") * 12)
            for campo, valor in linha.items():
                if campo.startswith("custo_") or campo in estudo.CAMPOS_FINANCEIROS:
                    self.assertIsInstance(valor, Decimal)

    def test_sensibilidade_preserva_feedbacks_e_altera_tokens_correspondentes(self):
        tabela, _ = self.executar()
        linhas = tabela.set_index("id_cenario")
        referencia = linhas.loc["C05"]
        for identificador, fator_entrada, fator_saida in (
            ("C10", 0.5, 1), ("C11", 2, 1), ("C12", 1, 0.5), ("C13", 1, 2),
        ):
            self.assertEqual(linhas.loc[identificador, "feedbacks_mensais"], referencia["feedbacks_mensais"])
            self.assertEqual(linhas.loc[identificador, "tokens_entrada_total"],
                             referencia["tokens_entrada_total"] * fator_entrada)
            self.assertEqual(linhas.loc[identificador, "tokens_saida_total"],
                             referencia["tokens_saida_total"] * fator_saida)

    def test_politicas_na_mesma_escala_nao_reduzem_consumo_ou_custo(self):
        tabela, _ = self.executar()
        for inicio in (0, 3, 6):
            for campo in ("feedbacks_mensais", "tokens_entrada_total", "tokens_saida_total",
                          "custo_ia_mensal_usd", "custo_ia_mensal_br"):
                valores = list(tabela.iloc[inicio:inicio + 3][campo])
                self.assertEqual(valores, sorted(valores))

    def test_calculo_reutiliza_mvp_sem_alterar_entradas_ou_consultar_rede(self):
        cenarios = estudo.ler_cenarios_estudo(self.cenarios)
        condicoes = estudo.ler_condicoes_fixas(self.condicoes)
        antes = deepcopy((cenarios, condicoes))
        with patch.object(estudo, "calcular_consumo_cenario", wraps=estudo.calcular_consumo_cenario) as consumo, \
                patch.object(estudo, "calcular_custo_ia_cenario", wraps=estudo.calcular_custo_ia_cenario) as custo, \
                patch("urllib.request.urlopen", side_effect=AssertionError("Rede proibida")):
            tabela = estudo.calcular_resultados(cenarios, condicoes)
        self.assertEqual(consumo.call_count, 13)
        self.assertEqual(custo.call_count, 13)
        self.assertEqual((cenarios, condicoes), antes)
        for campo, valor in condicoes.items():
            self.assertEqual(list(tabela[campo]), [valor] * 13)

    def test_tarifas_e_cambio_vem_do_arquivo_nao_de_constantes_comerciais(self):
        self.alterar(self.condicoes, "preco_entrada_por_milhao_usd", "0.123456789")
        self.alterar(self.condicoes, "brl_por_usd", "6.123456789")
        tabela, _ = self.executar()
        linha = tabela.iloc[1]
        esperado = Decimal("1.1") * Decimal("0.123456789") + Decimal("0.66") * Decimal("0.50")
        self.assertEqual(linha["custo_ia_mensal_usd"], esperado)
        self.assertEqual(linha["custo_ia_mensal_br"], esperado * Decimal("6.123456789"))

    def test_exportacao_completa_precisa_sem_indice_e_sem_modificar_tabela(self):
        self.alterar(self.condicoes, "brl_por_usd", "5.81023456789")
        tabela, texto = self.executar()
        antes = tabela.copy(deep=True)
        estudo.exportar_resultados(tabela, self.saida)
        with redirect_stdout(io.StringIO()):
            estudo.apresentar_resultados(tabela)
        assert_frame_equal(tabela, antes, check_exact=True)
        with self.saida.open(encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            self.assertEqual(leitor.fieldnames, list(tabela.columns))
            registros = list(leitor)
        self.assertEqual(len(registros), 13)
        self.assertEqual(len(registros[0]), 35)
        for registro, original in zip(registros, tabela.to_dict("records"), strict=True):
            self.assertEqual(registro["cenario"], original["cenario"])
            for campo, valor in original.items():
                if isinstance(valor, Decimal):
                    self.assertEqual(Decimal(registro[campo]).as_tuple(), valor.as_tuple())
                    self.assertEqual(registro[campo], str(valor))
        self.assertIn("US$ 0,44", texto)
        self.assertIn("R$ 2,56", texto)
        self.assertNotIn("{'", texto)

    def test_erro_de_validacao_nao_sobrescreve_resultado_nem_apresenta_parciais(self):
        self.saida.parent.mkdir()
        self.saida.write_bytes(b"resultado anterior\n")
        for caminho, campo, valor in ((self.cenarios, "taxa_acerto", "2"),
                                     (self.condicoes, "brl_por_usd", "0")):
            original = caminho.read_bytes()
            self.alterar(caminho, campo, valor)
            with redirect_stdout(io.StringIO()) as texto, self.assertRaises(ValueError):
                estudo.executar_estudo(self.cenarios, self.condicoes, self.saida)
            self.assertEqual(self.saida.read_bytes(), b"resultado anterior\n")
            self.assertEqual(texto.getvalue(), "")
            caminho.write_bytes(original)

    def test_erro_de_calculo_nao_sobrescreve_resultado(self):
        self.saida.parent.mkdir()
        self.saida.write_bytes(b"anterior")
        with patch.object(estudo, "calcular_custo_ia_cenario", side_effect=ValueError("inválido")), \
                self.assertRaises(ValueError):
            self.executar()
        self.assertEqual(self.saida.read_bytes(), b"anterior")

    def test_main_encerra_com_codigo_nao_zero_e_mensagem_clara(self):
        with patch.object(estudo, "executar_estudo", side_effect=ValueError("registro 2 inválido")), \
                self.assertRaises(SystemExit) as erro:
            estudo.main()
        self.assertIsInstance(erro.exception.code, str)  # SystemExit com texto tem código 1.
        self.assertIn("Estudo não executado", erro.exception.code)

    def test_importacao_sem_leitura_interacao_rede_ou_exportacao(self):
        with patch("builtins.input", side_effect=AssertionError("input")), \
                patch("pathlib.Path.open", side_effect=AssertionError("leitura")), \
                patch("pathlib.Path.mkdir", side_effect=AssertionError("mkdir")), \
                patch("urllib.request.urlopen", side_effect=AssertionError("rede")), \
                patch.object(pd.DataFrame, "to_csv", side_effect=AssertionError("exportação")), \
                redirect_stdout(io.StringIO()) as texto:
            runpy.run_path(str(Path(estudo.__file__)), run_name="importacao_estudo")
        self.assertEqual(texto.getvalue(), "")

    def test_caminhos_independentes_da_pasta_atual_e_reexecucao_sem_duplicacao(self):
        origem = Path(__file__).resolve().parent
        for nome in ("analise_estudo.py", "calculadora.py"):
            shutil.copyfile(origem / nome, self.raiz / nome)
        entrada = self.raiz / "dados" / "estudo_de_caso"
        entrada.mkdir(parents=True)
        shutil.copyfile(self.cenarios, entrada / "cenarios.csv")
        shutil.copyfile(self.condicoes, entrada / "condicoes_fixas.csv")
        outra_pasta = self.raiz / "outra_pasta"
        outra_pasta.mkdir()
        comando = [sys.executable, "-X", "utf8", "-B", str(self.raiz / "analise_estudo.py")]
        saida = self.raiz / "resultados" / "estudo_de_caso" / "resultados_cenarios.csv"
        for _ in range(2):
            processo = subprocess.run(comando, cwd=outra_pasta, capture_output=True,
                                      text=True, encoding="utf-8", timeout=30)
            self.assertEqual(processo.returncode, 0, processo.stderr)
            self.assertEqual(len(self.ler_texto(saida)), 13)
        anterior = saida.read_bytes()
        (entrada / "cenarios.csv").unlink()
        processo = subprocess.run(comando, cwd=outra_pasta, capture_output=True,
                                  text=True, encoding="utf-8", timeout=30)
        self.assertNotEqual(processo.returncode, 0)
        self.assertIn("Estudo não executado", processo.stderr)
        self.assertEqual(saida.read_bytes(), anterior)


if __name__ == "__main__":
    unittest.main()
