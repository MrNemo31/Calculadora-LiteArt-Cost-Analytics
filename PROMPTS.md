# Prompts relevantes — LiteArt Cost Analytics

Este arquivo reúne uma seleção dos prompts que orientaram o desenvolvimento do projeto
com apoio de IA. O objetivo é documentar os pedidos que orientaram o escopo, o aprendizado e as
principais decisões técnicas, sem reproduzir toda a conversa.

Modelo utilizado nessas interações: **GPT-6.1 Sol, com esforço de raciocínio
médio**. Essa informação descreve a ferramenta de apoio ao desenvolvimento, não o modelo da API que
será considerado pela calculadora.

## Como ler este registro

- Os blocos de citação reproduzem os pedidos originais, preservados sem correções de escrita.
- O registro 1 reúne trechos do pedido inicial. Os registros 2 a 5 contêm pedidos completos. Os
  registros a partir do 6 sintetizam pedidos relacionados, sem reproduzir literalmente cada
  mensagem.
- As descrições de objetivo e contribuição são notas de organização, não fazem parte dos prompts
  originais.
- As respostas da IA não estão reproduzidas. As decisões atuais estão no [README](README.md) e no
  [planejamento](PLANEJAMENTO.md) , que devem prevalecer caso o projeto evolua.
- Novos registros serão incluídos quando ajudarem a entender uma decisão, um aprendizado ou uma
  mudança relevante no projeto.

## 1. Definição do projeto e da forma de aprendizado

**Etapa:** planejamento inicial.

**Objetivo do pedido:** apresentar a finalidade da ferramenta e estabelecer uma orientação técnica
gradual.

**Trecho original — objetivo:**

> Desenvolver uma calculadora e, posteriormente, um dashboard interativo capaz de simular, analisar
> e visualizar os custos operacionais de uma aplicação de software, utilizando o LiteArt como estudo
> de caso.

**Trecho original — origem dos dados:**

> A calculadora deverá distinguir preços pesquisados, hipóteses de consumo e resultados estimados.
> Também quero registrar as fontes e datas dos preços utilizados.

**Trecho original — orientação e aprendizado:**

> **Quero que você atue como um orientador técnico, e não apenas como um gerador de código.**
>
> Sempre que introduzirmos um conceito novo, explique seu funcionamento, por que ele é necessário e
> como será aplicado no projeto.
>
> Evite gerar grandes quantidades de código de uma só vez. Prefiro implementar pequenas
> funcionalidades, testar, compreender os resultados e avançar gradualmente.
>
> Quando eu apresentar algum código, revise-o e explique possíveis erros, melhorias e alternativas,
> sem reescrever tudo desnecessariamente.

**Contribuição para o projeto:** definiu a finalidade da ferramenta, a separação entre preços,
hipóteses e estimativas e o desenvolvimento por pequenas entregas compreendidas e verificadas.

## 2. Definição das entradas e organização inicial

**Etapa:** planejamento das entradas e da documentação.

**Objetivo do pedido:** entender os dados necessários antes da implementação e discutir o registro
do trabalho.

**Prompt original completo:**

> Vamos começar a Etapa 1. Me ajude a listar as entradas necessárias, suas unidades e quais são
> preços pesquisados ou hipóteses de consumo, explicando cada item antes de escrevermos código. Eu
> pensei de fazer já uma pasta para deixar os arquivos e já subir no GitHub para ficar salvo, mas já
> eu deixo público? Outra coisa, por eu estar utilizado IA, eu pensei de criar o arquivo PROMPT.md
> para deixar os prompts que eu te mandei para fazer o projeto, o que acha? Já que a primeira versão
> será para apenas uma IA, eu pensei de usar as APIs do ChatGPT mesmo.

**Contribuição para o projeto:** orientou a definição das entradas, unidades e classificações;
propôs documentar o apoio de IA e usar inicialmente um modelo da API da OpenAI. O arquivo de
registros recebeu posteriormente o nome `PROMPTS.md` .

## 3. Feedback opcional nos acertos

**Etapa:** definição da regra de negócio.

**Objetivo do pedido:** considerar uma opção de feedback nos acertos para reduzir o consumo de IA.

**Prompt original completo:**

> Eu acho que eu vou fazer da seguinte maneira, o que pode tornar mais complicado essa calculadora
> mas diminui o custo. Eu pensei de deixar uma opção de toggle se o usuário vai querer o feeedback
> caso acerte a respostas, pois o que eu vi pela a pequena pesquisa que eu fiz, não a oficial
> completa, os usuários preferem o feedback quando erram.

**Contribuição para o projeto:** motivou a regra de feedback nos erros e feedback opcional nos
acertos, considerando a escolha antes da chamada à API. A preferência relatada permanece uma
hipótese de produto a validar. Para a simulação, foram acrescentadas taxa de acerto e parcela dos
acertos que recebe feedback.

## 4. Comparação futura de outros modelos de IA

**Etapa:** revisão do README e definição de evoluções futuras.

**Objetivo do pedido:** ampliar a visão do projeto para incluir a seleção de outras opções de IA.

**Prompt original completo:**

> Pode fazer esses dois ajustes no README.md. No fim fala que utilizaremos APIs da OpenIA, mas eu
> tembém pensei de colocar uma opção de você poder selecionar APIs de outros modelos de IA, tipo o
> Claude, Qwen, Gemini e outros.

**Contribuição para o projeto:** incluiu a comparação de outros modelos como evolução futura. A
primeira versão permaneceu limitada a um modelo da OpenAI. Os dois ajustes mencionados no pedido
eram separar Pandas de CSV na tabela e esclarecer que a etapa final trata da publicação da
aplicação.

## 5. Alinhamento entre planejamento e apresentação

**Etapa:** revisão da documentação.

**Objetivo do pedido:** conferir a consistência entre o escopo apresentado no README e as regras
detalhadas no planejamento.

**Prompt original completo:**

> Agora vamos revisar o PLANEJAMENTO.md juntos. Me explique cada parte e ajuste o que for necessário
> para ficar alinhado com o README, incluindo a comparação futura de outros modelos de IA.

**Contribuição para o projeto:** explicitou a separação entre provedor e modelo e os cuidados
previstos para comparar custos: fontes oficiais, unidades compatíveis, mesma tarefa pedagógica e
hipóteses de consumo declaradas para cada modelo.

## 6. Cenário didático, escolha do modelo e consumo de tokens

**Etapa:** conclusão das premissas iniciais e preparação da calculadora.

**Objetivo dos pedidos:** definir um cenário de aprendizado, pesquisar preços oficiais e entender a
diferença entre hipóteses de tokens e contagens medidas.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Adotar o cenário de 100 usuários, 40 respostas por usuário, 60% de acerto e feedback em 25% dos
acertos. Pesquisar os preços oficiais dos modelos da OpenAI, inicialmente considerando Terra, e usar
Luna como referência após a comparação. Preparar um exemplo de feedback curto que explique o que a
questão pede e mostre a resolução correta. Manter 500 tokens de entrada e 300 de saída como
hipóteses didáticas e esclarecer como uma contagem medida difere de uma estimativa.

**Contribuição para o projeto:** definiu o cenário de 2.200 feedbacks mensais, a referência GPT-6
Luna e as hipóteses de consumo. Preços e fontes foram registrados no planejamento; não foram feitas
chamadas à API para medir os tokens.

## 7. Implementação gradual dos cálculos mensais e anuais

**Etapa:** calculadora básica com Python puro.

**Objetivo dos pedidos:** implementar pequenas partes, revisar o código em desenvolvimento e
compreender cada fórmula antes de avançar.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar `calculadora.py` e explicar as variáveis, operações e resultados. Revisar os cálculos de
tokens mensais já implementados, corrigindo a base de respostas para feedbacks e deixando a
divisão por um milhão para o cálculo dos custos. Acrescentar as tarifas do Luna, explicar o uso de
`Decimal` , conferir a conversão com cotação didática de R$ 5,00 por dólar e apresentar os símbolos
monetários. Revisar a projeção anual em dólares e reais, mantendo preços, consumo e câmbio
constantes.

**Contribuição para o projeto:** os cálculos de tokens foram corrigidos, e a conversão cambial e a
projeção anual foram acrescentadas. A revisão com apoio de IA ajudou a conferir as fórmulas,
adicionar os custos de IA e explicar os conceitos. O cenário resultou em US$ 0,44 ou R$ 2,20 por
mês e US$ 5,28 ou R$ 26,40 por ano, apenas para IA e sob as hipóteses registradas.

## 8. Organização dos cálculos em funções

**Etapa:** refatoração da calculadora básica.

**Objetivo dos pedidos:** tornar os cálculos reutilizáveis, entendendo parâmetros, retorno de
valores e organização das responsabilidades.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Avaliar a criação de funções após o cálculo anual. Explicar uma primeira função de projeção anual e
revisar as funções de conversão para reais e de tokens já implementadas. Acrescentar as
funções restantes para respostas, feedbacks e custo de tokens, explicando cada uma e preservando os
resultados. Atualizar a documentação para registrar esse marco antes de iniciar a validação das
entradas.

**Contribuição para o projeto:** os cálculos foram organizados em seis funções:
`calcular_respostas_mensais` , `calcular_feedbacks_mensais` , `calcular_tokens_mensais` ,
`calcular_custo_tokens` , `calcular_real` e `calcular_custo_anual` . A cotação foi centralizada em
uma variável e os resultados permaneceram separados dos `print()` . O nome inicial da função de
tokens era `calcular_tokens_por_feedback` ; passou a ser `calcular_tokens_mensais` para
expressar melhor os totais devolvidos.

O cenário didático e casos com consumo zero e feedback em 0% ou 100% dos acertos foram conferidos
durante a refatoração. Naquele marco, as funções ainda pressupunham entradas válidas; a
implementação das validações está registrada na seção 9.

**Marco anterior:** cálculos anuais e organização em funções, registrado em 2026-10-25.

## 9. Validação das entradas da calculadora

**Etapa:** validação dos argumentos das seis funções da calculadora básica.

**Objetivo dos pedidos:** impedir cálculos com tipos inadequados e valores incompatíveis com o
cenário, aprendendo cada regra por pequenas alterações e testes.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Antes de alterar o código, explicar quais entradas devem ser validadas e por quê. Começar em
`calcular_respostas_mensais` , recusando negativos, depois textos e usuários fracionários, e então
infinito e NaN. Explicar o funcionamento de `if` , `raise` , `TypeError` , `ValueError` e da
verificação de valores finitos. Validar em seguida as taxas entre 0 e 1 e os tipos de
`calcular_feedbacks_mensais` , incluindo respostas mensais. Proteger também esse volume contra
negativos e valores não finitos. Aplicar o mesmo processo aos três argumentos de
`calcular_tokens_mensais` . Após compreender o padrão, completar as validações das funções
monetárias e revisar a consistência das regras anteriores. Atualizar a documentação para registrar
esse marco antes de fazer um novo commit.

**Participação e aprendizado:** os exemplos de testes foram executados no VS Code após cada
alteração, com confirmação dos resultados. A comparação com NaN na documentação do PostgreSQL
ajudou a discutir a diferença entre um valor especial e uma operação que levanta uma exceção em
Python. Os testes foram apresentados aos poucos para distinguir tipos inválidos, valores
negativos, limites permitidos e valores não finitos.

**Decisões registradas:**

- Usuários ativos devem ser `int` e não negativos.
- Médias e volumes estimados aceitam `int` ou `float` , inclusive frações finitas, sem valores
  negativos.
- As taxas recebem proporções entre 0 e 1, com os dois limites permitidos.
- Preços e custos monetários devem ser `Decimal` , finitos e não negativos.
- A cotação aceita `int` , `float` ou `Decimal` , é convertida internamente para `Decimal` e deve
  ser finita e maior que zero.
- Textos passados diretamente, `None` e booleanos são recusados. Zero continua válido para consumo e
  custos.
- `TypeError` identifica tipos não permitidos; `ValueError` identifica valores que desrespeitam as
  regras.

**Contribuição para o projeto:** todas as seis funções passaram a validar seus argumentos antes dos
cálculos. Um roteiro de verificação executado durante o desenvolvimento conferiu 110 casos,
incluindo as funções monetárias e regras anteriores, sem alterar os resultados do cenário didático.
Esse roteiro ainda não está salvo como suíte de testes no repositório. As funções sinalizam erros; o
tratamento dessas mensagens em uma interface ainda será desenvolvido.

**Marco anterior:** validação das entradas, registrada em 2026-10-25. A reutilização dessas regras
está documentada na seção 10.

## 10. Refatoração com a auxiliar de validação

**Etapa:** reutilização das validações na calculadora básica.

**Objetivo dos pedidos:** reduzir a repetição das condições de validação, preservando os tipos
aceitos e os resultados, com explicações e testes por pequenas alterações.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Após salvar as validações em um commit, criar a primeira função auxiliar e aplicá-la em apenas uma
função da calculadora. Entender por que a auxiliar recebe um valor e um nome, o papel desse rótulo
nas mensagens e por que essa validação não precisa devolver um resultado. Reutilizar a auxiliar na
função de respostas mensais, mantendo a exigência de usuários inteiros. Em seguida, aplicá-la às
funções restantes, explicando as adaptações necessárias para tipos monetários e preservando as
regras específicas. Registrar a refatoração na documentação antes de fazer um novo commit.

**Participação e aprendizado:** os testes das primeiras aplicações da auxiliar motivaram pedidos de
esclarecimento sobre parâmetros, retorno e mensagens de erro. A explicação distinguiu o papel de
uma função auxiliar da decisão de usar ou não `return` : funções auxiliares também podem processar e
retornar valores; esta apenas valida e sinaliza erros.

**Decisões registradas:**

- Criar `validar_numero_nao_negativo` para centralizar tipos permitidos, valores finitos e ausência
  de negativos.
- Usar `nome` como rótulo legível do campo na mensagem de erro; não é necessário que o texto seja
  igual ao nome da variável.
- Aplicar inicialmente a auxiliar em `calcular_tokens_mensais` e depois em
  `calcular_respostas_mensais` , preservando a regra de usuários inteiros.
- Acrescentar `tipos_permitidos=(int, float)` como parâmetro opcional para reutilizar a auxiliar nas
  funções monetárias sem alterar seus contratos.
- Exigir `(Decimal,)` para preços e custos e aceitar `(int, float, Decimal)` para a cotação.
- Manter verificações específicas de usuários inteiros, taxas até 1 e cotação maior que zero nas
  funções de cálculo.
- Preservar as fórmulas; padronizar as mensagens de validação com o rótulo de cada campo.

**Contribuição para o projeto:** as seis funções de cálculo passaram a reutilizar a auxiliar. A
última conferência executou 232 casos de tipos, limites e valores especiais, além de conferir
frações válidas e o cenário original. Os resultados permaneceram em US$ 0,44 e R$ 2,20 por mês e US$
5,28 e R$ 26,40 por ano, nas hipóteses didáticas registradas. Os roteiros de verificação ainda não
estão salvos como uma suíte de testes no repositório.

**Marco deste registro:** documentação atualizada em 2026-10-26, até a refatoração com a auxiliar de
validação, sem novas dependências ou chamadas reais à API.

## 11. Separação da execução e testes automatizados

**Etapa:** testes reproduzíveis da calculadora básica.

**Objetivo dos pedidos:** importar as funções sem executar o cenário didático e transformar as
conferências manuais em testes salvos no repositório, compreendendo cada alteração.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Adicionar `if __name__ == "__main__":` e explicar a diferença entre executar e importar a
calculadora. Criar os primeiros testes de respostas mensais, começando pelo cenário didático, zero
usuários e usuários negativos. Acrescentar testes para usuários fracionários, textos, infinito e
NaN. Explicar por que uma exceção esperada é capturada por `assertRaises` e aparece como teste
aprovado. Testar em seguida feedbacks mensais, incluindo os resultados, taxas nos limites e fora do
intervalo, tipos e valores não finitos nos três argumentos. Completar os testes das funções de
tokens, custo de tokens, conversão para reais e custo anual. Explicar `for` , `subTest` , tipos
monetários e como executar um teste, uma classe ou a suíte completa. Atualizar README e registro de
prompts antes do próximo commit.

**Participação e aprendizado:** os testes foram executados no terminal após cada incremento, com
confirmação dos resultados. As dúvidas abordaram a captura de `ValueError` , o percurso do laço
pelos subtestes e a conversão com cotações representadas como `int` , `float` e `Decimal` .

**Decisões registradas:**

- Proteger o cenário e os `print()` com `if __name__ == "__main__":` ; manter as funções disponíveis
  na importação.
- Usar `unittest` , incluído no Python, sem dependências externas.
- Manter os testes em `test_calculadora.py` , com uma classe para cada função de cálculo.
- Conferir resultados com `assertEqual` , tipos de retorno com `assertIsInstance` e exceções com
  `assertRaises` .
- Introduzir `subTest` nos novos grupos para verificar várias entradas sem repetir um método para
  cada valor e identificar a tentativa que falhar.
- Testar consumo e custos zero quando permitidos; exigir cotação maior que zero.
- Preservar as diferenças de contrato: volumes aceitam `int` ou `float` , preços e custos exigem
  `Decimal` , e cotação aceita os três tipos.
- Cobrir tipos inválidos, negativos, infinito e NaN nos argumentos das quatro funções de cálculo
  restantes, além dos resultados didáticos e estimativas fracionárias permitidas.

**Contribuição para o projeto:** o repositório passou a conter uma suíte reproduzível com 59 métodos
de teste, distribuídos em seis classes. Parte dos métodos executa vários subtestes, que não aumentam
a contagem exibida em `Ran 59 tests` . A execução completa passou; a auxiliar de validação também é
exercitada indiretamente. Os roteiros temporários de 110 e 232 casos, mencionados nos marcos
anteriores, continuam sendo registros históricos distintos dessa suíte.

**Marco deste registro:** documentação atualizada em 2026-10-27, até os testes automatizados das
seis funções de cálculo, sem dependências externas ou chamadas reais à API.

## 12. Custos fixos de infraestrutura e total com IA

**Etapa:** ampliação da calculadora básica para incluir backend e banco de dados.

**Objetivo dos pedidos:** compreender a cobrança de hospedagem e PostgreSQL, calcular mensalidades
fixas e somá-las ao custo variável de IA, com valores didáticos e testes.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Explicar o que representam as cobranças de backend e banco de dados. Criar calcular_custo_servico e
seus testes, reutilizando a auxiliar de validação. Usar a função no cenário principal com preços
inventados para aprendizado, converter os custos para reais e apresentar infraestrutura, IA e totais
mensais e anuais. Explicar cada alteração e como conferir os resultados, incluindo o comportamento
com zero usuários. Atualizar README e registro de prompts antes de fazer um novo commit.

**Participação e aprendizado:** os testes da nova função e o cenário integrado foram executados,
com confirmação dos resultados. As explicações distinguiram preço por unidade, quantidade
contratada, custo fixo de infraestrutura e custo variável de IA.

**Decisões registradas:**

- Criar `calcular_custo_servico(preco_mensal_por_unidade, quantidade)` , retornando preço mensal
  multiplicado pela quantidade, na mesma moeda do preço.
- Exigir preço `Decimal` , finito e não negativo, e quantidade `int` não negativa; recusar booleanos
  e quantidades como `2.0` .
- Permitir preço gratuito e zero unidades.
- Adotar backend a US$ 5,00 por unidade, com duas unidades, e banco a US$ 3,00 por unidade, com uma
  unidade. São preços didáticos, sem fonte comercial ou comprovação de capacidade.
- Converter os custos com a cotação didática de R$ 5,00 por dólar e somar apenas valores na mesma
  moeda.
- Preservar a projeção anual de 12 meses constantes, sem arredondar etapas intermediárias.
- Manter a infraestrutura contratada mesmo quando o consumo de IA for zero.
- Registrar serviços incluídos em um mesmo pacote para evitar duplicar cobranças quando forem
  pesquisados planos reais.

**Contribuição para o projeto:** a calculadora passou a incluir sete funções de cálculo. O cenário
apresenta infraestrutura de US$ 13,00 ou R$ 65,00 mensais e IA de US$ 0,44 ou R$ 2,20 mensais. O
total é US$ 13,44 ou R$ 67,20 por mês e US$ 161,28 ou R$ 806,40 por ano, sob as hipóteses
registradas.

Foram acrescentados oito métodos de teste para o serviço, levando a suíte a 67 métodos em sete
classes. A execução completa passou. Uma conferência adicional do cenário principal, realizada em
memória e não salva como teste na suíte, confirmou os totais com 100 usuários e, com zero usuários,
IA zero e infraestrutura de US$ 13,00 ou R$ 65,00 mensais. A execução também foi confirmada no
terminal.

**Marco deste registro:** documentação atualizada em 2026-10-28, até a integração de infraestrutura
e IA, sem novas dependências ou chamadas reais à API.

## 13. Pesquisa de hospedagem e Firebase como alternativa

**Etapa:** pesquisa de infraestrutura e avaliação de alternativas, antes de alterar o cenário da
calculadora.

**Objetivo dos pedidos:** comparar opções gratuitas e pagas em fontes oficiais e compreender se o
Firebase pode atender ao LiteArt, aproveitando o aprendizado da faculdade sem substituir
antecipadamente a arquitetura planejada.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Pesquisar três opções de hospedagem para backend e PostgreSQL, priorizando baixo custo e incluindo
pelo menos uma combinação gratuita. Explicar preços, limites e condições aos poucos e registrar a
comparação no planejamento antes de alterar o código. Verificar o Firebase, apresentado na
disciplina de programação de dispositivos móveis, especialmente para login com Google e possível
centralização de backend e banco. Explicar sua hospedagem, os produtos envolvidos e os custos e
limitações. Registrar o Firebase como alternativa, mantendo NestJS e PostgreSQL como referência.
Atualizar README e registro de prompts para salvar esse marco em um commit.

**Participação e aprendizado:** a experiência com Firebase na faculdade motivou uma avaliação antes
da decisão sobre a arquitetura. A orientação distinguiu autenticação, execução de
backend, hospedagem de frontend e armazenamento de dados, além de mensalidade fixa, consumo,
franquia e teste gratuito temporário.

**Decisões registradas:**

- Comparar Render + Neon, Railway e Koyeb + Neon, registrando fontes e data da consulta de
  2026-10-28 no planejamento.
- Distinguir uma combinação gratuita dentro das franquias de créditos limitados e ofertas
  temporárias; considerar suspensão por inatividade e condições de cadastro.
- Registrar a avaliação do Firebase com consulta de 2026-10-30, incluindo Spark e Blaze e a
  separação dos serviços e suas cobranças.
- Considerar Firebase Authentication para login com Google no Flutter sem exigir a troca do NestJS
  ou do PostgreSQL.
- Distinguir Firestore, orientado a documentos, de SQL Connect com PostgreSQL via Cloud SQL;
  registrar que a gratuidade de teste deste último é temporária.
- Distinguir Hosting tradicional de App Hosting e dos serviços que executam código de backend, como
  Functions e Cloud Run.
- Manter Flutter, Node.js/NestJS e PostgreSQL como arquitetura de referência; Firebase permanece uma
  alternativa em estudo.
- Manter os preços didáticos no cenário principal e nos testes. A pesquisa não implementa seleção de
  provedores, migração ou contratação.
- Preparar hipóteses de operações, armazenamento, processamento e tráfego antes de simular ofertas
  cobradas por consumo.

**Contribuição para o projeto:** o planejamento passou a registrar três combinações de hospedagem e
uma alternativa Firebase com fontes, datas, custos e limitações. O README resume a pesquisa e aponta
para os detalhes no planejamento. Nenhum provedor foi escolhido para substituir as
entradas didáticas, e código e testes permaneceram inalterados neste marco.

**Marco deste registro:** documentação atualizada em 2026-10-31, consolidando a pesquisa de
hospedagem e o Firebase como alternativa, com NestJS e PostgreSQL preservados como referência.

## 14. Organização das entradas em dicionários

**Etapa:** organização dos dados da calculadora básica para preparar futuros cenários.

**Objetivo dos pedidos:** separar hipóteses de consumo, preços e cotação, aprendendo dicionários e
acesso por chaves sem alterar as fórmulas ou os resultados.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar um dicionário com as hipóteses de consumo e adaptar as chamadas das funções, explicando cada
parte e como testar se os resultados continuam iguais. Esclarecer se a cotação do dólar poderá ser
consultada automaticamente no futuro. Organizar depois os preços de IA, os preços de infraestrutura
e a cotação em dicionários separados das hipóteses, explicando a leitura das chaves e a conferência
dos cálculos. Atualizar README e registro de prompts antes de fazer um novo commit.

**Participação e aprendizado:** o cenário e os testes foram executados após cada incremento, com
confirmação dos resultados. As explicações abordaram pares de chave e valor, uso de chaves entre
colchetes, preservação de Decimal e a diferença entre testar uma função com entradas próprias e
executar o cenário principal.

**Decisões registradas:**

- Criar `hipoteses_consumo` com seis entradas: usuários ativos, respostas por usuário, taxa de
  acerto, parcela dos acertos com feedback e tokens de entrada e saída por feedback.
- Criar `precos_ia` com as tarifas em USD por milhão de tokens; preservar os comentários de fonte,
  data e condições.
- Criar `precos_infraestrutura` com os preços didáticos mensais por unidade de backend e banco.
- Criar `cotacao` com a chave `brl_por_usd` , mantendo a taxa manual didática de `Decimal("5.00")` .
- Manter as quantidades contratadas como variáveis separadas, pois representam hipóteses de
  capacidade.
- Adaptar as chamadas para buscar os valores por chave, mantendo os contratos e as validações das
  funções.
- Manter os resultados separados das entradas e preservar todos os valores do cenário.
- Considerar futuramente consulta de câmbio por API, registrando fonte e data e mantendo a opção
  manual. Essa consulta não foi implementada e não prevê o câmbio dos meses futuros.

**Contribuição para o projeto:** quatro dicionários passaram a organizar as entradas no bloco
principal. A conferência da última refatoração comparou a saída completa antes e depois e confirmou
sua preservação; os 67 métodos de teste passaram. O total permaneceu em US$ 13,44 ou R$ 67,20 por
mês e US$ 161,28 ou R$ 806,40 por ano. A organização prepara comparações futuras, mas ainda não
implementa uma função de cenário completo nem importação de dados.

**Marco deste registro:** documentação atualizada em 2026-10-31, até a organização de hipóteses,
preços e cotação em dicionários, sem novas dependências ou consulta automática de câmbio.

## 15. Função de consumo do cenário e seus testes

**Etapa:** reutilização da sequência de cálculos de consumo.

**Objetivo dos pedidos:** receber as hipóteses em um dicionário, coordenar as funções existentes e
retornar os resultados de consumo, mantendo validações e apresentação separadas.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Antes de implementar a nova função, esclarecer a diferença entre dicionário Python e JSON, a
consulta por chave e a passagem de um valor individual ou de um dicionário inteiro a uma função.
Criar calcular_consumo_cenario e seus testes, explicando cada parte e como executar aos poucos.
Atualizar README e registro de prompts antes do próximo commit.

**Participação e aprendizado:** as dúvidas sobre dicionários e acesso aos dados foram esclarecidas
antes da implementação. Depois, os testes foram executados e os resultados confirmados. As explicações
abordaram validação de chaves, reutilização de funções, propagação de exceções, retorno de um novo
dicionário e preservação da entrada.

**Decisões registradas:**

- Criar `calcular_consumo_cenario(hipoteses_consumo)` para coordenar respostas mensais, feedbacks e
  tokens, reutilizando as funções existentes.
- Exigir um `dict` , com `TypeError` para outros tipos, e as seis chaves obrigatórias, com
  `ValueError` identificando o campo ausente.
- Manter a validação dos números nas funções de cálculo, propagando suas exceções.
- Permitir chaves adicionais sem utilizá-las nos cálculos.
- Retornar um novo dicionário com sete resultados, sem modificar as hipóteses recebidas.
- Integrar o retorno ao bloco principal, preservando os cálculos monetários e os `print()` .
- Acrescentar `TestCalcularConsumoCenario` , com dez métodos de teste e uma auxiliar que cria
  hipóteses independentes para cada caso.
- Conferir cenário didático, zero usuários, zero respostas, tipo do argumento, cada chave ausente,
  tipos e valores inválidos nos campos, preservação da entrada e aceitação de chave adicional.

**Contribuição para o projeto:** o consumo passou a ser calculado por uma função reutilizável que
recebe e devolve dicionários. A suíte passou de 67 para 77 métodos, distribuídos em oito classes; a
execução completa passou. A comparação da saída do cenário antes e depois da integração confirmou
sua preservação. Os totais continuam em US$ 13,44 ou R$ 67,20 por mês e US$ 161,28 ou R$ 806,40 por
ano, sob as hipóteses didáticas. A função de cenário completo, incluindo custos, ainda não foi
implementada.

**Marco deste registro:** documentação atualizada em 2026-10-31, até a função de consumo do cenário
e seus testes, sem novas dependências ou chamadas externas.

## 16. Função de custos de IA do cenário e seus testes

**Etapa:** reutilização dos cálculos monetários de IA.

**Objetivo dos pedidos:** coordenar os custos de tokens, a conversão e a projeção anual a partir de
dicionários, preservando a separação entre cálculo e apresentação.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar calcular_custo_ia_cenario e seus testes, integrar a função ao cenário principal e explicar
cada parte e como conferir que os resultados continuam iguais. Retomar a explicação da função e dos
testes após a implementação, distinguindo validação dos dicionários, cálculo, retorno e execução no
terminal. Atualizar README e registro de prompts antes do próximo commit.

**Participação e aprendizado:** a execução dos testes confirmou os resultados. As explicações
abordaram passagem de três dicionários, chaves obrigatórias, propagação das exceções, retorno de
valores Decimal e uso de entradas independentes nos testes.

**Decisões registradas:**

- Criar `calcular_custo_ia_cenario(consumo_cenario, precos_ia, cotacao)` , reutilizando as funções
  de custo de tokens, conversão e projeção anual.
- Exigir três argumentos do tipo `dict` e cinco chaves no total; sinalizar tipos incorretos com
  `TypeError` e chaves ausentes com `ValueError` .
- Manter as validações numéricas nas funções existentes e propagar suas exceções.
- Aceitar chaves adicionais sem utilizá-las nos cálculos, permitindo receber o retorno completo do
  consumo.
- Retornar um novo dicionário com oito valores em `Decimal` , sem modificar os três dicionários
  recebidos.
- Integrar a chamada ao bloco principal, preservando a apresentação e a soma com infraestrutura.
- Acrescentar `TestCalcularCustoIaCenario` , com 12 métodos: cenário didático e tipos de retorno,
  zeros de consumo, preços gratuitos, tokens fracionários, cotações permitidas, estrutura dos
  dicionários, erros dos campos, preservação das entradas e chaves adicionais.

**Contribuição para o projeto:** a suíte passou de 77 para 89 métodos, distribuídos em nove classes,
e a execução completa passou. A saída do cenário antes e depois da integração foi comparada e
permaneceu idêntica. O custo de IA continua em US$ 0,44 ou R$ 2,20 por mês e US$ 5,28 ou R$ 26,40
por ano. O total com infraestrutura permanece em US$ 13,44 ou R$ 67,20 mensais e US$ 161,28 ou R$
806,40 anuais, nas hipóteses didáticas registradas.

**Marco deste registro:** documentação atualizada em 2026-10-31, até a função de custos de IA do
cenário, seus testes e integração, sem novas dependências, consulta automática de câmbio ou chamadas
reais à API.

## 17. Hipóteses de capacidade e custos de infraestrutura por cenário

**Etapa:** reutilização dos cálculos de infraestrutura.

**Objetivo dos pedidos:** reunir as quantidades contratadas em um dicionário e coordenar os custos
de backend e banco, preservando os resultados e o padrão das funções de cenário anteriores.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar hipoteses_capacidade e calcular_custo_infra_cenario com seus testes, integrar ao cenário
principal e explicar cada parte e como conferir que os resultados continuam iguais, aos poucos.
Atualizar README e registro de prompts para documentar esse incremento antes de fazer um commit.

**Participação e aprendizado:** a execução dos testes confirmou os resultados. As explicações
distinguiram quantidade contratada de preço e consumo, revisaram validação de dicionários e chaves e
demonstraram a reutilização das funções de serviço, conversão e projeção anual.

**Decisões registradas:**

- Criar `hipoteses_capacidade` com `quantidade_backend: 2` e `quantidade_banco: 1` , substituindo as
  variáveis individuais do cenário.
- Criar `calcular_custo_infra_cenario(precos_infraestrutura, hipoteses_capacidade, cotacao)` .
- Exigir três dicionários e as cinco chaves necessárias; usar `TypeError` para tipos incorretos e
  `ValueError` para chave obrigatória ausente.
- Reutilizar as validações numéricas existentes, propagando suas exceções; manter quantidades
  inteiras não negativas, preços Decimal não negativos e cotação positiva.
- Retornar um novo dicionário com oito resultados em Decimal, preservando as entradas e aceitando
  chaves adicionais.
- Integrar o retorno ao cenário principal e mover a projeção anual da infraestrutura para a função
  coordenadora, evitando calculá-la novamente no bloco principal.
- Acrescentar `TestCalcularCustoInfraCenario` , com 11 métodos de teste: resultados e tipos, zero
  unidades, preços gratuitos, cotação, estrutura dos dicionários, erros dos campos, preservação e
  chaves adicionais.

**Contribuição para o projeto:** as entradas passaram a ser organizadas em cinco dicionários, e a
infraestrutura passou a ter uma função coordenadora própria. A suíte passou de 89 para 100 métodos
de teste, distribuídos em dez classes; a execução completa passou. A comparação da saída antes e
depois confirmou a preservação dos resultados.

A infraestrutura continua em US$ 13,00 ou R$ 65,00 por mês e US$ 156,00 ou R$ 780,00 por ano. O
total com IA permanece em US$ 13,44 ou R$ 67,20 mensais e US$ 161,28 ou R$ 806,40 anuais, sob as
hipóteses didáticas. A função de cenário completo ainda será implementada.

**Marco deste registro:** documentação atualizada em 2026-11-02, até o dicionário de capacidade, a
função de infraestrutura, seus testes e integração, sem novas dependências ou chamadas externas.

## 18. Cenário completo, testes e formatação da documentação

**Etapa:** integração dos cálculos e padronização dos arquivos Markdown.

**Objetivo dos pedidos:** reunir consumo, IA, infraestrutura e totais em uma função reutilizável e
manter a documentação consistente e sem os avisos de formatação identificados.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Explicar os avisos MD060 de espaçamento nas tabelas e MD012 de linhas em branco consecutivas. Criar
calcular_cenario e seus testes, integrar ao bloco principal e explicar cada parte e como conferir os
resultados aos poucos. Após executar os testes, atualizar README e registro de prompts, corrigir a
formatação dos arquivos Markdown e preparar uma forma de evitar a repetição dos avisos antes do
próximo commit.

**Participação e aprendizado:** os avisos do Markdownlint foram analisados, e a execução dos novos
testes confirmou os resultados. As explicações abordaram coordenação das funções existentes,
dicionários aninhados, acesso por duas chaves e desempacotamento de argumentos com asterisco nos
testes.

**Decisões registradas:**

- Criar `calcular_cenario` com os cinco dicionários de entrada e reutilizar as três funções
  coordenadoras.
- Retornar quatro grupos: `consumo` , `custos_ia` , `custos_infraestrutura` e `totais` .
- Somar apenas custos na mesma moeda e projetar 12 meses constantes.
- Propagar as validações existentes, preservar as entradas e produzir resultados independentes entre
  execuções.
- Integrar uma chamada ao cenário completo ao bloco principal e manter os prints separados.
- Acrescentar `TestCalcularCenario` , com 11 métodos para resultados completos, zeros de consumo ou
  capacidade, preços gratuitos, câmbio, erros de estrutura e valores, preservação, independência e
  campos extras.
- Corrigir tabelas e linhas em branco em README, PLANEJAMENTO e PROMPTS e quebrar linhas de texto
  sem reescrever os prompts históricos.
- Registrar regras locais do Markdownlint, mantendo os avisos ativos, com limite de 100 caracteres
  para texto e exceções para tabelas e blocos de código.
- Configurar o VS Code para aplicar as correções disponíveis do Markdownlint ao salvar
  explicitamente arquivos Markdown, quando a extensão estiver instalada.

**Contribuição para o projeto:** a suíte passou de 100 para 111 métodos, distribuídos em 11 classes,
e a execução completa passou. A comparação antes e depois da integração confirmou a saída idêntica.
O total permanece em US$ 13,44 ou R$ 67,20 mensais e US$ 161,28 ou R$ 806,40 anuais nas hipóteses
didáticas. A documentação registra o cenário completo e recebe uma configuração reproduzível de
formatação, sem mudanças adicionais no código Python neste marco documental.

**Marco deste registro:** documentação atualizada em 2026-11-02, até o cenário completo, seus testes
e a padronização de Markdown.

## 19. Comparação dos cenários de 100 e 500 usuários

**Etapa:** primeira comparação de cenários com Python puro.

**Objetivo dos pedidos:** reutilizar o cenário completo em uma lista, compreender o laço de
repetição e observar como consumo, custo variável e custo fixo se comportam.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar a lista com dois cenários didáticos de 100 e 500 usuários, calcular cada um com for e
apresentar a comparação no terminal, explicando cada parte e como conferir os resultados aos
poucos. Após executar e confirmar os testes, atualizar README e registro de prompts, preservando
a formatação Markdown, para fazer um commit.

**Participação e aprendizado:** a execução do programa e dos testes confirmou os resultados.
As explicações abordaram cópia de dicionários, listas de cenários, repetição com for, armazenamento
dos resultados com append e a diferença entre custos variáveis de IA e mensalidades fixas.

**Decisões registradas:**

- Criar cópias das hipóteses de consumo para 100 e 500 usuários; alterar apenas os usuários no
  segundo cenário.
- Criar `cenarios_didaticos` com nome, hipóteses de consumo e uma cópia da capacidade para cada
  cenário, mantendo os preços e a cotação compartilhados.
- Usar `for` para chamar `calcular_cenario` uma vez por item e apresentar o resumo no terminal.
- Guardar nome, usuários e resultado em `comparacao_cenarios`, utilizando `append()`.
- Preservar o detalhamento original e acrescentar a comparação ao final.
- Declarar que a infraestrutura constante é uma hipótese, sem validar sua capacidade para
  atender 500 usuários.
- Manter Python puro, sem CSV, Pandas ou gráficos neste incremento.

**Contribuição para o projeto:** a aplicação passou a apresentar uma comparação didática no
terminal. Com 100 usuários, são 2.200 feedbacks, R$ 2,20 de IA e R$ 67,20 de total mensal. Com 500,
são 11.000 feedbacks, R$ 11,00 de IA e R$ 76,00 mensais. A infraestrutura permanece em R$ 65,00 nos
dois casos. Os totais anuais são R$ 806,40 e R$ 912,00, respectivamente, com condições constantes.

Uma conferência adicional verificou resultados, consumo e IA multiplicados por cinco, entradas
independentes e preservadas e manutenção do detalhamento anterior. Esse roteiro não foi salvo
como teste na suíte. Os 111 métodos existentes passaram; não foram acrescentados métodos neste
incremento. README e PROMPTS foram atualizados mantendo as regras locais de Markdown.

**Marco deste registro:** documentação atualizada em 2026-11-02, até a comparação dos dois cenários
didáticos no terminal.

## 20. Lista de resumos dos cenários

**Etapa:** preparação dos resultados para análise tabular, ainda com Python puro.

**Objetivo dos pedidos:** transformar os resultados aninhados em registros com os mesmos campos,
preservando os valores e preparando a futura introdução do Pandas.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar a lista de resumos dos dois cenários com Python puro, explicando cada parte e como testar
se os valores continuam corretos antes de usar Pandas. Após executar os testes, atualizar README
e registro de prompts mantendo a formatação Markdown e sugerir uma mensagem de commit. Discutir
também a proposta de usar este chat para planejamento e orientação e outro chat do Codex para
as implementações, com prompts de escopo pequeno e revisão dos resultados a cada incremento.

**Participação e aprendizado:** a execução do programa e dos testes confirmou os resultados.
As explicações abordaram lista vazia, seleção de campos, acesso a dicionários aninhados,
armazenamento com append e criação de um registro independente por rodada do laço.

**Decisões registradas:**

- Criar `resumos_cenarios` e preenchê-la a partir de `comparacao_cenarios`, sem recalcular custos.
- Usar sete campos por registro: nome, usuários, feedbacks, IA mensal, infraestrutura mensal,
  total mensal e total anual em BRL.
- Preservar custos em `Decimal`, sem símbolos monetários nos dados ou conversão para texto.
- Criar um dicionário novo para cada cenário e preservar os resultados completos existentes.
- Exibir a estrutura no terminal para inspeção, mantendo a apresentação anterior.
- Adiar DataFrame, instalação do Pandas e CSV para incrementos posteriores.

**Contribuição para o projeto:** a calculadora passou a produzir dois registros planos que podem
ser usados como linhas de uma futura tabela. Uma conferência adicional verificou comprimento
da lista, campos, valores, tipos e independência dos registros; esse roteiro não foi salvo na
suíte. Os 111 métodos existentes passaram e os totais de 100 e 500 usuários foram preservados.
README e PROMPTS registram o incremento, sem alterações adicionais em código nesta revisão.

**Marco deste registro:** documentação atualizada em 2026-11-03, até a lista de resumos dos
cenários com Python puro, antes da introdução do Pandas.

## 21. Primeiro DataFrame com Pandas e preservação de Decimal

**Data:** 04/11/2026.

**Etapa:** início da análise de dados com Pandas.

**Objetivo dos pedidos:** criar uma tabela a partir dos resumos existentes, preservando os
resultados e os tipos monetários, com uma alteração pequena e explicada.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Conferir o código, os testes e o Pandas disponível na `.venv-win`, sem instalar pacotes. Criar
`tabela_cenarios` a partir de `resumos_cenarios`, manter os dois cenários, os sete campos e os
valores financeiros em Decimal. Apresentar a tabela no terminal, preservar as saídas e conferir
os dados, os resultados exatos e os testes existentes. Documentar o incremento sem alterar código,
dependências ou planejamento nesta revisão documental e sem fazer commit ou push.

**Participação e aprendizado:** os pedidos priorizaram a explicação de cada linha, a diferença
entre os tipos das colunas e os objetos armazenados e a conferência explícita dos valores
financeiros, sem tomar `dtype object` como prova de que são Decimal.

**Decisões registradas:**

- Importar `pandas as pd` e criar a tabela dentro do bloco principal com
  `pd.DataFrame.from_records(resumos_cenarios, coerce_float=False)`.
- Preservar duas linhas, para 100 e 500 usuários, e sete colunas na ordem da lista original.
- Manter os quatro campos financeiros como objetos `Decimal`, sem conversão para float ou texto
  e sem arredondar dados intermediários.
- Acrescentar a impressão com `to_string(index=False)`, mantendo as saídas anteriores.
- Preservar as funções de cálculo e a importação do módulo sem executar os cenários.
- Usar o Python convencional da `.venv-win`, preservando o ambiente MSYS2 anterior.

**Contribuição para o projeto:** a implementação foi concluída e validada. As verificações
pontuais confirmaram formato `(2, 7)`, ordem dos campos, igualdade com `resumos_cenarios` e
preservação da lista original. Os oito valores financeiros foram conferidos individualmente com
`isinstance(valor, Decimal)` e comparados com os resultados esperados usando Decimal.

Para 100 usuários, foram confirmados 2.200 feedbacks, R$ 2,20 de IA, R$ 65,00 de infraestrutura,
R$ 67,20 de total mensal e R$ 806,40 anuais. Para 500, foram 11.000 feedbacks, R$ 11,00 de IA,
R$ 65,00 de infraestrutura, R$ 76,00 mensais e R$ 912,00 anuais. São estimativas didáticas,
com as hipóteses e exclusões existentes, sem representar despesas reais.

Os 111 métodos de teste existentes passaram. As conferências específicas do DataFrame foram
roteiros pontuais executados em memória; não foram adicionados novos testes automatizados ao
repositório. As funções de cálculo, a importação silenciosa e as saídas anteriores foram
preservadas. CSV, gráficos e dashboard continuam planejados.

**Marco deste registro:** documentação de 04/11/2026, até o primeiro DataFrame no terminal.

## 22. Seleção e ordenação dos custos com Pandas

**Data:** 05/11/2026.

**Etapa:** comparação dos custos mensais com Pandas.

**Objetivo dos pedidos:** selecionar três colunas e ordenar os cenários pelo custo mensal,
preservando os valores financeiros e a tabela original, com explicações de cada operação.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar `comparacao_custos` com cenário, usuários e custo total mensal, nessa ordem. Usar
`sort_values` com `ascending=False`, sem `inplace=True`, e apresentar a comparação no terminal.
Conferir os valores como Decimal, a preservação integral de `tabela_cenarios`, a importação
silenciosa e os 111 testes existentes. Atualizar somente README e PROMPTS, reformulando referências
pessoais que deixavam a escrita artificial e mantendo a terceira pessoa, sem commit ou push.

**Participação e aprendizado:** as explicações abordaram os colchetes de seleção, a lista de nomes
das colunas, o parâmetro `by`, a ordem decrescente e o retorno de outro DataFrame pela ordenação.

**Decisões registradas:**

- Selecionar `cenario`, `usuarios_ativos` e `custo_total_mensal_br`, nessa ordem.
- Ordenar por `custo_total_mensal_br` com `ascending=False`, atribuindo o retorno a
  `comparacao_custos`.
- Preservar os valores, tipos, colunas, índices e ordem das linhas de `tabela_cenarios`.
- Manter os custos como objetos `Decimal`, sem conversão para float ou texto e sem arredondamento.
- Acrescentar um título e `to_string(index=False)` ao final, mantendo as saídas existentes.

**Contribuição para o projeto:** a comparação foi implementada com duas linhas e três colunas.
O cenário de 500 usuários aparece primeiro, com custo mensal igual a `Decimal("76.00")`, seguido
pelo de 100 usuários, com `Decimal("67.20")`. Os índices da comparação são `[1, 0]`; os da tabela
original permanecem `[0, 1]`. Os resultados continuam sendo estimativas didáticas.

As verificações pontuais confirmaram formato, colunas, ordem e custos exatos, com
`isinstance(valor, Decimal)` nos dois valores financeiros. A comparação com uma cópia anterior,
usando `assert_frame_equal` e conferências dos tipos individuais, confirmou a preservação integral
de `tabela_cenarios`. As funções de cálculo, as saídas anteriores e a importação sem executar os
cenários também foram preservadas.

A calculadora e os 111 testes existentes foram executados com a `.venv-win` e passaram.
As verificações específicas foram roteiros pontuais em memória; não foram acrescentados testes
automatizados ao repositório. Documentação e dependências não foram alteradas na implementação.

**Marco deste registro:** documentação de 05/11/2026, até a seleção e ordenação dos custos mensais.

## 23. Filtro de cenários por orçamento mensal

**Data:** 06/11/2026.

**Etapa:** seleção de cenários com máscara booleana no Pandas.

**Objetivo dos pedidos:** filtrar os cenários por um limite mensal didático, preservando Decimal
e os DataFrames de origem, com uma alteração pequena e explicada.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Definir o orçamento de R$ 70,00 após a ordenação dos custos. Comparar a coluna de custo mensal
com o limite usando `<=`, selecionar as linhas aprovadas com `.loc` e apresentar o resultado ou
uma mensagem quando nenhum cenário couber no orçamento. Conferir limites adicionais, tipos,
preservação das tabelas e testes existentes. Documentar o comportamento implementado somente em
README e PROMPTS, sem alterar código, testes ou dependências e sem commit ou push nesta revisão.

**Participação e aprendizado:** as explicações abordaram o operador menor ou igual, a máscara
de valores True e False, a seleção com `.loc` e a identificação de resultados vazios com `.empty`.

**Decisões registradas:**

- Definir `orcamento_mensal_br = Decimal("70.00")` como limite didático, sem entrada interativa.
- Criar `dentro_do_orcamento` pela comparação entre custo mensal e orçamento com `<=`.
- Guardar a seleção com `.loc` em `cenarios_no_orcamento`, mantendo as três colunas, a ordem
  dos cenários aprovados e seus índices originais.
- Preservar os custos como Decimal, sem conversão para float ou texto e sem arredondamento.
- Apresentar orçamento, título e tabela sem índices; usar uma mensagem para o resultado vazio.
- Preservar integralmente `tabela_cenarios`, `comparacao_custos` e as saídas existentes.

**Contribuição para o projeto:** o filtro foi implementado no bloco principal. Com o limite de
R$ 70,00, o resultado tem uma linha e três colunas: o cenário de 100 usuários, com custo mensal
igual a `Decimal("67.20")` e índice `[0]`. Quando nenhum cenário é aprovado, a mensagem informa:
"Nenhum cenário avaliado cabe no orçamento mensal informado."

As verificações pontuais executadas em memória também confirmaram que `Decimal("67.20")` inclui
somente 100 usuários, `Decimal("76.00")` inclui 500 e depois 100 usuários, e `Decimal("60.00")`
produz resultado vazio com a mensagem esperada. O orçamento principal permaneceu em R$ 70,00.
Os valores financeiros selecionados passaram por `isinstance(valor, Decimal)`. A comparação dos
dois DataFrames de origem com cópias anteriores à filtragem confirmou valores, tipos, colunas,
índices e ordem das linhas preservados. A importação silenciosa e as funções também foram mantidas.

A calculadora e os 111 testes existentes foram executados com a `.venv-win` e passaram.
As conferências específicas do filtro foram verificações pontuais, sem novos testes automatizados
adicionados ao repositório. Os limites e resultados representam hipóteses didáticas, não despesas
reais nem comprovação de capacidade dos serviços.

**Marco deste registro:** documentação de 06/11/2026, até o filtro por orçamento mensal.

## 24. Coluna calculada de saldo do orçamento

**Data:** 06/11/2026.

**Etapa:** cálculo de uma nova coluna com Pandas.

**Objetivo dos pedidos:** analisar a sobra ou o excesso sobre o orçamento mensal em todos os
cenários, preservando Decimal e os DataFrames anteriores, com uma alteração pequena e explicada.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar `analise_orcamento` como cópia de `comparacao_custos` e acrescentar `saldo_orcamento_br`
pela subtração direta do custo mensal do orçamento, sem laço, apply ou conversões para float.
Apresentar a tabela e explicar os sinais do saldo. Conferir resultados, tipos, preservação das
tabelas e testes existentes. Atualizar somente README e PROMPTS com o comportamento implementado,
sem alterar código, testes, planejamento ou dependências e sem commit ou push nesta revisão.

**Participação e aprendizado:** as explicações abordaram a finalidade de `copy()`, a subtração
elemento por elemento, a criação de uma coluna por atribuição e a validade de saldos negativos.

**Decisões registradas:**

- Reutilizar o orçamento didático de `Decimal("70.00")`.
- Criar `analise_orcamento` com `comparacao_custos.copy()`, mantendo ambos os cenários e sua ordem.
- Acrescentar o saldo como última coluna: orçamento mensal menos custo total mensal.
- Preservar custos e saldos como objetos Decimal, sem arredondamento intermediário.
- Acrescentar título, indicação de sobra ou excesso e tabela sem índices às saídas existentes.
- Manter integralmente `tabela_cenarios`, `comparacao_custos` e `cenarios_no_orcamento`.

**Contribuição para o projeto:** a implementação foi concluída com duas linhas e quatro colunas,
na ordem de 500 e depois 100 usuários, com índices `[1, 0]`. Para 500 usuários, foram confirmados
custo mensal de `Decimal("76.00")` e saldo de `Decimal("-6.00")`. Para 100, custo de
`Decimal("67.20")` e saldo de `Decimal("2.80")`. O saldo compara custo e limite didático;
não representa lucro, pois não considera receitas.

As verificações pontuais conferiram os dois custos e os dois saldos com `isinstance` e Decimal.
Uma subtração adicional em memória com limite de `Decimal("67.20")` confirmou saldo zero para
100 usuários, sem alterar o orçamento principal de R$ 70,00 nem os resultados finais.
Os três DataFrames anteriores foram comparados com cópias anteriores à análise, incluindo valores,
tipos individuais, colunas, índices e ordem das linhas, e permaneceram iguais.
As funções de cálculo, a importação silenciosa e as saídas anteriores foram preservadas.

A calculadora e os 111 testes existentes foram executados com a `.venv-win` e passaram.
As verificações específicas do saldo foram roteiros pontuais em memória; não foram acrescentados
testes automatizados persistentes ao repositório. Os resultados continuam sendo estimativas
didáticas, sem receitas, chamadas reais à API ou validação de capacidade dos serviços.

**Marco deste registro:** documentação de 06/11/2026, até a coluna de saldo do orçamento.

## 25. Resumo dos custos mensais com agregações

**Data:** 06/11/2026.

**Etapa:** agregações de uma coluna com Pandas.

**Objetivo dos pedidos:** obter o menor e o maior custo mensal e a diferença entre eles,
preservando Decimal, os DataFrames anteriores e as saídas existentes.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Usar a coluna de custo total mensal de `comparacao_custos`, incluindo os dois cenários sem filtro
de orçamento. Calcular os extremos com `.min()` e `.max()` e subtrair o menor do maior.
Apresentar o resumo em reais, com duas casas somente na exibição, explicar as agregações e
conferir resultados, tipos, tabelas e testes existentes. Atualizar somente README e PROMPTS,
executar o Markdownlint e sugerir uma mensagem de commit, sem fazer commit ou push.

**Participação e aprendizado:** as explicações distinguiram a seleção de uma coluna do retorno
de um único valor por agregação. Também abordaram a inclusão dos dois cenários completos e a
dependência dos resultados em relação às hipóteses de consumo, preços, câmbio e infraestrutura.

**Decisões registradas:**

- Calcular `menor_custo_mensal_br` com `.min()` e `maior_custo_mensal_br` com `.max()`.
- Calcular `diferenca_custos_mensais_br` subtraindo o menor custo do maior.
- Usar os dois cenários de `comparacao_custos`, sem aplicar o filtro de orçamento.
- Manter os três resultados como Decimal, sem conversões para float ou arredondamento intermediário.
- Acrescentar rótulos claros e valores com R$ e duas casas decimais somente na exibição.
- Preservar os quatro DataFrames anteriores, as funções de cálculo e a importação silenciosa.

**Contribuição para o projeto:** o resumo foi implementado e validado. As verificações pontuais
confirmaram menor custo igual a `Decimal("67.20")`, maior custo igual a `Decimal("76.00")` e
diferença igual a `Decimal("8.80")`. Os três resultados passaram por `isinstance(valor, Decimal)`.
Os quatro DataFrames foram comparados com cópias anteriores às operações, incluindo valores,
tipos individuais, colunas, índices e ordem das linhas, e permaneceram iguais.
As funções, as saídas anteriores e a importação sem executar cenários também foram preservadas.

A calculadora e os 111 testes existentes foram executados com a `.venv-win` e passaram.
As verificações específicas do resumo foram roteiros pontuais em memória; não foram adicionados
testes automatizados persistentes ao repositório. A diferença reflete as hipóteses didáticas
atuais, com infraestrutura constante e variação do custo de IA, sem representar despesas reais.

**Marco deste registro:** documentação de 06/11/2026, até o resumo dos extremos dos custos mensais.

## 26. Formatação monetária e precisão interna

**Data:** 06/11/2026.

**Etapa:** legibilidade da apresentação financeira no terminal.

**Objetivo dos pedidos:** apresentar valores monetários com duas casas decimais nas tabelas e
nos resumos, mantendo a precisão de Decimal nos dados usados para cálculos, ordenação e filtros.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Melhorar a legibilidade financeira sem substituir ou arredondar os dados internos. Documentar
o uso de `:.2f`, dos formatadores de `to_string()` e de `resumo_exibicao`, distinguindo textos
de apresentação dos valores em `resumos_cenarios`. Conferir precisão, apresentação e testes
existentes. Atualizar somente README e PROMPTS e verificar o Markdown, sem commit ou push.

**Participação e aprendizado:** a distinção central é entre formatar uma representação exibida
e alterar o valor armazenado. Duas casas no terminal não limitam a precisão dos cálculos.

**Decisões registradas:**

- Usar `:.2f` nas mensagens individuais e nos textos financeiros de `resumo_exibicao`.
- Passar `formatadores_monetarios` ao argumento `formatters` de `DataFrame.to_string()` nas
  quatro tabelas, mantendo os índices ocultos somente na impressão.
- Manter `resumos_cenarios` e as colunas financeiras dos DataFrames com objetos Decimal.
- Gerar textos para apresentação sem atribuí-los de volta aos dados de cálculo.
- Esclarecer que a formatação pode arredondar a representação, preservando a precisão interna.

**Contribuição para o projeto:** a implementação foi conferida em `calculadora.py`. As tabelas
e os resumos apresentam os valores financeiros com duas casas decimais; os dados originais
continuam em Decimal. `resumo_exibicao` contém textos nos campos monetários, e os demais campos
mantêm seus valores. Cálculos, agregações, ordenação e filtros usam os dados originais.

Uma conferência pontual executada em memória confirmou a apresentação das quatro tabelas e dos
resumos e a preservação da lista e dos DataFrames, incluindo tipos, índices e precisão Decimal.
O formatador apresentou `Decimal("1.236")` como `1.24` sem alterar o valor original; o custo
`Decimal('67.200000')` também manteve sua precisão nos dados.

Os 111 testes existentes foram executados com a `.venv-win` e passaram. A conferência específica
de precisão e apresentação foi pontual; não foram adicionados novos testes automatizados ao
repositório. A atualização documental preserva código, testes, planejamento e dependências.

**Marco deste registro:** documentação de 06/11/2026, até a formatação monetária no terminal.
