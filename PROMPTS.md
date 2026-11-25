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

## 27. Exportação dos cenários para CSV com precisão financeira

**Data:** 07/11/2026.

**Etapa:** primeira exportação dos resultados calculados.

**Objetivo dos pedidos:** salvar a tabela atual em CSV, preservando a precisão financeira,
os dados de origem e as saídas existentes, com explicações de cada parte.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Exportar somente `tabela_cenarios` para `resultados/cenarios.csv`, relativo à pasta da calculadora.
Criar a pasta automaticamente, substituir o arquivo a cada execução e informar seu caminho.
Usar UTF-8, vírgula, ponto decimal, cabeçalho e ausência de índice, sem formatadores ou conversões
para float. Conferir estrutura, acentos, precisão, repetição da execução, preservação dos dados,
importação silenciosa e testes existentes. Documentar a implementação somente em README e PROMPTS,
sem alterar o CSV nesta revisão e sem commit ou push.

**Participação e aprendizado:** as explicações abordaram `Path`, `__file__`, a criação da pasta
com `mkdir`, os parâmetros de `to_csv()` e a diferença entre precisão dos dados e apresentação.
Também distinguiram a releitura de conferência da futura importação de hipóteses de cenários.

**Decisões registradas:**

- Usar a pasta de `calculadora.py` como referência, independentemente do diretório do terminal.
- Criar a pasta com `mkdir(parents=True, exist_ok=True)` e escrever o CSV com `mode="w"`.
- Exportar diretamente os dois cenários e sete colunas na ordem original, sem índice adicional.
- Preservar os valores completos, sem arredondamento de exibição ou passagem por float.
- Ignorar a pasta gerada com `/resultados/` no `.gitignore`, preservando as regras anteriores.
- Manter a exportação no bloco principal, sem efeitos ao importar o módulo.

**Contribuição para o projeto:** a exportação foi concluída. As verificações pontuais confirmaram
duas linhas de dados, sete colunas, cabeçalhos, ordem e acentos. Os oito valores financeiros foram
lidos como texto e convertidos diretamente para Decimal, com igualdade exata aos originais,
incluindo suas casas decimais. O valor `Decimal("1.23456789")` também foi preservado em escrita e
leitura com arquivo temporário, sem inserção nos cenários reais.

A lista e os quatro DataFrames permaneceram iguais, incluindo valores, tipos, colunas, índices
e ordem. A execução repetida a partir de outra pasta regenerou o mesmo CSV, sem acumular linhas.
A importação não imprimiu resultados, não criou o arquivo ausente e não modificou o existente.
O Git confirmou que o CSV está ignorado, e as saídas anteriores do terminal foram preservadas.

Os 111 testes existentes passaram durante a implementação. A suíte atual continua com 111 métodos
em 11 classes, com uso de subtests em parte dos métodos. Não foram adicionados testes persistentes
de exportação; as conferências específicas foram roteiros pontuais em memória e arquivo temporário.
A importação de hipóteses por CSV continua planejada, sem funcionalidade de entrada neste incremento.

**Marco deste registro:** documentação de 07/11/2026, até a exportação da tabela para CSV.

## 28. Leitura e validação de hipóteses de cenários por CSV

**Data:** 07/11/2026.

**Etapa:** primeira parte da importação, ainda separada da execução principal.

**Objetivo dos pedidos:** ler hipóteses de consumo com validação explícita, fornecer um exemplo
e acrescentar testes automatizados, preservando os cálculos e a exportação existentes.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar `ler_cenarios_csv(caminho)` usando Pandas, com leitura inicial como texto, validação das sete
colunas e conversões compatíveis com as funções atuais. Acrescentar o exemplo de 100 e 500 usuários
e testes com arquivos temporários. Identificar registro e coluna nos erros de campo e impedir
perda silenciosa de dados. Documentar somente o comportamento implementado, distinguindo a função
disponível da integração principal pendente, sem commit ou push.

**Participação e aprendizado:** as explicações abordaram inferência de tipos, leitura como texto,
conversões explícitas, proporções entre 0 e 1 e o retorno de dicionários independentes.
Também diferenciaram hipóteses de consumo, dados financeiros e resultados exportados.

**Decisões registradas:**

- Usar `dtype=str`, `keep_default_na=False`, vírgula e UTF-8 com ou sem BOM em `pd.read_csv()`.
- Conferir colunas antes dos registros, remover espaços externos e rejeitar campos vazios.
- Converter usuários diretamente para int e as demais hipóteses para float, aceitando médias
  fracionárias e reutilizando as validações de números finitos e não negativos.
- Exigir taxas entre 0 e 1 e rejeitar usuários com representação fracionária, sem truncamento.
- Retornar uma lista com `nome` e `hipoteses_consumo` por registro, preservando a ordem.
- Rejeitar arquivos inválidos sem retorno parcial, preservando `FileNotFoundError` quando ausentes.
- Criar `dados/cenarios_exemplo.csv` somente com nome e seis hipóteses de consumo.
- Manter cenários do código e exportação no fluxo principal; a nova função ainda não é chamada ali.

**Contribuição para o projeto:** a função, o exemplo e 25 novos métodos persistentes de teste foram
implementados. A leitura do exemplo preservou nomes, ordem e tipos e produziu 2.200 e 11.000
feedbacks ao chamar `calcular_consumo_cenario`. Os testes cobrem entradas válidas, BOM, espaços,
independência, ausência de arquivo, arquivos vazios, colunas incorretas, campos vazios, regras
numéricas, limites aceitos, arquivos malformados e mensagens com registro e coluna.

A suíte completa passou com 136 métodos em 12 classes. Subtests exercitam várias entradas dentro
de alguns métodos e não aumentam essa contagem. A classe de leitura usa arquivos temporários para
os casos de validação e também verifica importação sem leitura, impressão ou geração de arquivos.
As conferências de igualdade da saída principal e de preservação das funções e do bloco principal
foram pontuais; não devem ser confundidas com os novos testes persistentes da função de leitura.

A calculadora foi executada com a `.venv-win` e manteve a saída anterior. O CSV de exemplo pode ser
versionado. Integrar os cenários importados ao fluxo principal será o próximo incremento; a chamada
manual da função não calcula cenários nem substitui as hipóteses definidas no código.

**Marco deste registro:** documentação de 07/11/2026, até a leitura validada de cenários por CSV.

## 29. Integração dos cenários do CSV ao fluxo principal

**Data:** 07/11/2026.

**Etapa:** execução completa com hipóteses de consumo importadas.

**Objetivo dos pedidos:** utilizar os cenários lidos nas análises e na exportação, preservando
as funções, a precisão monetária e os resultados anteriores diante de falhas de leitura.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Localizar o CSV pela pasta da calculadora e validar todos os registros antes dos cálculos.
Substituir a lista manual, associar capacidade independente e reutilizar o fluxo existente.
Detalhar o primeiro cenário e encerrar com erro claro se a leitura falhar, sem gerar saídas.
Acrescentar testes de integração temporários e documentar somente o comportamento implementado,
preservando os demais arquivos nesta revisão, sem commit ou push.

**Participação e aprendizado:** as explicações abordaram caminhos relativos ao script, validação
antes de produzir resultados, cópias de capacidade e reutilização das funções de cálculo.
Também distinguiram a ordem dos registros da ordenação própria da comparação por custo.

**Decisões registradas:**

- Ler `dados/cenarios_exemplo.csv` com referência em `Path(__file__).resolve().parent`.
- Usar a lista retornada por `ler_cenarios_csv`, aceitando qualquer quantidade não vazia de
  cenários válidos, sem alternativa fixa quando a leitura falhar.
- Associar uma cópia de `hipoteses_capacidade` a cada cenário; manter preços e cotação separados.
- Identificar e utilizar o primeiro cenário do CSV no detalhamento individual.
- Remover o dicionário inicial fixo de consumo, `consumo_100_usuarios`, `consumo_500_usuarios`
  e a construção manual da lista de cenários.
- Preservar análises, formatação, Decimal e exportação; retirar a referência fixa a dois cenários
  do título do resumo para admitir outros arquivos válidos.
- Tratar falhas de leitura somente no fluxo principal, com mensagem e saída diferente de zero,
  preservando as exceções da função isolada e os arquivos de resultados anteriores.

**Contribuição para o projeto:** a integração foi concluída. Os testes confirmaram os cenários de
100 e 500 usuários, com 2.200 e 11.000 feedbacks, totais mensais de R$ 67,20 e R$ 76,00 e anuais
de R$ 806,40 e R$ 912,00. Também conferiram tabela, ordenação, filtro, saldos, agregações e Decimal
nas colunas financeiras, além da exportação com precisão completa.

Um CSV temporário com somente 200 usuários produziu 4.400 feedbacks, R$ 4,40 de IA, R$ 69,40 de
total mensal e R$ 832,80 anuais, chegando às tabelas e à exportação. Um arquivo com três cenários
confirmou a ordem original e a ordenação separada por custo. O exemplo versionado foi preservado.

Foram acrescentados oito métodos persistentes em `TestIntegracaoCenariosCsv`, usando cópias
temporárias da aplicação, entradas e saídas temporárias. Eles conferem também independência da
capacidade, execução de outra pasta e erros por arquivo ausente, inválido ou incompleto, sem
sobrescrever resultados ou produzir saídas parciais. O teste existente de importação silenciosa
continuou passando, sem leitura, impressão ou exportação ao importar o módulo.

A suíte completa passou com 144 métodos em 13 classes. Subtests não aumentam essa contagem.
A execução real da calculadora confirmou os resultados do exemplo; a comparação das funções
existentes foi uma verificação pontual, sem alteração de seus cálculos ou da função de leitura.

**Marco deste registro:** documentação de 07/11/2026, até o fluxo principal integrado ao CSV.

## 30. Escolha do modo e entrada manual de um cenário

**Data:** 07/11/2026.

**Etapa:** preenchimento pelo terminal com validação e reutilização do fluxo existente.

**Objetivo dos pedidos:** escolher entre CSV e um cenário manual, corrigir entradas inválidas
por campo e preservar precisão, configurações e resultados anteriores em caso de cancelamento.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar um menu com duas opções e `ler_cenario_terminal()`, solicitando nome e seis hipóteses com
unidades. Validar os textos digitados, repetir somente o campo incorreto e permitir cancelamento
sem exportação. Encaminhar os dois modos ao mesmo fluxo, sem exigir CSV no modo manual.
Simular a digitação nos testes, adaptar o modo CSV e documentar apenas as convenções implementadas,
sem alterar os demais arquivos nesta revisão e sem commit ou push.

**Participação e aprendizado:** as explicações abordaram o retorno textual de `input()`, as
conversões numéricas, a repetição para correção, a validação compartilhada e a simulação de entradas
com `unittest.mock.patch`.

**Decisões registradas:**

- Oferecer opção 1 para o CSV atual e 2 para um cenário manual; repetir opções inválidas.
- Retornar `nome` e `hipoteses_consumo` na leitura manual, removendo espaços externos.
- Converter usuários diretamente para int e as demais hipóteses para float, sem truncar usuários.
- Compartilhar `converter_hipotese_consumo` entre CSV e terminal, com tratamento próprio de erros
  de conversão e posterior validação numérica, preservando os contratos de leitura e cálculo.
- Exigir nome preenchido, números finitos e não negativos e taxas de 0 a 1; repetir só o campo inválido.
- Usar ponto decimal, inclusive na saída financeira. Vírgula decimal, taxas de 0 a 100 e saída
  monetária localizada no padrão brasileiro não foram implementadas.
- Tratar Ctrl+C e fim da entrada antes dos cálculos, com mensagem e encerramento sem exportação.
- Encaminhar o cenário manual como lista de um elemento ao mesmo fluxo, mantendo preços, cotação,
  capacidade, orçamento, Decimal e apresentação com duas casas decimais.

**Contribuição para o projeto:** o modo manual foi implementado sem leitura ou exigência do CSV.
O cenário de 100 usuários confirmou 2.200 feedbacks, IA mensal de `Decimal("2.20")`, total mensal
de `Decimal("67.20")` e anual de `Decimal("806.40")`. Com um cenário, os extremos mensais são
iguais e a diferença é zero. Os testes confirmaram igualdade entre tabelas e exportações dos dois
modos para as mesmas hipóteses.

Foram acrescentados 14 métodos persistentes: sete de leitura manual e sete de integração.
Eles simulam `input()` com `patch` e conferem estrutura, tipos, unidades, regras de entrada,
repetição do campo, opções inválidas, modo manual sem CSV e cancelamento por EOF ou Ctrl+C.
Também confirmam preservação de resultados anteriores e ausência de novas saídas no cancelamento.
Os testes CSV foram adaptados para selecionar explicitamente a opção 1; as saídas de integração
são temporárias. A importação do módulo continua sem perguntas, leitura ou exportação.

A suíte completa passou com 158 métodos em 14 classes. Subtests não aumentam essa contagem.
As conferências de entrada e integração descritas acima são testes persistentes; a comparação
das funções de cálculo existentes foi uma verificação pontual de preservação do escopo.

**Marco deste registro:** documentação de 07/11/2026, até o menu e a entrada manual de cenários.

## 31. MVP no terminal focado em custos de IA e apresentação brasileira

**Data:** 08/11/2026.

**Etapa:** simplificação do fluxo principal e alinhamento da documentação ao MVP de IA.

**Objetivo dos pedidos:** concentrar a versão atual nas estimativas de feedbacks de IA, melhorar a
legibilidade do terminal e preservar precisão, funções reutilizáveis e testes das etapas anteriores.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Melhorar mensagens e apresentação monetária; simplificar o cálculo e a saída para IA, mantendo os
modos CSV e manual. Retirar infraestrutura e orçamento da execução principal sem eliminar as
funções de infraestrutura e cálculo completo nem seus testes. Exportar as mesmas nove informações
da tabela final, com precisão completa. Atualizar README e planejamento conforme a implementação,
preservando os registros históricos e sem commit ou push.

**Participação e aprendizado:** as explicações distinguiram os dados Decimal dos textos exibidos,
a composição do consumo e a coordenação dos custos de IA. A simplificação separou o escopo da
calculadora no terminal da visão futura de custos completos e dashboard.

**Decisões registradas:**

- Usar `formatar_moeda_br()` e formatadores em `to_string()` para milhares, vírgula decimal e duas
  casas, com R$ ou US$ em cada valor financeiro da tabela, sem float ou dependência regional.
- Manter ponto decimal, taxas de 0 a 1 e as validações na entrada; não aplicar formatação ao CSV.
- Reutilizar diretamente `calcular_consumo_cenario()` e `calcular_custo_ia_cenario()` nos dois modos.
- Retirar associação de capacidade, infraestrutura, totais operacionais, orçamento, filtro e saldo
  do bloco principal; preservar `calcular_custo_servico()`, `calcular_custo_infra_cenario()` e
  `calcular_cenario()` e seus testes para evolução futura.
- Apresentar modelo, tarifas e cotação configurados, uma tabela na ordem de entrada e, somente com
  múltiplos cenários, menor custo de IA mensal em BRL, maior e diferença.
- Exportar nove colunas: cenário, usuários, feedbacks, tokens de entrada e saída, IA mensal em USD
  e BRL e IA anual em USD e BRL. Infraestrutura e totais operacionais saíram do CSV de resultados;
  o formato de entrada foi preservado.
- Manter Decimal nos dados, valores completos na exportação e anual constante de 12 meses.
- Adiar a definição da fonte e a implementação da consulta cambial com opção manual; consolidar
  documentação e validar instalação antes de fechar o MVP no terminal. Dashboard continua futuro.

**Contribuição para o projeto:** a simplificação está implementada. O exemplo de 100 usuários
produz 2.200 feedbacks, 1.100.000/660.000 tokens de entrada/saída, IA mensal de US$ 0,44/R$ 2,20 e
anual de US$ 5,28/R$ 26,40. Para 500 usuários, são 11.000 feedbacks, 5.500.000/3.300.000 tokens,
US$ 2,20/R$ 11,00 mensais e US$ 26,40/R$ 132,00 anuais. Não são custos operacionais completos.

A suíte atual tem 165 métodos em 15 classes e passou nesta atualização da documentação, com
`python -X utf8 -B -m unittest -q` usando a `.venv-win`. Inclui quatro métodos persistentes de
formatação e 18 de integração. As integrações foram ajustadas ao contrato de nove colunas de IA,
aos dois modos e à saída única; comprovam ausência de chamadas aos cálculos de infraestrutura e
cenário completo, preservação de Decimal, símbolos monetários, erros e cancelamento sem sobrescrita.
Usam digitação simulada e arquivos temporários. O cenário único de 200 usuários é coberto com
4.400 feedbacks e IA de US$ 0,88/R$ 4,40 mensais e US$ 10,56/R$ 52,80 anuais.

Os 111 métodos das funções de cálculo e coordenadoras permanecem, incluindo infraestrutura e
cenário completo. Subtests não aumentam a contagem. A conferência do código, dos cabeçalhos e da
preservação do escopo nesta revisão é pontual; esta edição modifica somente os três documentos e
não cria novos testes automatizados. Os registros anteriores retratam os escopos de suas datas.

**Marco deste registro:** documentação de 08/11/2026, com MVP de IA no terminal e consulta cambial
pendente, sem integração real com APIs de IA nem validação de qualidade pedagógica.

## 32. Consulta cambial pelo Banco Central e alternativa manual

**Data:** 14/11/2026.

**Etapa:** cotação automática ou manual integrada ao MVP de custos de IA no terminal.

**Objetivo dos pedidos:** consultar o dólar de venda diário do BCB, preservar a opção manual e a
precisão Decimal, sem depender da internet na suíte nem modificar o formato do CSV de resultados.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar uma função de consulta sem interação e outra para escolher a origem da cotação depois de
validar os cenários. Usar BCB/SGS série 1, tratar falhas com alternativa manual ou cancelamento e
preservar resultados anteriores. Mostrar origem e data automática, sem chamar a taxa de câmbio em
tempo real. Simular API e digitação nos testes e atualizar somente a documentação nesta revisão,
sem instalar pacotes, fazer commit ou push.

**Participação e aprendizado:** as explicações abordaram requisição HTTP por HTTPS, JSON, timeout,
conversão direta de texto para Decimal, datas ISO e separação entre consulta, interação e cálculo.
Também distinguiram respostas simuladas de conferência real e precisão interna de apresentação.

**Decisões registradas:**

- Adotar o Banco Central, SGS série 1, dólar americano de venda, diário, com unidade BRL por USD;
  consulta pública e gratuita, sem chave de API. A fonte oficial e o endpoint estão no planejamento.
- Usar `consultar_cotacao_bcb()` com `urllib.request`, `json` e timeout de 10 segundos, mantendo a
  verificação HTTPS padrão. Fazer uma única consulta, sem repetição automática ou taxa substituta.
- Validar lista de um registro, campos textuais, data válida e taxa finita e positiva. Converter
  diretamente para Decimal e retornar `brl_por_usd`, `origem` e `data_cotacao` em ISO.
- Usar `ler_cotacao_terminal()` após obter cenários válidos, aplicando a mesma taxa a todos eles.
- Permitir entrada manual sem rede, com ponto decimal, sem milhares e repetição do campo inválido;
  rejeitar vazio, texto inválido, zero, negativos, infinito e NaN. Não atribuir data do BCB ao manual.
- Tratar falhas esperadas com `ErroCotacaoBCB` e oferecer entrada manual ou cancelamento. Ctrl+C,
  fim da entrada e cancelamento explícito encerram antes da exportação, preservando resultados.
- Apresentar a última cotação diária disponível do BCB, com origem e data de referência brasileira,
  que pode ser anterior à execução. A taxa não inclui necessariamente adicionais do pagamento.
- Mostrar pelo menos quatro casas na cotação e preservar casas adicionais da entrada manual;
  manter duas casas nos custos e precisão Decimal nos dados. Origem e data não são exportadas;
  o CSV continua com nove colunas e valores financeiros completos.
- Manter o MVP restrito a IA, sem chamadas reais às APIs dos modelos, infraestrutura ou orçamento
  no caminho principal. Importar o módulo continua sem rede, leitura, interação ou exportação.

**Contribuição para o projeto:** a consulta automática e a opção manual foram implementadas.
Foram acrescentados 23 métodos persistentes: nove de consulta, oito de interação/apresentação
cambial e seis de integração. Os testes anteriores foram adaptados às novas perguntas; o teste de
importação também impede acesso à rede. A suíte completa passou nesta revisão com **188 métodos
em 17 classes**, usando a `.venv-win` e `python -X utf8 -B -m unittest -q`. Subtests não ampliam
essa contagem, e esta atualização documental não cria novos testes.

Os testes simulam respostas e `input()`, cobrindo timeout, HTTP/rede, leitura incompleta, JSON e
codificação inválidos, estrutura, campos, tipos, datas e taxas inválidas. Conferem modo manual sem
rede, falha seguida de preenchimento manual, cancelamento sem exportação e uma única consulta
para múltiplos cenários, usando arquivos temporários para resultados.

A taxa manual de `Decimal("5.00")` preserva os exemplos didáticos. Com taxa simulada de
`Decimal("6.2500")`, os custos mensais em BRL ficam R$ 2,75 e R$ 13,75 para 100 e 500 usuários;
consumo e custos em USD permanecem iguais. A entrada manual com casas adicionais preserva tanto
a identificação da taxa quanto a exportação financeira completa.

Separadamente, na implementação foi realizada uma consulta real em 14/11/2026, que retornou
`Decimal("5.6518")` para a observação de 13/11/2026. Essa conferência pontual não integra a suíte,
não fixa uma cotação atual permanente e não comprova disponibilidade futura da API. A pesquisa
documental de 14/11/2026 é distinta da data da observação e do momento de acesso ao endpoint.

**Marco deste registro:** consulta automática e alternativa manual concluídas; documentação e
roteiro alinhados. Consolidação de dependências, validação em ambiente limpo e publicação da versão
do MVP permanecem etapas próprias, sem declaração de conclusão nesta revisão.

## 33. Dependências fixadas e validação do MVP em ambiente novo

**Data:** 14/11/2026.

**Etapa:** preparo reproduzível do ambiente e registro da validação do MVP de custos de IA.

**Objetivo dos pedidos:** organizar somente as dependências necessárias, validar a instalação em
ambiente isolado novo e documentar os resultados, preservando os ambientes e arquivos existentes.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Conferir imports e metadados, criar requirements com versões exatas do conjunto já testado e copiar
os arquivos atuais para uma pasta temporária exclusiva. Criar um ambiente novo com o Python base
convencional, instalar pelo requirements, verificar isolamento, dependências, testes, execuções e
exportação. Depois, atualizar somente README, planejamento e este registro com as evidências,
sem alterar código, testes ou requisitos nesta revisão e sem commit, tag, release ou push.

**Participação e aprendizado:** as explicações distinguiram dependências diretas, indiretas e
biblioteca padrão; interpretador base e ambiente virtual; instalação que pode precisar de internet
e execução com cotação manual sem rede. As versões fixadas descrevem o conjunto validado, sem
constituir um lock completo ou garantia universal de reprodução.

**Decisões registradas:**

- Criar `requirements.txt` em UTF-8, após confirmar que não havia arquivo de dependências existente.
- Registrar Pandas `3.1.0` como dependência direta; NumPy `2.5.4`, python-dateutil `4.0.0` e
  tzdata `2026.6` como indiretas, com base nos metadados da `.venv-win`, sem atualizar seus pacotes.
- Não incluir pip, módulos da biblioteca padrão, ferramentas opcionais ou pacotes sem relação.
- Usar Python convencional `3.14.10` x64, plataforma `win-amd64`, no Windows 11, build 26300;
  confirmar o executável base da instalação `Python314`, sem usar MSYS2.
- Copiar somente código, testes, CSV de exemplo e requirements atuais, incluindo arquivos ainda
  sem commit, sem copiar ambientes, `.git`, caches, credenciais ou resultados anteriores.
- Criar um ambiente isolado na pasta temporária, sem pacotes globais ou do usuário, e instalar
  somente com seu próprio Python e `python -m pip install -r requirements.txt`.
- Preservar `.venv`, `.venv-win`, Python global, configurações, PATH e políticas do PowerShell.
- Limpar somente a pasta temporária desta tarefa, depois de conferir seu caminho.

**Contribuição para o projeto:** organização de dependências e validação concluídas em 14/11/2026.
A instalação usou wheels, sem compilação, com as quatro versões iguais ao requirements.
`python -m pip check` retornou **No broken requirements found** e a suíte da cópia passou com
**188 métodos em 17 classes**, usando `python -X utf8 -B -m unittest -q`. A primeira instalação
falhou por resolução de rede do PyPI; a repetição autorizada com acesso permitido funcionou,
sem mudar requisitos nem instalar pacotes avulsos para contornar o arquivo.

As verificações pontuais executaram CSV de 100 e 500 usuários e um cenário manual de 100 usuários
com cotação `Decimal("5.00")`, a partir de outra pasta, com conexões e DNS bloqueados. Confirmaram:

- 100 usuários: IA mensal US$ 0,44/R$ 2,20 e anual US$ 5,28/R$ 26,40.
- 500 usuários: IA mensal US$ 2,20/R$ 11,00 e anual US$ 26,40/R$ 132,00.
- Apresentação brasileira, nove colunas exportadas, acentos e reexecução sem duplicar linhas.
- Modo manual mesmo sem o CSV disponível e importação sem interação, rede, leitura ou exportação.
- Precisão além da segunda casa, recuperando `2.254320987160` do texto diretamente como Decimal,
  com taxa manual de mais casas, sem passar por float.

Essas conferências não acrescentaram testes automatizados persistentes; a contagem continua em
188 métodos, sem contar subtests como métodos adicionais. A suíte usa respostas simuladas do BCB,
sem depender da internet ou da cotação do dia. A consulta real registrada na etapa anterior é uma
conferência distinta, não uma nova consulta realizada nesta validação.

A pasta temporária foi removida. A conferência dos conteúdos confirmou a preservação de código,
testes, CSV de exemplo, resultados, documentos e configurações originais durante a validação;
os ambientes existentes também foram preservados. O único arquivo criado naquela tarefa foi
requirements. Esta revisão posterior modifica somente os três documentos e mantém esse arquivo.
As instruções de clonagem e preparo do README orientam futuras instalações; não representam uma
clonagem ou nova instalação executada nesta atualização documental.

**Marco deste registro:** dependências e validação concluídas em ambiente virtual novo neste
Windows, sem comprovação de outro computador, sistema ou reinstalação do Python. A revisão final
da documentação e a publicação da primeira versão do MVP no terminal permanecem pendentes.
O projeto continua estimando somente IA, sem chamadas reais às APIs dos modelos.

## 34. Revisão final e preparação local da primeira release

**Data:** 14/11/2026.

**Etapa:** revisão técnica do MVP e notas propostas para v0.1.0, sem publicação.

**Objetivo dos pedidos:** conferir funcionamento, documentação, arquivos versionados e limites,
preparando os materiais da primeira release sem alterar código, configurações ou o remoto.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Revisar entradas, validações, câmbio, custos exclusivamente de IA, Decimal, apresentação e CSV.
Conferir instalação descrita no README, licença, Git e tags; executar testes e Markdownlint sem
reinstalar dependências. Preparar RELEASE_NOTES e orientar a publicação posterior sobre o commit
final, sem criar licença, commit, tag ou release nesta tarefa.

**Participação e aprendizado:** as explicações distinguiram revisão técnica, aprovação dos materiais,
commit final, tag e release. Também separaram a distribuição do programa de terminal da hospedagem
de um dashboard e a situação do código dos termos próprios de dependências e dados de terceiros.

**Decisões registradas:**

- Revisar `main` no commit `3ebf7f745e6389fa239f7a4dc43057f6e07af11e`, sem mudanças pendentes ao iniciar.
- Propor v0.1.0 após confirmar ausência de tags locais e remotas, sem criar ou substituir tags.
- Criar `RELEASE_NOTES.md` como material local para revisão, com escopo, início de uso, ambiente,
  verificações, limitações, evoluções futuras e sequência de publicação.
- Corrigir descrições desatualizadas: requirements e CSV de exemplo já estão versionados.
- Confirmar que `.venv`, `.venv-win` e resultados estão ignorados; a `.venv-win` usa o `.gitignore`
  criado dentro do ambiente. Não alterar regras nem incluir ambientes ou resultados como anexos.
- Registrar ausência de LICENSE e avaliação de MIT, sem adoção autorizada ou atribuição de titular.
  A decisão fica pendente, sem ser tratada como impedimento técnico para publicar.

**Contribuição para o projeto:** não foram encontrados defeitos funcionais nos fluxos verificados.
Os **188 métodos em 17 classes passaram** na `.venv-win`, com `python -X utf8 -B -m unittest -q`.
`pip check` retornou **No broken requirements found**. A verificação de Markdown incluiu os três
registros documentais e as notas da versão. Não houve novos testes persistentes nem instalação;
a validação limpa anterior foi preservada porque código e dependências não mudaram.

As conferências de Git, documentação, licença e arquivos ignorados foram pontuais. Os ajustes
foram somente documentais. O histórico anterior foi preservado, sem reescrever decisões passadas.
A publicação futura deverá incorporar as notas e ajustes ainda sem commit, enviar o commit final
ao GitHub e criar a tag/release sobre ele; o commit base revisado não contém estes novos materiais.

**Marco deste registro:** revisão técnica final e materiais locais preparados. Aprovação dos
materiais, revisão da situação de licença, commit final, push, tag e release continuam posteriores.
O MVP permanece uma calculadora de IA no terminal, sem dashboard hospedado ou chamadas às APIs dos
modelos. Nenhuma alteração remota foi realizada.

## 35. Adoção explícita da licença MIT

**Data:** 14/11/2026.

**Etapa:** formalização da licença do código e alinhamento dos materiais da primeira versão.

**Objetivo dos pedidos:** adotar a MIT com autorização explícita, preservar as alterações da revisão
final e manter a primeira release como preparação, sem publicar.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar LICENSE com o texto padrão integral da MIT em inglês, ano atual e titular confirmado.
Atualizar README, planejamento e notas da versão, retirando a escolha da licença das pendências.
Conferir o texto e os links e executar Markdownlint, sem modificar código, testes, requisitos,
configurações ou CSVs e sem commit, push, tag ou release.

**Participação e aprendizado:** a decisão distinguiu os direitos de uso do código das condições
próprias de dependências e dados de terceiros. A identificação do titular foi solicitada ao
responsável, sem inferência a partir da conta do Windows, caminhos ou nomes no histórico.

**Decisões registradas:**

- Adotar MIT por escolha explícita e autorizada, com referência ao texto de Choose a License.
- Criar LICENSE na raiz, mantendo integralmente as cláusulas em inglês, com ano de 2026.
- Usar o titular confirmado: Natan Fernando.
- Declarar MIT e vincular LICENSE no README e nas notas da versão; manter as permissões de uso,
  modificação e distribuição, inclusive comercial, com preservação dos avisos exigidos.
- Registrar a escolha como concluída no planejamento somente após finalizar o arquivo.
- Preservar as licenças e condições próprias das dependências e fontes de dados.
- Manter somente a revisão/aprovação dos materiais, o commit final, o envio e a criação da
  tag/release como etapas posteriores, sem declarar publicação.

**Contribuição para o projeto:** LICENSE foi finalizado e os quatro documentos foram alinhados.
O texto foi conferido contra a referência, com ano e titular preenchidos, sem marcadores pendentes.
A verificação de Markdown abrangeu os quatro documentos, sem aplicar formatação ao texto jurídico.
O histórico anterior e as alterações documentais da revisão final foram preservados.

Não houve alteração de código, testes ou dependências. A suíte de 188 métodos aprovada na revisão
final não foi repetida, pois esta tarefa é documental. As conferências da licença e das referências
são verificações pontuais, não novos testes automatizados.

**Marco deste registro:** licença MIT concluída, com decisão registrada em 14/11/2026. O MVP continua
focado em custos de IA no terminal, e a primeira versão permanece preparada para publicação futura.
Nenhum commit, push, tag ou release foi realizado nesta tarefa.

## 36. Planejamento do estudo de caso e divulgação no README

**Data:** 18/11/2026.

**Etapa:** planejamento do estudo de caso do Google Data Analytics Professional Certificate.

**Objetivo dos pedidos:** definir pergunta, cenários, dados e etapas de uma análise de estimativas
com a calculadora, mantendo clara a diferença entre planejamento e trabalho executado.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar ESTUDO_DE_CASO.md com contexto, premissas, 13 cenários, proveniência, indicadores, etapas,
limitações e critérios de conclusão. Depois, apresentar brevemente esse planejamento no README,
com link relativo, e consolidar o registro dos pedidos, sem executar análise ou alterar o MVP.

**Participação e aprendizado:** o planejamento distinguiu hipóteses, tarifas pesquisadas, câmbio e
resultados derivados; definiu unidade de análise, referências e denominadores e separou comparação
de políticas da sensibilidade de tokens. Nenhum resultado foi produzido para o estudo.

**Decisões registradas:**

- Usar a calculadora v0.1.0 publicada como ferramenta e referência histórica, sem modificar sua tag
  ou apresentar o estudo como nova versão do MVP.
- Perguntar como usuários, política de feedback nos acertos e consumo de tokens afetam o custo
  mensal estimado de IA, sem dados reais de utilização dos estudantes.
- Planejar C01 a C09 cruzando 100, 500 e 1000 usuários com proporções de acertos com feedback
  0, 0.25 e 1, mantendo as demais hipóteses constantes.
- Usar C05 como referência de sensibilidade e variar somente uma entrada de tokens em C10 a C13.
- Separar tarifas e condições a revalidar, câmbio fixo a definir, hipóteses e resultados futuros,
  sem tratar preços históricos como atuais nem inventar fontes, datas de coleta ou custos.
- Organizar as etapas Perguntar, Preparar, Processar, Analisar, Compartilhar e Agir. Planejar dois
  gráficos e relatório, ainda não executados, e registrar apoio de IA conforme a atividade.
- Excluir infraestrutura, receitas, comparação de modelos e dashboard. Preservar Decimal nos
  cálculos monetários e arredondar somente a apresentação, quando a análise for realizada.
- Não tratar cenários como amostra estatística nem custo menor como comprovação de qualidade
  pedagógica equivalente, conclusão do estudo, aprovação do curso ou validação pelo Google.

**Contribuição para o projeto:** ESTUDO_DE_CASO.md foi criado na etapa documental anterior.
A conferência pontual confirmou 13 combinações distintas: nove principais e quatro de sensibilidade,
com C05 correto e uma única entrada de tokens alterada em cada variação. A verificação de Markdown
passou nessa criação, sem executar análise ou testes do MVP.

Nesta atualização, somente README e este registro foram alterados. O README apresenta pergunta,
desenho e situação do estudo, com link relativo para o planejamento, sem reproduzir a matriz.
As descrições antigas de preparação da primeira release foram ajustadas à v0.1.0 publicada informada
no pedido, preservando o escopo de IA no terminal. ESTUDO_DE_CASO.md e os demais arquivos foram
preservados, assim como os registros históricos anteriores. As verificações são documentais e
pontuais; nenhum teste automatizado persistente foi acrescentado ou repetido.

**Marco deste registro:** planejamento documentado, sem análise, gráficos ou relatório executados.
Os próximos passos são revisar e confirmar a matriz, revalidar modelo, tarifas e condições e definir
a cotação fixa; somente depois preparar os dados e executar a análise. Nenhum commit ou push faz
parte desta atualização.

## 37. Condições fixas de modelo, tarifas e câmbio do estudo de caso

**Data:** 18/11/2026.

**Etapa:** registro da revalidação documental e definição das condições fixas, antes da análise.

**Objetivo dos pedidos:** documentar modelo, tarifas e cotação constantes para comparar os 13
cenários de forma reproduzível, sem misturar mudanças de preço ou câmbio com as hipóteses variadas.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Conferir as fontes oficiais e registrar em ESTUDO_DE_CASO.md as condições propostas, distinguindo
Standard de outras modalidades, disponibilidade no catálogo de acesso à conta e cotação histórica
de uma consulta dinâmica. Depois, atualizar somente README e este registro com as condições já
documentadas, sem nova pesquisa de preços ou câmbio, geração de CSVs ou execução dos cenários.

**Participação e aprendizado:** as explicações distinguiram pesquisa documental, acesso à API e
medição real; tokens por requisição e totais mensais; dados de entrada, custos em USD e conversão
para BRL. A escolha de um modelo e condições constantes permite isolar os efeitos das hipóteses.

**Decisões registradas:**

- Fixar OpenAI, API direta, GPT-6 Luna (`gpt-6-luna`), Standard para texto e contexto curto.
- Registrar entrada sem cache de `Decimal("0.10")` USD por milhão de tokens e saída faturável de
  `Decimal("0.50")` USD por milhão. Data da pesquisa: **2026-11-18**.
- Fixar `Decimal("5.8102")` BRL por USD, Banco Central, SGS série 1, dólar americano de venda diário.
  Data da observação: **2026-11-18**; data da consulta: **2026-11-18**. Nenhum horário foi inventado.
- Preservar a evidência cambial observada: data 18/11/2026 e valor textual `5.8102`.
  O endpoint últimos/1 é dinâmico; consultas futuras não atualizarão automaticamente a taxa do estudo.
- Manter os mesmos preços e a mesma cotação nos 13 cenários, inclusive na sensibilidade de tokens.
  Na execução futura, reaplicar a taxa pela opção manual, sem mudar o menu ou os cálculos do MVP.
- Preservar R$ 5,00 como cotação didática dos exemplos históricos do MVP, distinta da taxa do estudo.
- Considerar todo o consumo de saída faturável, incluindo componentes não visíveis quando existirem,
  sem dupla contagem. Os tokens continuam sendo hipóteses didáticas, não medições ou garantias.
- Manter os limites documentados: requisições curtas; sem cache, Batch/Flex, modos acelerados,
  adicionais regionais, ferramentas, tributos ou adicionais do meio de pagamento. O anual, se
  apresentado, pressupõe 12 meses sob condições constantes.

**Contribuição para o projeto:** ESTUDO_DE_CASO.md recebeu, na etapa anterior, o registro das
condições e das fontes oficiais conferidas em 2026-11-18: página do modelo, preços e sua tabela
Standard de contexto curto, depreciações, guia de raciocínio, catálogo BCB e endpoint cambial.
Não foi identificada divergência material nas condições propostas. A presença no catálogo foi
tratada como disponibilidade documentada, sem comprovação de habilitação, saldo, limites ou acesso
pela conta responsável. Não houve chamada paga, solicitação de credenciais ou teste do modelo.

A consulta pública ao BCB naquela etapa coincidiu com a evidência informada para 18/11/2026.
Isso é uma observação cambial de referência, não acesso às APIs dos modelos nem teste automatizado.
As tarifas e o câmbio são históricos e fixos para este recorte, sem validade permanente presumida.
A revalidação documental não comprova qualidade pedagógica, configuração de raciocínio testada ou
consumo real de tokens.

Nesta atualização, somente README e este registro foram alterados. Os valores e as datas foram
conferidos contra ESTUDO_DE_CASO.md, sem nova consulta de preços ou câmbio. O README resume a matriz
revisada e as condições, mantém o link relativo e distingue o estudo do MVP publicado v0.1.0,
que continua oferecendo consulta ao BCB ou cotação manual. O histórico anterior foi preservado.
As conferências foram documentais e pontuais; os testes do MVP não foram repetidos e nenhum teste
persistente foi acrescentado. As alterações pendentes do estudo foram preservadas.

**Marco deste registro:** matriz revisada e condições fixas documentadas. Preparação dos dados e
resultados dos 13 cenários, análise, gráficos, relatório e recomendações continuam pendentes.
O próximo passo será preparar os dados dos cenários e os registros das condições fixas; validar
estrutura, identificadores e cobertura antes de executar a análise e a conferência manual.
Nenhum código, CSV, dependência ou configuração foi alterado; a tag v0.1.0 permanece intacta.
Não houve commit ou push.

## 38. Preparação dos CSVs de entrada do estudo de caso

**Data:** 18/11/2026.

**Etapa:** preparação e conferência pontual dos dados, antes da validação de leitura e da análise.

**Objetivo dos pedidos:** transformar a matriz revisada e as condições fixas em arquivos de entrada
separados, preservando o funcionamento do MVP e as referências históricas do estudo.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar dados/estudo_de_caso/cenarios.csv e condicoes_fixas.csv com os campos e valores definidos,
conferir estrutura e conteúdo e atualizar somente ESTUDO_DE_CASO.md naquela etapa. Depois,
registrar a preparação no README e neste histórico, sem alterar os CSVs, executar cenários,
consultar novos preços ou câmbio, mudar o MVP ou repetir os testes de código.

**Participação e aprendizado:** as explicações distinguiram hipóteses dos cenários, condições
pesquisadas compartilhadas e resultados calculados. Também esclareceram que CSV armazena texto,
que os campos financeiros devem ser convertidos diretamente para Decimal e que uma coluna
adicional exige preparação de leitura sem modificar o importador da versão publicada.

**Decisões registradas:**

- Criar `dados/estudo_de_caso/cenarios.csv` com oito colunas e 13 registros, ordenados de C01 a C13,
  incluindo `id_cenario`, nomes descritivos únicos e as seis hipóteses da matriz revisada.
- Criar `dados/estudo_de_caso/condicoes_fixas.csv` com 12 colunas e uma linha de modelo, modalidade,
  tarifas, câmbio, fontes e datas, aplicável aos 13 cenários.
- Manter OpenAI, `gpt-6-luna`, Standard, entrada `0.10` e saída `0.50` USD por milhão de tokens e
  câmbio fixo `5.8102` BRL por USD. Pesquisa, referência e consulta cambial continuam em 2026-11-18.
- Usar UTF-8 sem BOM, vírgula, ponto decimal, cabeçalho e ausência de índice; não incluir símbolos,
  sinais de porcentagem ou separadores de milhares nas representações numéricas.
- Registrar em `fonte_cambio` o catálogo oficial BCB/SGS série 1, mantendo no estudo a evidência
  histórica do endpoint dinâmico. Não atribuir horário ou atualizar a cotação automaticamente.
- Distinguir os CSVs do estudo da entrada `dados/cenarios_exemplo.csv` e da saída
  `resultados/cenarios.csv` do MVP. Nenhum dos arquivos do estudo é lido automaticamente pelo menu.
- Explicar que `id_cenario` é adicional às sete colunas aceitas pelo importador atual, que rejeita
  colunas inesperadas. Não apresentar o CSV de cenários do estudo como diretamente compatível.
- Preservar todos os identificadores na futura leitura e manter preços e câmbio como texto até
  convertê-los diretamente para Decimal, sem float intermediário.

**Contribuição para o projeto:** os dois CSVs foram criados e ESTUDO_DE_CASO.md foi atualizado na
etapa anterior. A conferência pontual na `.venv-win` confirmou cabeçalhos e ordem, 13 registros de
cenários e uma linha de condições, UTF-8, acentos, campos obrigatórios e ausência de índice.
Confirmou 13 identificadores e nomes únicos, 13 combinações distintas, cobertura das nove
combinações principais e C05 correto. Cada variação C10 a C13 altera somente uma hipótese numérica.

Também foram conferidos usuários inteiros não negativos, médias finitas não negativas e taxas
entre 0 e 1. Os valores financeiros das condições foram lidos como texto e reconstruídos como
Decimal, confirmando positividade e correspondência exata com as referências. Fontes e datas
coincidiram com o estudo, sem divergências ou nova pesquisa. Os dois arquivos não estão ignorados
pelo Git e podem ser versionados.

Essas verificações foram pontuais, sem criação de testes automatizados persistentes ou repetição
da suíte do MVP. Não foram calculados feedbacks, tokens mensais ou custos. A preparação das entradas
não representa análise concluída, medição real de uso ou validação de qualidade pedagógica.

Nesta atualização, somente README e este registro foram alterados. O README inclui links relativos
para os dois CSVs, preserva o link do estudo e esclarece formato, responsabilidades e compatibilidade.
O histórico anterior, os CSVs, ESTUDO_DE_CASO.md, demais arquivos e alterações pendentes foram
preservados, assim como a tag v0.1.0. Não houve nova consulta de preços ou câmbio.

**Marco deste registro:** preparação e conferência pontual concluídas. O próximo passo será validar
a leitura e analisar os arquivos preparados, preservando identificadores, unidades, condições fixas
e Decimal nos cálculos monetários. Resultados, gráficos, relatório e conclusões ainda não foram
produzidos. Nenhum commit ou push foi realizado nesta atualização.

## 39. Rotina reproduzível de validação e cálculo do estudo de caso

**Data:** 18/11/2026.

**Etapa:** validação e cálculo dos arquivos preparados, antes das comparações e da interpretação.

**Objetivo dos pedidos:** tornar reproduzível o cálculo dos 13 cenários com as condições fixas,
preservando integralmente o MVP publicado, seus testes e as entradas do estudo.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar analise_estudo.py e test_analise_estudo.py, separar leitura/validação, cálculo e apresentação/
exportação, reutilizar as funções do MVP e conferir precisão e erros com arquivos temporários.
Depois, atualizar somente README.md, ESTUDO_DE_CASO.md e este histórico para registrar o estado
confirmado, sem repetir testes ou cálculos nesta etapa documental.

**Participação e aprendizado:** as explicações distinguiram texto de CSV, tipos numéricos,
validação e cálculo. As hipóteses respeitam os tipos aceitos pelo MVP; tarifas e câmbio passam
diretamente de texto para Decimal. Formatar dinheiro no terminal não substitui os dados por textos
nem limita a precisão exportada. As conferências por fórmula não são evidências sobre estudantes.

**Decisões registradas:**

- Implementar a rotina em arquivo separado, com funções pequenas, caminhos relativos à pasta do
  script, caminhos configuráveis nas funções e importação sem interação, leitura, rede ou exportação.
- Validar os esquemas próprios do estudo, campos obrigatórios, identificadores únicos C01 a C13,
  13 combinações distintas, números finitos não negativos, usuários inteiros e taxas entre 0 e 1.
- Exigir uma linha de condições fixas, tarifas e câmbio em Decimal finito e positivo e datas ISO
  válidas, mantendo as fontes e os metadados. Não atualizar referências pela internet.
- Reutilizar `converter_hipotese_consumo()`, as validações numéricas, `calcular_consumo_cenario()`,
  `calcular_custo_ia_cenario()` e a auxiliar `formatar_moeda_br()` sem modificar o MVP.
- Aplicar entrada `0.10` e saída `0.50` USD por milhão e câmbio `5.8102` BRL por USD a todos os
  cenários, conforme os arquivos e as referências de 2026-11-18, sem constantes comerciais substitutas.
- Exibir tabela curta e exportar `resultados/estudo_de_caso/resultados_cenarios.csv` com 13 linhas
  e 35 colunas: identificação, hipóteses, consumos, custos e condições com fontes e datas.
- Exportar valores completos em UTF-8, com vírgula, ponto decimal, cabeçalho e sem índice; manter
  símbolos e duas casas somente na apresentação. Validar e calcular tudo antes da gravação.

**Contribuição para o projeto:** os dois arquivos Python foram criados na implementação anterior.
Os 30 novos métodos em uma classe cobrem leitura, validações, datas, precisão, reaproveitamento,
importação sem efeitos, caminhos, reexecução e falhas sem sobrescrever resultados anteriores.
A execução conjunta em 18/11/2026 aprovou **218 métodos em 18 classes**: 188 do MVP e 30 do estudo.
Casos de `subTest` não aumentam a contagem de métodos; os testes antigos não foram alterados.

Os testes conferiram fórmulas independentes em Decimal para os 13 registros e verificaram C02
com 2200 feedbacks, 1100000 tokens de entrada, 660000 de saída e IA mensal de USD 0.44; C05 com
11000 feedbacks, 5500000 tokens de entrada, 3300000 de saída e USD 2.20. A conversão exata por
5.8102 produziu BRL 2.556488 e BRL 12.78244, respectivamente, sem arredondamento de exibição.
Também conferiram feedbacks constantes na sensibilidade e consumo/custo não decrescente com
mais feedback nos acertos dentro de cada escala. São verificações das fórmulas e hipóteses.

Separadamente, a execução real dos CSVs e a releitura do resultado confirmaram C01 a C13 na ordem,
35 colunas, condições e datas coerentes com o documento e valores financeiros reconstruídos de
texto para Decimal, sem float. Essas conferências foram pontuais, sem métodos de teste adicionais.
O CSV gerado está ignorado pela regra de resultados do Git. Não houve consultas a APIs ou instalação.

Nesta atualização, README recebeu instruções e o estado atual; ESTUDO_DE_CASO.md recebeu o fluxo,
validações, esquema, evidências e andamento das etapas. Somente esses documentos e este registro
foram editados, preservando o histórico, as entradas, os resultados e demais alterações pendentes.
Os testes e cálculos não foram repetidos nesta atualização exclusivamente documental.

**Marco deste registro:** validação, cálculo e exportação concluídos. O próximo passo é comparar
políticas dentro de cada escala e avaliar a sensibilidade dos tokens contra C05. Interpretação,
gráficos, relatório e recomendações permanecem pendentes. Os cenários não são dados observados,
o estudo não está concluído ou aprovado pelo curso e a rotina não representa nova release.
A v0.1.0 publicada e sua tag foram preservadas. Não houve commit ou push.

## 40. Comparação das políticas de feedback e sensibilidade dos tokens

**Data desta atualização documental:** 19/11/2026.

**Etapa:** registro das comparações implementadas e exportadas, antes dos gráficos e da síntese final.

**Objetivo dos pedidos:** comparar políticas dentro da mesma escala e variações de tokens contra
C05, mantendo hipóteses e condições comparáveis e preservando o MVP v0.1.0 publicado.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Acrescentar à rotina do estudo as comparações por identificador, validar os pares e condições,
calcular diferenças absolutas e percentuais com Decimal e exportar duas tabelas específicas.
Registrar depois o comportamento confirmado no README, no estudo e neste histórico, sem alterar
código ou repetir os testes nesta atualização documental.

**Participação e aprendizado:** as explicações distinguem redução de custo, calculada como
referência menos política, de variação de sensibilidade, calculada como cenário menos C05.
O percentual depende da referência correta; denominador zero não deve ser substituído por zero.
Preservar Decimal não significa precisão infinita em divisões: o contexto rege as dízimas.

**Decisões e implementação registradas:**

- `comparar_politicas()` produz seis pares: C01/C02 contra C03, C04/C05 contra C06 e C07/C08
  contra C09. As referências usam feedback em todas as respostas na mesma escala de usuários.
- `analisar_sensibilidade()` compara C10/C11 com C05 alterando somente entrada e C12/C13 alterando
  somente saída. As demais hipóteses e todos os campos de condições devem permanecer iguais.
- `_indexar_comparacoes()` e `_validar_par()` verificam colunas, identificadores, presença dos
  cenários necessários, hipóteses e condições. Ordem das linhas e índices não definem os pares.
- A rotina compara resultados já calculados, sem modificar a tabela de origem ou recalcular pelo
  MVP. As validações e ambas as comparações terminam antes de iniciar as três exportações.
- Exportar `resultados/estudo_de_caso/comparacao_politicas.csv` com seis linhas e 20 colunas e
  `resultados/estudo_de_caso/sensibilidade_tokens.csv` com quatro linhas e 24 colunas. Ambos incluem
  as condições e preservam UTF-8, vírgula, ponto decimal, cabeçalho, ausência de índice e Decimal.
- Manter dados completos no CSV, formatação somente na apresentação e percentuais não aplicáveis
  como campos vazios quando a referência for zero, preservando as diferenças absolutas.

**Resultados registrados:** as exportações existentes e os resultados esperados nos testes
mostram redução de 60% para feedback somente nos erros e de 45% para erros e 25% dos acertos,
nas três escalas. As variações contra C05 são -12,5% em C10, +25% em C11, -37,5% em C12 e +75%
em C13. Em C05, entrada custa USD 0.55 e representa 25%; saída custa USD 1.65 e representa 75%.
Essa participação foi conferida pontualmente; não é um indicador incorporado à rotina para todos
os cenários. Custo por usuário também não foi acrescentado.

**Testes e evidências:** o arquivo atual confirma 17 métodos adicionados aos 30 do estudo, somando
47; com os 188 do MVP, são **235 métodos em 18 classes**. Os novos testes cobrem referências,
fórmulas, independência da ordem e do índice, hipóteses e condições incompatíveis, campos e custos
inválidos, preservação da tabela, referência zero, contexto Decimal, exportação precisa e falha de
comparabilidade sem sobrescrever os resultados anteriores. Casos de `subTest` não são métodos extras.

A aprovação dos 235 métodos na execução anterior foi informada no pedido desta atualização.
Não foi encontrado log adicional dessa execução nos arquivos consultados; a suíte não foi repetida
em 19/11/2026. A data exata da implementação e dessa execução não foi presumida. As condições fixas
continuam com pesquisa e referência cambial de 18/11/2026, distintas desta atualização documental.

Nesta revisão, a leitura dos CSVs existentes conferiu esquemas, referências e percentuais, e uma
conferência pontual com Decimal verificou os componentes e participações de C05. Essas verificações
não executaram a rotina nem a suíte, não geraram arquivos e não acrescentaram testes persistentes.
Não houve nova pesquisa de preços, câmbio ou chamada real a APIs. Os resultados decorrem das
hipóteses e fórmulas, sem comprovar comportamento dos estudantes ou qualidade pedagógica equivalente.

**Marco deste registro:** comparações calculadas e conferidas. Gráficos, síntese final, relatório
e recomendações permanecem pendentes. Somente README.md, ESTUDO_DE_CASO.md e este histórico foram
atualizados. Código e testes pendentes do autor foram preservados, assim como entradas, resultados,
dependências, configurações e a tag v0.1.0. A rotina do estudo não representa nova release do MVP.
Não houve commit ou push.

## 41. Primeiro gráfico Plotly do estudo de caso

**Data desta atualização documental:** 19/11/2026.

**Etapa:** registro do primeiro gráfico implementado, antes da inspeção visual e da síntese final.

**Objetivo dos pedidos:** apresentar o custo mensal estimado de IA por escala e política de feedback,
preservando o MVP publicado, a precisão financeira e os dados já calculados.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar graficos_estudo.py e test_graficos_estudo.py, ler e validar o CSV de resultados sem executar
a análise automaticamente, selecionar C01 a C09 e produzir barras agrupadas com Plotly Express.
Exportar HTML completo offline, conferir a figura e executar toda a suíte. Depois, atualizar
somente README, ESTUDO_DE_CASO.md e este histórico, sem repetir testes ou gerar novos resultados
nesta etapa documental.

**Participação e aprendizado:** as explicações distinguiram dados financeiros em Decimal de uma
cópia numérica para desenhar alturas aproximadas. Os textos monetários são preparados diretamente
dos Decimal; a geometria não conserva precisão decimal exata. Barras lado a lado representam
alternativas, sem somar cenários. Testes estruturais não substituem a inspeção visual no navegador.

**Decisões e implementação registradas:**

- Ler `resultados/estudo_de_caso/resultados_cenarios.csv` inicialmente como texto e reconstruir
  os campos financeiros diretamente como Decimal, sem regravar a entrada ou consultar fontes.
- Selecionar C01 a C09 por identificador, sem depender da ordem das linhas, e conferir IDs únicos,
  campos necessários, matriz principal, números finitos não negativos, datas e condições iguais.
- Manter três escalas de 100, 500 e 1000 usuários e três séries: “Somente nos erros”,
  “Erros + 25% dos acertos” e “Todas as respostas”, com cores, padrões e barras agrupadas.
- Excluir C10 a C13. Mostrar custo mensal de IA em BRL a partir de zero e identificar cenários
  hipotéticos, modelo, modalidade, tarifas e câmbio fixos conforme os dados.
- Separar leitura/validação, criação e exportação. A função de criação retorna a figura sem gravar
  ou abrir navegador; importar o módulo não produz interação, leitura ou exportação.
- Converter somente a coluna de alturas de uma cópia de visualização para float. Usar Decimal
  para os textos monetários brasileiros das barras e do hover, sem alterar cálculos ou CSVs.
- Exportar `resultados/estudo_de_caso/custo_mensal_por_escala_politica.html` com `full_html=True`,
  `include_plotlyjs=True` e `auto_open=False`, com a biblioteca incorporada para uso offline.
  Orientar abertura manual e preservar um HTML anterior diante de dados inválidos.

**Dependências:** na implementação de 19/11/2026 foram instalados somente `plotly==7.1.0`, direto,
`narwhals==2.29.0` e `packaging==26.3`, indiretos necessários. As versões foram registradas em
requirements.txt, preservando as entradas e os pacotes anteriores. `pip check` não encontrou
problemas. Não foram instalados Kaleido, navegadores, Dash ou ferramentas opcionais. Não foi
repetida a instalação em ambiente limpo com esse conjunto ampliado.

**Testes e evidências:** test_graficos_estudo.py acrescentou 18 métodos em uma classe com unittest,
dados controlados e temporários. Conferem nove barras, três séries, ordens, associações por ID,
alturas aproximadas, textos monetários, preservação dos dados, validações, importação sem efeitos
e HTML completo com Plotly incorporado. Também verificam que falhas preservam o HTML anterior.
Os 18 métodos novos passaram e a execução conjunta em 19/11/2026 aprovou **253 métodos em
19 classes**: 188 do MVP, 47 da análise e 18 do gráfico. Casos de subTest não são métodos extras.

Após os testes, o HTML real foi gerado. A conferência pontual confirmou a estrutura da figura,
correspondência das alturas e textos com os Decimal, biblioteca incorporada e preservação dos CSVs
e arquivos protegidos. Essa conferência não é um novo teste persistente. **Não houve inspeção
visual da renderização**: legibilidade, margens, sobreposições e legenda continuam por revisar
manualmente no navegador.

Nesta atualização documental, apenas README.md, ESTUDO_DE_CASO.md e este registro foram editados.
Não foram repetidos testes, cálculo, instalação ou geração de HTML. As alterações pendentes do
autor, código, testes, requirements, CSVs, HTML e demais arquivos foram preservados.

**Marco deste registro:** primeiro gráfico implementado e gerado, com revisão visual pendente.
Gráfico de sensibilidade, exportação em imagem, dashboard, síntese final e recomendações não foram
concluídos. As estimativas não comprovam uso real dos estudantes ou qualidade pedagógica equivalente.
A evolução do estudo não representa nova release; o MVP v0.1.0 publicado e sua tag permanecem
preservados. Não houve commit ou push.

## 42. Segundo gráfico do estudo: sensibilidade dos tokens contra C05

**Data desta atualização documental:** 19/11/2026.

**Etapa:** registro do segundo gráfico implementado e integrado, com revisão visual pendente.

**Objetivo dos pedidos:** apresentar as quatro variações de custo mensal de IA contra C05,
preservando o primeiro gráfico, os resultados financeiros, a rotina de análise e o MVP v0.1.0.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Acrescentar ao módulo de gráficos a leitura e validação da sensibilidade, criar barras horizontais
com sinais e referência clara e integrar a exportação ao comando existente. Validar ambas as
figuras antes de gravar os HTMLs, acrescentar testes e gerar os arquivos reais após a suíte.
Depois, atualizar somente README.md, ESTUDO_DE_CASO.md e este histórico, sem repetir testes,
cálculos ou geração de HTML nesta etapa documental.

**Participação e aprendizado:** as explicações distinguiram a variação dos tokens da variação do
custo total de IA. O denominador é o custo mensal de C05; negativo indica redução, positivo indica
aumento. Os dados já são percentuais, sem multiplicação adicional por 100 na apresentação.
Percentual vazio significa não aplicável e não deve ser convertido em zero ou barra fictícia.

**Decisões e implementação registradas:**

- Ler `resultados/estudo_de_caso/sensibilidade_tokens.csv` inicialmente como texto e reconstruir
  campos financeiros e percentuais diretamente como Decimal, preservando negativos válidos.
- Exigir exatamente C10 a C13, sem duplicidades, selecionar por identificador e ordenar as linhas,
  sem depender da ordem ou do índice de entrada. Todos devem referenciar C05.
- Conferir campos obrigatórios, finitude, condições comerciais, custo e tokens da referência,
  datas e campos alterados. C10/C11 variam entrada; C12/C13 variam saída, mantendo o outro token.
- Criar quatro barras horizontais em escala linear simétrica, com linha em zero, sinais, cores e
  rótulos baseados nos dados. Exibir referências, tokens, custos e variações no hover.
- Restringir float às coordenadas de uma cópia de visualização; preparar textos dos Decimal sem
  alterar contexto global, dados financeiros ou CSVs. Não recalcular custos nem consultar fontes.
- Integrar o segundo gráfico ao comando `graficos_estudo.py`, validando e construindo ambas as
  figuras antes de gravar. Entrada inválida, percentual não aplicável ou base sem custo positivo
  impedem a geração e preservam os dois HTMLs anteriores.
- Exportar `resultados/estudo_de_caso/sensibilidade_tokens.html` com Plotly incorporado, HTML completo
  e abertura automática desativada. Preservar o primeiro gráfico e sua saída. Os arquivos ficam
  ignorados pelo Git e podem ser abertos manualmente no navegador, offline.

**Testes e resultados:** foram acrescentados 18 métodos em uma segunda classe, preservando os 18
do primeiro gráfico e adaptando os dados temporários necessários à integração. Cobrem referências,
ordem, sinais, orientação, linha em zero, coordenadas e textos, IDs inválidos, condições divergentes,
percentuais vazios ou não finitos, negativos válidos, preservação dos dados e contexto Decimal,
HTML offline e falha no segundo gráfico sem sobrescrever nenhum HTML anterior.

Na implementação de 19/11/2026, passaram os **36 métodos dos gráficos** e os **271 métodos em
20 classes** da suíte completa: 188 do MVP, 47 da análise e 36 dos gráficos. Casos de subTest não
são métodos adicionais. Esses resultados são da execução anterior registrada nesta sessão,
sem repetição nesta atualização documental e sem instalação ou atualização de pacotes.

Após a suíte, o comando integrado gerou os dois HTMLs reais. A conferência estrutural confirmou
quatro barras de sensibilidade com C10 -12,5%, C11 +25%, C12 -37,5% e C13 +75%, textos preparados
dos Decimal e arquivos completos com Plotly incorporado. Os CSVs e demais arquivos protegidos
foram preservados. Isso é execução real e conferência pontual, sem novos testes persistentes.
**Não houve inspeção visual da renderização dos HTMLs**; essa revisão permanece pendente.

**Marco deste registro:** dois gráficos implementados e gerados. Indicadores restantes,
interpretação final, relatório e recomendações continuam pendentes. As relações decorrem de
hipóteses e condições fixas, sem comprovar uso dos estudantes ou qualidade pedagógica equivalente.
Somente os três documentos autorizados foram atualizados nesta etapa; código, testes, CSVs, HTMLs,
requirements, configurações e demais alterações pendentes foram preservados. O estudo permanece
separado do MVP v0.1.0 publicado, cuja tag não foi alterada. Não houve commit ou push.

## 43. Revisão visual dos dois gráficos do estudo

**Data desta atualização documental:** 19/11/2026.

**Data efetiva da revisão registrada:** 19/11/2026. A revisão e esta atualização são etapas
separadas, embora na mesma data; as condições fixas continuam com referência de 18/11/2026.

**Etapa:** registro da inspeção visual e de interação, com uma correção mínima de apresentação.

**Objetivo dos pedidos:** observar os dois HTMLs reais, comparar sua apresentação com os CSVs e
conferir legibilidade e interações, sem tratar testes estruturais como prova de renderização.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Abrir os gráficos em navegador disponível, revisar janelas ampla e menor, testar hover e legenda,
conferir eixos, rótulos, valores e funcionamento offline. Corrigir somente defeitos concretos,
preservando dados e MVP. Depois, atualizar apenas README, ESTUDO_DE_CASO.md e este histórico,
com base no relatório e nas evidências, sem executar novamente testes ou gerar arquivos.

**Participação e aprendizado:** a revisão distinguiu observação visual, conferência dos valores,
testes estruturais e acesso efetivamente necessário à rede. A presença de referências externas no
código incorporado não foi interpretada como dependência de rede sem observar as requisições.
A legibilidade em duas dimensões não comprova funcionamento em todos os dispositivos.

**Revisão realizada:** os dois HTMLs foram renderizados no Chrome instalado, com perfil temporário
separado e rede desativada nas páginas, em 1440×900 e 800×800 pixels. Não foram instaladas ferramentas.
O primeiro apresentou nove barras agrupadas, escalas e políticas na ordem prevista, custo em BRL
partindo de zero e exclusão de C10 a C13. O segundo mostrou quatro barras C10 a C13, referência C05,
linha em zero e percentuais -12,5%, +25%, -37,5% e +75%, com reduções à esquerda e aumentos à direita.

Hover em todas as barras e ocultação/restauração pela legenda foram testados nas duas dimensões.
Zoom por arraste e restauração por duplo clique foram conferidos na janela ampla dos dois gráficos.
Valores, identificadores e textos dos hovers corresponderam aos CSVs. Não foram observadas falhas
de recursos ou erros de JavaScript; os registros da revisão continham somente arquivos locais,
confirmando a renderização offline. Capturas e registros JSON ficaram fora do repositório.

**Problema e correção:** a referência do segundo gráfico se sobrepunha ao título nas duas janelas.
Em `criar_figura_sensibilidade()`, apenas a posição vertical da anotação mudou de `1.22` para `1.16`.
Não houve redesenho ou alteração de dados, eixos, fórmulas, identificadores ou conversões financeiras.
Os HTMLs foram regenerados e revistos; o texto ficou abaixo do título sem a sobreposição encontrada.
O primeiro gráfico não exigiu correção. A revisão não cobre telas menores ou outros navegadores.

**Testes e evidências:** após o ajuste de código, os 36 métodos dos gráficos passaram. Não foram
criados ou modificados testes. A suíte completa de 271 métodos não foi repetida durante a revisão;
seu resultado anterior permanece o da implementação do segundo gráfico. As capturas e os registros
de interação comprovam renderização e ações reais; a comparação dos hovers com os CSVs é uma
conferência de dados. São evidências distintas, sem comprovação de uso real ou qualidade pedagógica.
Os dados financeiros continuam Decimal e float permanece restrito à visualização. O navegador
temporário foi encerrado e seu perfil exclusivo removido; as evidências foram preservadas.

Nesta atualização, as evidências, o relatório da conversa e o diff de código foram conferidos.
Somente README.md, ESTUDO_DE_CASO.md e este histórico foram editados. Não houve nova execução de
testes, abertura do navegador, instalação ou regeneração de HTML. Código, testes, entradas,
resultados, capturas, dependências e demais alterações pendentes foram preservados.

**Marco deste registro:** revisão visual concluída no alcance comprovado: Chrome, 1440×900 e
800×800, com interações e uso offline descritos. Não foram testados dispositivos móveis, toque ou
outras condições. Indicadores restantes, interpretação, recomendações e relatório final continuam
pendentes. O estudo permanece separado do MVP v0.1.0 publicado, cuja tag não foi alterada.
Não houve commit nem push.

## 44. Indicadores de participação e custo mensal de IA por usuário ativo

**Data desta atualização documental:** 25/11/2026.

**Etapa:** registro dos indicadores implementados e conferidos; interpretação e relatório pendentes.

**Objetivo dos pedidos:** completar o estudo com participações de entrada/saída e custo por usuário
em USD e BRL, preservando precisão, resultados anteriores e o MVP publicado.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar calcular_indicadores(tabela) em analise_estudo.py, usar custos já calculados sem repetir as
funções do MVP e produzir uma tabela separada. Validar as bases, tratar denominadores zero,
exportar um quarto CSV e conferir os indicadores com testes temporários. Registrar essa etapa em
ESTUDO_DE_CASO.md e, depois, atualizar somente README.md e este histórico, sem repetir a execução.

**Participação e aprendizado:** as participações usam componente e total na mesma moeda; custos
unitários usam a contagem de usuários ativos. Cada denominador é independente. Não aplicável é
None, diferente de um resultado financeiro zero. A precisão Decimal vigente limita divisões não
exatas; oito casas na exibição dos custos unitários não arredondam os dados exportados.

**Implementação e decisões registradas:**

- Acrescentar `calcular_indicadores()` com identificação, usuários, custos de base, participações
  de entrada/saída e custo mensal de IA por usuário ativo em USD e BRL, preservando os 13 cenários
  e a ordem recebida sem alterar a tabela de entrada ou recalcular consumo/custos do MVP.
- Dividir entrada e saída em USD pelo total mensal em USD e multiplicar por Decimal("100").
  Dividir o total de cada moeda pelos usuários, convertidos de inteiro diretamente para Decimal.
- Validar colunas, nomes, IDs preenchidos e únicos, custos Decimal finitos não negativos e
  usuários inteiros não negativos, incluindo escalares inteiros do Pandas e rejeitando booleanos
  ou frações. Conferir componentes e total mensal na precisão vigente.
- Retornar None nas participações quando o total USD for zero e nos custos por usuário quando
  usuários forem zero. Tratar as duas bases separadamente, sem inventar zero ou percentual.
- Herdar a precisão e o arredondamento em `localcontext()`, sem alterar o contexto global.
  Apresentar participações com duas casas e custos unitários com oito casas em uma cópia textual,
  com unidade por usuário ativo/mês e `Não aplicável` nos casos sem denominador válido.
- Exportar `resultados/estudo_de_caso/indicadores_cenarios.csv` com 13 linhas e 11 colunas, UTF-8,
  vírgula, ponto decimal, cabeçalho e sem índice. Preservar Decimal completo e None como campo vazio.
- Calcular e validar todas as tabelas antes da exportação. Preservar o retorno de executar_estudo(),
  os três esquemas anteriores e chamadas existentes; acrescentar caminho opcional para indicadores.

**Resultados e testes da implementação em 25/11/2026:** os 19 novos métodos de TestIndicadores
conferiram os 13 cenários com expectativas independentes, denominadores zero separados, entrada
gratuita, custos e usuários inválidos, coerência de total, IDs, inteiros do Pandas e precisão.
Também cobriram preservação da entrada e do contexto, divisões não exatas, releitura exata dos
Decimal, None vazio na exportação, apresentação com oito casas e falhas sem sobrescrever resultados.
A análise passou com **66 métodos em duas classes** e a suíte completa com **290 métodos em
21 classes**: 188 do MVP, 66 da análise e 36 dos gráficos. Subtests não são métodos adicionais.

Em C05 foram conferidos 25% de entrada, 75% de saída, USD 0.0044 e BRL 0.02556488 por usuário
ativo/mês. C02, C05 e C08 têm os mesmos custos unitários sob as hipóteses atuais. Isso decorre das
fórmulas e não comprova economia de escala, viabilidade ou qualidade pedagógica. O custo por
usuário inclui somente IA, sem representar o custo operacional completo da aplicação.

A execução real gerou o novo CSV. Conferências pontuais confirmaram sua precisão na releitura e
os três CSVs anteriores idênticos. Os leitores dos gráficos continuaram compatíveis, com figuras
de nove e quatro barras construídas em memória, sem alterar os HTMLs ou realizar nova inspeção
visual. Essas conferências não acrescentaram métodos automatizados persistentes.

**Condições históricas preservadas:** OpenAI, gpt-6-luna, Standard, entrada 0.10 e saída 0.50 USD
por milhão e cotação fixa Decimal("5.8102") BRL por USD, com pesquisa e referência de 18/11/2026.
A pausa no desenvolvimento não alterou essas referências. A implementação e a verificação são de
25/11/2026, sem consulta à cotação atual, atualização de preços ou substituição de datas históricas.

Nesta atualização, somente README.md e este registro foram alterados, com base na implementação,
testes e ESTUDO_DE_CASO.md. Não foram repetidos testes, cálculos ou exportações. Os demais
arquivos e alterações pendentes foram preservados, incluindo código, dados, HTMLs e dependências.

**Marco deste registro:** indicadores implementados e verificados. Interpretação final,
recomendações e relatório permanecem como próximos passos. O estudo continua separado do MVP
v0.1.0 publicado, sem alteração da tag. Não houve instalações, commit ou push.
