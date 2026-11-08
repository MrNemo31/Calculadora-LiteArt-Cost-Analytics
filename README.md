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
3. Calcular respostas, feedbacks e tokens com `calcular_consumo_cenario()`.
4. Calcular custos de IA em USD e BRL com `calcular_custo_ia_cenario()`.
5. Organizar `resumos_cenarios` em `tabela_cenarios` com Pandas, preservando a ordem da entrada.
6. Apresentar a identificação da simulação e uma única tabela final.
7. Exportar essa tabela para `resultados/cenarios.csv`, substituindo o arquivo anterior.

O primeiro cenário não recebe mais um detalhamento individual separado. A lista de dicionários,
as tabelas redundantes e a ordenação por custo foram retiradas da apresentação principal.
Com mais de um cenário, há um resumo de menor custo, maior custo e diferença, calculado com
`.min()` e `.max()` exclusivamente sobre o custo mensal de IA em BRL. Com um cenário, esse resumo
não é exibido.

### Configurações da simulação

Modelo, preços e cotação continuam nas configurações de `calculadora.py`, separados das hipóteses
de consumo. Não são opções do menu nem campos solicitados no modo manual.

| Configuração atual | Valor |
| --- | --- |
| Modelo de referência | GPT-6 Luna (`gpt-6-luna`) |
| Entrada sem cache, Standard | US$ 0,10 por milhão de tokens |
| Saída faturável, Standard | US$ 0,50 por milhão de tokens |
| Cotação didática | R$ 5,00 por US$ 1,00 |

As tarifas são as já registradas no código, com consulta em 23/10/2026 à
[referência do modelo](https://developers.openai.com/api/docs/models/gpt-6-luna).
Esta documentação não atualiza nem confirma preços comerciais atuais. A cotação é uma hipótese
didática; **a consulta automática do dólar ainda não foi implementada**. Não há seleção de modelos.

## Como executar

Pré-requisitos: Python convencional para Windows e Pandas disponíveis na `.venv-win` já preparada.
Pandas é importado também ao usar as funções nos testes; `decimal`, `pathlib` e `unittest` pertencem
à biblioteca padrão. A `.venv` anterior, baseada em MSYS2, permanece separada.

No PowerShell:

```powershell
Set-Location -LiteralPath 'D:\Natan\LiteArt Cost Analytics'
& '.\.venv-win\Scripts\python.exe' -B -c "import pandas as pd; print(pd.__version__)"
& '.\.venv-win\Scripts\python.exe' -X utf8 -B calculadora.py
```

Os comandos usam diretamente o interpretador do projeto, sem ativar o ambiente ou alterar o PATH.
Não instalam nem atualizam pacotes. `-X utf8` mantém os acentos na saída e `-B` evita gerar bytecode.
No VS Code, usar **Python: Select Interpreter** e selecionar
`D:\Natan\LiteArt Cost Analytics\.venv-win\Scripts\python.exe`.

O menu oferece:

- **1 — Importar `dados/cenarios_exemplo.csv`:** aceita uma quantidade não vazia de cenários válidos.
- **2 — Preencher um único cenário pelo terminal:** não lê nem exige a existência do CSV.

Para um exemplo manual, escolher `2` e responder, na ordem: `Cenário manual`, `100`, `40`, `0.60`,
`0.25`, `500` e `300`. O resultado é 2.200 feedbacks, IA mensal de US$ 0,44 e R$ 2,20, e IA anual de
US$ 5,28 e R$ 26,40. Ao terminar, o terminal informa o caminho do CSV salvo.

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
A tabela abaixo resume os resultados esperados do CSV de exemplo; as contagens não são formatadas
como dinheiro, e a execução pode mostrar `.0` em contagens estimadas.

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

`test_calculadora.py` contém **165 métodos de teste em 15 classes**, usando `unittest`:

- 111 métodos em 11 classes de cálculos e coordenadoras, incluindo infraestrutura e cenário completo.
- 25 métodos para leitura e validação de CSV.
- 4 métodos para a formatação monetária brasileira.
- 7 métodos para entrada manual e suas validações.
- 18 métodos de integração dos modos CSV e manual, tabelas, mensagens e exportação.

A suíte completa passou nesta atualização. Alguns métodos usam `subTest`; suas combinações não
são métodos adicionais. Os testes persistentes simulam `input()` com `unittest.mock.patch` e usam
arquivos temporários nas integrações. Conferem erros e cancelamento sem sobrescrita, execução de
outra pasta, ordem de múltiplos cenários, cenário único, ausência de chamadas à infraestrutura e ao
cálculo completo, nove campos exportados e preservação exata de Decimal.

Também conferem os símbolos monetários da tabela sem alteração dos dados, precisão além da segunda
casa e equivalência dos dois modos para as mesmas hipóteses. As verificações pontuais históricas,
registradas em [PROMPTS.md](PROMPTS.md), não devem ser contadas como novos métodos automatizados.
Esta revisão de documentação não acrescenta testes.

Para executar a suíte com o ambiente existente:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest -q
```

## Próximos passos

1. Pesquisar e definir a fonte e as regras para consulta de cotação; a decisão está pendente.
2. Implementar essa consulta com opção manual, em incremento próprio e com testes.
3. Consolidar documentação e validar a instalação para fechar a versão do MVP no terminal.

Catálogo e seleção de modelos, comparação entre provedores, gráficos com Plotly, dashboard com
Streamlit, retomada de infraestrutura e orçamento e análises avançadas ficam para depois.
Comparar custos não exige chamadas reais às APIs nem comprova equivalência pedagógica.

## Documentação e aprendizado

O [planejamento](PLANEJAMENTO.md) separa estado atual, recursos preservados e roteiro futuro.
O [registro de prompts](PROMPTS.md) mantém as decisões e os marcos históricos do desenvolvimento.
O projeto evolui em pequenos incrementos, com apoio de IA para orientação, explicações e revisão.

A configuração `.markdownlint.json` limita o texto a 100 caracteres por linha, exceto tabelas e
blocos de código, e define tabelas no estilo `compact`. A verificação deve usar a ferramenta já
disponível no ambiente, sem alterar essas regras.
