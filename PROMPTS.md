# Prompts relevantes — LiteArt Cost Analytics

Este arquivo reúne uma seleção dos prompts enviados pelo autor durante o desenvolvimento do projeto com apoio de IA. O objetivo é documentar os pedidos que orientaram o escopo, o aprendizado e as principais decisões técnicas, sem reproduzir toda a conversa.

Modelo registrado pelo autor para essas interações: **GPT-6.1 Sol, com esforço de raciocínio médio**. Essa informação descreve a ferramenta de apoio ao desenvolvimento, não o modelo da API que será considerado pela calculadora.

## Como ler este registro

- Os blocos de citação contêm palavras do autor, preservadas sem correções de escrita.
- O primeiro registro reúne trechos do pedido inicial, identificados separadamente. Os demais contêm o texto integral dos pedidos selecionados.
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
