# Estudo de caso — análise de cenários de custos de IA do LiteArt

**Data do planejamento:** 18/11/2026.

**Situação atual — atualização documental de 26/11/2026:** estudo e
[relatório](../RELATORIO_ESTUDO.md) publicados no mesmo repositório do MVP v0.1.0. O responsável
confirmou a conferência das imagens e dos links na apresentação publicada e a conclusão do Google
Data Analytics Professional Certificate com este estudo como capstone. Não foram informadas datas
exatas desses eventos. Não se infere avaliação individual do relatório, nota ou endosso do Google.

**Navegação atual:** este documento está em `docs/`; testes estão em `tests/`. Os caminhos textuais
de dados, resultados e imagens e os comandos de reprodução partem da raiz do projeto, onde os
três scripts permanecem. Os links relativos consideram a pasta de cada documento.

**Registro histórico até 25/11/2026:** preparação, validação, cálculo dos 13 cenários e comparações
concluídos e conferidos. Os dois gráficos estão implementados, com revisão visual no alcance da
seção 5.10. Participações de custo e custos por usuário ativo foram implementados e verificados em
25/11/2026, conforme 5.11. A interpretação e as recomendações condicionais foram documentadas nessa
data, conforme 5.12. O relatório final e suas duas imagens foram produzidos conforme 5.13.
A revisão técnica final local de 25/11/2026 não encontrou divergências materiais, conforme 5.14.
Naquela revisão, conferência das orientações do curso e publicação ainda eram pendências.
Os estados atuais estão no topo; piloto, coleta e avaliação pedagógica não foram executados.
As condições fixas permanecem com pesquisa e referência de 18/11/2026; a pausa no desenvolvimento
não atualizou modelo, tarifas, cotação ou datas históricas.
As seções datadas preservam evidências e encaminhamentos de cada etapa. Menções a publicação ou
relatório pendentes nas seções 5.1 a 5.14 são históricas, não bloqueios atuais. O uso como capstone
e a conclusão do certificado não comprovam uma avaliação individual deste material pelo curso.

## 1. Contexto e objetivo

A rotina [analise_estudo.py](../analise_estudo.py) reutiliza as funções da calculadora
**LiteArt Cost Analytics v0.1.0**, preservando seu código e fluxo. O MVP publicado estima custos
de feedbacks de IA no terminal, conforme o [README](../README.md) e o
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

**Data do registro das condições fixas:** 2026-11-18. **Data da pesquisa de modelo e tarifas:**
2026-11-18. A revalidação documental e a definição das condições fixas estão concluídas nos pontos
confirmados abaixo. Os CSVs de entrada foram preparados e conferidos pontualmente em 2026-11-18,
conforme a seção 5.5. A validação e o cálculo foram concluídos na etapa da seção 5.6; as comparações
estão registradas na seção 5.7; a interpretação e as recomendações propostas estão na seção 5.12.
O relatório final está registrado na seção 5.13. Não houve
chamadas pagas, solicitação de credenciais ou teste de acesso à conta.

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

Arquivo: [dados/estudo_de_caso/cenarios.csv](../dados/estudo_de_caso/cenarios.csv).
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

Arquivo: [dados/estudo_de_caso/condicoes_fixas.csv](../dados/estudo_de_caso/condicoes_fixas.csv).
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

**Implementado e executado:** [analise_estudo.py](../analise_estudo.py), separado do código e do menu
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
  Todos os registros são validados, calculados e comparados antes de escrever. A etapa de
  indicadores da seção 5.11 acrescentou um quarto CSV, também calculado antes da exportação.
  `main()` trata falhas esperadas de entrada com mensagem e saída diferente de zero, sem
  sobrescrever resultados anteriores em erros de validação ou de comparabilidade.

As mensagens de validação identificam arquivo e, quando aplicável, registro e campo. Não há
retorno parcial ou descarte silencioso de registros inválidos. As funções de cálculo do MVP,
seus testes, as entradas e a tag v0.1.0 foram preservados. Não há consultas ao BCB ou às APIs de IA.

#### Execução, entradas e exportação

Com o terminal na raiz do projeto e a `.venv-win` existente:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest tests.test_analise_estudo -v
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest discover -s tests -t . -v
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

- **Testes automatizados da primeira etapa:** [test_analise_estudo.py](../tests/test_analise_estudo.py)
  recebeu inicialmente 30 métodos em uma classe, usando `unittest`, arquivos temporários e
  simulações. Os 17 métodos posteriores estão descritos na seção 5.7. Os primeiros cobrem as
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

A validação e o cálculo estão concluídos. As comparações monetárias e percentuais foram
implementadas posteriormente, conforme a seção 5.7. Participações e custo por usuário foram
incorporados em 25/11/2026, conforme a seção 5.11. Os gráficos estão nas seções 5.8 e 5.9;
a revisão visual está registrada na seção 5.10; a interpretação e as recomendações propostas estão
na seção 5.12. O relatório final está registrado na seção 5.13.

### 5.7. Políticas de feedback e sensibilidade dos tokens

**Registro documental:** 19/11/2026. A implementação e a execução são anteriores a esta atualização;
não foi atribuída uma data exata a esses eventos sem evidência adicional. Modelo, tarifas e câmbio
continuam com as referências históricas de 18/11/2026. Não houve nova consulta às fontes.

#### Funções e comparabilidade

`comparar_politicas()` e `analisar_sensibilidade()` recebem a tabela de resultados já calculada,
sem recalcular consumo ou custos pelo MVP. As auxiliares `_indexar_comparacoes()` e `_validar_par()`
verificam colunas obrigatórias e únicas, identificadores preenchidos, sem duplicidade, e presença
dos cenários necessários. Os pares são localizados por identificador, independentemente da ordem
das linhas ou dos índices do DataFrame. A tabela de origem não é modificada.

Os custos mensais em BRL e os campos financeiros exigidos devem ser Decimal finitos e não
negativos nas funções de comparação. A leitura de condições continua exigindo tarifas e câmbio
estritamente positivos. Entre cada cenário e sua referência devem coincidir as cinco hipóteses
não variadas e os 12 campos de condições: provedor, modelo, modalidade, tarifas, câmbio, fontes e
datas. O campo previsto deve realmente mudar; nomes e consumos derivados não definem o par.

Nas políticas, varia somente `proporcao_acertos_com_feedback`, entre 0 e 1; a referência deve usar
1, isto é, feedback em todas as respostas. Na sensibilidade, C10/C11 variam somente `tokens_entrada`
e C12/C13 somente `tokens_saida`, com valor finito não negativo. Alterações nas demais hipóteses ou
condições são rejeitadas com identificação do par e dos campos divergentes.

`apresentar_comparacoes()` mostra as duas tabelas com símbolos monetários, sinais e percentuais;
`formatar_percentual()` apresenta valores positivos com `+` e `None` como `Não aplicável`.
A execução calcula e valida ambas as comparações antes de iniciar a exportação. Os três arquivos
desta etapa foram preservados na ampliação para quatro tabelas descrita na seção 5.11.

#### Exportações das comparações

A execução continua sendo a da seção 5.6 e também substitui estes dois arquivos, sem acumular linhas:

- `resultados/estudo_de_caso/comparacao_politicas.csv`: **seis linhas e 20 colunas**.
- `resultados/estudo_de_caso/sensibilidade_tokens.csv`: **quatro linhas e 24 colunas**.

Os caminhos padrão são relativos à pasta do script. As funções aceitam destinos temporários;
por padrão, as comparações ficam na mesma pasta de `resultados_cenarios.csv`. A regra `/resultados/`
as mantém fora do Git. A tabela original conserva suas 13 linhas e 35 colunas.

Em cada exportação, os campos estão na ordem abaixo, seguidos dos mesmos 12 campos de condições
listados na seção 5.6, de `provedor` até `data_consulta_cambio`:

| Arquivo | Campos específicos, na ordem exportada |
| --- | --- |
| `comparacao_politicas.csv` | `id_cenario`, `id_referencia`, `usuarios_ativos`, `proporcao_acertos_com_feedback`, `custo_politica_mensal_br`, `custo_referencia_mensal_br`, `reducao_mensal_br`, `reducao_percentual` |
| `sensibilidade_tokens.csv` | `id_cenario`, `id_referencia`, `campo_alterado`, `usuarios_ativos`, `tokens_entrada_referencia`, `tokens_saida_referencia`, `tokens_entrada_cenario`, `tokens_saida_cenario`, `custo_referencia_mensal_br`, `custo_cenario_mensal_br`, `variacao_mensal_br`, `variacao_percentual` |

As exportações preservam UTF-8, vírgula entre campos, ponto decimal, cabeçalho e ausência de índice,
sem símbolos monetários, sinais de porcentagem ou arredondamento para duas casas. Custos,
diferenças e percentuais aplicáveis permanecem Decimal; os campos financeiros devem ser relidos
como texto e convertidos diretamente para Decimal.

As divisões percentuais das comparações seguem a precisão e o arredondamento do contexto Decimal
vigente.
A rotina não altera esse contexto nem aplica `quantize()` ou arredondamento explícito intermediário.
Isso não significa precisão infinita para dízimas: um teste com precisão local de dez dígitos
confere `33.33333333`, preservando a configuração. As duas casas são somente para apresentação.

**Referência zero:** o percentual é `None`, exibido como `Não aplicável` e exportado como campo vazio.
A diferença monetária permanece calculada e exportada, mesmo que negativa. Não substituir o
percentual indefinido por zero. Esse comportamento está coberto por testes com tabelas simuladas;
não é o caso das referências de custo positivo nos arquivos atuais do estudo.

#### Evidências e alcance

O arquivo de testes contém **17 métodos adicionais**, totalizando **47 métodos do estudo** e
**235 no conjunto com os 188 do MVP**, em 18 classes nessa etapa. A contagem de 47 neste arquivo
permanece; os 18 métodos do arquivo do gráfico ampliaram o total conforme a seção 5.8.
A aprovação dos 235 foi informada no pedido do registro das comparações; não havia log adicional
nos arquivos então consultados. A suíte não foi repetida naquela revisão documental. Na implementação
posterior do gráfico, os 253 métodos do conjunto ampliado passaram, conforme a seção 5.8.

Os novos testes cobrem os resultados e fórmulas independentes das comparações, referências,
identificadores ausentes/duplicados, colunas inválidas, hipóteses e condições incompatíveis,
custos inválidos, preservação da tabela e ausência de recálculo. Também cobrem referência zero,
precisão do contexto Decimal, exportação dos valores completos e falha de comparabilidade sem
sobrescrever os três resultados anteriores. Casos de `subTest` não são métodos adicionais.

Nesta revisão, as conferências pontuais de leitura dos CSVs já existentes confirmaram esquemas,
seis pares de políticas, quatro variações de tokens e percentuais descritos na seção 6.
Os componentes de custo de C05 também foram conferidos nos resultados exportados. Isso não é uma
nova execução de `analise_estudo.py`, da suíte ou dos cenários, nem cria novos testes persistentes.
As relações conferidas decorrem das hipóteses e fórmulas, sem comprovar comportamento dos
estudantes, aprendizagem ou qualidade pedagógica equivalente. Não houve chamadas reais a APIs.

### 5.8. Primeiro gráfico Plotly — 2026-11-19

**Implementado e gerado em 19/11/2026:** [graficos_estudo.py](../graficos_estudo.py), separado da rotina
de cálculo e do MVP. O primeiro gráfico apresenta custo mensal estimado de IA por escala e
política, usando somente C01 a C09. Esta evolução do estudo não publica uma nova versão nem altera
a tag v0.1.0. Fontes, tarifas, câmbio e referências de 18/11/2026 permanecem preservados.

#### Leitura, validação e seleção

`ler_resultados_grafico()` lê `resultados/estudo_de_caso/resultados_cenarios.csv` como texto,
reutilizando `ler_csv_texto()` com o esquema real de 35 colunas na ordem documentada. Não executa
a análise se o arquivo estiver ausente: informa como gerar os resultados com `analise_estudo.py`.

`validar_dados_grafico()` confere colunas necessárias e únicas, identificadores sem duplicidade e
presença de C01 a C09. Seleciona explicitamente esses nove IDs e os ordena, independentemente da
ordem ou dos índices recebidos. C10 a C13 ficam excluídos das barras, sem soma de cenários.

Nos registros selecionados, exige campos preenchidos, usuários inteiros e correspondência exata
entre ID e hipóteses da matriz principal: 100, 500 ou 1000 usuários; 40 respostas por usuário;
taxa de acerto 0.60; proporções 0, 0.25 e 1; 500 tokens de entrada e 300 de saída por feedback.
Campos numéricos são reconstruídos como Decimal finitos e não negativos, exceto usuários, que
usam `int`. Tarifas e câmbio devem ser positivos. As datas devem ser ISO válidas e os 12 campos
de condições comerciais e referências devem ser iguais entre os nove cenários.

A leitura financeira usa diretamente `Decimal(texto)`, sem float intermediário. `criar_figura()`
valida novamente os dados recebidos e retorna a figura, sem gravar arquivos ou abrir navegador.
Importar o módulo também não lê CSVs, pergunta, imprime, consulta rede ou exporta.

#### Eixos, séries e apresentação

O título é **Custo mensal estimado de IA por escala e política de feedback**. Plotly Express cria
nove barras com `barmode="group"`, organizadas em três séries:

1. Somente nos erros.
2. Erros + 25% dos acertos.
3. Todas as respostas.

O eixo X é categórico, na ordem **100, 500 e 1.000 usuários**; esses níveis são escalas alternativas,
não meses sucessivos ou previsão de crescimento. O eixo Y mostra o **custo mensal estimado de IA
em BRL**, começando em zero. As barras ficam lado a lado, pois os cenários são alternativas e seus
custos não devem ser empilhados ou somados como uma despesa única.

Cores distintas e padrões ajudam a distinguir as políticas. Os textos sobre as barras e no hover
usam `R$`, vírgula decimal e duas casas. O hover inclui identificador, usuários, política e feedbacks
mensais; contagens não recebem formatação monetária. A anotação identifica cenários hipotéticos,
modelo, modalidade, tarifas por milhão e cotação fixa, extraídos dos dados sem nova consulta.

A figura é construída a partir de uma cópia: somente `custo_grafico_br`, usada nas alturas,
converte os custos para `float`. Os dados financeiros originais continuam Decimal, e os textos
monetários são preparados diretamente deles com `formatar_moeda_br()`. A geometria tem aproximação
de ponto flutuante, sem promessa de precisão decimal exata. Os números gráficos não são usados
em cálculos financeiros ou exportações de resultados; o CSV de entrada não é modificado ou regravado.

#### Reprodução e HTML offline

Com o terminal na raiz e a `.venv-win` existente, executar nesta ordem:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B graficos_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest tests.test_graficos_estudo -v
```

`executar_grafico()` coordena leitura, criação e exportação, aceitando caminhos para testes.
A integração posterior do segundo gráfico está descrita na seção 5.9; o comando acima gera ambos.
`exportar_html()` cria a pasta quando necessário e grava
`resultados/estudo_de_caso/custo_mensal_por_escala_politica.html`, relativo à pasta do script.
Usa `write_html(full_html=True, include_plotlyjs=True, auto_open=False)`: o arquivo é completo,
incorpora a biblioteca Plotly e permite visualização offline sem CDN. O terminal informa o caminho;
para visualizar, localizar o HTML no Explorador de Arquivos e abri-lo manualmente no navegador.

Erros de entrada ou validação interrompem o fluxo antes da gravação, preservando um HTML anterior.
O arquivo gerado está ignorado pela regra `/resultados/` do Git. O segundo gráfico foi
acrescentado conforme a seção 5.9. Não há exportação PNG/JPEG, dashboard ou execução automática
da análise pelo script do gráfico.

#### Dependências e evidências

Em 19/11/2026, Plotly não estava instalado. Foram adicionados somente **plotly 7.1.0**, dependência
direta, e **narwhals 2.29.0** e **packaging 26.3**, exigidos por ele. As versões efetivamente
instaladas foram registradas em `requirements.txt`, preservando suas entradas e os pacotes
anteriores. `pip check` retornou `No broken requirements found.` Não houve instalação de Kaleido,
Dash, navegadores ou outros componentes opcionais. A instalação limpa do conjunto ampliado não
foi repetida; a validação histórica do MVP permanece com seu alcance original.

Na primeira etapa, [test_graficos_estudo.py](../tests/test_graficos_estudo.py) acrescentou
**18 métodos em uma classe**. A ampliação posterior está na seção 5.9. Os primeiros testes usam
`unittest`, dados controlados e arquivos temporários. Cobrem leitura e preservação exata de Decimal,
nove barras e três séries, ordens das escalas e políticas, cores e padrões distintos, alturas
aproximadas e textos monetários. Também conferem exclusão de C10 a C13, independência da ordem e
do índice, identificadores ausentes ou duplicados, campos/custos inválidos e condições ou hipóteses
incompatíveis. Verificam a preservação da entrada e do HTML anterior em falhas, criação sem
navegador ou gravação, importação sem efeitos e HTML completo com Plotly incorporado.

**Execução da implementação em 19/11/2026:** os 18 métodos novos passaram isoladamente e a suíte
completa aprovou **253 métodos em 19 classes**: 188 do MVP, 47 da análise e 18 do gráfico.
Casos de `subTest` não contam como métodos adicionais. Essa execução é anterior a esta atualização
documental; a suíte não foi repetida para editar os documentos.

Depois dos testes, o HTML real foi gerado. A conferência pontual da figura confirmou nove barras,
três séries, alturas aproximadas correspondentes aos valores financeiros e textos preparados dos
Decimal. O arquivo foi conferido como HTML completo com Plotly incorporado, e os hashes confirmaram
preservação dos CSVs e arquivos protegidos. Essas conferências não acrescentaram testes persistentes.

Na etapa inicial, houve somente conferência estrutural, que não comprovava legibilidade ou
renderização. A revisão visual posterior está registrada na seção 5.10, com dimensões e navegador
identificados. O gráfico representa estimativas sob hipóteses, sem comprovar uso real ou qualidade
pedagógica; a revisão visual não muda esses limites.

### 5.9. Segundo gráfico: sensibilidade dos tokens — 2026-11-19

**Implementado e gerado em 19/11/2026:** o módulo `graficos_estudo.py` passou a produzir também
**Sensibilidade do custo mensal de IA em relação a C05**. Reutiliza a exportação existente, sem
recalcular custos, consultar preços ou câmbio, alterar a análise ou o MVP v0.1.0. Não foram
instalados ou atualizados pacotes nessa implementação.

#### Leitura e validação da sensibilidade

`ler_sensibilidade_grafico()` lê `resultados/estudo_de_caso/sensibilidade_tokens.csv` em UTF-8 com
ou sem BOM, inicialmente como texto, com vírgula entre campos. Confere o cabeçalho real de 24
colunas na ordem da seção 5.7, a quantidade de campos e a presença de registros; remove espaços
externos. Se o arquivo estiver ausente, orienta a executar `analise_estudo.py`, sem chamá-lo.

`validar_sensibilidade_grafico()` exige exatamente C10, C11, C12 e C13, sem duplicidades, ordenados
por identificador independentemente das linhas ou índices recebidos. Todos devem referenciar C05.
A validação confere campos obrigatórios, usuários inteiros não negativos, datas ISO válidas e
campos numéricos finitos. Valores financeiros, tokens e percentuais são reconstruídos diretamente
como Decimal; a diferença em BRL e o percentual podem ser negativos, pois representam reduções.

Os quatro registros devem ter as mesmas condições comerciais e referências, quantidade de
usuários, custo mensal de C05 e tokens da referência. Tarifas, câmbio e custo de referência devem
ser positivos para o gráfico. C10/C11 devem indicar `tokens_entrada` como campo alterado e manter
saída igual à referência; C12/C13 devem indicar `tokens_saida` e manter entrada. O token previsto
deve realmente mudar. Essas verificações não atualizam as condições históricas nem recalculam custos.

**Percentual não aplicável:** um campo vazio, ou `None` nos dados recebidos pela função, não vira
zero. A rotina explica que falta base válida para representar as quatro comparações e interrompe
a geração, sem barras fictícias ou sobrescrita dos HTMLs anteriores. Custo de referência zero
também impede o gráfico. O CSV de análise permanece preservado, incluindo seus campos vazios;
não se altera o tratamento financeiro descrito na seção 5.7.

#### Figura, referência e precisão

`criar_figura_sensibilidade()` recebe os dados, valida uma cópia e retorna a figura sem gravar ou
abrir navegador. Há quatro barras horizontais, de cima para baixo:

1. C10 — Entrada: 500 → 250 tokens.
2. C11 — Entrada: 500 → 1.000 tokens.
3. C12 — Saída: 300 → 150 tokens.
4. C13 — Saída: 300 → 600 tokens.

Os rótulos são construídos com os tokens dos dados validados. O eixo horizontal é a **variação
percentual do custo mensal total de IA contra C05**, em escala linear simétrica, com linha em
zero. Reduções ficam à esquerda; aumentos, à direita. Cores, sinais e posição distinguem os
sentidos. Percentuais recebem sinal e vírgula decimal, como `-12,5%` e `+25,0%`.
Os dados já são percentuais: `Decimal("25")` é 25%, sem nova multiplicação por 100 na apresentação.

O denominador é sempre o custo mensal de C05, conforme a fórmula da seção 6. Os resultados
conferidos são **C10: -12,5%; C11: +25%; C12: -37,5%; C13: +75%**. Variação de tokens não equivale
à variação do custo total de IA: reduzir pela metade a entrada em C10 reduz o custo em 12,5%,
enquanto reduzir pela metade a saída em C12 reduz em 37,5%. Sob essas tarifas, entrada e saída
participam do custo de C05 em 25% e 75%, respectivamente, conforme a conferência já registrada.
Isso não demonstra consumo medido ou qualidade pedagógica equivalente.

A anotação identifica C05 e seu custo mensal, obtido dos dados: internamente `12.7824400` BRL,
apresentado como R$ 12,78. O hover inclui identificador do cenário e da referência, campo alterado,
tokens de entrada e saída antes/depois, custos mensais da referência e do cenário, diferença em
BRL e variação percentual. Valores monetários usam a auxiliar brasileira existente; tokens são
quantidades e não recebem símbolo monetário. A figura explicita hipóteses, tarifas e câmbio fixos.

Os dados originais e percentuais continuam Decimal. Só `variacao_grafica`, numa cópia de
visualização, converte os percentuais para float para definir coordenadas aproximadas. Textos
monetários e percentuais são preparados diretamente dos Decimal, sem novos cálculos financeiros
com valores gráficos ou alteração do contexto Decimal global. Nenhum CSV é regravado.

#### Comando integrado e exportação

Com o terminal na raiz do projeto, o comando existente gera os dois gráficos a partir dos CSVs:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B graficos_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest tests.test_graficos_estudo -v
```

O primeiro comando prepara os resultados quando necessário; o script dos gráficos não executa
a análise automaticamente. `executar_grafico()` aceita caminhos temporários para ambas as entradas
e saídas. Ele valida e constrói **as duas figuras antes da primeira gravação**, preservando o
primeiro gráfico e a importação sem leitura, impressão, interação ou exportação.

A nova saída é `resultados/estudo_de_caso/sensibilidade_tokens.html`; a primeira continua sendo
`resultados/estudo_de_caso/custo_mensal_por_escala_politica.html`. Os caminhos padrão partem da pasta
do script. Ambos usam `full_html=True`, `include_plotlyjs=True` e `auto_open=False`, com Plotly
incorporado para visualização offline. O terminal informa os caminhos: localizar cada HTML no
Explorador de Arquivos e abri-lo manualmente no navegador. Ambos ficam ignorados pelo Git.

#### Testes, execução real e revisão visual

Foram acrescentados **18 métodos em uma segunda classe** de `tests/test_graficos_estudo.py`, preservando
os 18 testes do primeiro gráfico e adaptando seus dados temporários para a integração. Os novos
conferem quatro barras, orientação, linha em zero, ordem, referência, sinais, textos monetários e
percentuais, associação por identificador e rótulos obtidos dos dados. Cobrem campos/IDs inválidos,
condições ou referências divergentes, percentual não aplicável, valores não finitos, negativos
válidos e preservação da entrada, dos Decimal e do contexto. Também verificam HTML offline,
preservação de ambos os HTMLs diante de erro no segundo e construção de ambas as figuras antes
de gravar, sem alterar a figura original. A importação sem efeitos permanece coberta pelos testes.

Na implementação de 19/11/2026, **36 métodos dos gráficos passaram** e a suíte completa aprovou
**271 métodos em 20 classes**: 188 do MVP, 47 da análise e 36 dos gráficos. Combinações de `subTest`
não são métodos adicionais. Essa execução anterior está registrada nesta sessão; não foi repetida
para esta atualização documental.

Após a suíte, os dois HTMLs reais foram gerados pelo comando integrado. A conferência pontual da
sensibilidade confirmou as quatro coordenadas e textos esperados; ambos os arquivos foram
conferidos como HTML completo com Plotly incorporado. A comparação de hashes confirmou a
preservação dos CSVs e demais arquivos protegidos. Isso é execução e conferência estrutural,
sem novos testes persistentes ou recálculo dos custos.

Na implementação dos gráficos, a validação foi estrutural, sem observação da renderização.
A inspeção visual posterior e a correção estão na seção 5.10. Os indicadores então pendentes
foram implementados na seção 5.11. A interpretação e as recomendações propostas estão na seção 5.12;
o relatório final está registrado na seção 5.13, sem dados reais de uso ou qualidade pedagógica
equivalente comprovada.

### 5.10. Revisão visual dos dois gráficos — 2026-11-19

**Data efetiva da revisão:** 19/11/2026. **Data desta atualização documental:** 19/11/2026.
As datas coincidem, mas são atividades distintas: esta atualização registra a revisão anterior
sem abrir novamente o navegador, executar testes ou regenerar arquivos. As condições históricas
de modelo, tarifas e câmbio permanecem com referência de 18/11/2026.

#### Evidências e alcance da revisão visual

O relatório da revisão está disponível nesta conversa, acompanhado de capturas e registros JSON
de renderização, hover, legenda, zoom e requisições. As evidências ficaram fora do repositório e
não foram copiadas para ele. Foram utilizados os HTMLs reais em Chrome instalado, com perfil
temporário separado do pessoal, sem instalação de pacotes, navegadores ou ferramentas adicionais.
O navegador foi encerrado e o perfil temporário exclusivo removido após a revisão.

Os dois gráficos foram observados em áreas de visualização de **1440×900** e **800×800 pixels**.
O acesso à rede das páginas estava desativado. As capturas continham as figuras efetivamente
renderizadas; leitura do HTML ou screenshot vazio não foi usada como prova de renderização.

| Gráfico e arquivo em `resultados/estudo_de_caso/` | Aspectos conferidos visualmente |
| --- | --- |
| Escala e política — `custo_mensal_por_escala_politica.html` | Nove barras agrupadas, escalas 100/500/1.000 e três políticas na ordem definida, sem C10 a C13 ou soma de alternativas; eixo de custo em BRL a partir de zero, rótulos, título, legenda, cores/padrões, margens e identificação das hipóteses, tarifas e câmbio fixos |
| Sensibilidade — `sensibilidade_tokens.html` | Quatro barras C10 a C13 de cima para baixo, referência C05, percentuais -12,5%, +25%, -37,5% e +75%; eixo linear simétrico e linha em zero, reduções à esquerda e aumentos à direita, identificação dos tokens alterados e custo de referência, sinais, rótulos e unidades |

Após a correção descrita abaixo, títulos, referências, legendas, rótulos e acentos estavam legíveis,
sem cortes ou sobreposições observados nas duas dimensões verificadas. A janela menor reduziu a
área útil das barras, especialmente no gráfico horizontal, mas as informações permaneceram
legíveis. Isso não certifica responsividade em qualquer largura ou dispositivo.

#### Interações, dados e uso offline

- **Inspeção visual e interação:** o hover foi acionado em todas as nove barras do primeiro
  gráfico e nas quatro do segundo, nas duas dimensões. No primeiro, foram observados identificador,
  usuários, política, feedbacks e custo mensal. No segundo, cenário/referência, campo alterado,
  tokens antes/depois, custos, diferença em BRL e percentual estavam disponíveis no hover.
- **Legenda:** ocultar e restaurar uma série funcionou nos dois gráficos, nas duas dimensões,
  sem trocar a associação dos cenários. A ocultação muda a visão, não os dados dos CSVs.
- **Zoom e restauração:** em 1440×900, o arraste alterou os intervalos dos eixos nos dois gráficos;
  o duplo clique restaurou os intervalos iniciais. Não se atribui esse teste a dispositivos táteis.
- **Conferência de dados:** os valores e textos dos hovers foram comparados aos CSVs de origem,
  incluindo os quatro percentuais e a referência C05. A leitura das evidências complementou a
  observação visual, sem recalcular custos ou medir consumo real. Tokens alterados e variação do
  custo estavam identificados separadamente; não foram tratados como percentuais equivalentes.
- **Offline observado:** as figuras renderizaram com rede desativada nas páginas, sem falhas de
  recursos ou erros de JavaScript observados. Os registros de requisição da revisão continham
  somente o carregamento dos arquivos locais. Isso comprova o uso offline dos HTMLs revisados,
  sem confundir referências externas existentes no código incorporado com recursos requisitados.

#### Defeito encontrado e correção mínima

No gráfico de sensibilidade, o texto da referência se sobrepunha ao título, tanto na janela ampla
quanto na menor. O problema foi confirmado nas capturas anteriores à correção.

A única alteração de código foi a posição vertical da anotação em `criar_figura_sensibilidade()`:
`y` passou de `1.22` para `1.16`, em coordenadas relativas à área do gráfico. Não houve redesenho,
alteração de eixos, dados, fórmulas ou percentuais. O primeiro gráfico não exigiu correção visual.
Os dois HTMLs foram regenerados pelo comando existente e revistos nas duas dimensões. Na nova
renderização, o texto da referência ficou abaixo do título, sem a sobreposição identificada.

Após esse ajuste, os **36 métodos de teste dos gráficos passaram**. Não foram acrescentados ou
alterados testes. A suíte completa de 271 métodos não foi repetida nessa revisão; seu resultado
anterior continua sendo o da implementação do segundo gráfico. Nesta atualização documental,
nem os 36 métodos nem a suíte completa foram executados.

As verificações visuais e de interação são distintas dos testes estruturais da figura e da
conferência dos valores. Nenhuma delas comprova comportamento dos estudantes ou qualidade
pedagógica. As comparações de hashes confirmaram a preservação dos CSVs e demais arquivos
protegidos; Decimal permanece nos dados, com float restrito à cópia de coordenadas já existente.

**Revisão concluída no alcance confirmado:** Chrome, 1440×900 e 800×800, HTMLs locais offline,
hover e legenda em ambos os tamanhos e zoom/restauração na janela ampla. Telas menores, outros
navegadores, dispositivos móveis, toque ou outros modos de acesso não foram testados. Não há
validação universal de legibilidade, acessibilidade ou responsividade. As instruções de abertura
manual dos HTMLs permanecem válidas. Ao encerrar essa revisão em 19/11/2026, os indicadores ainda
eram uma próxima etapa; sua implementação posterior está na seção 5.11. A interpretação e as
recomendações propostas estão na seção 5.12; o relatório está registrado na seção 5.13.
O MVP v0.1.0 e sua tag permanecem preservados.

### 5.11. Participações e custo mensal de IA por usuário — 2026-11-25

**Implementação:** 25/11/2026. **Execução dos testes e conferência real:** 25/11/2026.
**Atualização deste registro:** 25/11/2026. São atividades distintas, realizadas na mesma data.
Modelo `gpt-6-luna`, tarifas de entrada `0.10` e saída `0.50` USD por milhão e cotação fixa
`Decimal("5.8102")` BRL por USD continuam sendo as condições de 18/11/2026 dos arquivos do estudo.
Não houve consulta atual a preços, BCB ou APIs, instalação ou atualização de pacotes.

#### Cálculo, validação e denominadores independentes

`calcular_indicadores(tabela)` recebe os resultados já calculados, sem chamar novamente as funções
de consumo ou custo do MVP. Retorna uma tabela separada com os identificadores, nomes e ordem
recebidos, sem modificar valores, tipos, colunas, índices ou ordenação da entrada.

Valida colunas necessárias e únicas, tabela não vazia, identificadores textuais preenchidos e
únicos e nomes preenchidos. Exige usuários inteiros não negativos, aceitando escalares inteiros
do Pandas sem aceitar booleanos, texto, floats ou truncamento de frações. Os quatro custos de base
devem ser objetos Decimal finitos e não negativos. A soma de entrada e saída em USD deve coincidir
com o total mensal em USD, comparados na precisão Decimal vigente.

As quatro fórmulas são:

- `participacao_entrada_percentual = custo_entrada_usd / custo_ia_mensal_usd * Decimal("100")`.
- `participacao_saida_percentual = custo_saida_usd / custo_ia_mensal_usd * Decimal("100")`.
- `custo_ia_mensal_por_usuario_usd = custo_ia_mensal_usd / Decimal(int(usuarios_ativos))`.
- `custo_ia_mensal_por_usuario_br = custo_ia_mensal_br / Decimal(int(usuarios_ativos))`.

As participações usam componentes e total na mesma moeda, USD. O custo por usuário usa o total
mensal da respectiva moeda; a conversão da contagem inteira para Decimal não passa por float.
Todos os indicadores aplicáveis permanecem Decimal, sem arredondamento intermediário explícito.

Os denominadores são tratados separadamente:

| Condição | Participações de entrada/saída | Custos por usuário |
| --- | --- | --- |
| Total USD zero, usuários positivos | `None` | Divisão válida; custo USD por usuário é Decimal zero |
| Usuários zero, total USD positivo | Calculadas normalmente | `None` em USD e BRL |
| Ambos zero | `None` | `None` |
| Entrada gratuita e saída paga | 0% de entrada e 100% de saída | Calculados se houver usuários |

`None` significa não aplicável, nunca zero. Na exportação torna-se campo vazio; na apresentação,
texto `Não aplicável`. Nenhum indicador é inventado para contornar divisão por zero.

O cálculo usa `localcontext()` para herdar a precisão e o arredondamento atuais, isolando também
os flags das operações, sem alterar o contexto global. Isso não oferece precisão matemática
infinita: por exemplo, participações de um terço e dois terços, com dez dígitos de precisão,
produzem `33.33333333` e `66.66666667`. Os testes conferem a soma em 100% dentro da precisão adotada.
A verificação de coerência dos custos também usa essa precisão, sem arredondar os valores originais.

#### Integração, arquivo e apresentação

`executar_estudo()` calcula resultados, políticas, sensibilidade e indicadores antes de começar
qualquer exportação. Preserva o retorno existente, a tabela original de 13 linhas e 35 colunas,
e os esquemas dos três CSVs anteriores. O novo parâmetro opcional `caminho_indicadores` foi
acrescentado ao final da assinatura, preservando chamadas existentes e permitindo testes temporários.

A nova saída padrão é `resultados/estudo_de_caso/indicadores_cenarios.csv`, na mesma pasta dos
resultados. O arquivo contém **13 linhas e 11 colunas**, nesta ordem:

| Grupo | Colunas |
| --- | --- |
| Identificação e contagem | `id_cenario`, `cenario`, `usuarios_ativos` |
| Custos de base | `custo_entrada_usd`, `custo_saida_usd`, `custo_ia_mensal_usd`, `custo_ia_mensal_br` |
| Indicadores | `participacao_entrada_percentual`, `participacao_saida_percentual`, `custo_ia_mensal_por_usuario_usd`, `custo_ia_mensal_por_usuario_br` |

São usados UTF-8, vírgula entre campos, ponto decimal, cabeçalho e `index=False`. Decimal é
exportado com o valor completo e `None` com campo vazio; na releitura, manter texto até reconstruir
Decimal diretamente. As condições e fontes continuam nos arquivos de entrada e resultados já
existentes; não se atribuem colunas de metadados adicionais a esse novo CSV de 11 campos.
A pasta permanece ignorada pelo Git. Falhas no cálculo dos indicadores impedem a gravação de
qualquer uma das quatro tabelas, preservando exportações anteriores.

`apresentar_indicadores()` mostra participações com duas casas e custos com **oito casas decimais**,
com cabeçalhos `USD/usuário ativo/mês` e `BRL/usuário ativo/mês`. Assim, valores inferiores a um
centavo não ficam ocultos nos exemplos. Uma cópia recebe os textos de exibição, inclusive
`Não aplicável`; os dados originais não são substituídos por texto ou arredondados.

Os comandos executados na raiz, com a `.venv-win` existente, foram:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest tests.test_analise_estudo -v
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest discover -s tests -t . -v
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
```

A importação continua sem interação, leitura de arquivos, rede ou exportação. Código e testes do
MVP e dos gráficos foram preservados; nenhum HTML foi regravado. A nova tabela não modifica as
condições ou datas históricas nem representa uma nova release do MVP v0.1.0.

#### Resultados e evidências desta etapa

Em C05 foram confirmados **25% de entrada**, **75% de saída**, **USD 0.0044 por usuário ativo/mês**
e **BRL 0.02556488 por usuário ativo/mês**. A apresentação mostra `US$ 0,00440000` e `R$ 0,02556488`.
C02, C05 e C08 mantêm os mesmos custos por usuário, pois diferem apenas na escala sob as hipóteses
atuais. Isso é consequência do modelo de cálculo, sem evidência empírica de economia de escala.

Foram acrescentados **19 métodos** em `TestIndicadores`, sem remover testes anteriores. Cobrem os
13 cenários com expectativas independentes, C05 e a igualdade de custos unitários, denominadores
zero tratados separadamente, entrada gratuita, custos/tipos inválidos, total incoerente, IDs e
usuários inválidos e inteiros escalares do Pandas. Também conferem divisões não exatas, contexto
preservado, soma das participações, ordem e entrada intactas, ausência de recálculo pelo MVP,
releitura exata de Decimal, None vazio no CSV, oito casas na apresentação e integração sem
sobrescrever resultados diante de falha. Os testes usam arquivos temporários.

**Resultado em 25/11/2026:** passaram os **66 métodos da análise** e os **290 métodos da suíte
completa em 21 classes**: 188 do MVP, 66 da análise e 36 dos gráficos. Combinações de `subTest` não
são métodos adicionais. A rotina real foi executada e exportou 13 indicadores sem alterar os três
CSVs anteriores, cuja comparação de hashes confirmou conteúdo idêntico. A releitura dos campos
financeiros do novo CSV preservou exatamente os Decimal, sem etapa intermediária em float.

A conferência pontual de compatibilidade carregou os CSVs anteriores pelos leitores dos gráficos
e construiu as figuras em memória, confirmando nove e quatro barras. Não houve nova inspeção
visual, geração de imagens ou alteração dos HTMLs. Esse controle de compatibilidade é distinto
dos testes automatizados e da revisão visual de 19/11/2026.

O custo por usuário cobre **somente IA**: não inclui infraestrutura ou outras despesas e não
demonstra, sozinho, economia de escala ou viabilidade financeira. Os resultados decorrem de
hipóteses e condições fixas, sem dados observados de estudantes ou qualidade pedagógica comprovada.
Indicadores estão implementados e conferidos; a interpretação e as recomendações propostas estão
registradas na seção 5.12. O relatório final está registrado na seção 5.13.

### 5.12. Interpretação e recomendações condicionais — 2026-11-25

[INTERPRETACAO_ESTUDO.md](INTERPRETACAO_ESTUDO.md), criado em **25/11/2026**, reúne a síntese
analítica para o relatório final. Esta atualização documental, na mesma data, registra o material
produzido sem repetir os cálculos ou os testes. O documento interpreta políticas, sensibilidade
dos tokens e escala/custo por usuário e fundamenta propostas de ação com evidência, condição e
dado a medir.

Os achados principais, sob as hipóteses e fórmulas adotadas, são:

- Feedback somente nos erros reduz o custo de IA em 60%; erros mais 25% dos acertos reduzem em
  45%, contra C03, C06 ou C09 na mesma escala. Isso depende da taxa de acerto de 60% e de tokens
  iguais por feedback; não demonstra superioridade pedagógica.
- Contra C05, C10 a C13 variam o custo em -12,5%, +25%, -37,5% e +75%. A entrada representa 25%
  e a saída 75% do custo em C05; essa composição muda nas variações de tokens.
- Com a mesma política e demais hipóteses constantes, o custo cresce proporcionalmente aos
  usuários e o custo unitário permanece igual. C02/C05/C08 têm USD 0.0044 e BRL 0.02556488 por
  usuário ativo/mês. Isso não comprova economia de escala nem custo operacional completo.

As cinco recomendações propõem avaliar feedback somente nos erros e feedback opcional nos acertos,
medir tokens faturáveis antes de definir limites, avaliar clareza e concisão junto da qualidade e
dimensionar orçamento com hipóteses explícitas. São **propostas condicionais**, sem política
definitivamente adotada, orçamento máximo aprovado ou meta de qualidade inventada.

O plano de medição futura inclui uso mensal, acertos, parcela efetiva de acertos com feedback,
tokens por tipo de feedback, falhas, novas tentativas e correção, clareza e utilidade pedagógica.
Ele diferencia o toggle da parcela efetiva de acertos com feedback. **Formular esse plano não
significa executar piloto, coleta ou avaliação pedagógica:** nenhuma dessas ações foi realizada.

A conferência pontual de 25/11/2026 leu os dois CSVs de entrada e os quatro de resultados como
texto, reconstruindo valores diretamente como Decimal, sem float intermediário. Conferiu os
13 resultados, seis comparações, quatro sensibilidades e 13 indicadores, incluindo referências,
condições, denominadores e sinais; não encontrou divergências. Não foram executados novamente
`analise_estudo.py`, os testes ou os gráficos, nem criados testes automatizados nessa etapa.

Essas porcentagens e custos são resultados das hipóteses e fórmulas, sem evidências observadas dos
estudantes ou medição de aprendizagem. Modelo, tarifas e cotação fixa de 5.8102 BRL/USD permanecem
com as referências históricas de **18/11/2026**. Não houve pesquisa atual de preços ou câmbio.
O relatório final foi produzido na etapa posterior da seção 5.13. A revisão final de coerência,
a conferência das orientações do curso e a preparação da publicação permanecem pendentes.

### 5.13. Relatório final e imagens dos gráficos — 2026-11-25

**Produção do material:** 25/11/2026. **Atualização documental:** 25/11/2026. São etapas distintas,
realizadas na mesma data, sem nova pesquisa de preços ou câmbio.

[RELATORIO_ESTUDO.md](../RELATORIO_ESTUDO.md) reúne contexto, dados, método, resultados, dois gráficos,
recomendações condicionais, limitações, reprodução e declaração do apoio de IA. O relatório utiliza
a interpretação da seção 5.12; não substitui as condições históricas nem altera o MVP v0.1.0.
Os arquivos de imagem que acompanham o Markdown são:

- [Custo mensal por escala e política](imagens/custo_mensal_ia_por_escala_politica.png):
  `docs/imagens/custo_mensal_ia_por_escala_politica.png`, com 2880×1300 pixels; nove barras C01 a C09.
- [Sensibilidade do custo aos tokens](imagens/sensibilidade_custo_ia_tokens.png):
  `docs/imagens/sensibilidade_custo_ia_tokens.png`, com 2880×1200 pixels; quatro barras C10 a C13.

Os PNGs foram exportados dos HTMLs existentes por `Plotly.toImage()` no Chrome instalado, com as
páginas offline, sem instalar ferramentas, redesenhar figuras ou modificar os HTMLs. Na preparação
do relatório, as imagens finais foram inspecionadas quanto a títulos, eixos, legendas, acentos,
rótulos e nove/quatro barras, sem cortes ou sobreposições observados. Séries renderizadas e CSVs
foram utilizados para conferir valores. Essa inspeção dos PNGs é distinta da revisão interativa
de 19/11/2026 e dos testes estruturais; não amplia sua cobertura a outros dispositivos.

A conferência pontual dos números releu os dois CSVs de entrada e os quatro de resultados,
diretamente com Decimal, sem float intermediário. Foram verificados consumos e custos dos
13 cenários, seis comparações, quatro sensibilidades e 13 indicadores, além das condições fixas
repetidas nos resultados. Não foram encontradas divergências. Foram confirmados 14 links relativos
no relatório e a preservação por hashes de 27 arquivos existentes; o Markdownlint não apontou
problemas. Não houve nova execução da suíte ou da rotina de análise nem testes novos.

As imagens estão fora de `resultados/` e não estão ignoradas pelo Git; foram preparadas para
acompanhar o relatório no repositório. Os HTMLs interativos e os CSVs gerados continuam ignorados
e podem ser regenerados com os comandos documentados no relatório e no README. Sua existência
local não significa disponibilidade já publicada no GitHub.

Modelo, tarifas e câmbio fixo de 5.8102 BRL/USD preservam suas datas históricas de 18/11/2026.
Os resultados continuam hipotéticos, sem uso real observado ou qualidade pedagógica comprovada.
Recomendações e plano de medição foram formulados; piloto, coleta real e avaliação pedagógica
continuam futuros, sem política definitivamente adotada.

**Situação:** relatório e imagens produzidos, sem publicação nesta etapa. Permanecem a revisão
final de coerência, a conferência das orientações específicas do curso, inclusive o apoio de IA,
e a preparação da publicação. A produção do relatório não encerra o estudo nem comprova aprovação
pelo Google, avaliação pelo curso ou revisão final aprovada pelo responsável.

### 5.14. Revisão final local antes da publicação — 2026-11-25

Revisados README, planejamento do estudo, interpretação, relatório e registros pertinentes de
PROMPTS.md. O Git estava limpo em `main`, no commit
`e384020fbdd861082784bfcfdd0fea69436d89bc`; os ajustes documentais desta revisão ainda precisam
ser incorporados a um commit posterior. A tag v0.1.0 permanece no commit já registrado na seção 1.

A conferência independente dos seis CSVs com Decimal validou os 13 cenários/resultados, seis
comparações, quatro sensibilidades e 13 indicadores. Referências, denominadores, sinais, moedas,
valores citados, datas e condições históricas estão coerentes, sem divergências materiais.
O tratamento de denominadores zero foi conferido no código e nos testes existentes por leitura,
sem executá-los. A contagem estática confirma 290 métodos em 21 classes; isso não é nova aprovação
da suíte. As versões instaladas coincidem com requirements.txt, sem reinstalação ou atualização.

A prévia local do relatório usou Markdown-it já instalado e Chrome, com a página offline.
Foram observados abertura, figuras e tabelas de resultados/recomendações em 1440×1000; em 800×900,
foi conferida a seção de sensibilidade. Imagens carregaram sem cortes observados; seus textos
diminuem na janela menor, com valores também disponíveis nas tabelas e imagens em tamanho original.
Essa prévia não é a renderização final do GitHub. Os PNGs correspondem, por hash, às exportações
dos HTMLs atuais calculadas apenas em memória; nenhuma imagem ou gráfico foi substituído.

Relatório, imagens, entradas e arquivos necessários à reprodução estão versionados e não ignorados.
Resultados gerados, HTMLs e ambientes permanecem ignorados. O relatório é compreensível sem hover
ou acesso aos resultados ignorados. As instruções de reprodução estão coerentes; instalação limpa,
execução da análise e suíte completa não foram repetidas nesta revisão documental.

**Resultado:** pronto tecnicamente para publicação em portfólio no alcance local conferido,
sem declaração de publicação ou aprovação pelo responsável. Não foram disponibilizadas instruções
específicas ou critérios de avaliação do curso: sua conferência, inclusive quanto ao apoio de IA,
depende do responsável. A revisão dos materiais pelo responsável e a preparação da publicação
continuam pendentes. Não houve validação empírica, piloto ou avaliação de aprendizagem.

## 6. Unidade de análise e indicadores

No CSV de cenários e na tabela de resultados, **uma linha representa um cenário mensal**,
não um estudante nem uma despesa observada. A linha única de condições fixas, por sua vez, é
compartilhada pelos 13 cenários. Cada cenário é uma alternativa; seus custos não devem ser somados
como uma única despesa.

Indicadores do estudo, com estágios distintos:

- Quantidade mensal estimada de feedbacks: calculada.
- Tokens mensais de entrada e de saída faturáveis: calculados.
- Custo mensal de IA em USD e BRL: calculado.
- Participação da entrada e da saída no custo mensal de IA: implementada para os 13 cenários.
- Custo mensal de IA por usuário ativo em USD e BRL: implementado, somente IA.
- Diferenças monetárias e percentuais entre políticas e variações de tokens: calculadas e exportadas.

A rotina do estudo fornece consumos, custos, as duas comparações e a tabela separada de indicadores
da seção 5.11. Essa evolução não altera o menu ou o código do MVP.

### Participação no custo e custo por usuário

Os custos dos componentes já estão exportados. Em **C05**, entrada é **US$ 0,55**, isto é, **25%**
dos US$ 2,20 mensais; saída é **US$ 1,65**, ou **75%**. A conferência pontual usa `0.55 / 2.20`
e `1.65 / 2.20`, multiplicados por 100, diretamente com Decimal. São componentes de uma hipótese,
sem medição real ou comprovação de qualidade. A conferência inicialmente pontual foi ampliada
para os 13 cenários na rotina de indicadores de 25/11/2026, conforme a seção 5.11. As fórmulas são:

- Custo de entrada em USD = tokens mensais de entrada ÷ 1000000 × tarifa de entrada por milhão.
- Custo de saída em USD = tokens mensais de saída ÷ 1000000 × tarifa de saída por milhão.
- Participação de entrada (%) = 100 × custo de entrada em USD ÷ custo mensal de IA em USD.
- Participação de saída (%) = 100 × custo de saída em USD ÷ custo mensal de IA em USD.
- Custo mensal de IA por usuário em USD = custo mensal de IA em USD ÷ usuários ativos.
- Custo mensal de IA por usuário em BRL = custo mensal de IA em BRL ÷ usuários ativos.

As participações devem usar a mesma moeda no numerador e no denominador. Não somar ou dividir
valores em USD e BRL como se fossem a mesma unidade.

### Comparação das políticas

A rotina calcula seis pares dentro da mesma escala, em ordem fixa por identificador:

| Usuários | Políticas avaliadas | Referência: feedback em todas as respostas |
| --- | --- | --- |
| 100 | C01 e C02 | C03 |
| 500 | C04 e C05 | C06 |
| 1000 | C07 e C08 | C09 |

As fórmulas implementadas, com ambos os custos mensais em BRL, são:

- `reducao_mensal_br = custo_referencia - custo_politica`.
- `reducao_percentual = reducao_mensal_br / custo_referencia * 100`.

Redução positiva indica custo menor que a referência; negativa indicaria custo maior.
O denominador é o custo de feedback em todas as respostas **na mesma escala**.
Nos seis registros existentes, feedback somente nos erros reduz o custo em **60%**; feedback nos
erros e em 25% dos acertos reduz em **45%**. As reduções se repetem nas três escalas sob as mesmas
hipóteses, tarifas e cotação; não são evidência empírica de economia de escala ou aprendizagem.
Comparar escalas sob a mesma política é uma leitura distinta, sem confundir usuários e política.

### Sensibilidade dos tokens

A rotina compara C10 a C13 com **C05**, preservando as demais hipóteses e condições. As fórmulas são:

- `variacao_mensal_br = custo_cenario - custo_C05`.
- `variacao_percentual = variacao_mensal_br / custo_C05 * 100`.

| Cenário | Única hipótese alterada contra C05 | Variação do custo mensal |
| --- | --- | ---: |
| C10 | Entrada de 500 para 250 tokens por feedback | -12,5% |
| C11 | Entrada de 500 para 1000 tokens por feedback | +25% |
| C12 | Saída de 300 para 150 tokens por feedback | -37,5% |
| C13 | Saída de 300 para 600 tokens por feedback | +75% |

Aqui, variação negativa significa redução e positiva significa aumento: a subtração é **cenário
menos referência**, no sentido inverso da redução das políticas. O denominador é sempre o custo
de **C05**, e não C03, C06 ou C09. Esses sinais e denominadores não são intercambiáveis.
As variações usam tokens hipotéticos; não demonstram consumo medido ou qualidade equivalente.

Se uma referência for zero, o percentual é não aplicável, exportado como campo vazio; a diferença
absoluta é preservada. Outras razões futuras também deverão tratar denominador zero sem inventar
um percentual. A seção 5.7 distingue esse caso testado dos arquivos atuais com referências positivas.

## 7. Andamento das etapas da análise

1. **Perguntar — definido:** pergunta, público, decisão, limites e matriz revisados documentalmente.
2. **Preparar — concluído:** os dois CSVs de entrada foram preparados e conferidos, conforme 5.5.
   Hipóteses e condições pesquisadas permanecem separadas de dados observados.
3. **Processar e calcular — concluído:** a rotina da seção 5.6 valida os arquivos e produz consumos
   e custos dos 13 cenários, com condições fixas e Decimal financeiro. A execução foi conferida e
   a suíte passou. Isso não equivale a medição real de consumo ou teste de acesso à API.
4. **Analisar — comparações calculadas e conferidas:** seis pares de políticas por escala e quatro variações
   de tokens contra C05, com diferenças, percentuais e denominadores documentados. Participações
   e custos por usuário foram implementados e conferidos em 25/11/2026 para os 13 cenários.
   A interpretação está documentada na seção 5.12. Verificações aritméticas não comprovam
   comportamento real ou qualidade pedagógica.
5. **Compartilhar — material publicado:** dois gráficos gerados em HTML offline: custo
   mensal por escala/política e sensibilidade dos tokens contra C05, conforme 5.8 e 5.9. A revisão
   visual está concluída no alcance da seção 5.10. Síntese, relatório e PNGs estão produzidos,
   conforme 5.12 e 5.13. A revisão técnica local está em 5.14; o responsável confirmou depois
   a publicação e a conferência de imagens/links no GitHub, conforme a situação atual.
6. **Agir — propostas formuladas, execução pendente:** recomendações condicionais e plano de medição
   estão documentados na seção 5.12. Piloto, coleta de dados e avaliação pedagógica não foram realizados;
   nenhuma política foi adotada definitivamente com base nesta síntese.

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
- O uso como capstone e a conclusão do certificado não demonstram nota, avaliação individual
  deste relatório ou endosso do Google.

## 9. Entregáveis e critérios de conclusão

Situação dos entregáveis:

- Fontes, datas, tarifas, câmbio e condições fixas documentados; as justificativas das hipóteses
  deverão acompanhar a análise sem serem tratadas como evidência empírica.
- Tabela de entradas preparada em `dados/estudo_de_caso/cenarios.csv`, com C01 a C13, e condições
  compartilhadas em `condicoes_fixas.csv`: concluídas. Validação e cálculo reproduzíveis
  implementados em `analise_estudo.py`; exportação dos 13 resultados concluída, conforme 5.6.
- Comparações de políticas e tokens calculadas, conferidas e exportadas, conforme 5.7 e 6.
- Participações e custos por usuário implementados e exportados em `indicadores_cenarios.csv`,
  conforme 5.11. Interpretação e recomendações condicionais produzidas em
  [INTERPRETACAO_ESTUDO.md](INTERPRETACAO_ESTUDO.md), conforme 5.12; ações propostas não executadas.
- Dois gráficos implementados e gerados: custo mensal por escala/política e sensibilidade contra C05.
  Revisão visual concluída no alcance da seção 5.10; os dois PNGs do relatório foram exportados e
  inspecionados conforme 5.13, sem dashboard. Outros tamanhos e navegadores não foram validados.
- Relatório final com pergunta, fontes, preparação, resultados, dois gráficos, recomendações
  condicionais e limitações: produzido em [RELATORIO_ESTUDO.md](../RELATORIO_ESTUDO.md), com duas
  imagens conforme 5.13. Revisão técnica local realizada conforme 5.14; publicação e conferência
  de imagens/links na apresentação publicada confirmadas pelo responsável, sem data exata informada.
- Apoio de IA descrito no relatório e no histórico, sem atribuir decisões ou verificações pessoais
  não confirmadas. Certificado concluído com o estudo como capstone, sem inferir avaliação individual.

Critérios de qualidade definidos no planejamento:

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

A publicação e o uso como capstone não comprovam avaliação formal desses critérios nem validam
empiricamente as hipóteses. As evidências de cálculo e revisão permanecem nas seções correspondentes.

## 10. Próximo passo

1. Manter relatório, fontes e instruções de reprodução coerentes com os arquivos publicados,
   preservando as condições históricas da análise.
2. Definir um piloto apenas se houver decisão de prosseguir com medições reais. Uso, tokens e
   avaliação pedagógica continuam propostas futuras, sem inferir aprendizagem pelo custo.
3. Conferir outros tamanhos de tela ou navegadores se necessário, sem ampliar automaticamente
   o alcance das revisões documentadas ou presumir testes de dispositivos não observados.
4. Preservar a tag v0.1.0 do MVP. A publicação do estudo não cria uma nova release da calculadora.

**Concluído:** preparação, validação, cálculo e exportação dos 13 cenários; seis comparações de
políticas e quatro de sensibilidade, com as conferências descritas nas seções 5.6 e 5.7. Primeiro
gráfico implementado e gerado conforme 5.8 e segundo conforme 5.9, com revisão visual concluída
no alcance e nas dimensões da seção 5.10.
Pesquisa documental e cotação histórica fixa permanecem preservadas. Não foram comprovados acesso
à conta, configuração de raciocínio, consumo real ou qualidade pedagógica. Os indicadores foram
implementados e verificados em 25/11/2026. A interpretação e as recomendações condicionais foram
documentadas nessa data, conforme 5.12. Relatório final e imagens estão produzidos conforme 5.13;
revisão técnica local de coerência realizada conforme 5.14. Publicação do estudo, conferência de
imagens/links publicados e conclusão do certificado com o estudo como capstone foram confirmadas
pelo responsável, sem datas exatas ou avaliação individual do relatório informadas.
Nenhuma ação de piloto, coleta ou avaliação pedagógica foi executada.

A etapa dos indicadores de 25/11/2026 acrescentou cálculo, testes e exportação, conforme 5.11.
A etapa posterior de interpretação acrescentou somente a síntese e as propostas da seção 5.12.
A etapa do relatório acrescentou o texto e duas imagens exportadas dos HTMLs existentes, conforme
5.13. O registro documental dessa etapa não repetiu testes, cálculos, exportações ou inspeção
visual.
A revisão técnica local posterior está na seção 5.14. O funcionamento do MVP e as condições
históricas permanecem preservados.
