# LiteArt Cost Analytics

Projeto pessoal para aprender Python e Análise de Dados usando o LiteArt, uma plataforma
educacional em desenvolvimento, como estudo de caso. A visão mais ampla é analisar custos de
software; o **MVP atual é uma calculadora no terminal focada nos custos de feedbacks de IA**.
Dashboard e análises de custos operacionais completos permanecem como evoluções futuras.

## Escopo atual do MVP

A execução permite importar cenários por CSV ou preencher um cenário pelo terminal. Os dois modos
estimam feedbacks, tokens e custos mensais e anuais de IA em dólares e reais, usando as mesmas
validações e funções de cálculo.

Os resultados são estimativas baseadas nas hipóteses informadas, sem chamadas reais às APIs de IA
nem comprovação de qualidade pedagógica. Não representam o custo operacional completo da aplicação:
infraestrutura e demais despesas estão fora do fluxo principal. A projeção anual pressupõe
**12 meses com consumo, preços e câmbio constantes**, sem simulação de crescimento.

### Fluxo de execução

1. Escolher entre o CSV atual e um cenário manual; opções inválidas repetem o menu.
2. Ler e validar todas as hipóteses antes de calcular ou gerar resultados.
3. Escolher entre consultar a cotação no Banco Central e informar BRL por USD manualmente.
4. Obter uma taxa válida, reutilizada em todos os cenários da execução.
5. Calcular respostas, feedbacks e tokens com `calcular_consumo_cenario()`.
6. Calcular custos de IA em USD e BRL com `calcular_custo_ia_cenario()`.
7. Organizar `resumos_cenarios` em `tabela_cenarios` com Pandas, preservando a ordem da entrada.
8. Apresentar modelo, preços, origem e referência da cotação e uma única tabela final.
9. Exportar essa tabela para `resultados/cenarios.csv`, substituindo o arquivo anterior.

O primeiro cenário não recebe mais um detalhamento individual separado. A lista de dicionários,
as tabelas redundantes e a ordenação por custo foram retiradas da apresentação principal.
Com mais de um cenário, há um resumo de menor custo, maior custo e diferença, calculado com
`.min()` e `.max()` exclusivamente sobre o custo mensal de IA em BRL. Com um cenário, esse resumo
não é exibido.

### Configurações da simulação

Modelo e preços continuam nas configurações de `calculadora.py`, separados das hipóteses de consumo.
Não são selecionáveis no menu. A cotação é escolhida após a validação dos cenários, com consulta ao
Banco Central ou preenchimento manual, sem alterar o CSV de consumo.

| Configuração atual | Valor |
| --- | --- |
| Modelo de referência | GPT-6 Luna (`gpt-6-luna`) |
| Entrada sem cache, Standard | US$ 0,10 por milhão de tokens |
| Saída faturável, Standard | US$ 0,50 por milhão de tokens |
| Cotação dos exemplos reproduzíveis | Manual: R$ 5,00 por US$ 1,00 |

As tarifas são as já registradas no código, com consulta em 23/10/2026 à
[referência do modelo](https://developers.openai.com/api/docs/models/gpt-6-luna).
Esta documentação não atualiza nem confirma preços comerciais atuais. A taxa manual de R$ 5,00 é
uma hipótese didática dos exemplos e testes, não uma cotação fixa usada como alternativa automática.
Não há seleção de modelos.

### Cotação automática ou manual

Depois de obter cenários válidos, o terminal apresenta outro menu:

- **1 — Consultar Banco Central:** usa a última cotação diária disponível do BCB.
- **2 — Informar manualmente:** solicita reais por dólar, por exemplo `5.00`, com ponto decimal e
  sem separadores de milhares. Esse modo não consulta a internet.

A fonte automática é o **Banco Central do Brasil, SGS série 1, dólar americano de venda, diário**.
O acesso a essa consulta é público e gratuito, sem chave de API. Fonte:
[catálogo oficial do BCB](https://dadosabertos.bcb.gov.br/dataset/1-taxa-de-cambio---livre---dolar-americano-venda---diario).
A data da observação pode ser anterior à execução, pois se usa a última cotação diária disponível;
não é câmbio em tempo real nem necessariamente o câmbio efetivo de um pagamento.

`consultar_cotacao_bcb()` usa `urllib.request` para uma única consulta HTTPS com `timeout=10`
segundos, mantendo a verificação padrão do certificado. `json` interpreta a resposta e `datetime`
valida a data. Esses módulos, assim como `decimal`, `urllib.error` e `http.client`, pertencem à
biblioteca padrão; nenhuma dependência externa foi acrescentada para a consulta.

A resposta deve conter uma lista com um registro, campos `data` e `valor` do tipo texto, data válida
em DD/MM/AAAA e taxa finita e estritamente positiva. `converter_cotacao()` converte o texto
diretamente para `Decimal`, sem passar por float, e reutiliza a validação numérica existente.
A entrada manual remove espaços externos, rejeita campos vazios, texto inválido, vírgula decimal,
separadores de milhares, zero, negativos, infinito e NaN; um erro repete somente a taxa.
Opções inválidas repetem a escolha do menu.

O retorno contém `brl_por_usd`, `origem` e `data_cotacao`. No modo automático, a data fica em ISO
internamente e aparece em DD/MM/AAAA no terminal, acompanhada da origem. No manual, a origem é
`manual`, `data_cotacao` é `None` e não se apresenta uma data de publicação do BCB.

`formatar_cotacao_br()` mostra pelo menos quatro casas: uma taxa manual `5.00` aparece como
`R$ 5,0000 por US$ 1,00`; `5.1234567890` aparece como `R$ 5,1234567890 por US$ 1,00`.
A taxa mantém sua precisão como Decimal; somente os custos monetários são apresentados com duas
casas. A taxa é referência para simulação e não inclui possíveis adicionais do meio de pagamento.

Falhas esperadas de rede, HTTP, leitura, JSON ou validação geram `ErroCotacaoBCB`, com mensagem.
O terminal oferece **1 para preencher manualmente ou 2 para cancelar**, sem repetir a requisição
nem substituir a falha por cotação fixa. Cancelar, usar Ctrl+C ou encerrar a entrada interrompe o
fluxo antes da exportação, com mensagem e código diferente de zero, preservando resultados
anteriores. Importar o módulo não consulta a rede, não interage e não gera arquivos.

## Instalação e execução no Windows

O conjunto foi validado em **14/11/2026**, com **Python convencional 3.14.10 x64** e
**Windows 11, build 26300**. A validação não abrange outras versões de Python, outros sistemas ou
outro computador. É necessário ter o Python convencional instalado antes de criar o ambiente;
o Python do MSYS2 não foi utilizado nessa validação.

### Obter os arquivos

Usar uma cópia do projeto que contenha `calculadora.py`, `test_calculadora.py`,
`dados/cenarios_exemplo.csv` e `requirements.txt`. A documentação acompanha esses arquivos.
Código, testes, `requirements.txt` e CSV de exemplo estão versionados no repositório local.
A validação em ambiente novo usou uma cópia dos arquivos locais; o registro correspondente descreve
o estado daquela etapa. Antes de publicar uma versão, incorporar também os materiais finais e
confirmar o commit escolhido no GitHub.

Para obter o repositório com Git:

```powershell
git clone https://github.com/MrNemo31/Calculadora-LiteArt-Cost-Analytics.git LiteArt-Cost-Analytics
Set-Location -LiteralPath '.\LiteArt-Cost-Analytics'
```

Como alternativa, copiar os arquivos atuais para uma pasta própria e abrir o PowerShell nela.
Não é necessário copiar `.venv`, `.venv-win`, `.git`, caches, credenciais ou resultados gerados.
Os passos abaixo pressupõem a pasta do projeto aberta e a presença de `requirements.txt`.

### Preparar o ambiente e executar

Os comandos de criação destinam-se a uma pasta sem `.venv-win`. Preservar ambientes existentes;
para repetir o preparo com isolamento, usar outra cópia do projeto ou um nome de ambiente novo.
Informar o caminho completo do `python.exe` convencional quando solicitado. O primeiro comando de
inspeção mostra versão, plataforma e localização para conferir essa escolha; a plataforma validada
é `win-amd64`.

```powershell
$pythonBase = Read-Host 'Caminho completo do python.exe convencional (Python 3.14.10 x64)'
& $pythonBase -X utf8 -B -c "import sys, sysconfig; print(sys.executable); print(sys.version); print(sysconfig.get_platform())"
& $pythonBase -X utf8 -B -m venv .venv-win
$pythonProjeto = (Resolve-Path -LiteralPath '.\.venv-win\Scripts\python.exe').Path
& $pythonProjeto -X utf8 -B -m pip install -r requirements.txt
& $pythonProjeto -X utf8 -B -m pip check
& $pythonProjeto -X utf8 -B -m unittest -q
& $pythonProjeto -X utf8 -B calculadora.py
```

`venv` cria um ambiente isolado; `python -m pip` instala com o interpretador explicitamente escolhido.
`pip check` confere conflitos e dependências ausentes, mas não substitui os testes. Conferir o
resultado de cada comando antes de continuar. Não é necessário ativar o ambiente, alterar PATH ou
mudar a política de execução do PowerShell. `-X utf8` mantém os acentos na saída e `-B` evita bytecode.
No VS Code, selecionar o executável desse ambiente em **Python: Select Interpreter**, sem exigir
alterações automáticas de configuração. Os ambientes de desenvolvimento anteriores, `.venv`
baseada em MSYS2 e `.venv-win` convencional, foram preservados durante a validação.

### Dependências e versões fixadas

[requirements.txt](requirements.txt) registra o conjunto externo já instalado e testado:

| Pacote | Versão fixada | Relação com o projeto |
| --- | --- | --- |
| `pandas` | `3.1.0` | Direta: importado no código e nos testes para tabelas, CSV e comparação de DataFrames |
| `numpy` | `2.5.4` | Indireta: suporte numérico exigido pelo Pandas |
| `python-dateutil` | `4.0.0` | Indireta: tratamento de datas exigido pelo Pandas |
| `tzdata` | `2026.6` | Indireta: dados de fusos horários exigidos nesse conjunto no Windows |
| `plotly` | `7.1.0` | Direta: primeiro gráfico interativo do estudo, exportado como HTML offline |
| `narwhals` | `2.29.0` | Indireta: compatibilidade entre estruturas de dados exigida pelo Plotly |
| `packaging` | `26.3` | Indireta: suporte a versões e pacotes exigido pelo Plotly |

As versões foram obtidas dos metadados da `.venv-win`. Em 19/11/2026 foram acrescentados somente
Plotly e suas dependências Narwhals e Packaging, preservando as versões dos pacotes anteriores.
`pip check` não encontrou dependências ausentes ou conflitantes. Não foram instalados Kaleido,
navegadores, Dash ou ferramentas opcionais. A validação em ambiente limpo de 14/11/2026 refere-se
ao conjunto original do MVP; essa instalação limpa não foi repetida com Plotly. Os testes usam
`pandas.testing` e `unittest`, sem exigir pytest ou outras ferramentas opcionais. Módulos como
`decimal`, `pathlib`, `urllib`, `json` e `unittest` já pertencem ao Python e não entram no arquivo.
Pip também não é uma dependência da aplicação.

Fixar versões diretas e indiretas reduz variações do conjunto instalado, mas o arquivo não é um
lock completo nem garantia universal de reprodução. Ele não fixa o Python, o sistema, os artefatos
com hashes ou sua disponibilidade futura. O alcance comprovado é o ambiente descrito acima.

A instalação dos pacotes e a obtenção do projeto podem precisar de internet. A consulta automática
do BCB também usa internet; após a instalação, cenários manuais ou CSV com cotação manual funcionam
sem rede. A suíte simula o BCB e não depende da cotação do dia.

### Evidências da validação em ambiente novo

Em 14/11/2026, código, testes, CSV de exemplo e requirements foram copiados para uma pasta temporária
exclusiva. Um ambiente novo foi criado com o interpretador base convencional, sem pacotes globais
ou do usuário. A instalação por `pip install -r requirements.txt` usou wheels, sem compilação,
e as quatro versões instaladas corresponderam ao arquivo. `pip check` não encontrou conflitos;
os **188 métodos de teste em 17 classes passaram** nessa cópia.

Foram conferidos o fluxo CSV e um cenário manual equivalente a 100 usuários, com taxa manual
`Decimal("5.00")`, apresentação brasileira e os resultados didáticos da tabela abaixo. As execuções
a partir de outra pasta localizaram os arquivos corretamente. Conexões e DNS foram bloqueados
nessas conferências de execução; o modo manual funcionou mesmo sem o CSV disponível na cópia.

As verificações pontuais também confirmaram nove colunas exportadas, acentos, substituição sem
duplicar linhas e precisão além da segunda casa: `2.254320987160` foi recuperado do texto diretamente
como Decimal com uma taxa manual de mais casas. Importar o módulo não iniciou interação, rede,
leitura de CSV ou exportação nem modificou os resultados existentes.

A primeira tentativa de instalação falhou por resolução de rede do PyPI; a repetição com acesso
permitido concluiu a instalação. Isso foi uma limitação de rede, não uma falha do projeto ou
necessidade de internet para executar o modo manual. A pasta temporária foi removida após conferir
seu caminho. Arquivos e resultados originais e os dois ambientes de desenvolvimento foram preservados.
Não foram acrescentados testes persistentes nessa validação.

### Escolher os cenários e a cotação

O menu oferece:

- **1 — Importar `dados/cenarios_exemplo.csv`:** aceita uma quantidade não vazia de cenários válidos.
- **2 — Preencher um único cenário pelo terminal:** não lê nem exige a existência do CSV.

Para um exemplo manual, escolher `2` e responder, na ordem: `Cenário manual`, `100`, `40`, `0.60`,
`0.25`, `500` e `300`. No menu seguinte, escolher `2` para cotação manual e digitar `5.00`.
Com essa taxa didática, o resultado é 2.200 feedbacks, IA mensal de US$ 0,44 e R$ 2,20 e IA anual de
US$ 5,28 e R$ 26,40. Para reproduzir o CSV de exemplo, escolher `1` no menu de cenários, depois `2`
no menu de cotação e informar `5.00`. Ao terminar, o terminal informa o caminho do CSV salvo.
Escolher cotação automática pode alterar os valores em BRL; consumo e custos em USD são preservados.

### Entrada de cenários e regras de preenchimento

`dados/cenarios_exemplo.csv` contém os cenários didáticos de 100 e 500 usuários. É um arquivo de
**entrada**, versionável e distinto de `resultados/cenarios.csv`, que contém resultados calculados.
Usar UTF-8 com ou sem BOM, cabeçalho, vírgula entre campos e ponto decimal, sem separadores de
milhares. As sete colunas obrigatórias são:

| Coluna | Unidade e regra | Exemplo |
| --- | --- | --- |
| `cenario` | Nome não vazio | Turma de revisão |
| `usuarios_ativos` | Usuários/mês; inteiro não negativo | `100` |
| `respostas_por_usuario` | Média de respostas/usuário/mês; não negativa | `40` |
| `taxa_acerto` | Proporção das respostas corretas, de 0 a 1 | `0.60` |
| `proporcao_acertos_com_feedback` | Proporção dos acertos com feedback, de 0 a 1 | `0.25` |
| `tokens_entrada` | Média de tokens de entrada/feedback; não negativa | `500` |
| `tokens_saida` | Média de tokens de saída faturáveis/feedback; não negativa | `300` |

Os mesmos campos são solicitados no modo manual, com nome, unidades e exemplos. As taxas continuam
entre 0 e 1: `0.60` corresponde a 60%. Vírgula decimal e taxas digitadas de 0 a 100 não são aceitas.
Usuários devem ser representados como inteiro: `100.0` e `100.5` são rejeitados, sem truncamento.
Médias fracionárias, como `40.5`, são permitidas nos campos correspondentes.

Para editar ou acrescentar cenários, manter o cabeçalho e preencher uma linha por cenário, com
nomes que facilitem sua identificação. O arquivo inteiro é validado antes dos cálculos. A tabela
final e a exportação preservam sua ordem, sem ordenação automática por custo no MVP atual.
O exemplo contém 40 respostas por usuário, taxa de acerto de 0.60, proporção de acertos com feedback
de 0.25 e 500/300 tokens por feedback. Não incluir preços, cotação, capacidade ou resultados nesse
arquivo de consumo.

`ler_cenarios_csv(caminho)` começa lendo os campos como texto, sem transformar campos vazios em NaN.
`ler_cenario_terminal()` recebe textos de `input()`. Ambas reutilizam
`converter_hipotese_consumo()`: usuários são convertidos diretamente para `int`; as outras cinco
hipóteses, para `float`, com validação de números finitos e não negativos e taxas no intervalo
inclusivo de 0 a 1. Isso não converte os valores financeiros para float.

A leitura retorna uma lista de dicionários com `nome` e `hipoteses_consumo`; o modo manual retorna
um dicionário dessa estrutura, encaminhado como lista de um elemento ao fluxo comum.

### Validações, erros e cancelamento

- Espaços externos são removidos; nome e campos obrigatórios não podem ficar vazios.
- CSV vazio, somente com cabeçalho, colunas ausentes ou inesperadas e registros malformados falham.
- Textos não numéricos, negativos, infinito, NaN e taxas fora do intervalo são rejeitados.
- Erros de campo no CSV identificam o registro de dados, contado a partir de 1, e a coluna.
  Esse número não equivale necessariamente à linha física do arquivo.
- A função de leitura preserva `FileNotFoundError` para arquivo inexistente e usa `ValueError`
  nas falhas de validação, sem retornar resultados parciais.
- No terminal, um campo inválido informa o motivo e repete somente aquela pergunta.
- No modo CSV, falhas de leitura encerram a execução com mensagem e código diferente de zero,
  antes de criar ou sobrescrever resultados. Não há cenários fixos como alternativa oculta.
- Ctrl+C ou fim da entrada encerram o menu ou preenchimento com uma mensagem de cancelamento,
  sem gerar resultados nem modificar o arquivo de resultados anterior.

O caminho do CSV de entrada parte de `Path(__file__).resolve().parent`. Abrir o terminal em outra
pasta não muda sua localização. Importar `calculadora` não apresenta menu, lê arquivos, imprime
resultados nem exporta CSV: essas ações ficam em `if __name__ == "__main__":`.

## Regras de consumo e resultados didáticos

Cada erro gera um feedback. Nos acertos, apenas a proporção informada recebe feedback. Assim,
100 usuários com 40 respostas produzem 4.000 respostas, 1.600 erros e 600 feedbacks nos acertos:
2.200 feedbacks mensais. O gabarito determina acerto ou erro, sem consulta à IA na simulação.

Tokens de entrada incluem o conteúdo necessário à requisição; tokens de saída representam a
saída faturável. As médias de 500 e 300 tokens são hipóteses didáticas, sem medição ou garantia de
qualidade pedagógica. A regra agregada não mede quantos estudantes ativaram uma opção individual.

### Tabela final

O terminal identifica modelo, tarifas, cotação e limitações antes de apresentar uma única tabela.
Os títulos são legíveis e as quatro colunas financeiras mostram o símbolo da moeda em cada valor.
A tabela abaixo resume os resultados do CSV de exemplo **com cotação manual de R$ 5,00 por USD**.
As contagens não são formatadas como dinheiro, e a execução pode mostrar `.0` em contagens estimadas.

| Cenário | Usuários ativos | Feedbacks/mês | Tokens entrada/mês | Tokens saída/mês | IA mensal (USD) | IA mensal (BRL) | IA anual (USD) | IA anual (BRL) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Cenário didático: 100 usuários | 100 | 2200 | 1100000 | 660000 | US$ 0,44 | R$ 2,20 | US$ 5,28 | R$ 26,40 |
| Cenário didático: 500 usuários | 500 | 11000 | 5500000 | 3300000 | US$ 2,20 | R$ 11,00 | US$ 26,40 | R$ 132,00 |

Nesse exemplo, o resumo mensal de IA em BRL apresenta menor custo de R$ 2,20, maior de R$ 11,00 e
diferença de R$ 8,80. São extremos dos cenários completos de IA, sem filtro de orçamento.
A diferença depende das hipóteses de consumo, dos preços e da cotação configurados.

### Precisão e apresentação monetária

Preços e custos financeiros são mantidos como `Decimal`, sem conversão para float ou arredondamento
intermediário. `resumos_cenarios` conserva esses objetos; o DataFrame é criado com
`pd.DataFrame.from_records(resumos_cenarios, coerce_float=False)`.
As quatro colunas financeiras têm `dtype object`, que permite armazenar objetos Python, mas sozinho
não comprova o tipo: os testes verificam explicitamente `isinstance(valor, Decimal)`.

`formatar_moeda_br()` formata diretamente o Decimal com `:,.2f` e troca os separadores para o padrão
brasileiro, independentemente da configuração regional. Por exemplo, `Decimal("1400")` aparece como
`1.400,00`. Os formatadores passados a `DataFrame.to_string()` acrescentam `R$` ou `US$` apenas na
apresentação, sem substituir os dados do DataFrame por textos. A representação exibida tem duas
casas decimais; a precisão completa permanece nos cálculos e na exportação. Quantidades não recebem
formatação monetária e não são arredondadas para inteiros apenas para apresentação.

## Exportação dos resultados

`tabela_cenarios` é exportada para **`resultados/cenarios.csv`**, relativo à pasta de
`calculadora.py`, independentemente da pasta atual do terminal. A pasta é criada automaticamente
com `mkdir(parents=True, exist_ok=True)`. Cada execução concluída substitui o resultado anterior,
sem acumular linhas, e informa o caminho salvo.

O CSV tem cabeçalho e as mesmas nove informações da tabela final, nesta ordem:

| Coluna técnica | Conteúdo |
| --- | --- |
| `cenario` | Nome do cenário |
| `usuarios_ativos` | Usuários ativos no mês |
| `feedbacks_mensais` | Quantidade estimada de feedbacks no mês |
| `tokens_entrada_total` | Tokens estimados de entrada no mês |
| `tokens_saida_total` | Tokens estimados de saída faturáveis no mês |
| `custo_ia_mensal_usd` | Custo mensal de IA em USD |
| `custo_ia_mensal_br` | Custo mensal de IA em BRL |
| `custo_ia_anual_usd` | Custo anual constante de IA em USD |
| `custo_ia_anual_br` | Custo anual constante de IA em BRL |

**O formato de resultados mudou:** deixou de incluir infraestrutura e totais operacionais que
somavam infraestrutura e IA. O CSV de entrada continua com suas sete colunas de hipóteses.
Origem, data e valor da cotação não foram acrescentados às nove colunas de resultados: a origem e a
data automática são apresentadas no terminal, não exportadas como metadados.

A exportação usa UTF-8, vírgula entre campos, ponto decimal, cabeçalho e `index=False`, sem coluna
adicional de índice. Recebe os valores completos, sem símbolos de moeda, separadores de milhares,
conversão para float ou formatação de duas casas. Um custo exibido como `R$ 2,20` pode ser escrito
como `2.200000`, preservando o valor interno. `resultados/` está ignorada pelo Git.

CSV armazena texto e não preserva o tipo Python `Decimal`. Ao conferir ou reutilizar resultados,
ler os campos financeiros como texto e convertê-los diretamente para `Decimal`, sem passar por
float. Essa releitura não equivale a importar resultados como novas hipóteses de consumo.

## Recursos preservados fora do fluxo principal

As funções `calcular_custo_servico()`, `calcular_custo_infra_cenario()` e `calcular_cenario()`
continuam disponíveis no código, com seus testes unitários. Permitem retomar os cálculos de
infraestrutura e do cenário completo posteriormente. O fluxo principal usa diretamente consumo e
IA, sem chamar a coordenadora completa nem calcular infraestrutura desnecessariamente.

A associação de capacidade, o orçamento fixo, a comparação ordenada de custos operacionais, o filtro
e o saldo de orçamento saíram da execução principal. As experiências anteriores permanecem no
histórico; orçamento não é uma opção do menu atual. Sua retomada e a integração dos cálculos
preservados serão decisões futuras, separadas do MVP de IA.

As pesquisas históricas de infraestrutura, datas, fontes, fórmulas e ressalvas permanecem no
[planejamento](PLANEJAMENTO.md). Mensalidades pesquisadas não comprovam capacidade para atender aos
cenários. A arquitetura de referência do LiteArt continua Flutter, NestJS e PostgreSQL, com
Firebase como alternativa em estudo; isso não implica contratação ou migração.

## Testes e verificações

`test_calculadora.py` contém **188 métodos de teste em 17 classes**, usando `unittest`:

- 111 métodos em 11 classes de cálculos e coordenadoras, incluindo infraestrutura e cenário completo.
- 25 métodos para leitura e validação de CSV.
- 4 métodos para a formatação monetária brasileira.
- 7 métodos para entrada manual e suas validações.
- 9 métodos para consulta ao BCB com respostas simuladas e validação do retorno.
- 8 métodos para escolha, entrada e apresentação da cotação.
- 24 métodos de integração dos cenários, cotação, tabelas, mensagens e exportação.

Esses 188 métodos passaram na validação em ambiente novo de 14/11/2026. A rotina do estudo
acrescentou inicialmente 30 métodos, depois 17 para as comparações e **19 para os indicadores**,
totalizando **66 métodos em duas classes** em [test_analise_estudo.py](test_analise_estudo.py),
sem alterar os testes do MVP. Os gráficos possuem **36 métodos em duas classes** em
[test_graficos_estudo.py](test_graficos_estudo.py): 18 do primeiro e 18 acrescentados para o segundo.
O conjunto atual possui **290 métodos em 21 classes**: 188 do MVP, 66 da análise e 36 dos gráficos.
Todos passaram em **25/11/2026** na implementação dos indicadores, conforme a execução registrada
nesta sessão. A suíte não foi repetida nesta atualização documental. Casos de `subTest` não são
métodos adicionais.
Os testes persistentes simulam `input()` com `unittest.mock.patch` e usam
arquivos temporários nas integrações. Conferem erros e cancelamento sem sobrescrita, execução de
outra pasta, ordem de múltiplos cenários, cenário único, ausência de chamadas à infraestrutura e ao
cálculo completo, nove campos exportados e preservação exata de Decimal.

Também conferem os símbolos monetários da tabela sem alteração dos dados, precisão além da segunda
casa e equivalência dos dois modos para as mesmas hipóteses. As verificações pontuais históricas,
registradas em [PROMPTS.md](PROMPTS.md), não devem ser contadas como novos métodos automatizados.
Os testes cambiais simulam respostas da API, timeout, erros HTTP/rede e leitura, JSON inválido,
estruturas e tipos incorretos, campos ausentes, datas e taxas inválidas. Também conferem modo manual
sem rede, alternativa manual após falha, cancelamento sem exportação e uma consulta para múltiplos
cenários. Com taxa simulada diferente, somente os custos em BRL mudam; o CSV mantém seus nove campos.
A suíte não depende da internet nem da cotação do dia. Uma consulta real separada é verificação
pontual, não teste automatizado. Esta revisão de documentação não acrescenta testes.

Os testes do estudo cobrem esquema, campos obrigatórios, identificadores e combinações únicos,
conversões numéricas, taxas, datas e condições fixas. Também conferem fórmulas independentes,
Decimal, precisão da exportação, preservação das entradas e dos resultados anteriores diante de
falhas, importação sem efeitos, execução de outra pasta e reexecução sem duplicar linhas.
Os 17 métodos adicionais cobrem referências e fórmulas das comparações, identificação independente
de ordem/índice, condições compatíveis, preservação da tabela, percentuais com referência zero,
precisão do contexto Decimal e exportação das três tabelas. As conferências pontuais dos CSVs
existentes complementam esses testes, sem aumentar sua contagem.
Os 19 testes dos indicadores cobrem os 13 cenários, denominadores zero independentes, entrada
gratuita, custos e usuários inválidos, inteiros escalares do Pandas, coerência dos totais,
preservação da entrada e do contexto Decimal, divisões não exatas, exportação precisa e campos
vazios para None. Também conferem as oito casas na apresentação e a integração do quarto CSV
sem sobrescrever resultados anteriores diante de falhas.
Os 36 testes dos gráficos usam dados controlados e arquivos temporários. Os primeiros conferem
nove barras, três séries, ordens, associação por ID, valores e textos monetários, entrada inválida,
preservação dos dados, importação sem efeitos e HTML offline. Os 18 novos cobrem quatro barras
horizontais, sinais e referência C05, percentuais não aplicáveis, condições e tokens compatíveis,
preservação de Decimal e integração que constrói ambas as figuras antes de gravar os HTMLs.
Esses testes estruturais não comprovam legibilidade visual. A revisão separada no Chrome ocorreu
em 19/11/2026, no alcance descrito abaixo. Após um ajuste de posição de texto, os 36 testes dos
gráficos passaram novamente, sem alteração dos testes; a suíte completa não foi repetida nessa
revisão. Nenhum teste foi executado nesta atualização documental.

Para executar a suíte com o ambiente existente:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest -q
```

## Estudo de caso

O estudo de caso para o **Google Data Analytics Professional Certificate** utiliza as funções da
calculadora para analisar estimativas de custos de IA, sem dados reais de
utilização dos estudantes. O público será o responsável pelo planejamento do LiteArt, para apoiar
o orçamento de IA e identificar hipóteses que precisam ser medidas antes do lançamento.

**Pergunta principal:** como a quantidade de usuários, a política de feedback nos acertos e o
consumo de tokens afetam o custo mensal estimado de IA do LiteArt?

A matriz foi revisada: **nove cenários principais** cruzam escalas de usuários e políticas de
feedback, e **quatro variações de sensibilidade** alteram uma hipótese de tokens por vez em relação
a C05. As condições fixas de cálculo foram documentadas em **2026-11-18**:

- **Modelo:** OpenAI, API direta, GPT-6 Luna (`gpt-6-luna`), Standard para texto, contexto curto.
- **Tarifas:** entrada sem cache de `Decimal("0.10")` USD por milhão de tokens e saída faturável de
  `Decimal("0.50")` USD por milhão. Data da pesquisa documental: **2026-11-18**.
- **Cotação fixa:** `Decimal("5.8102")` BRL por USD, Banco Central, SGS série 1, dólar americano de
  venda diário. Data da observação cambial: **2026-11-18**; data da consulta: **2026-11-18**, sem
  horário registrado.

Essas tarifas e a cotação serão mantidas nos 13 cenários para permitir comparações reproduzíveis.
São referências históricas dessa pesquisa, sem afirmar preços, câmbio ou disponibilidade
permanentemente atuais. As fontes, modalidades, exclusões e evidência cambial estão em
[ESTUDO_DE_CASO.md](ESTUDO_DE_CASO.md), junto da matriz, indicadores e etapas.

O MVP continua permitindo consultar o BCB ou informar uma taxa manual. A rotina separada do estudo
lê **5.8102** de `condicoes_fixas.csv`, sem interação ou atualização automática do câmbio.
A cotação didática de R$ 5,00 dos exemplos e testes do MVP permanece histórica e não será usada
como taxa deste estudo. Essa definição documental não modifica o funcionamento da calculadora.

A definição documental e a **preparação e conferência pontual dos dados de entrada estão
concluídas**. Os arquivos do estudo são:

- [cenarios.csv](dados/estudo_de_caso/cenarios.csv): 13 cenários hipotéticos, ordenados de C01 a C13,
  com oito colunas para identificação, nome e seis hipóteses de consumo.
- [condicoes_fixas.csv](dados/estudo_de_caso/condicoes_fixas.csv): uma linha com 12 colunas, contendo
  modelo, modalidade, tarifas, câmbio, fontes e datas, aplicável a todos os cenários.

Os dois CSVs usam UTF-8 sem BOM, vírgula entre campos, ponto decimal, cabeçalho e ausência de índice,
sem símbolos monetários, percentuais ou separadores de milhares nos números. CSV não preserva tipos
Python: a rotina lê os campos financeiros como texto e os converte diretamente para `Decimal`,
sem passar por float ou aplicar arredondamento de exibição aos dados.

Essas entradas pertencem ao estudo. O arquivo `dados/cenarios_exemplo.csv` continua sendo a entrada
de cenários do menu CSV do MVP, enquanto `resultados/cenarios.csv` contém resultados gerados pela
calculadora. O `cenarios.csv` do estudo inclui `id_cenario` além das sete colunas aceitas por
`ler_cenarios_csv()`, que rejeita colunas inesperadas. Por isso, **não é diretamente compatível com
o importador atual**. O MVP não lê automaticamente nenhum dos dois arquivos do estudo.
A leitura específica está implementada em [analise_estudo.py](analise_estudo.py), separada do menu
e do código do MVP. Ela valida os dois CSVs, adapta as hipóteses às funções reutilizáveis, calcula
consumos e custos sob as condições fixas e calcula as comparações antes de exportar.
`comparar_politicas()` produz seis pares: C01/C02 contra C03, C04/C05 contra C06 e C07/C08 contra
C09, sempre dentro da mesma escala. `analisar_sensibilidade()` compara C10 a C13 com C05,
variando somente o token previsto e mantendo hipóteses e condições comerciais compatíveis.
`calcular_indicadores()` usa os resultados já calculados para obter participações e custos por
usuário ativo. Todas as tabelas são validadas e calculadas antes de iniciar a exportação.
Não consulta a rede. Importar o módulo não lê arquivos, imprime ou exporta resultados.

Com o terminal na raiz do projeto, executar o cálculo, os testes do estudo ou toda a suíte:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest test_analise_estudo -q
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest discover -v
```

A saída é `resultados/estudo_de_caso/resultados_cenarios.csv`, relativa à pasta do script,
independentemente da pasta atual do terminal. São **13 linhas e 35 colunas**: identificador e nome,
seis hipóteses, sete consumos, oito custos e os 12 campos das condições com fontes e datas.
A mesma execução também exporta:

- `resultados/estudo_de_caso/comparacao_politicas.csv`: seis linhas e 20 colunas, com referências,
  custos e reduções absolutas e percentuais, acompanhadas das condições utilizadas.
- `resultados/estudo_de_caso/sensibilidade_tokens.csv`: quatro linhas e 24 colunas, com tokens
  comparados, custos e variações absolutas e percentuais, acompanhadas das condições utilizadas.
- `resultados/estudo_de_caso/indicadores_cenarios.csv`: 13 linhas e 11 colunas, com identificação,
  usuários, custos de base, participações de entrada/saída e custos mensais por usuário em USD e BRL.

A pasta é criada automaticamente e cada execução substitui os arquivos, sem acumular linhas.
Erros de entrada ou comparabilidade impedem a exportação e preservam resultados anteriores.
Os quatro resultados ficam ignorados pelo Git, junto dos demais arquivos de `resultados/`.

Tarifas, câmbio e custos permanecem `Decimal`. A tabela de custos no terminal apresenta identificador,
usuários, feedbacks e custos mensais, usando `US$` e `R$`, vírgula decimal e duas casas somente na
apresentação. O CSV usa UTF-8, vírgula entre campos, ponto decimal, cabeçalho e ausência de índice,
com valores completos. Na releitura, converter os campos financeiros de texto diretamente para
Decimal. O esquema e as conferências estão em [ESTUDO_DE_CASO.md](ESTUDO_DE_CASO.md).

**Os 13 cenários foram calculados e conferidos em 18/11/2026; as comparações de políticas e tokens
já estão implementadas e exportadas.** A atualização documental de 19/11/2026 registra esse avanço
sem atualizar as condições fixas. Os dois gráficos foram implementados e gerados em 19/11/2026,
conforme abaixo. A revisão visual foi concluída no Chrome nas dimensões informadas. As participações
e os custos por usuário foram implementados e conferidos em **25/11/2026**. A interpretação e a
formulação de recomendações condicionais foram concluídas nessa data. O relatório final e as duas
imagens estão produzidos; revisão final, conferência das orientações do curso e publicação do
estudo permanecem pendentes.
As conferências não comprovam acesso pela conta da API, consumo real de tokens, configuração de
raciocínio testada ou qualidade pedagógica equivalente. O estudo não está concluído, aprovado pelo
curso ou validado pelo Google.

### Relatório final do estudo

**[Ler o relatório final — RELATORIO_ESTUDO.md](RELATORIO_ESTUDO.md)**

O relatório reúne contexto, dados, método, resultados, dois gráficos, recomendações condicionais
e limitações. As duas imagens em `docs/imagens/` acompanham o relatório nos arquivos preparados
para o repositório. Os HTMLs interativos e os quatro CSVs de resultados ficam fora do Git e podem
ser regenerados pelos comandos de reprodução abaixo.

O material foi produzido e conferido no alcance documentado, mas o estudo ainda não foi publicado,
aprovado pelo Google ou avaliado pelo curso. Permanecem a revisão final de coerência, a conferência
das orientações específicas da atividade e a preparação da publicação. O estudo é separado do
MVP v0.1.0 publicado e não representa uma nova release da calculadora.

### Interpretação e recomendações propostas

[INTERPRETACAO_ESTUDO.md](INTERPRETACAO_ESTUDO.md) reúne a interpretação das políticas de feedback,
da sensibilidade dos tokens e do custo por usuário. A síntese explica os resultados sob hipóteses
constantes e apresenta recomendações condicionais, acompanhadas de um plano de medição futura de
uso, tokens faturáveis e qualidade dos feedbacks.

Nenhuma política foi adotada definitivamente ou demonstrada como pedagogicamente superior.
Piloto, coleta de dados e avaliação pedagógica não foram executados. A interpretação e as propostas
já integram o relatório final; sua produção não significa execução dessas ações.

### Indicadores do estudo

A execução de `analise_estudo.py`, pelos comandos acima, também mostra e exporta as participações
de entrada e saída no custo de IA e o custo mensal de IA por usuário ativo, em USD e BRL.
A tabela separada preserva os 13 identificadores e a ordem dos cenários. Seu arquivo é
`resultados/estudo_de_caso/indicadores_cenarios.csv`, relativo à pasta do script, sem alterar
os três CSVs anteriores, o retorno da rotina ou o funcionamento do MVP v0.1.0.

As participações dividem cada componente pelo total mensal **na mesma moeda, USD**, multiplicando
por 100. O custo por usuário divide o total mensal da respectiva moeda pelos **usuários ativos**,
convertidos de inteiro diretamente para Decimal. Se o total USD for zero, as participações são
`None`; se os usuários forem zero, os dois custos unitários são `None`. Cada denominador é tratado
independentemente. Esses casos aparecem como `Não aplicável` no terminal e como **campo vazio no
CSV**; não são valores iguais a zero. Entrada gratuita com saída paga, por exemplo, tem participação
de entrada igual a zero, e não um indicador não aplicável.

Custos e percentuais aplicáveis continuam Decimal. As divisões seguem a precisão vigente em um
contexto local, sem alterar o contexto global ou arredondar explicitamente os dados intermediários.
No terminal, uma cópia de apresentação mostra percentuais com duas casas e custos unitários com
**oito casas decimais**, para não ocultar valores inferiores a um centavo. Em C05 são 25% de entrada,
75% de saída, `US$ 0,00440000` e `R$ 0,02556488` por usuário ativo/mês. O CSV exporta os valores
completos; na releitura, manter texto até convertê-lo diretamente para Decimal, sem float.

Esse custo unitário inclui **somente IA**, sem representar o custo operacional completo,
economia de escala ou viabilidade financeira comprovada. Modelo, tarifas e cotação histórica fixa
`Decimal("5.8102")` continuam com as referências de **18/11/2026**. A pausa no desenvolvimento não
atualizou essas condições. Fórmulas, validações e evidências estão em
[ESTUDO_DE_CASO.md](ESTUDO_DE_CASO.md).

### Gráficos do estudo

[graficos_estudo.py](graficos_estudo.py) gera o **custo mensal estimado de IA por escala e política
de feedback**, usando C01 a C09. São nove barras agrupadas: escalas de 100, 500 e 1.000 usuários e
políticas “Somente nos erros”, “Erros + 25% dos acertos” e “Todas as respostas”. Os cenários são
alternativas lado a lado, sem somar custos. C10 a C13 não entram nesse gráfico.

O segundo gráfico mostra a **sensibilidade do custo mensal de IA aos tokens**, comparando C10 a
C13 com C05. São quatro barras horizontais: negativas indicam redução de custo; positivas, aumento.
A linha em zero e o eixo percentual usam C05 como denominador, mantendo condições fixas.
Os detalhes das comparações estão em [ESTUDO_DE_CASO.md](ESTUDO_DE_CASO.md).

Com o terminal na raiz, gerar os CSVs e depois os dois gráficos pelo comando existente:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B graficos_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest test_graficos_estudo -q
```

O comando `graficos_estudo.py` gera ambos os arquivos, relativos à pasta do script:

- `resultados/estudo_de_caso/custo_mensal_por_escala_politica.html`: escala e política, C01 a C09.
- `resultados/estudo_de_caso/sensibilidade_tokens.html`: variações de tokens, C10 a C13 contra C05.

Para visualizar, localizar cada HTML no Explorador de Arquivos e abri-lo manualmente no navegador.
Ambos incorporam Plotly e funcionam offline, sem carregar a biblioteca de CDN ou abrir o navegador
automaticamente. Se um CSV estiver ausente, a rotina orienta como gerá-lo, sem executar a análise.
As duas entradas e figuras são validadas antes de gravar; dados inválidos ou percentual não
aplicável interrompem a geração e preservam os HTMLs anteriores, sem criar barras fictícias.

Os campos financeiros e percentuais são reconstruídos de texto diretamente para Decimal.
Somente a coluna de coordenadas de uma cópia de cada visualização usa `float`; ela não alimenta
cálculos ou exportações financeiras. Rótulos e hover são preparados dos Decimal, com formatação
brasileira. A geometria das barras é aproximada. Os CSVs permanecem intactos e os HTMLs ficam fora
do Git em `resultados/`.

Os dois HTMLs passaram por **revisão visual no Chrome em 19/11/2026**, em janelas de **1440×900**
e **800×800**, com rede desativada. Foram conferidos valores, rótulos, hover, legenda, zoom e
restauração dos eixos. Uma sobreposição entre título e referência no segundo gráfico foi corrigida;
os HTMLs foram regenerados e revistos. As instruções de abertura manual permanecem as mesmas.

A revisão não cobre telas menores, dispositivos móveis ou outros navegadores. As evidências e o
alcance estão em [ESTUDO_DE_CASO.md](ESTUDO_DE_CASO.md). A rotina gera HTMLs; os PNGs do relatório
foram exportados separadamente pelo navegador. Exportação automática em imagem pela rotina e
dashboard não foram implementados.

A **v0.1.0 permanece o MVP publicado**, com sua tag preservada. A rotina do estudo reutiliza suas
funções e não representa automaticamente uma nova release da calculadora.

## Próximos passos

A consulta BCB/SGS série 1, o registro de dependências e a validação em ambiente virtual novo estão
concluídos no alcance descrito.

A revisão técnica final de 14/11/2026 conferiu a coerência entre código, requisitos, exemplos e
instruções, com os 188 testes aprovados. A v0.1.0 está publicada como MVP de terminal; as
[notas da versão](RELEASE_NOTES.md) registram os materiais de sua preparação. Essa distribuição
não representa hospedagem de dashboard.

O relatório final do estudo e suas imagens estão produzidos. Os próximos passos são a revisão
final de coerência, a conferência das orientações específicas do curso, inclusive a declaração do
apoio de IA, e a preparação da publicação. O estudo ainda não foi publicado.
A revisão dos HTMLs em outros tamanhos ou navegadores depende de uma conferência própria, sem
ampliar automaticamente o alcance já comprovado.
As relações verificadas pelas fórmulas não são evidências empíricas sobre estudantes.
A tag v0.1.0 permanece preservada como referência histórica.

Ambientes e resultados gerados permanecem fora do versionamento: `.venv/` e `resultados/` pelas
regras da raiz, e `.venv-win/` pelo `.gitignore` criado dentro desse ambiente.

Catálogo e seleção de modelos, comparação entre provedores, demais gráficos e exportação automática
em imagem, dashboard com Streamlit, retomada de infraestrutura e orçamento e análises avançadas
ficam para depois. Os dois gráficos Plotly do estudo estão implementados, conforme descrito acima.
Comparar custos não exige chamadas reais às APIs nem comprova equivalência pedagógica.

## Licença

Este projeto é disponibilizado sob a [licença MIT](LICENSE), escolhida e autorizada explicitamente
em 14/11/2026. São permitidos uso, modificação e distribuição, inclusive comercial, preservando os
avisos de direitos autorais e de licença exigidos pelo texto integral.

Dependências e fontes de dados mantêm suas próprias licenças e condições. A licença do código do
projeto não substitui nem amplia as permissões sobre esses materiais de terceiros.

## Documentação e aprendizado

O [planejamento](PLANEJAMENTO.md) separa estado atual, recursos preservados e roteiro futuro.
O [registro de prompts](PROMPTS.md) mantém as decisões e os marcos históricos do desenvolvimento.
O projeto evolui em pequenos incrementos, com apoio de IA para orientação, explicações e revisão.

A configuração `.markdownlint.json` limita o texto a 100 caracteres por linha, exceto tabelas e
blocos de código, e define tabelas no estilo `compact`. A verificação deve usar a ferramenta já
disponível no ambiente, sem alterar essas regras.
