# Estudo de caso — análise de cenários de custos de IA do LiteArt

**Data do planejamento:** 18/11/2026.

**Atualização:** 18/11/2026. Preparação dos dados, validação e cálculo dos 13 cenários concluídos.
Comparações analíticas, interpretação, gráficos, relatório e recomendações continuam pendentes.
O estudo se destina ao Google Data Analytics Professional Certificate, sem aprovação formal do
curso ou validação pelo Google. As orientações da atividade, inclusive sobre apoio de IA, deverão
ser conferidas antes da entrega.

## 1. Contexto e objetivo

A rotina [analise_estudo.py](analise_estudo.py) reutiliza as funções da calculadora
**LiteArt Cost Analytics v0.1.0**, preservando seu código e fluxo. O MVP publicado estima custos
de feedbacks de IA no terminal, conforme o [README](README.md) e o
[planejamento do projeto](PLANEJAMENTO.md). A tag local v0.1.0 identifica o commit
`10cc485cde5d1c00a743611017fac58f226b7458`, conferido nesta preparação documental.

O trabalho será uma análise de cenários e sensibilidade, sem dados reais de utilização dos
estudantes. A análise de sensibilidade variará uma hipótese por vez para examinar seu efeito sobre
o custo estimado, mantendo as demais condições constantes.

- **Público:** responsável pelo planejamento do LiteArt.
- **Decisão apoiada:** dimensionar o orçamento de IA e identificar quais hipóteses precisam ser
  medidas antes do lançamento.
- **Objetivo:** comparar políticas de feedback em diferentes escalas e avaliar a influência das
  estimativas de tokens, sem apresentar o custo calculado como despesa observada.

Dimensionar esse orçamento é a finalidade do estudo; não significa reintroduzir o filtro ou saldo
de orçamento no fluxo do MVP. Não haverá chamadas reais às APIs dos modelos para esta simulação.

## 2. Pergunta principal

Como a quantidade de usuários, a política de feedback nos acertos e o consumo de tokens afetam o
custo mensal estimado de IA do LiteArt?

## 3. Escopo e premissas

- Utilizar um único modelo de referência: GPT-6 Luna (`gpt-6-luna`), OpenAI, API direta,
  Standard para texto. Identificador, tarifas e condições foram conferidos documentalmente em
  2026-11-18, conforme a seção 5; isso não comprova acesso pela conta ou execução real do modelo.
- Gerar feedback em todas as respostas erradas.
- Usar a mesma estimativa de tokens por feedback para acertos e erros.
- Considerar uma chamada por feedback, sem novas tentativas ou geração duplicada.
- Comparar custos mensais. O anual exportado é o mensal multiplicado por 12, com consumo, preços
  e cotação constantes.
- Manter os mesmos preços e uma única cotação documentada em todas as comparações.
- Tratar os níveis de usuários como alternativas de escala, sem representar meses sucessivos ou
  uma previsão temporal de crescimento.
- Excluir infraestrutura, receitas, comparação de modelos e dashboard deste estudo.

Os valores serão hipóteses para explorar as fórmulas, sem comprovação de capacidade operacional,
consumo real ou qualidade pedagógica equivalente.

## 4. Matriz dos 13 cenários planejados

Cada identificador será estável durante o estudo. Os números usam ponto decimal nas proporções e
não usam separadores de milhares, conforme a convenção das entradas do MVP.

| Identificador | Grupo | Usuários ativos | Respostas por usuário/mês | Taxa de acerto | Proporção dos acertos com feedback | Tokens de entrada por feedback | Tokens de saída faturáveis por feedback | Finalidade da comparação |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| C01 | principal | 100 | 40 | 0.60 | 0 | 500 | 300 | Somente erros na escala de 100 usuários |
| C02 | principal | 100 | 40 | 0.60 | 0.25 | 500 | 300 | Erros e 25% dos acertos na escala de 100 usuários |
| C03 | principal | 100 | 40 | 0.60 | 1 | 500 | 300 | Todas as respostas; referência de política para 100 usuários |
| C04 | principal | 500 | 40 | 0.60 | 0 | 500 | 300 | Somente erros na escala de 500 usuários |
| C05 | principal | 500 | 40 | 0.60 | 0.25 | 500 | 300 | Erros e 25% dos acertos; referência da sensibilidade |
| C06 | principal | 500 | 40 | 0.60 | 1 | 500 | 300 | Todas as respostas; referência de política para 500 usuários |
| C07 | principal | 1000 | 40 | 0.60 | 0 | 500 | 300 | Somente erros na escala de 1000 usuários |
| C08 | principal | 1000 | 40 | 0.60 | 0.25 | 500 | 300 | Erros e 25% dos acertos na escala de 1000 usuários |
| C09 | principal | 1000 | 40 | 0.60 | 1 | 500 | 300 | Todas as respostas; referência de política para 1000 usuários |
| C10 | sensibilidade | 500 | 40 | 0.60 | 0.25 | 250 | 300 | Reduzir apenas tokens de entrada em relação a C05 |
| C11 | sensibilidade | 500 | 40 | 0.60 | 0.25 | 1000 | 300 | Aumentar apenas tokens de entrada em relação a C05 |
| C12 | sensibilidade | 500 | 40 | 0.60 | 0.25 | 500 | 150 | Reduzir apenas tokens de saída em relação a C05 |
| C13 | sensibilidade | 500 | 40 | 0.60 | 0.25 | 500 | 600 | Aumentar apenas tokens de saída em relação a C05 |

São **13 combinações distintas, todas hipotéticas**. C01 a C09 cruzam três escalas com três
políticas, em ordem crescente de usuários e depois de proporção. A referência de sensibilidade é
**C05: 500 usuários, 40 respostas, taxa 0.60, proporção 0.25, entrada 500 e saída 300**.

As proporções têm estes significados:

- `0`: feedback somente nas respostas erradas.
- `0.25`: feedback nos erros e em 25% dos acertos.
- `1`: feedback em todas as respostas.

A proporção dos acertos com feedback não equivale necessariamente à proporção de usuários com o
toggle ligado: estudantes podem responder quantidades diferentes de questões. O valor representa
uma parcela agregada dos acertos.

C10 a C13 alteram uma entrada por vez em relação a C05. Usuários, respostas, taxa de acerto e
política permanecem iguais. Os valores de tokens não são médias medidas, limites garantidos ou
evidência de qualidade equivalente entre as variações.

## 5. Dados necessários, condições fixas e proveniência

### 5.1. Revalidação documental — 2026-11-18

**Data desta atualização documental:** 2026-11-18. **Data da pesquisa de modelo e tarifas:**
2026-11-18. A revalidação documental e a definição das condições fixas estão concluídas nos pontos
confirmados abaixo. Os CSVs de entrada foram preparados e conferidos pontualmente em 2026-11-18,
conforme a seção 5.5. A validação e o cálculo foram concluídos na etapa da seção 5.6; comparações,
interpretação e conclusões continuam pendentes. Não houve chamadas pagas, solicitação de
credenciais ou teste de acesso à conta.

| Condição fixa do estudo | Valor ou definição | Moeda, unidade ou recorte |
| --- | --- | --- |
| Provedor e acesso considerados | OpenAI, API direta | Sem intermediação de outro provedor |
| Modelo de referência | GPT-6 Luna | Identificador `gpt-6-luna` |
| Modalidade | Standard, texto | Contexto curto; entrada sem cache |
| Tarifa de entrada | `Decimal("0.10")` | USD por milhão de tokens de entrada sem cache |
| Tarifa de saída faturável | `Decimal("0.50")` | USD por milhão de tokens de saída faturáveis |
| Data da pesquisa de tarifas | 2026-11-18 | Conferência documental nas fontes oficiais |
| Cotação fixa | `Decimal("5.8102")` | BRL por USD |
| Fonte cambial | Banco Central do Brasil, SGS série 1 | Dólar americano de venda, diário |
| Data de referência cambial | 2026-11-18 | Data da observação recebida do BCB |
| Data da consulta cambial | 2026-11-18 | Data do acesso; horário não registrado |

As condições propostas foram mantidas: não foi identificada divergência material no identificador,
nas tarifas Standard de contexto curto ou na observação cambial conferida. Esses registros são
válidos como recorte histórico desta pesquisa, sem afirmar preços ou disponibilidade permanentes.

### 5.2. Fontes oficiais conferidas e alcance da confirmação

- **Modelo:** [página do GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna).
  Confirma o identificador, texto como entrada e saída, unidade por milhão, tarifas e condições
  de contexto e processamento. Sua presença no catálogo é disponibilidade documentada, não
  comprovação de habilitação, limites, saldo ou acesso na conta responsável pelo estudo.
- **Tarifas:** [página geral de preços](https://developers.openai.com/api/docs/pricing), conferida
  também em sua [versão Markdown](https://developers.openai.com/api/docs/pricing.md).
  A seção `Standard pricing data`, nas colunas de entrada e saída de contexto curto, registra
  os valores adotados. A página reúne várias tabelas: valores de Batch, Flex, Fast, contexto longo
  ou cache não foram interpretados como tarifas Standard de contexto curto.
- **Ciclo de vida:** [depreciações](https://developers.openai.com/api/docs/deprecations).
  Na consulta não foi identificado anúncio de retirada do próprio `gpt-6-luna` como modelo afetado;
  ele também aparece como substituto recomendado de outros modelos. Isso não é teste de acesso
  nem garantia de disponibilidade futura.
- **Tokens faturáveis:** [guia de raciocínio](https://developers.openai.com/api/docs/guides/reasoning).
  A documentação informa que tokens internos de raciocínio podem ser cobrados como saída, mesmo
  sem aparecer no texto entregue. Sua contabilização deverá seguir o total faturável, sem duplicação.
- **Definição cambial:** [catálogo BCB/SGS série 1](https://dadosabertos.bcb.gov.br/dataset/1-taxa-de-cambio---livre---dolar-americano-venda---diario).
  Identifica dólar americano de venda diário; a unidade usada no estudo é reais por dólar.
- **Observação cambial:** [endpoint últimos/1 em JSON](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json).
  A resposta observada em 2026-11-18 foi fornecida para o registro e coincidiu com a consulta
  desta atualização. A evidência preservada é:

```json
[{"data":"18/11/2026","valor":"5.8102"}]
```

O endpoint é dinâmico. Uma consulta posterior pode retornar outra data ou outro valor e **não deve
atualizar automaticamente a cotação fixa escolhida para este estudo**. A data da pesquisa de
preços, a data desta atualização, a data da observação cambial e a data de acesso são campos
conceitualmente diferentes, embora coincidam aqui em 2026-11-18. Nenhum horário foi presumido.
A cotação é referência de simulação, não câmbio em tempo real nem garantia do valor de um pagamento.

### 5.3. Condições e exclusões do cálculo

Manter um modelo permite isolar os efeitos de usuários, política de feedback e tokens. As mesmas
tarifas e `Decimal("5.8102")` BRL por USD ficarão constantes nos 13 cenários, inclusive na análise
de sensibilidade. A projeção anual exportada é o mensal multiplicado por 12 sob essas mesmas
condições, sem simular crescimento, alterações tarifárias ou variação cambial.

A hipótese é de **requisições curtas, dentro da faixa padrão de preço**: até 272000 tokens de
entrada por requisição completa, conforme o limite de contexto curto indicado para a cobrança.
Acima desse patamar, a página do modelo descreve outras condições de preço; elas estão fora deste
recorte. A entrada por chamada deve incluir instruções, conteúdo e demais componentes enviados.
**Tokens por chamada não são os totais mensais**: somar consumo de várias requisições ao longo do
mês não transforma cada requisição curta em uma requisição de contexto longo.

As entradas de 250, 500 ou 1000 tokens por feedback são orçamentos didáticos da matriz, não
contagens medidas de prompts reais ou garantias de enquadramento de uma futura requisição.
Os tokens de saída de 150, 300 ou 600 representam **todo o consumo de saída faturável**, incluindo
componentes internos não visíveis quando existirem. Não representam apenas o texto visível e não
deverão receber uma segunda soma dos mesmos tokens de raciocínio já incluídos nesse total.

Nenhuma configuração de modo ou esforço de raciocínio foi testada ou atribuída aos cenários.
Standard identifica o recorte de processamento e preços; não comprova uma configuração de
raciocínio adequada, geração dentro do orçamento de tokens ou qualidade pedagógica equivalente.
Uma futura medição real deverá registrar configuração e consumo faturável, antes de substituir
as hipóteses. A presença no catálogo não elimina essa necessidade.

Ficam fora do cálculo:

- Descontos por entrada em cache e operações de leitura, gravação ou manutenção de cache.
- Batch, Flex, Fast e outros modos acelerados ou modalidades com preços diferentes.
- Descontos de processamento em segundo plano e adicionais de processamento regional.
- Ferramentas, serviços adicionais, tributos e tarifas ou adicionais do meio de pagamento.
- Infraestrutura e demais despesas que não sejam os tokens de IA definidos para o estudo.

Esse recorte não é uma estimativa de fatura completa. A cotação didática de **R$ 5,00** permanece
nos exemplos históricos e testes do MVP; **não é a cotação deste estudo**. Não serão alterados os
valores da release ou sua tag. A rotina do estudo lê 5.8102 do CSV de condições e usa a mesma taxa
em todos os cenários, sem consulta à rede. O modo manual do MVP permanece disponível separadamente.

### 5.4. Organização das entradas e proveniência

Manter separados, com vínculo pelos identificadores dos cenários:

- **Tarifas pesquisadas:** condições e referências confirmadas acima, com provedor, modelo, moeda,
  unidade, modalidade e data. A pesquisa atual não substitui as datas das pesquisas históricas.
- **Câmbio:** valor fixo, fonte, data da observação e data da consulta acima, sem horário inventado.
- **Hipóteses:** os 13 cenários já revisados, suas unidades, justificativas e natureza didática.
  A revisão de coerência da matriz não é validação empírica do comportamento dos estudantes.
- **Resultados derivados:** consumos e custos calculados pela rotina separada do estudo,
  identificados por cenário e acompanhados das condições utilizadas, conforme a seção 5.6.
  A referência histórica da ferramenta continua sendo a v0.1.0, sem mover sua tag.

As entradas próprias do estudo foram preparadas nos dois CSVs descritos na seção 5.5. O CSV de
exemplo do MVP permanece preservado. Os identificadores C01 a C13 acompanham cada nome e deverão
acompanham os resultados calculados. Não há resultados calculados nos dois CSVs de entrada.

O CSV de resultados da v0.1.0 contém nove colunas e não exporta modelo, tarifas, cotação, origem ou
data como metadados. A rotina separada do estudo inclui as condições em sua própria exportação
de 35 colunas, sem modificar o formato de nove colunas ou o funcionamento histórico do MVP.

### 5.5. CSVs de entrada preparados e conferidos — 2026-11-18

**Preparação concluída:** os dois arquivos foram criados e conferidos com a `.venv-win` existente,
sem instalar pacotes ou atualizar as referências históricas. Ambos usam UTF-8 sem BOM, vírgula entre
campos, ponto decimal, cabeçalho e ausência de coluna de índice. Números não têm símbolos monetários,
sinais de porcentagem ou separadores de milhares. Esses CSVs são dados de entrada, não resultados.

#### Hipóteses dos cenários

Arquivo: [dados/estudo_de_caso/cenarios.csv](dados/estudo_de_caso/cenarios.csv).
Contém **13 registros**, ordenados de C01 a C13, com identificadores e nomes descritivos únicos.
Cada registro representa uma hipótese de cenário mensal. As oito colunas, nesta ordem, são:

| Campo | Conteúdo, unidade e regra |
| --- | --- |
| `id_cenario` | Identificador textual estável, de C01 a C13 |
| `cenario` | Nome descritivo da combinação hipotética |
| `usuarios_ativos` | Usuários ativos no mês; inteiro não negativo |
| `respostas_por_usuario` | Média de respostas por usuário por mês; número finito não negativo |
| `taxa_acerto` | Proporção das respostas corretas, entre 0 e 1 inclusive |
| `proporcao_acertos_com_feedback` | Proporção dos acertos com feedback, entre 0 e 1 inclusive |
| `tokens_entrada` | Média hipotética de tokens de entrada por feedback; finita e não negativa |
| `tokens_saida` | Média hipotética de tokens de saída faturáveis por feedback; finita e não negativa |

Todos os registros mantêm 40 respostas por usuário/mês e taxa de acerto `0.60`, isto é, 60%.
A proporção `0.25` corresponde a feedback em 25% dos acertos. Todos os erros continuam recebendo
feedback. A coluna `proporcao_acertos_com_feedback` não mede a parcela de usuários com toggle ativo.
Tokens são por feedback, sem representar tokens mensais calculados ou consumo medido.

**Compatibilidade:** este arquivo tem `id_cenario` além das sete colunas aceitas por
`ler_cenarios_csv()` no MVP v0.1.0. O importador rejeita colunas inesperadas; portanto, o CSV do estudo
**não é diretamente compatível com o importador atual**. Não substituir
`dados/cenarios_exemplo.csv` por ele nem tratá-lo como entrada já integrada ao menu.
A leitura específica foi implementada em `ler_cenarios_estudo()`, preservando o identificador e
preparando as hipóteses no formato esperado pelas funções do MVP, sem alterar sua versão publicada.

#### Referências pesquisadas e condições compartilhadas

Arquivo: [dados/estudo_de_caso/condicoes_fixas.csv](dados/estudo_de_caso/condicoes_fixas.csv).
Contém **uma única linha de dados**, aplicável a todos os 13 cenários. Não há associação por linha
ou necessidade de repetir tarifas e câmbio em cada cenário. As 12 colunas são:

| Campo | Conteúdo ou unidade |
| --- | --- |
| `provedor` | Provedor considerado: OpenAI, com API direta conforme a seção 5.1 |
| `modelo` | Identificador do modelo: `gpt-6-luna` |
| `modalidade` | Modalidade de processamento e preços: Standard |
| `preco_entrada_por_milhao_usd` | USD por milhão de tokens de entrada sem cache; referência `0.10` |
| `preco_saida_por_milhao_usd` | USD por milhão de tokens de saída faturáveis; referência `0.50` |
| `brl_por_usd` | Reais por dólar americano; cotação histórica fixa `5.8102` BRL/USD |
| `fonte_modelo` | URL oficial completa da página do modelo |
| `fonte_precos` | URL oficial completa da página geral de preços |
| `data_consulta_precos` | Data da pesquisa de tarifas: `2026-11-18`, no formato ISO AAAA-MM-DD |
| `fonte_cambio` | URL oficial completa do catálogo BCB/SGS série 1 |
| `data_referencia_cambio` | Data da observação cambial: `2026-11-18`, no formato ISO AAAA-MM-DD |
| `data_consulta_cambio` | Data do acesso à fonte cambial: `2026-11-18`, no formato ISO AAAA-MM-DD |

As fontes foram copiadas das referências da seção 5.2. `fonte_modelo` aponta para a página do
GPT-6 Luna; `fonte_precos`, para a página geral de preços da OpenAI. O recorte é o de texto Standard,
contexto curto e entrada sem cache, conforme a pesquisa documentada, sem aplicar outras modalidades.
`fonte_cambio` identifica o catálogo oficial do BCB; o endpoint dinâmico e a evidência da resposta
histórica permanecem registrados na seção 5.2. Nenhum horário ou nova data foi atribuído aos dados.

Tarifas e câmbio são referências pesquisadas, separadas das hipóteses dos cenários. Valem igualmente
para as 13 combinações, sem atualização automática durante a análise. O CSV não altera a cotação
interativa do MVP nem redefine seus exemplos históricos de R$ 5,00.

#### Leitura implementada e precisão

A rotina do estudo usa `csv.reader()` para ler os campos inicialmente como texto. CSV não preserva
tipos Python: tarifas e câmbio são convertidos diretamente por `Decimal(texto)`, sem float
intermediário ou arredondamento de exibição. As datas ISO permanecem como texto validado, sem
horário presumido. Tarifas e câmbio devem ser finitos e estritamente positivos neste estudo;
isso não muda a regra geral das funções do MVP, que podem aceitar tarifas gratuitas.

As hipóteses reutilizam `converter_hipotese_consumo()`: usuários são convertidos diretamente para
`int`, rejeitando `100.0` e `100.5`; as cinco demais hipóteses usam `float`, conforme os contratos
existentes de consumo, com validações de finitude, não negatividade e taxas entre 0 e 1.
A preservação de Decimal se refere aos campos financeiros; não implica conversão das contagens
ou médias para Decimal. O vínculo com a única linha de condições acompanha cada resultado.
Os dois CSVs continuam fora do menu principal da v0.1.0.

#### Conferência pontual da preparação dos dados

A conferência verificou cabeçalhos e ordem das colunas, 13 registros de cenários e uma linha de
condições, UTF-8, acentos, nomes e identificadores únicos, campos preenchidos e ausência de índice
ou resultados.
Confirmou as 13 combinações distintas das seis hipóteses, a cobertura das nove combinações
principais e C05 como referência. Cada variação de C10 a C13 altera somente uma hipótese numérica.
Também conferiu usuários inteiros não negativos, números finitos não negativos e taxas válidas.

Os campos financeiros da linha de condições foram lidos como texto e reconstruídos diretamente
como Decimal, confirmando positividade e igualdade com `0.10`, `0.50` e `5.8102`, sem float.
Fontes e datas foram comparadas com este documento. Não houve divergências, consulta a preços ou
câmbio atuais, nem substituição da referência histórica fixada. Ambos os arquivos não estão
ignorados pelo Git e podem ser versionados.

Essas verificações da preparação foram pontuais, sem novos testes persistentes naquela etapa.
Na preparação, nenhum feedback, token mensal ou custo foi calculado. A etapa seguinte implementou
os cálculos e os testes descritos abaixo; isso não comprova as hipóteses nem publica uma nova versão.

### 5.6. Rotina de validação e cálculo — 2026-11-18

**Implementado e executado:** [analise_estudo.py](analise_estudo.py), separado do código e do menu
do MVP. A rotina resolve caminhos a partir de `Path(__file__).resolve().parent`; suas funções
aceitam caminhos para permitir testes com arquivos temporários. O bloco `if __name__ == "__main__"`
protege a importação: importar o módulo não lê CSVs, pergunta, imprime, consulta a rede ou exporta.

#### Funções e validações

- `ler_csv_texto()`: usa `csv.reader(strict=True)`, UTF-8 com ou sem BOM, remove espaços externos
  e exige o cabeçalho documentado na ordem exata. Rejeita colunas ausentes, inesperadas, duplicadas
  ou fora de ordem, arquivos vazios ou somente com cabeçalho, campos obrigatórios vazios,
  quantidade incorreta de campos, codificação inválida e erros de sintaxe detectados pelo leitor.
- `ler_cenarios_estudo()`: exige identificadores únicos com cobertura C01 a C13 e 13 combinações
  distintas das seis hipóteses. Preserva nomes e ordem recebida, reutilizando o conversor e as
  validações numéricas do MVP. Não utiliza o importador de sete colunas como se aceitasse oito.
- `ler_condicoes_fixas()`: exige uma única linha preenchida, converte tarifas e câmbio diretamente
  para Decimal finito e positivo e valida datas reais no formato ISO `AAAA-MM-DD`.
  Mantém fontes e demais metadados. Não pesquisa novamente nem comprova as fontes na execução.
- `calcular_resultados()`: adapta os nomes de tarifas aos contratos de
  `calcular_consumo_cenario()` e `calcular_custo_ia_cenario()`, importadas do MVP. Aplica a mesma
  configuração aos 13 registros e cria o DataFrame com `coerce_float=False`, preservando Decimal.
- `apresentar_resultados()`: mostra identificador, usuários, feedbacks e custos mensais em USD e
  BRL. Reutiliza `formatar_moeda_br()` em formatadores de `to_string()`, sem modificar a tabela.
- `exportar_resultados()` e `executar_estudo()`: coordenam a gravação e o fluxo completo.
  Todos os registros são validados e calculados antes de escrever. `main()` trata falhas esperadas
  de entrada com mensagem e saída diferente de zero, sem sobrescrever resultados anteriores.

As mensagens de validação identificam arquivo e, quando aplicável, registro e campo. Não há
retorno parcial ou descarte silencioso de registros inválidos. As funções de cálculo do MVP,
seus testes, as entradas e a tag v0.1.0 foram preservados. Não há consultas ao BCB ou às APIs de IA.

#### Execução, entradas e exportação

Com o terminal na raiz do projeto e a `.venv-win` existente:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest test_analise_estudo -q
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest discover -v
```

As entradas são `dados/estudo_de_caso/cenarios.csv` e
`dados/estudo_de_caso/condicoes_fixas.csv`. Manter esses arquivos e as condições históricas da
seção 5 permite reproduzir o cálculo, sem cotação do dia ou valores comerciais fixados no script.

A saída é `resultados/estudo_de_caso/resultados_cenarios.csv`, relativa à pasta do script.
A pasta é criada quando necessário; a execução substitui o CSV, sem acumular linhas.
O arquivo é ignorado pela regra `/resultados/` do Git. Ele contém **13 linhas e 35 colunas**,
na ordem dos grupos abaixo; dentro de cada grupo, a ordem é a listada:

| Grupo | Quantidade | Colunas |
| --- | ---: | --- |
| Identificação | 2 | `id_cenario`, `cenario` |
| Hipóteses | 6 | `usuarios_ativos`, `respostas_por_usuario`, `taxa_acerto`, `proporcao_acertos_com_feedback`, `tokens_entrada`, `tokens_saida` |
| Consumo mensal | 7 | `respostas_mensais`, `acertos_mensais`, `erros_mensais`, `feedbacks_nos_acertos`, `feedbacks_mensais`, `tokens_entrada_total`, `tokens_saida_total` |
| Custos de IA | 8 | `custo_entrada_usd`, `custo_saida_usd`, `custo_ia_mensal_usd`, `custo_entrada_br`, `custo_saida_br`, `custo_ia_mensal_br`, `custo_ia_anual_usd`, `custo_ia_anual_br` |
| Condições e proveniência | 12 | `provedor`, `modelo`, `modalidade`, `preco_entrada_por_milhao_usd`, `preco_saida_por_milhao_usd`, `brl_por_usd`, `fonte_modelo`, `fonte_precos`, `data_consulta_precos`, `fonte_cambio`, `data_referencia_cambio`, `data_consulta_cambio` |

Os custos por componente são mensais; os anuais usam 12 meses constantes. As condições são
repetidas em cada linha para identificar tarifas, câmbio, fontes e datas utilizadas.
O formato é UTF-8, vírgula entre campos, ponto decimal, cabeçalho e ausência de índice.
Não se aplicam símbolos, separadores de milhares ou arredondamento de duas casas à exportação.
O terminal usa `US$` e `R$` e duas casas somente na representação exibida. Para reler os valores
financeiros do CSV, manter texto até convertê-los diretamente para Decimal.

#### Resultados de referência e evidências

A execução dos arquivos do estudo em 18/11/2026 produziu C01 a C13 na ordem de entrada.
As condições coincidiram com as referências documentadas, sem atualização pela internet.
Os valores abaixo são resultados das fórmulas sob as hipóteses fixas, não despesas observadas:

| Cenário | Feedbacks/mês | Tokens de entrada/mês | Tokens de saída/mês | IA mensal USD | IA mensal BRL sem arredondamento de exibição |
| --- | ---: | ---: | ---: | ---: | ---: |
| C02 | 2200 | 1100000 | 660000 | 0.44 | 2.556488 |
| C05 | 11000 | 5500000 | 3300000 | 2.20 | 12.78244 |

A conversão usou os valores exatos em USD multiplicados por `Decimal("5.8102")`.
Zeros finais adicionais no CSV preservam a representação de Decimal, sem alterar esses valores.

- **Testes automatizados persistentes:** [test_analise_estudo.py](test_analise_estudo.py) contém
  30 métodos em uma classe, usando `unittest`, arquivos temporários e simulações. Cobrem as
  validações, importação sem efeitos, preservação das entradas e da tabela, ausência de rede,
  precisão além de duas casas e releitura financeira com comparação por `Decimal.as_tuple()`.
  Conferem saída não zero em falhas, preservação de resultados anteriores, caminhos independentes
  da pasta atual e reexecução sem duplicação. Também verificam fórmulas independentes em Decimal
  para os 13 registros, sem usar a função testada para construir os resultados esperados.
- **Resultado da suíte na implementação:** 30 métodos novos e os 188 do MVP passaram juntos:
  **218 métodos em 18 classes**, em 18/11/2026. Combinações de `subTest` não são métodos extras.
  A suíte não foi repetida nesta atualização exclusivamente documental.
- **Conferências pontuais:** a execução real e a releitura de seu CSV confirmaram 13 registros,
  35 colunas, condições e datas documentadas e igualdade exata dos campos financeiros reconstruídos
  diretamente como Decimal. Essas conferências não acrescentaram métodos de teste.
- **Coerência das fórmulas:** os testes confirmaram que C10 a C13 mantêm os feedbacks de C05 e
  variam os totais de tokens correspondentes. Dentro de cada escala, aumentar feedback nos
  acertos não reduziu consumo ou custo. São relações determinadas pelas entradas e fórmulas,
  sem evidência empírica sobre comportamento, aprendizagem ou qualidade dos feedbacks.

A validação e o cálculo estão concluídos. Comparações monetárias e percentuais entre políticas,
participações, custo por usuário, interpretação, gráficos, relatório e recomendações ainda não
foram produzidos nesta rotina.

## 6. Unidade de análise e indicadores

No CSV de cenários e na tabela de resultados, **uma linha representa um cenário mensal**,
não um estudante nem uma despesa observada. A linha única de condições fixas, por sua vez, é
compartilhada pelos 13 cenários. Cada cenário é uma alternativa; seus custos não devem ser somados
como uma única despesa.

Indicadores do estudo, com estágios distintos:

- Quantidade mensal estimada de feedbacks: calculada.
- Tokens mensais de entrada e de saída faturáveis: calculados.
- Custo mensal de IA em USD e BRL: calculado.
- Participação da entrada e da saída no custo mensal de IA.
- Custo mensal de IA por usuário ativo, sem infraestrutura ou outras despesas.
- Diferenças monetárias e percentuais entre políticas e entre as variações de tokens.

A rotina do estudo já reutiliza o MVP para fornecer consumos e custos por cenário. Participações,
custo por usuário e comparações específicas permanecem planejados para a próxima etapa; não são
novas funcionalidades implementadas no terminal nem colunas já acrescentadas à exportação.

### Participação no custo e custo por usuário

Os custos dos componentes já estão exportados; suas participações e o custo por usuário são futuros:

- Custo de entrada em USD = tokens mensais de entrada ÷ 1000000 × tarifa de entrada por milhão.
- Custo de saída em USD = tokens mensais de saída ÷ 1000000 × tarifa de saída por milhão.
- Participação de entrada (%) = 100 × custo de entrada em USD ÷ custo mensal de IA em USD.
- Participação de saída (%) = 100 × custo de saída em USD ÷ custo mensal de IA em USD.
- Custo mensal de IA por usuário em BRL = custo mensal de IA em BRL ÷ usuários ativos.

As participações devem usar a mesma moeda no numerador e no denominador. Não somar ou dividir
valores em USD e BRL como se fossem a mesma unidade.

### Comparação das políticas

Comparar políticas dentro da mesma escala. Feedback em todas as respostas será a referência:
**C03 para 100 usuários, C06 para 500 e C09 para 1000**.

Para cada comparação, chamar de `C_ref` o custo mensal dessa referência e de `C_pol` o da política
avaliada, ambos na mesma moeda:

- Diferença monetária, expressa como economia = `C_ref − C_pol`.
- Redução percentual = `100 × (C_ref − C_pol) ÷ C_ref`.

O denominador percentual é o custo da política de feedback em todas as respostas na mesma escala.
Valor positivo de economia indica custo menor que a referência; negativo indica custo maior.
Comparar escalas sob a mesma política separadamente, sem confundir os efeitos de usuários e política.

### Sensibilidade dos tokens

Comparar cada cenário de **C10 a C13 com C05**, mantendo a referência fixa. Chamar de `C_var` o
custo mensal da variação e de `C_05` o custo mensal de C05, na mesma moeda:

- Variação monetária = `C_var − C_05`.
- Variação percentual = `100 × (C_var − C_05) ÷ C_05`.

Variação positiva significa aumento; negativa significa redução. Aqui o denominador é C05, e não
a política de feedback em todas as respostas usada na comparação principal.

**Se qualquer denominador for zero, a razão ou variação percentual correspondente será não
aplicável**, com o motivo registrado. Não substituir esse caso por zero ou uma divisão inválida.

## 7. Andamento das etapas da análise

1. **Perguntar — definido:** pergunta, público, decisão, limites e matriz revisados documentalmente.
2. **Preparar — concluído:** os dois CSVs de entrada foram preparados e conferidos, conforme 5.5.
   Hipóteses e condições pesquisadas permanecem separadas de dados observados.
3. **Processar e calcular — concluído:** a rotina da seção 5.6 valida os arquivos e produz consumos
   e custos dos 13 cenários, com condições fixas e Decimal financeiro. A execução foi conferida e
   a suíte passou. Isso não equivale a medição real de consumo ou teste de acesso à API.
4. **Analisar e interpretar — pendente:** comparar políticas por escala e variações de tokens
   contra C05, com diferenças monetárias, percentuais e denominadores claros. A conferência por
   fórmula independente já está nos testes; as verificações aritméticas não substituem a análise.
5. **Compartilhar — pendente:** produzir síntese interpretativa, relatório e dois gráficos:
   - Custo mensal por escala e política, com moeda e referência identificadas.
   - Variação do custo em relação a C05 na análise de tokens, identificando o fator alterado.
6. **Agir — pendente:** apresentar recomendações condicionais às hipóteses e plano de medição real
   antes do lançamento, incluindo uso, política de feedback, tokens faturáveis e avaliação pedagógica.

Os cálculos preservam Decimal nos campos financeiros e arredondam somente a apresentação.
Na releitura de CSV, recuperar os campos financeiros como texto e convertê-los diretamente para
Decimal, sem reutilizar os textos monetários do terminal.

## 8. Limitações

- Não há dados observados de utilização ou aprendizagem; os cenários não formam uma amostra
  estatística de estudantes nem sustentam generalização sobre seu comportamento real.
- Não propor testes de significância para diferenças determinadas pelas fórmulas e entradas fixas.
- Menor custo não comprova melhor aprendizagem nem qualidade pedagógica equivalente.
- Sob tarifas e hipóteses constantes, aumento proporcional de custos com usuários é esperado
  pelo modelo; não constitui evidência empírica de economia de escala.
- As hipóteses de tokens não foram medidas e não garantem o consumo de requisições reais.
- Cotações, preços, condições e disponibilidade do modelo podem mudar. O estudo deverá registrar
  o recorte utilizado, sem apresentar suas referências como permanentemente atuais.
- A projeção anual constante não simula crescimento, sazonalidade ou mudanças de consumo e câmbio.
- O custo cobre somente IA; não representa o custo operacional completo ou a viabilidade do LiteArt.
- A adequação do trabalho às orientações e à avaliação do curso ainda precisará ser conferida.

## 9. Entregáveis e critérios de conclusão

Situação dos entregáveis:

- Fontes, datas, tarifas, câmbio e condições fixas documentados; as justificativas das hipóteses
  deverão acompanhar a análise sem serem tratadas como evidência empírica.
- Tabela de entradas preparada em `dados/estudo_de_caso/cenarios.csv`, com C01 a C13, e condições
  compartilhadas em `condicoes_fixas.csv`: concluídas. Validação e cálculo reproduzíveis
  implementados em `analise_estudo.py`; exportação dos 13 resultados concluída, conforme 5.6.
- Dois gráficos conforme a etapa Compartilhar, ainda não produzidos, sem dashboard neste escopo.
- Relatório curto com pergunta, preparação, resultados, recomendações condicionais e limitações,
  ainda não produzido.
- Registro transparente do apoio de IA, a preparar para a entrega conforme as orientações da
  atividade, distinguindo sua contribuição das decisões e conferências realizadas pelo estudante.

Critérios para encerrar a análise futuramente:

- Os 13 cenários estão presentes, identificados e sem duplicidade de combinações.
- C05 permanece a referência de tokens, e as políticas usam a referência da mesma escala.
- Comparações e indicadores têm unidades, denominadores e sinais explicitados; divisões por zero
  são tratadas como não aplicáveis.
- Cálculos monetários preservam Decimal, com arredondamento somente na apresentação.
- Fontes, datas, hipóteses, cotação fixa e versão da ferramenta permitem reproduzir os resultados.
- Conferência independente dos cálculos registrada: fórmulas alternativas nos testes e releitura
  pontual realizadas, sem divergências; não confundir com medição ou validação empírica.
- Conclusões distinguem estimativas, hipóteses e evidências reais, sem inferir qualidade pelo custo.
- Tabela, gráficos e relatório respondem à pergunta, respeitam os limites e registram o apoio de IA.

A matriz está documentada; isso não significa que esses critérios já tenham sido atendidos ou que
o estudo tenha sido aprovado pelo curso.

## 10. Próximo passo

1. Comparar políticas dentro de cada escala, usando C03, C06 e C09 como referências de feedback
   em todas as respostas para 100, 500 e 1000 usuários, respectivamente.
2. Avaliar a sensibilidade de C10 a C13 em relação a C05, mantendo modelo, tarifas e câmbio fixos.
   Calcular indicadores pendentes da seção 6, explicitar denominadores e tratar divisões por zero.
3. Interpretar as estimativas sob as hipóteses e somente depois produzir gráficos, relatório e
   recomendações condicionais. Não apresentar relações aritméticas como descobertas sobre estudantes.
4. Manter a v0.1.0 publicada como referência histórica, sem mover, substituir ou modificar sua tag.
   A rotina separada do estudo não representa automaticamente uma nova release.

**Concluído:** preparação dos dois CSVs, validação, cálculo, exportação dos 13 cenários e conferências
registradas na seção 5.6. A pesquisa documental e a cotação histórica fixa permanecem preservadas.
Não foram comprovados acesso à conta, configuração de raciocínio, consumo real ou qualidade
pedagógica. Comparações analíticas, gráficos, relatório e recomendações continuam pendentes.

Esta atualização altera somente documentação, sem repetir a execução dos cenários ou os testes.
O código e o funcionamento do MVP permanecem inalterados.
