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

- Utilizar um único modelo de referência. O MVP registra GPT-6 Luna (`gpt-6-luna`); identificador,
  disponibilidade, tarifas e condições deverão ser revalidados antes de executar a análise.
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

## 5. Dados necessários e proveniência

Antes da execução, organizar quatro tipos de informação, sem misturá-los:

- **Tarifas pesquisadas:** provedor, modelo e identificador confirmado, disponibilidade, preços de
  entrada e saída, moeda, unidade de cobrança, condições aplicáveis, URL oficial e data da consulta.
  Revalidação e valores a adotar: **pendentes**. As tarifas registradas na release são históricas
  e não serão consideradas automaticamente atuais.
- **Câmbio:** taxa em BRL por USD, fonte, data de referência e momento da consulta. Fonte e valor a
  fixar para este estudo: **pendentes de definição e registro**. Se a fonte escolhida for BCB/SGS
  série 1, registrar a data da observação separadamente do momento do acesso; não tratar a taxa
  diária como câmbio em tempo real ou como valor efetivo do pagamento.
- **Hipóteses:** campos e unidades da matriz, justificativas dos níveis escolhidos e natureza
  didática. A matriz está proposta; sua confirmação e o registro das justificativas são pendentes.
  Os valores servem para explorar alternativas, sem terem sido coletados de estudantes.
- **Resultados derivados:** feedbacks, tokens e custos calculados, com identificação do cenário,
  versão da ferramenta e vínculo às tarifas e à cotação utilizadas. Ainda não foram produzidos
  para este estudo.

A cotação será fixada para o estudo e reutilizada em todas as execuções, permitindo reproduzir os
resultados sem misturar variação cambial com mudanças de escala, política ou tokens. A opção manual
do MVP permitirá reaplicar a taxa documentada, sem consultar uma taxa diferente para cada cenário.

Datas da pesquisa, data de referência cambial e momento de consulta têm significados diferentes.
Não preencher informações ainda não pesquisadas com datas presumidas. Nenhum preço, fonte nova,
data de coleta ou resultado foi pesquisado ou inventado nesta etapa documental.

Na preparação futura, os 13 cenários deverão ser organizados em uma entrada própria do estudo,
preservando o CSV de exemplo do MVP. O identificador C01 a C13 deverá acompanhar cada nome e cada
resultado, permitindo associar entradas e saídas. Não criar ou alterar arquivos de dados nesta etapa.

O CSV de resultados da v0.1.0 contém nove colunas e não exporta modelo, tarifas, cotação, origem ou
data como metadados. Esses registros deverão acompanhar os resultados em um artefato do estudo,
sem presumir que já estão armazenados pelo programa ou modificar o formato histórico da release.

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
2. **Preparar:** revalidar modelo e tarifas, definir e documentar a cotação fixa e organizar as
   hipóteses e suas justificativas, sem tratar registros históricos como pesquisa atual.
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

1. Revisar e confirmar a matriz de 13 cenários e suas justificativas.
2. Depois, revalidar o modelo, disponibilidade, tarifas e condições e definir a cotação fixa.
3. Somente então preparar os dados e executar a análise e a conferência manual planejada.
4. Manter a v0.1.0 publicada como referência histórica, sem mover, substituir ou modificar sua tag.

Esta preparação não executa a análise, não pesquisa novos preços, não gera CSV ou gráficos e não
altera o código do MVP. As próximas etapas dependerão das definições e verificações acima.
