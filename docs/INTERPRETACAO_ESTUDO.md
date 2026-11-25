# Interpretação do estudo de custos de IA do LiteArt

**Data da interpretação e conferência:** 25/11/2026.

**Situação:** síntese analítica para preparar o relatório final. As recomendações são propostas
condicionais, sem decisões aprovadas atribuídas ao responsável pelo projeto. Este documento não
declara o estudo concluído, aprovado pelo curso ou validado pelo Google.

## 1. Resposta à pergunta principal

Sob as hipóteses deste estudo, o custo mensal estimado de IA aumenta proporcionalmente ao número
de usuários quando as demais entradas permanecem constantes. Oferecer feedback em menos acertos
reduz a quantidade de chamadas e o custo. Alterar os tokens por feedback modifica o custo segundo
a participação de entrada e saída na cobrança: em C05, a saída tem maior peso financeiro.

O recorte utiliza um único modelo: OpenAI, API direta, `gpt-6-luna`, Standard para texto e contexto
curto. As tarifas históricas são **USD 0.10 por milhão de tokens de entrada sem cache** e
**USD 0.50 por milhão de tokens de saída faturáveis**. A cotação fixa é **5.8102 BRL por USD**,
BCB/SGS série 1, dólar de venda diário. Pesquisa de preços, referência e consulta cambial são de
**18/11/2026**, conforme [ESTUDO_DE_CASO.md](ESTUDO_DE_CASO.md) e
[condicoes_fixas.csv](../dados/estudo_de_caso/condicoes_fixas.csv). Não houve nova consulta às fontes.

Os [13 cenários de entrada](../dados/estudo_de_caso/cenarios.csv) são hipotéticos. Todos consideram
40 respostas por usuário/mês, taxa de acerto de 60% e feedback em todos os erros. C01 a C09 usam
500 tokens de entrada e 300 de saída por feedback; C10 a C13 variam um desses consumos contra C05.
Há uma chamada por feedback, sem novas tentativas, e o mesmo consumo por feedback de acerto e erro.

Assim, os resultados ajudam a comparar alternativas e planejar medições. **Não são uma previsão
validada do uso do LiteArt**, uma despesa observada ou o custo operacional completo da aplicação.
Menor custo não demonstra melhor aprendizagem nem qualidade pedagógica equivalente.

## 2. Comparação das políticas de feedback

As seis comparações de `resultados/estudo_de_caso/comparacao_politicas.csv` mantêm a escala e as
demais hipóteses iguais. A referência oferece feedback em todas as respostas: **C03 para 100
usuários, C06 para 500 e C09 para 1.000**.

| Política e cenário | Usuários | Referência | Custo mensal da política (BRL) | Custo mensal da referência (BRL) | Redução mensal (BRL) | Redução |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| Somente erros — C01 | 100 | C03 | 1,86 | 4,65 | 2,79 | 60% |
| Erros + 25% dos acertos — C02 | 100 | C03 | 2,56 | 4,65 | 2,09 | 45% |
| Somente erros — C04 | 500 | C06 | 9,30 | 23,24 | 13,94 | 60% |
| Erros + 25% dos acertos — C05 | 500 | C06 | 12,78 | 23,24 | 10,46 | 45% |
| Somente erros — C07 | 1000 | C09 | 18,59 | 46,48 | 27,89 | 60% |
| Erros + 25% dos acertos — C08 | 1000 | C09 | 25,56 | 46,48 | 20,92 | 45% |

Os valores monetários da tabela foram arredondados somente para apresentação. A redução é
`custo_referencia - custo_politica`; o percentual divide essa diferença pelo custo da **referência
na mesma escala**, multiplicando por 100. Não se usa o custo da política como denominador.

Por exemplo, com 500 usuários, C06 custa **USD 4.00 / BRL 23.2408000 por mês**, enquanto C05 custa
**USD 2.20 / BRL 12.7824400**. Usando os valores completos, a diferença é **BRL 10.4583600**, e
`10.4583600 / 23.2408000 × 100 = 45%`. No terminal, esses valores aparecem como R$ 23,24,
R$ 12,78 e R$ 10,46. A redução não deve ser reconstruída dos valores já arredondados.

A explicação está na proporção de respostas que recebe feedback. Com 60% de acerto, os erros são
40% das respostas. Oferecer feedback somente nos erros atende 40%, reduzindo 60% das chamadas
contra todas as respostas. Acrescentar feedback em 25% dos acertos adiciona `0.25 × 0.60 = 0.15`
das respostas: `0.40 + 0.15 = 0.55`. Permanecem 55% das chamadas, com redução de 45%.

Essa relação também se aplica ao custo porque se supõem tokens iguais por feedback, sem cobrança
adicional por chamada. Se a taxa de acerto, o consumo por tipo de feedback, as tentativas ou os
preços mudarem, os percentuais de custo precisam ser revistos. **Não se generalizam 60% e 45% para
outras taxas de acerto nem para custos que incluam infraestrutura.**

## 3. Sensibilidade dos tokens em relação a C05

Em C05, os 500 usuários geram 11.000 feedbacks/mês. Os custos mensais dos componentes são
**USD 0.55 de entrada** e **USD 1.65 de saída**, totalizando **USD 2.20 / BRL 12.7824400**.
Portanto, a entrada representa **25%** e a saída, **75%** do custo desse cenário.

Fonte dos componentes: `resultados/estudo_de_caso/resultados_cenarios.csv` e
`resultados/estudo_de_caso/indicadores_cenarios.csv`. A saída pesa mais em C05 porque sua tarifa é
cinco vezes a de entrada: 300 tokens de saída por feedback custam mais que 500 de entrada.
Isso descreve a cobrança adotada, sem demonstrar que a saída é desnecessária ou de menor utilidade.

As quatro linhas de `resultados/estudo_de_caso/sensibilidade_tokens.csv` mantêm a quantidade de
feedbacks e alteram somente o consumo indicado:

| Cenário | Alteração por feedback contra C05 | Variação dos tokens alterados | IA mensal (BRL, seis casas) | Diferença mensal contra C05 (BRL) | Variação do custo de IA |
| --- | --- | ---: | ---: | ---: | ---: |
| C10 | Entrada: 500 → 250; saída permanece 300 | -50% | 11,184635 | -1,597805 | -12,5% |
| C11 | Entrada: 500 → 1000; saída permanece 300 | +100% | 15,978050 | +3,195610 | +25% |
| C12 | Saída: 300 → 150; entrada permanece 500 | -50% | 7,989025 | -4,793415 | -37,5% |
| C13 | Saída: 300 → 600; entrada permanece 500 | +100% | 22,369270 | +9,586830 | +75% |

Aqui a diferença é `custo_cenario - custo_C05`, e o percentual usa **C05 como denominador**.
Negativo indica redução; positivo, aumento. O sentido da subtração é diferente da redução das
políticas apresentada na seção 2.

Reduzir a entrada pela metade não reduz o custo total pela metade: em C10, o efeito é metade dos
25% que a entrada representa em C05, ou 12,5%. Reduzir a saída pela metade em C12 afeta metade
dos 75%, ou 37,5%. Dobrar cada componente produz os aumentos de 25% e 75%, respectivamente.

**A saída não representa 75% em todos os cenários.** Pelos indicadores, ela representa 60% em C11
e C12 e aproximadamente 85,71% em C10 e C13. Alterar um componente modifica também a composição
do total. As participações foram calculadas em USD, com numerador e denominador na mesma moeda.

Esses consumos são hipóteses exploratórias, sem comprovação de qualidade equivalente. Os valores
simulados não são limites garantidos de geração nem intervalos estatísticos de confiança.

## 4. Escala e custo mensal de IA por usuário ativo

Para avaliar escala, é necessário manter a política e todas as demais hipóteses constantes.
Os grupos comparáveis são C01/C04/C07, C02/C05/C08 e C03/C06/C09. Os custos mensais e unitários
abaixo vêm de `resultados_cenarios.csv` e `indicadores_cenarios.csv`, na pasta de resultados do estudo.

| Política e cenários | Mensal com 100 usuários (BRL) | Mensal com 500 usuários (BRL) | Mensal com 1000 usuários (BRL) | USD/usuário ativo/mês | BRL/usuário ativo/mês |
| --- | ---: | ---: | ---: | ---: | ---: |
| Somente erros — C01/C04/C07 | 1,859264 | 9,296320 | 18,592640 | 0,00320000 | 0,01859264 |
| Erros + 25% dos acertos — C02/C05/C08 | 2,556488 | 12,782440 | 25,564880 | 0,00440000 | 0,02556488 |
| Todas as respostas — C03/C06/C09 | 4,648160 | 23,240800 | 46,481600 | 0,00800000 | 0,04648160 |

De 100 para 500 usuários, o custo mensal é multiplicado por cinco; de 500 para 1000, por dois.
O custo por usuário permanece constante dentro de cada política. Por exemplo, C02, C05 e C08
resultam em **USD 0.0044 / BRL 0.02556488 por usuário ativo/mês**.

O denominador é a quantidade de usuários ativos, não o número de feedbacks. A proporcionalidade
é esperada porque cada usuário mantém a mesma quantidade de respostas, taxa de acerto, política,
tokens e preços. Não há desconto por volume nem custo fixo de IA distribuído entre mais usuários
nesse modelo. **Custo unitário constante não é evidência de economia de escala.**

Comparar, por exemplo, C02 com C06 mudaria escala e política ao mesmo tempo; a diferença não
poderia ser atribuída exclusivamente ao número de usuários. Os níveis de 100, 500 e 1000 usuários
também não representam meses sucessivos ou uma previsão de crescimento temporal.

Se o total mensal de IA fosse zero, as participações seriam não aplicáveis; com usuários positivos,
o custo unitário zero continuaria válido. Se usuários fossem zero, os custos por usuário seriam
não aplicáveis. A rotina exporta esses casos como campos vazios, sem confundi-los com zero.
Nos 13 registros conferidos, todos esses denominadores são positivos.

## 5. Recomendações condicionais

As propostas abaixo apoiam um piloto e a revisão das hipóteses; não constituem decisões aprovadas,
metas de qualidade ou um orçamento máximo definido para o LiteArt.

### 5.1. Avaliar feedback somente nos erros como alternativa de menor custo

- **Evidência:** C01, C04 e C07 têm custo 60% menor que suas referências. São a política de menor
  custo entre as três políticas principais, com a mesma escala e 500/300 tokens por feedback.
- **Ação proposta:** incluir essa política entre as alternativas a avaliar antes de escolher
  um comportamento padrão de feedback.
- **Condição:** menor custo não define a melhor política pedagógica. É necessário verificar se
  deixar acertos sem feedback compromete explicações úteis ou a experiência de aprendizagem.
- **Dado a medir:** utilidade do feedback em acertos e erros, necessidades de explicação e
  evidências de compreensão dos estudantes em uma avaliação de piloto a definir.

### 5.2. Avaliar feedback opcional nos acertos com uso efetivo medido

- **Evidência:** C05 conserva redução de 45% contra C06. Em relação a C04, passa de 8000 para
  11000 feedbacks/mês e de BRL 9.2963200 para BRL 12.7824400: mais 3000 feedbacks e BRL 3.4861200.
- **Ação proposta:** avaliar a opção de solicitar feedback também nos acertos, considerando
  adesão e utilidade antes de manter uma proporção como 0.25 nas estimativas.
- **Condição:** 25% dos acertos com feedback não significa 25% dos usuários com o toggle ativado.
  Usuários podem responder volumes diferentes ou mudar a opção durante o uso.
- **Dado a medir:** acertos efetivamente acompanhados de feedback, oportunidades elegíveis,
  estado do toggle por interação e avaliação de utilidade dos feedbacks solicitados.

### 5.3. Medir tokens faturáveis antes de definir limites de geração

- **Evidência:** C05 distribui o custo em 25% de entrada e 75% de saída, e as quatro variações
  mostram efeitos diferentes sobre o total. As hipóteses não provêm de contagens reais.
- **Ação proposta:** registrar tokens por chamada e por tipo de feedback em um piloto antes de
  escolher limites ou substituir as estimativas de 500/300 tokens.
- **Condição:** medir entrada completa e saída faturável, incluindo componentes não visíveis
  quando existirem, sem contar os mesmos tokens duas vezes. Limites precisam ser avaliados com
  a configuração do modelo e com a qualidade do conteúdo.
- **Dado a medir:** tokens de entrada, saída faturável, parcela visível quando identificável,
  feedback de acerto/erro, configuração utilizada e ocorrências de resposta incompleta.

### 5.4. Avaliar clareza e concisão junto da qualidade dos feedbacks

- **Evidência:** C12 reduz a saída hipotética de 300 para 150 tokens e o custo em 37,5%; C13 dobra
  a saída e eleva o custo em 75%. O estudo não mede a qualidade desses textos.
- **Ação proposta:** revisar se o feedback pode ser mais claro e conciso sem perder explicação
  necessária, comparando exemplos por critérios pedagógicos antes de adotar uma mudança.
- **Condição:** não cortar conteúdo apenas para reduzir custo nem presumir que 150 tokens são
  suficientes. Mais tokens tampouco comprovam melhor explicação.
- **Dado a medir:** correção, clareza, utilidade, omissões importantes, compreensão e tokens
  faturáveis das versões avaliadas, sem inventar uma meta de aprovação.

### 5.5. Dimensionar orçamento com hipóteses explícitas e revisá-las após o piloto

- **Evidência:** sob a política intermediária, C02/C05/C08 variam de BRL 2.5564880 a BRL 25.5648800
  mensais conforme a escala; os custos unitários permanecem iguais pelas hipóteses constantes.
- **Ação proposta:** usar os cenários como referências condicionais para planejar a parcela de IA,
  identificando escala, consumo, política, preços e câmbio; revisar essas entradas após medições.
- **Condição:** não somar alternativas de cenário, transformar escala em previsão temporal ou
  tratar estes valores como custo operacional completo. Não há orçamento máximo aprovado aqui.
- **Dado a medir:** usuários ativos e respostas por mês, distribuição de uso, taxas de feedback,
  tokens reais, falhas, novas tentativas e despesas adicionais fora deste recorte.

## 6. Plano de medição futura

Um piloto deverá permitir comparar as hipóteses com o uso real. A proposta de coleta é:

| Dimensão | Dado a registrar | Pergunta que ajuda a responder |
| --- | --- | --- |
| Uso mensal | Usuários ativos distintos, respostas por usuário e distribuição do volume | A escala e a média de 40 respostas representam o uso? |
| Acertos e política | Respostas corretas/incorretas, acertos com feedback e total de acertos elegíveis | A taxa de 60% e a proporção de feedback nos acertos são adequadas? |
| Toggle | Configuração da opção e ocorrência efetiva de feedback por interação | A opção ligada se traduz em qual parcela dos acertos com feedback? |
| Consumo faturável | Tokens por chamada, separados por entrada/saída e feedback de acerto/erro | As médias são diferentes entre tipos de feedback? |
| Operação | Chamadas, falhas, novas tentativas e geração duplicada | Uma chamada por feedback representa o consumo e a cobrança? |
| Condições | Modelo/configuração, preços aplicáveis, referência cambial e unidades | A simulação pode ser reproduzida e reconciliada com a cobrança? |
| Qualidade | Avaliação da correção, clareza e utilidade pedagógica, com critérios a definir | A redução de consumo preserva explicações necessárias? |

A taxa de acerto deverá relacionar acertos ao total de respostas do mesmo recorte. A proporção de
acertos com feedback deverá usar como denominador os acertos elegíveis do período. O percentual
de usuários com toggle ligado é outro indicador e não pode substituir essa proporção.

O piloto poderá mostrar consumo diferente entre feedbacks de acerto e erro. Nesse caso, usar uma
média única por feedback deverá ser reavaliado, em vez de conservar a simplificação por conveniência.
Falhas e novas tentativas também podem gerar consumo ou cobrança, que precisarão ser conferidos.

A avaliação de qualidade deverá combinar revisão de conteúdo e evidência de utilidade para os
estudantes. Correção textual e satisfação não comprovam, sozinhas, ganho de aprendizagem.
Se for proposta uma comparação de resultados educacionais, seu desenho deverá ser definido antes
da coleta. Não há participantes observados, tamanho de amostra suficiente ou resultados de piloto
estabelecidos neste documento. Nenhuma coleta, chamada de API ou experimento foi implementado.

## 7. Limitações, proveniência e próximos passos

Não há dados reais de utilização nem medição de aprendizagem. As diferenças são determinadas
pelas entradas e fórmulas; não justificam testes de significância ou conclusões sobre estudantes.
Os tokens são hipóteses e a saída visível pode ser menor que a saída faturável. Não foi testada
uma configuração de raciocínio ou comprovado acesso ao modelo pela conta responsável.

Tarifas e câmbio são históricos, não valores permanentemente atuais ou garantia do câmbio de um
pagamento. Ficam excluídos infraestrutura, demais despesas operacionais, tributos, adicionais do
meio de pagamento, ferramentas, cache e outras modalidades de cobrança. O estudo não compara
qualidade entre modelos e não demonstra viabilidade financeira. O anual exportado pressupõe
12 meses constantes, sem crescimento, sazonalidade ou mudança tarifária/cambial.

### Proveniência e conferência realizada

As definições, fontes históricas, unidades e limites estão em
[ESTUDO_DE_CASO.md](ESTUDO_DE_CASO.md). Foram utilizados:

| Arquivo | Conteúdo utilizado nesta síntese |
| --- | --- |
| [dados/estudo_de_caso/cenarios.csv](../dados/estudo_de_caso/cenarios.csv) | 13 combinações hipotéticas e seus identificadores |
| [dados/estudo_de_caso/condicoes_fixas.csv](../dados/estudo_de_caso/condicoes_fixas.csv) | Uma configuração histórica compartilhada, fontes e datas |
| `resultados/estudo_de_caso/resultados_cenarios.csv` | 13 registros de hipóteses, consumo, custos e condições |
| `resultados/estudo_de_caso/comparacao_politicas.csv` | Seis comparações com C03, C06 ou C09 |
| `resultados/estudo_de_caso/sensibilidade_tokens.csv` | Quatro variações contra C05 |
| `resultados/estudo_de_caso/indicadores_cenarios.csv` | 13 registros de participações e custos por usuário |

Em 25/11/2026, os seis CSVs foram lidos como texto; valores financeiros e hipóteses numéricas foram
conferidos diretamente com Decimal, sem float intermediário. Uma conferência independente das
fórmulas comparou os 13 consumos/custos às entradas, as seis reduções, as quatro sensibilidades e
os 13 indicadores. Foram conferidos identificadores, contagens, condições, unidades, denominadores
e sinais. **Não foram encontradas divergências nos arquivos utilizados.**

A conferência usou os valores completos e contexto Decimal com precisão de 28 dígitos, coerente
com os resultados gerados; dízimas não têm precisão matemática infinita. Nas tabelas deste
documento, valores mensais usam duas ou seis casas e valores unitários usam oito, somente na
apresentação. Não houve nova execução da rotina de análise, testes de código, consulta externa ou
alteração das entradas e resultados. A conferência aritmética não é uma validação empírica.

Os resultados são reproduzíveis por `analise_estudo.py`, mas a pasta `resultados/` está ignorada
pelo Git. Portanto, os quatro CSVs e os HTMLs não devem ser presumidos disponíveis no GitHub.
Na raiz de uma cópia preparada conforme o [README](../README.md), os comandos podem gerá-los;
eles são instruções de reprodução e não foram executados nesta tarefa:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B analise_estudo.py
& '.\.venv-win\Scripts\python.exe' -X utf8 -B graficos_estudo.py
```

A referência histórica do MVP permanece a v0.1.0 publicada; a interpretação usa os arquivos
produzidos pela rotina separada do estudo, sem alterar essa versão ou sua tag.

### Próximo passo

Elaborar o relatório final com a pergunta principal, os dois gráficos existentes, esta síntese,
as recomendações condicionais e as limitações. Os gráficos previstos para composição são
`resultados/estudo_de_caso/custo_mensal_por_escala_politica.html` e
`resultados/estudo_de_caso/sensibilidade_tokens.html`; nenhum novo gráfico foi gerado aqui.

O relatório deverá distinguir o que foi calculado, o que se propõe avaliar no piloto e o que ainda
depende de observação real. As orientações da atividade do curso, inclusive a transparência sobre
apoio de IA, deverão ser conferidas antes da entrega. Esta síntese não é o relatório final nem
uma declaração de conclusão ou aprovação do estudo.
