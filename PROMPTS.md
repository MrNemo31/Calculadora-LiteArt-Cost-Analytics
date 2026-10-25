# Prompts relevantes — LiteArt Cost Analytics

Este arquivo reúne uma seleção dos prompts enviados pelo autor durante o desenvolvimento do projeto com apoio de IA. O objetivo é documentar os pedidos que orientaram o escopo, o aprendizado e as principais decisões técnicas, sem reproduzir toda a conversa.

Modelo registrado pelo autor para essas interações: **GPT-6.1 Sol, com esforço de raciocínio médio**. Essa informação descreve a ferramenta de apoio ao desenvolvimento, não o modelo da API que será considerado pela calculadora.

## Como ler este registro

- Os blocos de citação contêm palavras do autor, preservadas sem correções de escrita.
- O registro 1 reúne trechos do pedido inicial. Os registros 2 a 5 contêm pedidos completos. Os registros 6 a 8 sintetizam pedidos relacionados, sem reproduzir literalmente cada mensagem.
- As descrições de objetivo e contribuição são notas de organização, não fazem parte dos prompts originais.
- As respostas da IA não estão reproduzidas. As decisões atuais estão no [README](README.md) e no [planejamento](PLANEJAMENTO.md), que devem prevalecer caso o projeto evolua.
- Novos registros serão incluídos quando ajudarem a entender uma decisão, um aprendizado ou uma mudança relevante no projeto.

## 1. Definição do projeto e da forma de aprendizado

**Etapa:** planejamento inicial.

**Objetivo do pedido:** apresentar a finalidade da ferramenta e estabelecer uma orientação técnica gradual.

**Trecho original — objetivo:**

> Desenvolver uma calculadora e, posteriormente, um dashboard interativo capaz de simular, analisar e visualizar os custos operacionais de uma aplicação de software, utilizando o LiteArt como estudo de caso.

**Trecho original — origem dos dados:**

> A calculadora deverá distinguir preços pesquisados, hipóteses de consumo e resultados estimados. Também quero registrar as fontes e datas dos preços utilizados.

**Trecho original — orientação e aprendizado:**

> **Quero que você atue como um orientador técnico, e não apenas como um gerador de código.**
>
> Sempre que introduzirmos um conceito novo, explique seu funcionamento, por que ele é necessário e como será aplicado no projeto.
>
> Evite gerar grandes quantidades de código de uma só vez. Prefiro implementar pequenas funcionalidades, testar, compreender os resultados e avançar gradualmente.
>
> Quando eu apresentar algum código, revise-o e explique possíveis erros, melhorias e alternativas, sem reescrever tudo desnecessariamente.

**Contribuição para o projeto:** definiu a finalidade da ferramenta, a separação entre preços, hipóteses e estimativas e o desenvolvimento por pequenas entregas compreendidas e verificadas.

## 2. Definição das entradas e organização inicial

**Etapa:** planejamento das entradas e da documentação.

**Objetivo do pedido:** entender os dados necessários antes da implementação e discutir o registro do trabalho.

**Prompt original completo:**

> Vamos começar a Etapa 1. Me ajude a listar as entradas necessárias, suas unidades e quais são preços pesquisados ou hipóteses de consumo, explicando cada item antes de escrevermos código. Eu pensei de fazer já uma pasta para deixar os arquivos e já subir no GitHub para ficar salvo, mas já eu deixo público? Outra coisa, por eu estar utilizado IA, eu pensei de criar o arquivo PROMPT.md para deixar os prompts que eu te mandei para fazer o projeto, o que acha? Já que a primeira versão será para apenas uma IA, eu pensei de usar as APIs do ChatGPT mesmo.

**Contribuição para o projeto:** orientou a definição das entradas, unidades e classificações; propôs documentar o apoio de IA e usar inicialmente um modelo da API da OpenAI. O arquivo de registros recebeu posteriormente o nome `PROMPTS.md`.

## 3. Feedback opcional nos acertos

**Etapa:** definição da regra de negócio.

**Objetivo do pedido:** considerar uma opção de feedback nos acertos para reduzir o consumo de IA.

**Prompt original completo:**

> Eu acho que eu vou fazer da seguinte maneira, o que pode tornar mais complicado essa calculadora mas diminui o custo. Eu pensei de deixar uma opção de toggle se o usuário vai querer o feeedback caso acerte a respostas, pois o que eu vi pela a pequena pesquisa que eu fiz, não a oficial completa, os usuários preferem o feedback quando erram.

**Contribuição para o projeto:** motivou a regra de feedback nos erros e feedback opcional nos acertos, considerando a escolha antes da chamada à API. A preferência relatada permanece uma hipótese de produto a validar. Para a simulação, foram acrescentadas taxa de acerto e parcela dos acertos que recebe feedback.

## 4. Comparação futura de outros modelos de IA

**Etapa:** revisão do README e definição de evoluções futuras.

**Objetivo do pedido:** ampliar a visão do projeto para incluir a seleção de outras opções de IA.

**Prompt original completo:**

> Pode fazer esses dois ajustes no README.md. No fim fala que utilizaremos APIs da OpenIA, mas eu tembém pensei de colocar uma opção de você poder selecionar APIs de outros modelos de IA, tipo o Claude, Qwen, Gemini e outros.

**Contribuição para o projeto:** incluiu a comparação de outros modelos como evolução futura. A primeira versão permaneceu limitada a um modelo da OpenAI. Os dois ajustes mencionados no pedido eram separar Pandas de CSV na tabela e esclarecer que a etapa final trata da publicação da aplicação.

## 5. Alinhamento entre planejamento e apresentação

**Etapa:** revisão da documentação.

**Objetivo do pedido:** conferir a consistência entre o escopo apresentado no README e as regras detalhadas no planejamento.

**Prompt original completo:**

> Agora vamos revisar o PLANEJAMENTO.md juntos. Me explique cada parte e ajuste o que for necessário para ficar alinhado com o README, incluindo a comparação futura de outros modelos de IA.

**Contribuição para o projeto:** explicitou a separação entre provedor e modelo e os cuidados previstos para comparar custos: fontes oficiais, unidades compatíveis, mesma tarefa pedagógica e hipóteses de consumo declaradas para cada modelo.

## 6. Cenário didático, escolha do modelo e consumo de tokens

**Etapa:** conclusão das premissas iniciais e preparação da calculadora.

**Objetivo dos pedidos:** definir um cenário de aprendizado, pesquisar preços oficiais e entender a diferença entre hipóteses de tokens e contagens medidas.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Adotar o cenário de 100 usuários, 40 respostas por usuário, 60% de acerto e feedback em 25% dos acertos. Pesquisar os preços oficiais dos modelos da OpenAI, inicialmente considerando Terra, e usar Luna como referência após a comparação. Preparar um exemplo de feedback curto que explique o que a questão pede e mostre a resolução correta. Manter 500 tokens de entrada e 300 de saída como hipóteses didáticas e esclarecer como uma contagem medida difere de uma estimativa.

**Contribuição para o projeto:** definiu o cenário de 2.200 feedbacks mensais, a referência GPT-6 Luna e as hipóteses de consumo. Preços e fontes foram registrados no planejamento; não foram feitas chamadas à API para medir os tokens.

## 7. Implementação gradual dos cálculos mensais e anuais

**Etapa:** calculadora básica com Python puro.

**Objetivo dos pedidos:** implementar pequenas partes, revisar o código escrito pelo autor e compreender cada fórmula antes de avançar.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar `calculadora.py` e explicar as variáveis, operações e resultados. Revisar os cálculos de tokens mensais implementados pelo autor, corrigindo a base de respostas para feedbacks e deixando a divisão por um milhão para o cálculo dos custos. Acrescentar as tarifas do Luna, explicar o uso de `Decimal`, conferir a conversão com cotação didática de R$ 5,00 por dólar e apresentar os símbolos monetários. Revisar a projeção anual em dólares e reais, mantendo preços, consumo e câmbio constantes.

**Contribuição para o projeto:** o autor corrigiu os cálculos de tokens e acrescentou a conversão cambial e a projeção anual. A revisão com apoio de IA ajudou a conferir as fórmulas, adicionar os custos de IA e explicar os conceitos. O cenário resultou em US$ 0,44 ou R$ 2,20 por mês e US$ 5,28 ou R$ 26,40 por ano, apenas para IA e sob as hipóteses registradas.

## 8. Organização dos cálculos em funções

**Etapa:** refatoração da calculadora básica.

**Objetivo dos pedidos:** tornar os cálculos reutilizáveis, entendendo parâmetros, retorno de valores e organização das responsabilidades.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Avaliar a criação de funções após o cálculo anual. Explicar uma primeira função de projeção anual e revisar as funções de conversão para reais e de tokens implementadas pelo autor. Acrescentar as funções restantes para respostas, feedbacks e custo de tokens, explicando cada uma e preservando os resultados. Atualizar a documentação para registrar esse marco antes de iniciar a validação das entradas.

**Contribuição para o projeto:** os cálculos foram organizados em seis funções: `calcular_respostas_mensais`, `calcular_feedbacks_mensais`, `calcular_tokens_mensais`, `calcular_custo_tokens`, `calcular_real` e `calcular_custo_anual`. A cotação foi centralizada em uma variável e os resultados permaneceram separados dos `print()`. O nome inicial da função de tokens era `calcular_tokens_por_feedback`; o autor passou a usar `calcular_tokens_mensais` para expressar melhor os totais devolvidos.

O cenário didático e casos com consumo zero e feedback em 0% ou 100% dos acertos foram conferidos durante a refatoração. As funções ainda pressupõem entradas válidas: a validação será o próximo incremento.

**Marco deste registro:** documentação atualizada em 2026-10-25, até os cálculos anuais e a organização em funções.
