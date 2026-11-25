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


    def resultados_comparacoes(self):
        return estudo.calcular_resultados(
            estudo.ler_cenarios_estudo(self.cenarios), estudo.ler_condicoes_fixas(self.condicoes),
        )

    def test_comparacao_politicas_referencias_custos_e_reducoes_independentes(self):
        politicas = estudo.comparar_politicas(self.resultados_comparacoes())
        esperados = (
            ("C01", "C03", "0.32", "0.80", "60"),
            ("C02", "C03", "0.44", "0.80", "45"),
            ("C04", "C06", "1.60", "4.00", "60"),
            ("C05", "C06", "2.20", "4.00", "45"),
            ("C07", "C09", "3.20", "8.00", "60"),
            ("C08", "C09", "4.40", "8.00", "45"),
        )
        self.assertEqual(len(politicas), 6)
        for linha, (id_, ref, custo, base, percentual) in zip(
            politicas.to_dict("records"), esperados, strict=True,
        ):
            self.assertEqual((linha["id_cenario"], linha["id_referencia"]), (id_, ref))
            custo_br = Decimal(custo) * Decimal("5.8102")
            base_br = Decimal(base) * Decimal("5.8102")
            self.assertEqual(linha["custo_politica_mensal_br"], custo_br)
            self.assertEqual(linha["custo_referencia_mensal_br"], base_br)
            self.assertEqual(linha["reducao_mensal_br"], base_br - custo_br)
            self.assertEqual(linha["reducao_percentual"], Decimal(percentual))
            for campo in ("custo_politica_mensal_br", "custo_referencia_mensal_br",
                          "reducao_mensal_br", "reducao_percentual", *estudo.CAMPOS_FINANCEIROS):
                self.assertIsInstance(linha[campo], Decimal)

    def test_sensibilidade_custos_diferencas_percentuais_e_campos_alterados(self):
        tabela = self.resultados_comparacoes()
        self.assertEqual(tabela.set_index("id_cenario").loc["C05", "custo_ia_mensal_usd"], Decimal("2.20"))
        sensibilidade = estudo.analisar_sensibilidade(tabela)
        esperados = (
            ("C10", "tokens_entrada", "1.925", "-12.5", 250, 300),
            ("C11", "tokens_entrada", "2.75", "25", 1000, 300),
            ("C12", "tokens_saida", "1.375", "-37.5", 500, 150),
            ("C13", "tokens_saida", "3.85", "75", 500, 600),
        )
        self.assertEqual(len(sensibilidade), 4)
        for linha, (id_, campo, usd, percentual, entrada, saida) in zip(
            sensibilidade.to_dict("records"), esperados, strict=True,
        ):
            self.assertEqual((linha["id_cenario"], linha["id_referencia"]), (id_, "C05"))
            self.assertEqual(linha["campo_alterado"], campo)
            self.assertEqual((linha["tokens_entrada_referencia"], linha["tokens_saida_referencia"]), (500, 300))
            self.assertEqual((linha["tokens_entrada_cenario"], linha["tokens_saida_cenario"]), (entrada, saida))
            self.assertEqual(tabela.set_index("id_cenario").loc[id_, "custo_ia_mensal_usd"], Decimal(usd))
            custo_br = Decimal(usd) * Decimal("5.8102")
            base_br = Decimal("2.20") * Decimal("5.8102")
            self.assertEqual(linha["custo_cenario_mensal_br"], custo_br)
            self.assertEqual(linha["custo_referencia_mensal_br"], base_br)
            self.assertEqual(linha["variacao_mensal_br"], custo_br - base_br)
            self.assertEqual(linha["variacao_percentual"], Decimal(percentual))
            for coluna in ("custo_cenario_mensal_br", "custo_referencia_mensal_br",
                           "variacao_mensal_br", "variacao_percentual"):
                self.assertIsInstance(linha[coluna], Decimal)

    def test_comparacoes_por_identificador_independem_da_ordem_e_do_indice(self):
        tabela = self.resultados_comparacoes()
        reordenada = tabela.iloc[::-1].copy()
        reordenada.index = ["mesmo_indice"] * 13
        for funcao in (estudo.comparar_politicas, estudo.analisar_sensibilidade):
            assert_frame_equal(funcao(reordenada), funcao(tabela), check_exact=True)

    def test_comparacoes_nao_alteram_entradas_nem_recalculam_mvp(self):
        tabela = self.resultados_comparacoes()
        antes = tabela.copy(deep=True)
        with patch.object(estudo, "calcular_consumo_cenario", side_effect=AssertionError("recálculo")), \
                patch.object(estudo, "calcular_custo_ia_cenario", side_effect=AssertionError("recálculo")):
            politicas = estudo.comparar_politicas(tabela)
            sensibilidade = estudo.analisar_sensibilidade(tabela)
        with redirect_stdout(io.StringIO()):
            estudo.apresentar_comparacoes(politicas, sensibilidade)
        assert_frame_equal(tabela, antes, check_exact=True)

    def test_comparacoes_rejeitam_identificadores_ausentes_ou_duplicados(self):
        tabela = self.resultados_comparacoes()
        for funcao, ids in (
            (estudo.comparar_politicas, [f"C{i:02d}" for i in range(1, 10)]),
            (estudo.analisar_sensibilidade, ["C05", "C10", "C11", "C12", "C13"]),
        ):
            for id_ in ids:
                with self.subTest(funcao=funcao.__name__, id=id_):
                    with self.assertRaisesRegex(ValueError, f"ausentes.*{id_}"):
                        funcao(tabela[tabela["id_cenario"] != id_])
                    duplicada = pd.concat([tabela, tabela[tabela["id_cenario"] == id_]])
                    with self.assertRaisesRegex(ValueError, f"duplicado.*{id_}"):
                        funcao(duplicada)

    def test_comparacoes_rejeitam_colunas_ausentes_duplicadas_e_id_vazio(self):
        tabela = self.resultados_comparacoes()
        for funcao in (estudo.comparar_politicas, estudo.analisar_sensibilidade):
            for campo in ("id_cenario", "taxa_acerto", "modelo", "custo_ia_mensal_br"):
                with self.subTest(funcao=funcao.__name__, campo=campo):
                    with self.assertRaisesRegex(ValueError, "colunas obrigatórias ausentes"):
                        funcao(tabela.drop(columns=campo))
            with self.assertRaisesRegex(ValueError, "colunas duplicadas"):
                funcao(pd.concat([tabela, tabela[["modelo"]]], axis=1))
            invalida = tabela.copy()
            invalida.loc[invalida["id_cenario"] == "C05", "id_cenario"] = ""
            with self.assertRaisesRegex(ValueError, "id_cenario.*preenchido"):
                funcao(invalida)

    def test_politicas_rejeitam_hipoteses_ou_condicoes_diferentes(self):
        tabela = self.resultados_comparacoes()
        campos = [c for c in estudo.COLUNAS_HIPOTESES if c != "proporcao_acertos_com_feedback"]
        for campo in (*campos, *estudo.COLUNAS_CONDICOES):
            with self.subTest(campo=campo):
                invalida = tabela.copy(deep=True)
                valor = invalida.loc[0, campo]
                invalida.loc[0, campo] = valor + " alterado" if isinstance(valor, str) else valor + 1
                with self.assertRaisesRegex(ValueError, f"C01 contra C03.*{campo}"):
                    estudo.comparar_politicas(invalida)

    def test_politicas_exigem_referencia_todas_respostas_e_taxa_valida(self):
        tabela = self.resultados_comparacoes()
        for id_, valor in (("C03", 0.5), ("C01", 1.1), ("C01", -0.1)):
            with self.subTest(id=id_, valor=valor):
                invalida = tabela.copy()
                invalida.loc[invalida["id_cenario"] == id_, "proporcao_acertos_com_feedback"] = valor
                with self.assertRaises(ValueError):
                    estudo.comparar_politicas(invalida)

    def test_sensibilidade_rejeita_alteracoes_fora_do_token_previsto(self):
        tabela = self.resultados_comparacoes()
        for id_, alterado in (("C10", "tokens_entrada"), ("C11", "tokens_entrada"),
                              ("C12", "tokens_saida"), ("C13", "tokens_saida")):
            campos = [c for c in estudo.COLUNAS_HIPOTESES if c != alterado]
            for campo in (*campos, *estudo.COLUNAS_CONDICOES):
                with self.subTest(id=id_, campo=campo):
                    invalida = tabela.copy(deep=True)
                    indice = invalida.index[invalida["id_cenario"] == id_][0]
                    valor = invalida.loc[indice, campo]
                    invalida.loc[indice, campo] = valor + " alterado" if isinstance(valor, str) else valor + 1
                    with self.assertRaisesRegex(ValueError, f"{id_} contra C05.*{campo}"):
                        estudo.analisar_sensibilidade(invalida)

    def test_sensibilidade_exige_mudanca_real_no_token_previsto(self):
        tabela = self.resultados_comparacoes()
        invalida = tabela.copy()
        invalida.loc[invalida["id_cenario"] == "C10", "tokens_entrada"] = 500
        with self.assertRaisesRegex(ValueError, "C10 contra C05.*tokens_entrada.*diferente"):
            estudo.analisar_sensibilidade(invalida)

    def test_comparacoes_rejeitam_custos_float_negativos_e_nao_finitos(self):
        tabela = self.resultados_comparacoes()
        for funcao in (estudo.comparar_politicas, estudo.analisar_sensibilidade):
            for valor in (2.2, Decimal("-1"), Decimal("NaN"), Decimal("Infinity")):
                with self.subTest(funcao=funcao.__name__, valor=valor):
                    invalida = tabela.copy()
                    invalida.loc[invalida["id_cenario"] == "C05", "custo_ia_mensal_br"] = valor
                    with self.assertRaises((TypeError, ValueError)):
                        funcao(invalida)

    def test_politicas_referencia_zero_nao_inventa_percentual(self):
        tabela = self.resultados_comparacoes()
        tabela.loc[tabela["id_cenario"].isin(["C03", "C06", "C09"]), "custo_ia_mensal_br"] = Decimal("0")
        politicas = estudo.comparar_politicas(tabela)
        for linha in politicas.to_dict("records"):
            self.assertIsNone(linha["reducao_percentual"])
            self.assertEqual(linha["reducao_mensal_br"], -linha["custo_politica_mensal_br"])
        self.assertEqual(estudo.formatar_percentual(None), "Não aplicável")

    def test_sensibilidade_referencia_zero_preserva_diferenca_absoluta(self):
        tabela = self.resultados_comparacoes()
        tabela.loc[tabela["id_cenario"] == "C05", "custo_ia_mensal_br"] = Decimal("0")
        for linha in estudo.analisar_sensibilidade(tabela).to_dict("records"):
            self.assertIsNone(linha["variacao_percentual"])
            self.assertEqual(linha["variacao_mensal_br"], linha["custo_cenario_mensal_br"])

    def test_percentuais_seguem_precisao_decimal_sem_alterar_configuracao(self):
        from decimal import getcontext, localcontext
        tabela = self.resultados_comparacoes()
        tabela.loc[tabela["id_cenario"] == "C01", "custo_ia_mensal_br"] = Decimal("2")
        tabela.loc[tabela["id_cenario"] == "C03", "custo_ia_mensal_br"] = Decimal("3")
        precisao_original = getcontext().prec
        with localcontext() as contexto:
            contexto.prec = 10
            resultado = estudo.comparar_politicas(tabela)
            self.assertEqual(resultado.iloc[0]["reducao_percentual"], Decimal("33.33333333"))
            self.assertEqual(contexto.prec, 10)
        self.assertEqual(getcontext().prec, precisao_original)

    def test_exportacao_comparacoes_preserva_decimal_e_percentual_nao_aplicavel(self):
        self.alterar(self.condicoes, "brl_por_usd", "5.81023456789")
        tabela = self.resultados_comparacoes()
        for nome, funcao, percentual in (
            ("politicas", estudo.comparar_politicas, "reducao_percentual"),
            ("sensibilidade", estudo.analisar_sensibilidade, "variacao_percentual"),
        ):
            for zero in (False, True):
                with self.subTest(nome=nome, zero=zero):
                    entrada = tabela.copy()
                    if zero:
                        ids = ["C03", "C06", "C09"] if nome == "politicas" else ["C05"]
                        entrada.loc[entrada["id_cenario"].isin(ids), "custo_ia_mensal_br"] = Decimal("0")
                    comparacoes = funcao(entrada)
                    antes = comparacoes.copy(deep=True)
                    caminho = self.raiz / f"{nome}_{zero}.csv"
                    estudo.exportar_resultados(comparacoes, caminho)
                    registros = self.ler_texto(caminho)
                    self.assertEqual(len(registros), len(comparacoes))
                    for texto, original in zip(registros, comparacoes.to_dict("records"), strict=True):
                        for campo, valor in original.items():
                            if isinstance(valor, Decimal):
                                self.assertEqual(texto[campo], str(valor))
                                self.assertEqual(Decimal(texto[campo]).as_tuple(), valor.as_tuple())
                        if zero:
                            self.assertEqual(texto[percentual], "")
                    assert_frame_equal(comparacoes, antes, check_exact=True)

    def test_fluxo_exporta_tres_tabelas_e_mostra_sinais_sem_modificar_dados(self):
        caminho_politicas = self.raiz / "outra" / "politicas.csv"
        caminho_sensibilidade = self.raiz / "outra" / "tokens.csv"
        with redirect_stdout(io.StringIO()) as texto:
            tabela = estudo.executar_estudo(
                self.cenarios, self.condicoes, self.saida, caminho_politicas, caminho_sensibilidade,
            )
        self.assertEqual(tabela.shape, (13, 35))
        self.assertEqual(len(self.ler_texto(self.saida)), 13)
        self.assertEqual(len(self.ler_texto(caminho_politicas)), 6)
        self.assertEqual(len(self.ler_texto(caminho_sensibilidade)), 4)
        self.assertIn("+60,00%", texto.getvalue())
        self.assertIn("-12,50%", texto.getvalue())
        self.assertIn("+75,00%", texto.getvalue())
        self.assertIn("campo vazio no CSV", texto.getvalue())
        self.assertEqual(estudo.formatar_percentual(Decimal("0")), "0,00%")

    def test_falha_de_comparabilidade_preserva_todos_os_csvs_anteriores(self):
        self.saida.parent.mkdir()
        destinos = (
            self.saida, self.saida.parent / "comparacao_politicas.csv",
            self.saida.parent / "sensibilidade_tokens.csv",
        )
        for caminho in destinos:
            caminho.write_bytes(b"anterior")
        original = self.cenarios.read_bytes()
        for numero in (0, 9):
            with self.subTest(registro=numero):
                self.cenarios.write_bytes(original)
                self.alterar(self.cenarios, "taxa_acerto", "0.61", numero=numero)
                with redirect_stdout(io.StringIO()) as texto, self.assertRaisesRegex(ValueError, "não comparáveis"):
                    estudo.executar_estudo(self.cenarios, self.condicoes, self.saida)
                self.assertEqual(texto.getvalue(), "")
                for caminho in destinos:
                    self.assertEqual(caminho.read_bytes(), b"anterior")

class TestIndicadores(unittest.TestCase):
    def tabela(self, **alteracoes):
        registro = {
            "id_cenario": "C05", "cenario": "Cenário de referência", "usuarios_ativos": 500,
            "custo_entrada_usd": Decimal("0.55"), "custo_saida_usd": Decimal("1.65"),
            "custo_ia_mensal_usd": Decimal("2.20"), "custo_ia_mensal_br": Decimal("12.7824400"),
        }
        registro.update(alteracoes)
        return pd.DataFrame([registro], dtype=object)

    def resultados_reais(self):
        entrada = Path(__file__).resolve().parent / "dados" / "estudo_de_caso"
        return estudo.calcular_resultados(
            estudo.ler_cenarios_estudo(entrada / "cenarios.csv"),
            estudo.ler_condicoes_fixas(entrada / "condicoes_fixas.csv"),
        )

    def test_indicadores_dos_13_cenarios_com_expectativas_independentes(self):
        resultados = estudo.calcular_indicadores(self.resultados_reais())
        self.assertEqual(resultados.shape, (13, 11))
        self.assertEqual(list(resultados.columns), [*estudo.COLUNAS_BASE_INDICADORES, *estudo.COLUNAS_INDICADORES])
        self.assertEqual(list(resultados["id_cenario"]), [f"C{i:02d}" for i in range(1, 14)])
        esperados = (
            ("25", "75", "0.0032", "0.01859264"),
            ("25", "75", "0.0044", "0.02556488"),
            ("25", "75", "0.008", "0.0464816"),
            ("25", "75", "0.0032", "0.01859264"),
            ("25", "75", "0.0044", "0.02556488"),
            ("25", "75", "0.008", "0.0464816"),
            ("25", "75", "0.0032", "0.01859264"),
            ("25", "75", "0.0044", "0.02556488"),
            ("25", "75", "0.008", "0.0464816"),
            (Decimal("100") / 7, Decimal("600") / 7, "0.00385", "0.02236927"),
            ("40", "60", "0.0055", "0.0319561"),
            ("40", "60", "0.00275", "0.01597805"),
            (Decimal("100") / 7, Decimal("600") / 7, "0.0077", "0.04473854"),
        )
        for registro, valores in zip(resultados.to_dict("records"), esperados, strict=True):
            with self.subTest(id=registro["id_cenario"]):
                for campo, esperado in zip(estudo.COLUNAS_INDICADORES, valores, strict=True):
                    self.assertIsInstance(registro[campo], Decimal)
                    self.assertEqual(registro[campo], Decimal(esperado))
                soma = registro["participacao_entrada_percentual"] + registro["participacao_saida_percentual"]
                self.assertLessEqual(abs(soma - Decimal("100")), Decimal("1e-25"))

    def test_c05_e_mesmo_custo_unitario_em_c02_c05_c08(self):
        indicadores = estudo.calcular_indicadores(self.resultados_reais()).set_index("id_cenario")
        for id_ in ("C02", "C05", "C08"):
            self.assertEqual(indicadores.loc[id_, "custo_ia_mensal_por_usuario_usd"], Decimal("0.0044"))
            self.assertEqual(indicadores.loc[id_, "custo_ia_mensal_por_usuario_br"], Decimal("0.02556488"))
        self.assertEqual(indicadores.loc["C05", "participacao_entrada_percentual"], Decimal("25"))
        self.assertEqual(indicadores.loc["C05", "participacao_saida_percentual"], Decimal("75"))

    def test_zero_total_participacoes_none_custo_unitario_zero(self):
        dados = self.tabela(custo_entrada_usd=Decimal("0"), custo_saida_usd=Decimal("0"),
                            custo_ia_mensal_usd=Decimal("0"), custo_ia_mensal_br=Decimal("0"))
        resultado = estudo.calcular_indicadores(dados).iloc[0]
        for campo in estudo.COLUNAS_INDICADORES[:2]:
            self.assertIsNone(resultado[campo])
        for campo in estudo.COLUNAS_INDICADORES[2:]:
            self.assertIsInstance(resultado[campo], Decimal)
            self.assertEqual(resultado[campo], Decimal("0"))

    def test_zero_usuarios_custo_unitario_none_participacoes_validas(self):
        resultado = estudo.calcular_indicadores(self.tabela(usuarios_ativos=0)).iloc[0]
        self.assertEqual(resultado["participacao_entrada_percentual"], Decimal("25"))
        self.assertEqual(resultado["participacao_saida_percentual"], Decimal("75"))
        for campo in estudo.COLUNAS_INDICADORES[2:]:
            self.assertIsNone(resultado[campo])

    def test_ambos_denominadores_zero(self):
        dados = self.tabela(usuarios_ativos=0, custo_entrada_usd=Decimal("0"),
                            custo_saida_usd=Decimal("0"), custo_ia_mensal_usd=Decimal("0"),
                            custo_ia_mensal_br=Decimal("0"))
        resultado = estudo.calcular_indicadores(dados).iloc[0]
        self.assertTrue(all(resultado[campo] is None for campo in estudo.COLUNAS_INDICADORES))

    def test_entrada_gratuita_com_saida_paga(self):
        dados = self.tabela(custo_entrada_usd=Decimal("0"), custo_saida_usd=Decimal("2.20"))
        resultado = estudo.calcular_indicadores(dados).iloc[0]
        self.assertEqual(resultado["participacao_entrada_percentual"], Decimal("0"))
        self.assertEqual(resultado["participacao_saida_percentual"], Decimal("100"))

    def test_custos_invalidos_rejeitados_com_identificador_e_campo(self):
        for campo in estudo.COLUNAS_BASE_INDICADORES[3:]:
            for valor in (1.0, "1.00", True, None, Decimal("-1"), Decimal("NaN"), Decimal("Infinity")):
                with self.subTest(campo=campo, valor=valor):
                    with self.assertRaises((TypeError, ValueError)) as erro:
                        estudo.calcular_indicadores(self.tabela(**{campo: valor}))
                    self.assertIn("C05", str(erro.exception))
                    self.assertIn(campo, str(erro.exception))

    def test_total_incoerente_rejeitado(self):
        with self.assertRaisesRegex(ValueError, "C05.*incoerentes"):
            estudo.calcular_indicadores(self.tabela(custo_ia_mensal_usd=Decimal("2.21")))

    def test_usuarios_invalidos_sem_booleanos_ou_truncamento(self):
        for valor in (-1, True, False, 500.0, 500.5, Decimal("500"), "500", None):
            with self.subTest(valor=valor):
                with self.assertRaisesRegex(ValueError, "usuarios_ativos.*inteiro"):
                    estudo.calcular_indicadores(self.tabela(usuarios_ativos=valor))

    def test_inteiros_escalares_e_nullable_do_pandas(self):
        escalar = pd.Series([500], dtype="int64").iloc[0]
        dados = self.tabela(usuarios_ativos=escalar)
        self.assertEqual(estudo.calcular_indicadores(dados).iloc[0]["custo_ia_mensal_por_usuario_usd"], Decimal("0.0044"))
        dados["usuarios_ativos"] = pd.Series([500], dtype="Int64")
        self.assertEqual(estudo.calcular_indicadores(dados).iloc[0]["custo_ia_mensal_por_usuario_br"], Decimal("0.02556488"))

    def test_ids_nomes_vazios_e_identificadores_duplicados(self):
        for campo in ("id_cenario", "cenario"):
            for valor in (None, "", "  ", 5):
                with self.subTest(campo=campo, valor=valor):
                    with self.assertRaises(ValueError):
                        estudo.calcular_indicadores(self.tabela(**{campo: valor}))
        with self.assertRaisesRegex(ValueError, "duplicado.*C05"):
            estudo.calcular_indicadores(pd.concat([self.tabela(), self.tabela()]))

    def test_colunas_ausentes_duplicadas_e_tabela_vazia(self):
        dados = self.tabela()
        for campo in estudo.COLUNAS_BASE_INDICADORES:
            with self.subTest(campo=campo), self.assertRaisesRegex(ValueError, "colunas.*ausentes"):
                estudo.calcular_indicadores(dados.drop(columns=campo))
        with self.assertRaisesRegex(ValueError, "colunas duplicadas"):
            estudo.calcular_indicadores(pd.concat([dados, dados[["cenario"]]], axis=1))
        with self.assertRaisesRegex(ValueError, "sem cenários"):
            estudo.calcular_indicadores(dados.iloc[:0])

    def test_preserva_ordem_indices_valores_tipos_sem_recalcular(self):
        dados = self.resultados_reais().iloc[::-1].copy()
        dados.index = ["repetido"] * 13
        antes = dados.copy(deep=True)
        with patch.object(estudo, "calcular_consumo_cenario", side_effect=AssertionError("recálculo")), \
                patch.object(estudo, "calcular_custo_ia_cenario", side_effect=AssertionError("recálculo")):
            indicadores = estudo.calcular_indicadores(dados)
        self.assertEqual(list(indicadores["id_cenario"]), list(dados["id_cenario"]))
        assert_frame_equal(dados, antes, check_exact=True)
        for campo in estudo.COLUNAS_BASE_INDICADORES:
            self.assertEqual(list(indicadores[campo]), list(dados[campo]))

    def test_divisoes_nao_exatas_contexto_herdado_e_global_preservado(self):
        from decimal import getcontext, localcontext
        global_antes = getcontext().copy()
        with localcontext() as contexto:
            contexto.prec = 10
            contexto.clear_flags()
            dados = self.tabela(usuarios_ativos=3, custo_entrada_usd=Decimal("1"),
                                custo_saida_usd=Decimal("2"), custo_ia_mensal_usd=Decimal("3"),
                                custo_ia_mensal_br=Decimal("5"))
            resultado = estudo.calcular_indicadores(dados).iloc[0]
            self.assertEqual(resultado["participacao_entrada_percentual"], Decimal("33.33333333"))
            self.assertEqual(resultado["participacao_saida_percentual"], Decimal("66.66666667"))
            self.assertEqual(resultado["custo_ia_mensal_por_usuario_br"], Decimal("1.666666667"))
            self.assertEqual(contexto.prec, 10)
            self.assertFalse(any(contexto.flags.values()))
        self.assertEqual(getcontext().prec, global_antes.prec)
        self.assertEqual(getcontext().rounding, global_antes.rounding)
        self.assertEqual(getcontext().flags, global_antes.flags)

    def test_coerencia_dos_componentes_na_precisao_vigente(self):
        from decimal import localcontext
        with localcontext() as contexto:
            contexto.prec = 5
            dados = self.tabela(custo_entrada_usd=Decimal("0.123456"), custo_saida_usd=Decimal("0.234567"),
                                custo_ia_mensal_usd=Decimal("0.358023"))
            self.assertEqual(len(estudo.calcular_indicadores(dados)), 1)

    def test_exportacao_decimal_completa_e_none_vazio(self):
        dados = pd.concat([
            self.tabela(id_cenario="A", usuarios_ativos=0),
            self.tabela(id_cenario="B", custo_entrada_usd=Decimal("0"), custo_saida_usd=Decimal("0"),
                        custo_ia_mensal_usd=Decimal("0"), custo_ia_mensal_br=Decimal("0")),
            self.tabela(id_cenario="C", custo_ia_mensal_br=Decimal("12.7824400123456789")),
        ], ignore_index=True)
        indicadores = estudo.calcular_indicadores(dados)
        antes = indicadores.copy(deep=True)
        with TemporaryDirectory(prefix="liteart_indicadores_") as pasta:
            destino = Path(pasta) / "indicadores.csv"
            estudo.exportar_resultados(indicadores, destino)
            with destino.open(encoding="utf-8", newline="") as arquivo:
                leitor = csv.DictReader(arquivo)
                self.assertEqual(leitor.fieldnames, list(indicadores.columns))
                registros = list(leitor)
            for registro, original in zip(registros, indicadores.to_dict("records"), strict=True):
                for campo, valor in original.items():
                    if isinstance(valor, Decimal):
                        self.assertEqual(Decimal(registro[campo]).as_tuple(), valor.as_tuple())
                        self.assertEqual(registro[campo], str(valor))
                    elif valor is None:
                        self.assertEqual(registro[campo], "")
        assert_frame_equal(indicadores, antes, check_exact=True)

    def test_apresentacao_oito_casas_unidades_e_nao_aplicavel(self):
        indicadores = estudo.calcular_indicadores(pd.concat([
            self.tabela(), self.tabela(id_cenario="zero", usuarios_ativos=0),
        ]))
        antes = indicadores.copy(deep=True)
        with redirect_stdout(io.StringIO()) as texto:
            estudo.apresentar_indicadores(indicadores)
        self.assertIn("usuário ativo/mês", texto.getvalue())
        self.assertIn("US$ 0,00440000", texto.getvalue())
        self.assertIn("R$ 0,02556488", texto.getvalue())
        self.assertIn("Não aplicável", texto.getvalue())
        self.assertIn("25,00%", texto.getvalue())
        assert_frame_equal(indicadores, antes, check_exact=True)

    def test_integracao_quarto_csv_retorno_e_esquemas_anteriores_preservados(self):
        with TemporaryDirectory(prefix="liteart_indicadores_fluxo_") as pasta:
            saida = Path(pasta) / "resultados.csv"
            indicadores = Path(pasta) / "opcional" / "indicadores.csv"
            with redirect_stdout(io.StringIO()) as texto:
                tabela = estudo.executar_estudo(caminho_saida=saida, caminho_indicadores=indicadores)
            self.assertEqual(tabela.shape, (13, 35))
            for nome, linhas, colunas in (
                (saida, 13, 35), (saida.parent / "comparacao_politicas.csv", 6, 20),
                (saida.parent / "sensibilidade_tokens.csv", 4, 24), (indicadores, 13, 11),
            ):
                with nome.open(encoding="utf-8", newline="") as arquivo:
                    leitor = csv.DictReader(arquivo)
                    self.assertEqual(len(leitor.fieldnames), colunas)
                    self.assertEqual(len(list(leitor)), linhas)
            self.assertIn(str(indicadores), texto.getvalue())

    def test_falha_nos_indicadores_preserva_todas_as_exportacoes_anteriores(self):
        with TemporaryDirectory(prefix="liteart_indicadores_falha_") as pasta:
            pasta = Path(pasta)
            nomes = ("resultados_cenarios.csv", "comparacao_politicas.csv",
                     "sensibilidade_tokens.csv", "indicadores_cenarios.csv")
            for nome in nomes:
                (pasta / nome).write_bytes(b"anterior")
            with patch.object(estudo, "calcular_indicadores", side_effect=ValueError("total incoerente")), \
                    redirect_stdout(io.StringIO()) as texto, self.assertRaisesRegex(ValueError, "incoerente"):
                estudo.executar_estudo(caminho_saida=pasta / nomes[0])
            self.assertEqual(texto.getvalue(), "")
            for nome in nomes:
                self.assertEqual((pasta / nome).read_bytes(), b"anterior")


if __name__ == "__main__":
    unittest.main()
