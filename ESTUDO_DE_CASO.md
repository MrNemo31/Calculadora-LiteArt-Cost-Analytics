# Estudo de caso — planejamento da análise de custos de IA do LiteArt

**Data do planejamento:** 18/11/2026.

**Situação:** planejamento para o estudo de caso do Google Data Analytics Professional Certificate.
A análise ainda não foi executada. Este documento não registra resultados nem aprovação formal do
curso. As orientações da atividade, inclusive sobre apoio de IA, deverão ser conferidas antes da
entrega.

## 1. Contexto e objetivo

A calculadora **LiteArt Cost Analytics v0.1.0** será a ferramenta de cálculo do estudo. Seu escopo
é estimar custos de feedbacks de IA no terminal, conforme o [README](README.md) e o
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
- Comparar custos mensais. O anual, se apresentado, será apenas o mensal multiplicado por 12,
  com consumo, preços e cotação constantes.
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
confirmados abaixo. Preparação dos dados, execução dos cenários, análise e conclusões continuam
pendentes; não houve chamadas pagas, solicitação de credenciais ou teste de acesso à conta.

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

### 5.3. Condições e exclusões do cálculo planejado

Manter um modelo permite isolar os efeitos de usuários, política de feedback e tokens. As mesmas
tarifas e `Decimal("5.8102")` BRL por USD ficarão constantes nos 13 cenários, inclusive na análise
de sensibilidade. A projeção anual, se apresentada, será o mensal multiplicado por 12 sob essas
mesmas condições, sem simular crescimento, alterações tarifárias ou variação cambial.

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
valores da release ou sua tag. Nas futuras execuções, a opção manual permitirá reaplicar 5.8102,
sem consultar uma nova taxa para cada cenário.

### 5.4. Registros a preparar antes da análise

Manter separados, com vínculo pelos identificadores dos cenários:

- **Tarifas pesquisadas:** condições e referências confirmadas acima, com provedor, modelo, moeda,
  unidade, modalidade e data. A pesquisa atual não substitui as datas das pesquisas históricas.
- **Câmbio:** valor fixo, fonte, data da observação e data da consulta acima, sem horário inventado.
- **Hipóteses:** os 13 cenários já revisados, suas unidades, justificativas e natureza didática.
  A revisão de coerência da matriz não é validação empírica do comportamento dos estudantes.
- **Resultados derivados:** consumos e custos a calcular posteriormente, identificados por cenário
  e versão da ferramenta. Ainda não foram produzidos para este estudo.

Na próxima etapa, preparar uma entrada própria com os 13 cenários, preservando o CSV de exemplo
do MVP, e um registro separado das condições fixas. Não criar ou alterar arquivos de dados nesta
atualização. Os identificadores C01 a C13 deverão acompanhar cada nome e resultado.

O CSV de resultados da v0.1.0 contém nove colunas e não exporta modelo, tarifas, cotação, origem ou
data como metadados. Essas informações deverão acompanhar os resultados no registro do estudo,
sem presumir que já são armazenadas pelo programa ou modificar o formato histórico da release.

## 6. Unidade de análise e indicadores

**Uma linha representa um cenário mensal**, não um estudante nem uma despesa observada.
Cada cenário é uma alternativa. Seus custos não devem ser somados como uma única despesa.

Indicadores planejados:

- Quantidade mensal estimada de feedbacks.
- Tokens mensais de entrada e de saída faturáveis.
- Custo mensal de IA em USD e BRL.
- Participação da entrada e da saída no custo mensal de IA.
- Custo mensal de IA por usuário ativo, sem infraestrutura ou outras despesas.
- Diferenças monetárias e percentuais entre políticas e entre as variações de tokens.

O MVP fornece os consumos e custos por cenário. Participações, custo por usuário e comparações
específicas serão derivados na etapa de análise em um artefato próprio do estudo; não são novas
funcionalidades implementadas no terminal nem colunas já acrescentadas à exportação.

### Participação no custo e custo por usuário

Para cada cenário, planejar o cálculo dos componentes usando os mesmos preços documentados:

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

## 7. Etapas da análise planejada

1. **Perguntar:** confirmar pergunta, decisão, público e limites; revisar a matriz antes de iniciar.
2. **Preparar:** organizar os dados dos cenários, suas justificativas e os registros das condições
   fixas. A revalidação documental de modelo, tarifas e câmbio está registrada na seção 5; ela não
   equivale a testes da API ou medição real de consumo.
3. **Processar:** validar estrutura, campos, tipos, unidades, números finitos e intervalos; conferir
   usuários inteiros, duplicidades, identificadores e cobertura das 13 combinações. As entradas
   monetárias deverão ser convertidas de texto diretamente para Decimal, sem passagem por float.
4. **Analisar:** comparar políticas por escala e variações de tokens contra C05. Conferir manualmente
   pelo menos um cálculo completo de consumo e custo contra a ferramenta, registrando as entradas
   e eventuais divergências. Essa conferência ainda será realizada.
5. **Compartilhar:** preparar tabela de síntese e dois gráficos, ainda não produzidos:
   - Custo mensal por escala e política, com moeda e referência identificadas.
   - Variação do custo em relação a C05 na análise de tokens, identificando o fator alterado.
6. **Agir:** apresentar recomendações condicionais às hipóteses, acompanhadas de plano de medição
   real antes do lançamento. Priorizar o registro de uso, escolha de feedback nos acertos, tokens
   faturáveis e avaliação pedagógica antes de substituir hipóteses por evidências observadas.

A análise não deverá arredondar os valores monetários intermediários. Preservar Decimal nos dados
e usar arredondamento apenas na apresentação. Na releitura de CSV, recuperar os campos financeiros
como texto e convertê-los diretamente para Decimal, sem reutilizar textos monetários do terminal.

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

Entregáveis planejados, ainda não concluídos:

- Registro das fontes, datas, tarifas, câmbio, condições e justificativas das hipóteses.
- Tabela de entradas e resultados reproduzíveis, com os identificadores dos cenários.
- Dois gráficos conforme a etapa Compartilhar, sem dashboard neste escopo.
- Relatório curto com pergunta, preparação, resultados, recomendações condicionais e limitações.
- Registro transparente do apoio de IA, distinguindo sua contribuição das decisões e conferências
  realizadas pelo estudante, conforme as orientações da atividade a confirmar.

Critérios para encerrar a análise futuramente:

- Os 13 cenários estão presentes, identificados e sem duplicidade de combinações.
- C05 permanece a referência de tokens, e as políticas usam a referência da mesma escala.
- Comparações e indicadores têm unidades, denominadores e sinais explicitados; divisões por zero
  são tratadas como não aplicáveis.
- Cálculos monetários preservam Decimal, com arredondamento somente na apresentação.
- Fontes, datas, hipóteses, cotação fixa e versão da ferramenta permitem reproduzir os resultados.
- Pelo menos um cálculo foi conferido manualmente e eventuais divergências foram esclarecidas.
- Conclusões distinguem estimativas, hipóteses e evidências reais, sem inferir qualidade pelo custo.
- Tabela, gráficos e relatório respondem à pergunta, respeitam os limites e registram o apoio de IA.

A matriz está documentada; isso não significa que esses critérios já tenham sido atendidos ou que
o estudo tenha sido aprovado pelo curso.

## 10. Próximo passo

1. Preparar os dados dos 13 cenários revisados e um registro das condições fixas da seção 5,
   incluindo fontes, datas, unidades e justificativas, sem alterar o CSV de exemplo ou o MVP.
2. Validar estrutura, identificadores e cobertura da matriz nos dados preparados, preservando
   Decimal nas condições e nos futuros cálculos monetários.
3. Somente então executar a análise e a conferência manual previstas, registrando divergências,
   antes de produzir gráficos, relatório ou recomendações.
4. Manter a v0.1.0 publicada como referência histórica, sem mover, substituir ou modificar sua tag.

**Concluído nesta etapa:** revalidação documental do modelo e das tarifas propostas e definição
da cotação histórica fixa, nos limites confirmados na seção 5. Acesso na conta, configuração de
raciocínio, consumo real e qualidade pedagógica não foram comprovados.

Esta atualização não prepara CSVs, não executa os 13 cenários, não produz resultados ou gráficos
e não altera o código do MVP. As próximas atividades continuam sendo etapas próprias do estudo.
