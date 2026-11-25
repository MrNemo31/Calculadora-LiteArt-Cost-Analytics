"""Testes dos gráficos, sem navegador, rede ou resultados pessoais."""

from contextlib import redirect_stdout
import csv
from decimal import Decimal
import io
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import pandas as pd
from pandas.testing import assert_frame_equal

import graficos_estudo as graficos


def registros_sensibilidade():
    """Quatro registros controlados; resultados esperados não usam o código testado."""
    registros = []
    for id_, campo, entrada, saida, custo, diferenca, percentual in (
        ("C10", "tokens_entrada", "250", "300", "11.18463500", "-1.59780500", "-12.5"),
        ("C11", "tokens_entrada", "1000", "300", "15.9780500", "3.1956100", "25"),
        ("C12", "tokens_saida", "500", "150", "7.98902500", "-4.79341500", "-37.5"),
        ("C13", "tokens_saida", "500", "600", "22.3692700", "9.5868300", "75"),
    ):
        registros.append(dict(zip(graficos.COLUNAS_SENSIBILIDADE, (
            id_, "C05", campo, "500", "500", "300", entrada, saida, "12.7824400", custo,
            diferenca, percentual, "Provedor didático", "modelo-controlado", "Standard", "0.10",
            "0.50", "5.8102", "https://example.org/modelo", "https://example.org/precos",
            "2026-11-18", "https://example.org/cambio", "2026-11-18", "2026-11-18",
        ), strict=True)))
    return registros


def escrever_sensibilidade(caminho, registros):
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=graficos.COLUNAS_SENSIBILIDADE)
        escritor.writeheader()
        escritor.writerows(registros)


class TestGraficosEstudo(unittest.TestCase):
    def setUp(self):
        temporario = TemporaryDirectory(prefix="liteart_grafico_")
        self.addCleanup(temporario.cleanup)
        self.raiz = Path(temporario.name).resolve()
        self.entrada = self.raiz / "resultados.csv"
        self.saida = self.raiz / "grafico.html"
        self.registros = []
        # Dados controlados: custos com casas adicionais, sem depender do CSV real.
        for numero in range(1, 14):
            posicao = min(numero, 9) - 1
            registro = {campo: "0" for campo in graficos.COLUNAS_RESULTADOS}
            registro.update(
                id_cenario=f"C{numero:02d}", cenario=f"Cenário hipotético {numero}",
                usuarios_ativos=str((100, 500, 1000)[posicao // 3]),
                respostas_por_usuario="40", taxa_acerto="0.60",
                proporcao_acertos_com_feedback=str(graficos.PROPORCOES[posicao % 3]),
                tokens_entrada="500", tokens_saida="300", feedbacks_mensais="2200.5",
                custo_ia_mensal_br=str(Decimal(numero) + Decimal("0.23456789")),
                provedor="Provedor didático", modelo="modelo-controlado", modalidade="Standard",
                preco_entrada_por_milhao_usd="0.10", preco_saida_por_milhao_usd="0.50",
                brl_por_usd="5.8102", fonte_modelo="https://example.org/modelo",
                fonte_precos="https://example.org/precos", fonte_cambio="https://example.org/cambio",
                data_consulta_precos="2026-11-18", data_referencia_cambio="2026-11-18",
                data_consulta_cambio="2026-11-18",
            )
            self.registros.append(registro)
        self.escrever()
        escrever_sensibilidade(self.raiz / "sensibilidade_tokens.csv", registros_sensibilidade())

    def escrever(self, registros=None, colunas=None):
        with self.entrada.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas or graficos.COLUNAS_RESULTADOS)
            escritor.writeheader()
            escritor.writerows(self.registros if registros is None else registros)

    def dados(self):
        return graficos.ler_resultados_grafico(self.entrada)

    def test_leitura_decimal_exata_selecao_explicita_e_ordem(self):
        dados = self.dados()
        self.assertEqual(list(dados["id_cenario"]), [f"C{i:02d}" for i in range(1, 10)])
        self.assertEqual(len(dados), 9)
        for numero, valor in enumerate(dados["custo_ia_mensal_br"], 1):
            self.assertIsInstance(valor, Decimal)
            self.assertEqual(valor, Decimal(numero) + Decimal("0.23456789"))
        self.assertEqual(dados.iloc[0]["feedbacks_mensais"], Decimal("2200.5"))

    def test_nove_barras_tres_series_agrupadas_e_ordens(self):
        figura = graficos.criar_figura(self.dados())
        self.assertEqual(len(figura.data), 3)
        self.assertEqual(sum(len(serie.y) for serie in figura.data), 9)
        self.assertEqual([serie.name for serie in figura.data], list(graficos.POLITICAS))
        self.assertEqual(figura.layout.barmode, "group")
        self.assertEqual(figura.layout.xaxis.type, "category")
        self.assertEqual(list(figura.layout.xaxis.categoryarray), list(graficos.ESCALAS))
        self.assertEqual(figura.layout.yaxis.range[0], 0)
        self.assertEqual(len({s.marker.color for s in figura.data}), 3)
        self.assertEqual(len({s.marker.pattern.shape for s in figura.data}), 3)

    def test_alturas_aproximadas_textos_exatos_e_hover(self):
        dados = self.dados()
        figura = graficos.criar_figura(dados)
        por_id = dados.set_index("id_cenario")
        for serie in figura.data:
            self.assertEqual(list(serie.x), list(graficos.ESCALAS))
            for altura, texto, custom in zip(serie.y, serie.text, serie.customdata, strict=True):
                id_ = custom[0]
                valor = por_id.loc[id_, "custo_ia_mensal_br"]
                self.assertAlmostEqual(altura, float(valor), places=12)
                esperado = f"R$ {graficos.formatar_moeda_br(valor)}"
                self.assertEqual(texto, esperado)
                self.assertEqual(custom[4], esperado)
                self.assertEqual(custom[2], serie.name)
                self.assertEqual(custom[3], "2200.5")
                self.assertNotIn(id_, ("C10", "C11", "C12", "C13"))
            self.assertIn("Feedbacks/mês", serie.hovertemplate)
            self.assertIn("Usuários:", serie.hovertemplate)

    def test_reordenar_arquivo_ou_indice_nao_troca_associacao(self):
        original = graficos.criar_figura(self.dados())
        self.escrever(list(reversed(self.registros)))
        dados = self.dados().iloc[::-1].copy()
        dados.index = ["repetido"] * 9
        reordenada = graficos.criar_figura(dados)
        self.assertEqual(original.to_json(), reordenada.to_json())

    def test_preserva_dados_arquivo_e_decimal_apos_criar_e_exportar(self):
        bytes_antes = self.entrada.read_bytes()
        dados = self.dados()
        antes = dados.copy(deep=True)
        figura = graficos.criar_figura(dados)
        graficos.exportar_html(figura, self.saida)
        assert_frame_equal(dados, antes, check_exact=True)
        self.assertEqual(self.entrada.read_bytes(), bytes_antes)
        for valor in dados["custo_ia_mensal_br"]:
            self.assertIsInstance(valor, Decimal)

    def test_criar_figura_nao_grava_nem_abre_navegador(self):
        dados = self.dados()
        with patch("webbrowser.open", side_effect=AssertionError("navegador")), \
                patch("plotly.graph_objects.Figure.write_html", side_effect=AssertionError("gravação")), \
                patch("plotly.graph_objects.Figure.show", side_effect=AssertionError("show")):
            graficos.criar_figura(dados)
        self.assertFalse(self.saida.exists())

    def test_html_completo_offline_e_parametros_de_exportacao(self):
        figura = graficos.criar_figura(self.dados())
        with patch.object(figura, "write_html", wraps=figura.write_html) as escrita, \
                patch("webbrowser.open", side_effect=AssertionError("navegador")):
            destino = graficos.exportar_html(figura, self.raiz / "pasta" / "grafico.html")
        escrita.assert_called_once_with(destino, full_html=True, include_plotlyjs=True, auto_open=False)
        html = destino.read_text(encoding="utf-8")
        self.assertIn("<html>", html)
        self.assertIn("</html>", html)
        self.assertIn("plotly.js v", html)
        self.assertIn("Plotly.newPlot", html)
        self.assertNotIn('<script src="https://cdn.plot.ly', html)

    def test_identificador_ausente(self):
        self.escrever(self.registros[1:])
        with self.assertRaisesRegex(ValueError, "identificadores ausentes.*C01"):
            self.dados()

    def test_identificador_duplicado_inclusive_sensibilidade(self):
        for numero in (0, 9):
            with self.subTest(numero=numero):
                self.escrever([*self.registros, self.registros[numero]])
                with self.assertRaisesRegex(ValueError, "identificador duplicado"):
                    self.dados()

    def test_campos_ausentes_ou_vazios(self):
        colunas = [c for c in graficos.COLUNAS_RESULTADOS if c != "custo_ia_mensal_br"]
        registros = [{c: r[c] for c in colunas} for r in self.registros]
        self.escrever(registros, colunas)
        with self.assertRaisesRegex(ValueError, "ausentes.*custo_ia_mensal_br"):
            self.dados()
        self.registros[0]["modelo"] = " "
        self.escrever()
        with self.assertRaisesRegex(ValueError, "modelo.*vazio"):
            self.dados()

    def test_custo_invalido_negativo_infinito_nan_e_texto(self):
        for valor in ("-1", "Infinity", "NaN", "texto"):
            with self.subTest(valor=valor):
                self.registros[0]["custo_ia_mensal_br"] = valor
                self.escrever()
                with self.assertRaisesRegex(ValueError, "C01.*custo_ia_mensal_br"):
                    self.dados()

    def test_float_financeiro_nao_e_aceito_como_decimal_original(self):
        dados = self.dados()
        dados.loc[0, "custo_ia_mensal_br"] = 1.2
        with self.assertRaisesRegex(ValueError, "sem float intermediário"):
            graficos.criar_figura(dados)

    def test_condicoes_incompativeis(self):
        for campo in graficos.COLUNAS_CONDICOES:
            with self.subTest(campo=campo):
                original = self.registros[1][campo]
                self.registros[1][campo] = (
                    "6.20" if campo in graficos.CAMPOS_FINANCEIROS else
                    "2026-11-19" if campo in graficos.CAMPOS_DATAS else "diferente"
                )
                self.escrever()
                with self.assertRaisesRegex(ValueError, "condições.*incompatíveis"):
                    self.dados()
                self.registros[1][campo] = original

    def test_hipoteses_e_associacao_id_escala_politica(self):
        for campo, valor in (("usuarios_ativos", "100.0"), ("usuarios_ativos", "500"),
                             ("respostas_por_usuario", "41"), ("taxa_acerto", "0.5"),
                             ("proporcao_acertos_com_feedback", "0.25"),
                             ("tokens_entrada", "250"), ("tokens_saida", "150")):
            with self.subTest(campo=campo):
                original = self.registros[0][campo]
                self.registros[0][campo] = valor
                self.escrever()
                with self.assertRaises(ValueError):
                    self.dados()
                self.registros[0][campo] = original

    def test_ausencia_informa_como_gerar_sem_executar_analise(self):
        with patch("analise_estudo.executar_estudo", side_effect=AssertionError("análise")):
            with self.assertRaisesRegex(FileNotFoundError, "analise_estudo.py"):
                graficos.ler_resultados_grafico(self.raiz / "ausente.csv")
        self.assertFalse(self.saida.exists())

    def test_dados_invalidos_preservam_html_anterior(self):
        self.saida.write_bytes(b"html anterior")
        self.registros[0]["modelo"] = "outro modelo"
        self.escrever()
        with redirect_stdout(io.StringIO()), self.assertRaises(ValueError):
            graficos.executar_grafico(self.entrada, self.saida)
        self.assertEqual(self.saida.read_bytes(), b"html anterior")

    def test_importacao_sem_leitura_rede_impressao_ou_exportacao(self):
        with patch("pathlib.Path.open", side_effect=AssertionError("leitura")), \
                patch("builtins.input", side_effect=AssertionError("input")), \
                patch("urllib.request.urlopen", side_effect=AssertionError("rede")), \
                patch("plotly.graph_objects.Figure.write_html", side_effect=AssertionError("gravação")), \
                redirect_stdout(io.StringIO()) as texto:
            runpy.run_path(str(Path(graficos.__file__)), run_name="importacao_grafico")
        self.assertEqual(texto.getvalue(), "")

    def test_titulo_metadados_dos_dados_e_fluxo_com_caminhos_temporarios(self):
        with redirect_stdout(io.StringIO()) as texto:
            figura = graficos.executar_grafico(self.entrada, self.saida)
        self.assertEqual(figura.layout.title.text,
                         "Custo mensal estimado de IA por escala e política de feedback")
        anotacao = figura.layout.annotations[0].text
        self.assertIn("Cenários hipotéticos", anotacao)
        self.assertIn("modelo-controlado", anotacao)
        self.assertIn("5,8102", anotacao)
        self.assertIn(str(self.saida), texto.getvalue())
        self.assertIn("manualmente", texto.getvalue())


class TestGraficoSensibilidade(unittest.TestCase):
    def setUp(self):
        temporario = TemporaryDirectory(prefix="liteart_sensibilidade_")
        self.addCleanup(temporario.cleanup)
        self.raiz = Path(temporario.name).resolve()
        self.entrada = self.raiz / "sensibilidade_tokens.csv"
        self.saida = self.raiz / "sensibilidade_tokens.html"
        self.registros = registros_sensibilidade()
        self.escrever()

    def escrever(self, registros=None):
        escrever_sensibilidade(self.entrada, self.registros if registros is None else registros)

    def dados(self):
        return graficos.ler_sensibilidade_grafico(self.entrada)

    def preparar_primeiro(self):
        primeiro = TestGraficosEstudo()
        primeiro.setUp()
        self.addCleanup(primeiro.doCleanups)
        return primeiro

    def test_leitura_tipos_precisao_e_negativos_validos(self):
        dados = self.dados()
        self.assertEqual(list(dados["id_cenario"]), ["C10", "C11", "C12", "C13"])
        for linha, esperado in zip(dados.to_dict("records"), ("-12.5", "25", "-37.5", "75"), strict=True):
            self.assertIsInstance(linha["variacao_percentual"], Decimal)
            self.assertEqual(linha["variacao_percentual"], Decimal(esperado))
            for campo in ("custo_referencia_mensal_br", "custo_cenario_mensal_br", "variacao_mensal_br"):
                self.assertIsInstance(linha[campo], Decimal)
        self.assertLess(dados.iloc[0]["variacao_mensal_br"], 0)

    def test_quatro_barras_horizontais_sinais_ordem_e_linha_zero(self):
        figura = graficos.criar_figura_sensibilidade(self.dados())
        self.assertEqual(sum(len(s.x) for s in figura.data), 4)
        self.assertTrue(all(s.orientation == "h" for s in figura.data))
        rotulos = list(figura.layout.yaxis.categoryarray)
        self.assertEqual(rotulos, [
            "C10 — Entrada: 500 → 250 tokens", "C11 — Entrada: 500 → 1.000 tokens",
            "C12 — Saída: 300 → 150 tokens", "C13 — Saída: 300 → 600 tokens",
        ])
        self.assertEqual(figura.layout.yaxis.autorange, "reversed")
        self.assertEqual(figura.layout.xaxis.type, "linear")
        inicio, fim = figura.layout.xaxis.range
        self.assertEqual(inicio, -fim)
        self.assertLess(inicio, -37.5)
        self.assertGreater(fim, 75)
        self.assertTrue(any(s.x0 == 0 and s.x1 == 0 for s in figura.layout.shapes))
        self.assertEqual(len({s.marker.color for s in figura.data}), 2)
        esperados = {"C10": -12.5, "C11": 25, "C12": -37.5, "C13": 75}
        for serie in figura.data:
            for coordenada, custom in zip(serie.x, serie.customdata, strict=True):
                self.assertAlmostEqual(coordenada, esperados[custom[0]], places=12)

    def test_textos_monetarios_percentuais_e_hover_dos_decimal(self):
        dados = self.dados().set_index("id_cenario")
        figura = graficos.criar_figura_sensibilidade(self.dados())
        textos = {"C10": "-12,5%", "C11": "+25,0%", "C12": "-37,5%", "C13": "+75,0%"}
        for serie in figura.data:
            for texto, custom in zip(serie.text, serie.customdata, strict=True):
                linha = dados.loc[custom[0]]
                self.assertEqual(texto, textos[custom[0]])
                self.assertEqual(custom[1], "C05")
                for indice, campo in ((7, "custo_referencia_mensal_br"),
                                      (8, "custo_cenario_mensal_br"), (9, "variacao_mensal_br")):
                    self.assertEqual(custom[indice], "R$ " + graficos.formatar_moeda_br(linha[campo]))
                self.assertEqual(custom[10], texto)
            self.assertIn("Diferença mensal", serie.hovertemplate)
            self.assertIn("Entrada/feedback", serie.hovertemplate)
            self.assertIn("Saída/feedback", serie.hovertemplate)
        self.assertIn("Referência C05: R$ 12,78/mês", figura.layout.annotations[0].text)

    def test_ordem_de_entrada_e_indices_nao_trocam_associacao(self):
        original = graficos.criar_figura_sensibilidade(self.dados())
        self.escrever(list(reversed(self.registros)))
        dados = self.dados().iloc[::-1].copy()
        dados.index = ["repetido"] * 4
        reordenada = graficos.criar_figura_sensibilidade(dados)
        self.assertEqual(original.to_json(), reordenada.to_json())

    def test_rotulos_usam_tokens_e_custo_referencia_dos_dados(self):
        for registro in self.registros:
            registro["tokens_entrada_referencia"] = "600"
            registro["custo_referencia_mensal_br"] = "21.23456789"
            if registro["campo_alterado"] == "tokens_saida":
                registro["tokens_entrada_cenario"] = "600"
        self.escrever()
        figura = graficos.criar_figura_sensibilidade(self.dados())
        self.assertIn("600 → 250", figura.layout.yaxis.categoryarray[0])
        self.assertIn("R$ 21,23/mês", figura.layout.annotations[0].text)

    def test_identificadores_ausentes_duplicados_ou_inesperados(self):
        for registros in (self.registros[:-1], [*self.registros, self.registros[0]],
                          [{**self.registros[0], "id_cenario": "C14"}, *self.registros[1:]]):
            with self.subTest(quantidade=len(registros)):
                self.escrever(registros)
                with self.assertRaisesRegex(ValueError, "identificador|C10"):
                    self.dados()

    def test_referencia_deve_ser_c05(self):
        self.registros[0]["id_referencia"] = "C06"
        self.escrever()
        with self.assertRaisesRegex(ValueError, "referência deve ser C05"):
            self.dados()

    def test_condicoes_comerciais_e_base_devem_ser_iguais(self):
        for campo in (*graficos.COLUNAS_CONDICOES, "custo_referencia_mensal_br",
                      "tokens_entrada_referencia", "tokens_saida_referencia", "usuarios_ativos"):
            with self.subTest(campo=campo):
                self.registros = registros_sensibilidade()
                original = self.registros[1][campo]
                valor = (
                    "2026-11-19" if campo in graficos.CAMPOS_DATAS else
                    "6.20" if campo in (*graficos.CAMPOS_FINANCEIROS, "custo_referencia_mensal_br") else
                    str(int(original) + 1) if campo in ("usuarios_ativos", "tokens_entrada_referencia", "tokens_saida_referencia") else
                    "incompatível"
                )
                self.registros[1][campo] = valor
                self.escrever()
                with self.assertRaisesRegex(ValueError, "incompatíveis"):
                    self.dados()

    def test_campo_alterado_e_token_nao_variado(self):
        for id_, campo, valor in (("C10", "campo_alterado", "tokens_saida"),
                                 ("C12", "campo_alterado", "tokens_entrada"),
                                 ("C10", "tokens_saida_cenario", "301"),
                                 ("C12", "tokens_entrada_cenario", "501"),
                                 ("C10", "tokens_entrada_cenario", "500")):
            with self.subTest(id=id_, campo=campo):
                self.registros = registros_sensibilidade()
                next(r for r in self.registros if r["id_cenario"] == id_)[campo] = valor
                self.escrever()
                with self.assertRaises(ValueError):
                    self.dados()

    def test_percentual_vazio_nao_aplicavel_e_referencia_zero(self):
        for campo, valor in (("variacao_percentual", ""), ("custo_referencia_mensal_br", "0")):
            with self.subTest(campo=campo):
                self.registros = registros_sensibilidade()
                self.registros[0][campo] = valor
                self.escrever()
                with self.assertRaisesRegex(ValueError, "não aplicável|base deve ser positiva"):
                    self.dados()

    def test_numero_nao_finito_texto_invalido_e_campo_obrigatorio_vazio(self):
        for campo in ("variacao_percentual", "variacao_mensal_br", "custo_cenario_mensal_br"):
            for valor in ("NaN", "Infinity", "-Infinity", "texto"):
                with self.subTest(campo=campo, valor=valor):
                    self.registros = registros_sensibilidade()
                    self.registros[0][campo] = valor
                    self.escrever()
                    with self.assertRaisesRegex(ValueError, campo):
                        self.dados()
        self.registros = registros_sensibilidade()
        self.registros[0]["modelo"] = " "
        self.escrever()
        with self.assertRaisesRegex(ValueError, "modelo.*vazio"):
            self.dados()

    def test_cabecalho_e_quantidade_de_campos_invalidos(self):
        for texto in ("", "coluna\nvalor\n", ",".join(graficos.COLUNAS_SENSIBILIDADE) + "\nC10,C05\n"):
            with self.subTest(texto=texto):
                self.entrada.write_text(texto, encoding="utf-8")
                with self.assertRaises(ValueError):
                    self.dados()

    def test_arquivo_inexistente_nao_executa_analise(self):
        with patch("analise_estudo.executar_estudo", side_effect=AssertionError("recálculo")):
            with self.assertRaisesRegex(FileNotFoundError, "analise_estudo.py"):
                graficos.ler_sensibilidade_grafico(self.raiz / "ausente.csv")

    def test_preserva_arquivo_dados_contexto_e_nao_tem_efeitos_ao_criar(self):
        from decimal import getcontext
        contexto = getcontext().copy()
        bytes_antes = self.entrada.read_bytes()
        dados = self.dados()
        antes = dados.copy(deep=True)
        with patch("webbrowser.open", side_effect=AssertionError("navegador")), \
                patch("plotly.graph_objects.Figure.write_html", side_effect=AssertionError("gravação")), \
                patch("analise_estudo.calcular_resultados", side_effect=AssertionError("cálculo")):
            graficos.criar_figura_sensibilidade(dados)
        assert_frame_equal(dados, antes, check_exact=True)
        self.assertEqual(self.entrada.read_bytes(), bytes_antes)
        self.assertEqual(getcontext().prec, contexto.prec)
        self.assertEqual(getcontext().rounding, contexto.rounding)
        self.assertEqual(getcontext().flags, contexto.flags)
        self.assertFalse(self.saida.exists())

    def test_html_completo_com_plotly_incorporado(self):
        figura = graficos.criar_figura_sensibilidade(self.dados())
        with patch("webbrowser.open", side_effect=AssertionError("navegador")), \
                patch.object(figura, "write_html", wraps=figura.write_html) as escrita:
            graficos.exportar_html(figura, self.saida)
        escrita.assert_called_once_with(self.saida, full_html=True, include_plotlyjs=True, auto_open=False)
        html = self.saida.read_text(encoding="utf-8")
        self.assertIn("<html>", html)
        self.assertIn("plotly.js v", html)
        self.assertIn("Plotly.newPlot", html)
        self.assertIn("</html>", html)

    def test_falha_no_segundo_nao_sobrescreve_primeiro_nem_segundo_html(self):
        primeiro = self.preparar_primeiro()
        primeiro.saida.write_bytes(b"primeiro anterior")
        self.saida.write_bytes(b"segundo anterior")
        self.registros[0]["variacao_percentual"] = ""
        self.escrever()
        with redirect_stdout(io.StringIO()) as texto, self.assertRaisesRegex(ValueError, "não aplicável"):
            graficos.executar_grafico(primeiro.entrada, primeiro.saida, self.entrada, self.saida)
        self.assertEqual(primeiro.saida.read_bytes(), b"primeiro anterior")
        self.assertEqual(self.saida.read_bytes(), b"segundo anterior")
        self.assertEqual(texto.getvalue(), "")

    def test_ambas_as_figuras_sao_construidas_antes_da_primeira_gravacao(self):
        primeiro = self.preparar_primeiro()
        eventos = []
        criar_primeira = graficos.criar_figura
        criar_segunda = graficos.criar_figura_sensibilidade
        def primeira(dados):
            eventos.append("primeira")
            return criar_primeira(dados)
        def segunda(dados):
            eventos.append("segunda")
            return criar_segunda(dados)
        with patch.object(graficos, "criar_figura", side_effect=primeira), \
                patch.object(graficos, "criar_figura_sensibilidade", side_effect=segunda), \
                patch.object(graficos, "exportar_html", side_effect=lambda fig, p: eventos.append("gravação") or p), \
                redirect_stdout(io.StringIO()):
            graficos.executar_grafico(primeiro.entrada, primeiro.saida, self.entrada, self.saida)
        self.assertEqual(eventos, ["primeira", "segunda", "gravação", "gravação"])

    def test_integracao_caminhos_temporarios_e_preserva_primeira_figura(self):
        primeiro = self.preparar_primeiro()
        figura_antes = graficos.criar_figura(primeiro.dados())
        with redirect_stdout(io.StringIO()) as texto:
            figura = graficos.executar_grafico(primeiro.entrada, primeiro.saida, self.entrada, self.saida)
        self.assertEqual(figura.to_json(), figura_antes.to_json())
        self.assertTrue(primeiro.saida.exists())
        self.assertTrue(self.saida.exists())
        self.assertIn(str(primeiro.saida), texto.getvalue())
        self.assertIn(str(self.saida), texto.getvalue())


if __name__ == "__main__":
    unittest.main()
