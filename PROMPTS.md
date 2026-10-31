# Prompts relevantes — LiteArt Cost Analytics

Este arquivo reúne uma seleção dos prompts enviados pelo autor durante o desenvolvimento do projeto com apoio de IA. O objetivo é documentar os pedidos que orientaram o escopo, o aprendizado e as principais decisões técnicas, sem reproduzir toda a conversa.

Modelo registrado pelo autor para essas interações: **GPT-6.1 Sol, com esforço de raciocínio médio**. Essa informação descreve a ferramenta de apoio ao desenvolvimento, não o modelo da API que será considerado pela calculadora.

## Como ler este registro

- Os blocos de citação contêm palavras do autor, preservadas sem correções de escrita.
- O registro 1 reúne trechos do pedido inicial. Os registros 2 a 5 contêm pedidos completos. Os registros a partir do 6 sintetizam pedidos relacionados, sem reproduzir literalmente cada mensagem.
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

O cenário didático e casos com consumo zero e feedback em 0% ou 100% dos acertos foram conferidos durante a refatoração. Naquele marco, as funções ainda pressupunham entradas válidas; a implementação das validações está registrada na seção 9.

**Marco anterior:** cálculos anuais e organização em funções, registrado em 2026-10-25.

## 9. Validação das entradas da calculadora

**Etapa:** validação dos argumentos das seis funções da calculadora básica.

**Objetivo dos pedidos:** impedir cálculos com tipos inadequados e valores incompatíveis com o cenário, aprendendo cada regra por pequenas alterações e testes.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Antes de alterar o código, explicar quais entradas devem ser validadas e por quê. Começar em `calcular_respostas_mensais`, recusando negativos, depois textos e usuários fracionários, e então infinito e NaN. Explicar o funcionamento de `if`, `raise`, `TypeError`, `ValueError` e da verificação de valores finitos. Validar em seguida as taxas entre 0 e 1 e os tipos de `calcular_feedbacks_mensais`, incluindo respostas mensais. Proteger também esse volume contra negativos e valores não finitos. Aplicar o mesmo processo aos três argumentos de `calcular_tokens_mensais`. Após compreender o padrão, completar as validações das funções monetárias e revisar a consistência das regras anteriores. Atualizar a documentação para registrar esse marco antes de fazer um novo commit.

**Participação e aprendizado:** o autor executou os exemplos de testes no VS Code após cada alteração e confirmou os resultados. A comparação com NaN na documentação do PostgreSQL ajudou a discutir a diferença entre um valor especial e uma operação que levanta uma exceção em Python. Os testes foram apresentados aos poucos para distinguir tipos inválidos, valores negativos, limites permitidos e valores não finitos.

**Decisões registradas:**

- Usuários ativos devem ser `int` e não negativos.
- Médias e volumes estimados aceitam `int` ou `float`, inclusive frações finitas, sem valores negativos.
- As taxas recebem proporções entre 0 e 1, com os dois limites permitidos.
- Preços e custos monetários devem ser `Decimal`, finitos e não negativos.
- A cotação aceita `int`, `float` ou `Decimal`, é convertida internamente para `Decimal` e deve ser finita e maior que zero.
- Textos passados diretamente, `None` e booleanos são recusados. Zero continua válido para consumo e custos.
- `TypeError` identifica tipos não permitidos; `ValueError` identifica valores que desrespeitam as regras.

**Contribuição para o projeto:** todas as seis funções passaram a validar seus argumentos antes dos cálculos. Um roteiro de verificação executado durante o desenvolvimento conferiu 110 casos, incluindo as funções monetárias e regras anteriores, sem alterar os resultados do cenário didático. Esse roteiro ainda não está salvo como suíte de testes no repositório. As funções sinalizam erros; o tratamento dessas mensagens em uma interface ainda será desenvolvido.

**Marco anterior:** validação das entradas, registrada em 2026-10-25. A reutilização dessas regras está documentada na seção 10.

## 10. Refatoração com a auxiliar de validação

**Etapa:** reutilização das validações na calculadora básica.

**Objetivo dos pedidos:** reduzir a repetição das condições de validação, preservando os tipos aceitos e os resultados, com explicações e testes por pequenas alterações.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Após salvar as validações em um commit, criar a primeira função auxiliar e aplicá-la em apenas uma função da calculadora. Entender por que a auxiliar recebe um valor e um nome, o papel desse rótulo nas mensagens e por que essa validação não precisa devolver um resultado. Reutilizar a auxiliar na função de respostas mensais, mantendo a exigência de usuários inteiros. Em seguida, aplicá-la às funções restantes, explicando as adaptações necessárias para tipos monetários e preservando as regras específicas. Registrar a refatoração na documentação antes de fazer um novo commit.

**Participação e aprendizado:** o autor testou as primeiras aplicações da auxiliar e pediu esclarecimentos sobre parâmetros, retorno e mensagens de erro. A explicação distinguiu o papel de uma função auxiliar da decisão de usar ou não `return`: funções auxiliares também podem processar e retornar valores; esta apenas valida e sinaliza erros.

**Decisões registradas:**

- Criar `validar_numero_nao_negativo` para centralizar tipos permitidos, valores finitos e ausência de negativos.
- Usar `nome` como rótulo legível do campo na mensagem de erro; não é necessário que o texto seja igual ao nome da variável.
- Aplicar inicialmente a auxiliar em `calcular_tokens_mensais` e depois em `calcular_respostas_mensais`, preservando a regra de usuários inteiros.
- Acrescentar `tipos_permitidos=(int, float)` como parâmetro opcional para reutilizar a auxiliar nas funções monetárias sem alterar seus contratos.
- Exigir `(Decimal,)` para preços e custos e aceitar `(int, float, Decimal)` para a cotação.
- Manter verificações específicas de usuários inteiros, taxas até 1 e cotação maior que zero nas funções de cálculo.
- Preservar as fórmulas; padronizar as mensagens de validação com o rótulo de cada campo.

**Contribuição para o projeto:** as seis funções de cálculo passaram a reutilizar a auxiliar. A última conferência executou 232 casos de tipos, limites e valores especiais, além de conferir frações válidas e o cenário original. Os resultados permaneceram em US$ 0,44 e R$ 2,20 por mês e US$ 5,28 e R$ 26,40 por ano, nas hipóteses didáticas registradas. Os roteiros de verificação ainda não estão salvos como uma suíte de testes no repositório.

**Marco deste registro:** documentação atualizada em 2026-10-26, até a refatoração com a auxiliar de validação, sem novas dependências ou chamadas reais à API.

## 11. Separação da execução e testes automatizados

**Etapa:** testes reproduzíveis da calculadora básica.

**Objetivo dos pedidos:** importar as funções sem executar o cenário didático e transformar as conferências manuais em testes salvos no repositório, compreendendo cada alteração.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Adicionar `if __name__ == "__main__":` e explicar a diferença entre executar e importar a calculadora. Criar os primeiros testes de respostas mensais, começando pelo cenário didático, zero usuários e usuários negativos. Acrescentar testes para usuários fracionários, textos, infinito e NaN. Explicar por que uma exceção esperada é capturada por `assertRaises` e aparece como teste aprovado. Testar em seguida feedbacks mensais, incluindo os resultados, taxas nos limites e fora do intervalo, tipos e valores não finitos nos três argumentos. Completar os testes das funções de tokens, custo de tokens, conversão para reais e custo anual. Explicar `for`, `subTest`, tipos monetários e como executar um teste, uma classe ou a suíte completa. Atualizar README e registro de prompts antes do próximo commit.

**Participação e aprendizado:** o autor executou os testes no terminal após cada incremento e confirmou os resultados. Pediu esclarecimentos sobre a captura de `ValueError`, o percurso do laço pelos subtestes e a conversão com cotações representadas como `int`, `float` e `Decimal`.

**Decisões registradas:**

- Proteger o cenário e os `print()` com `if __name__ == "__main__":`; manter as funções disponíveis na importação.
- Usar `unittest`, incluído no Python, sem dependências externas.
- Manter os testes em `test_calculadora.py`, com uma classe para cada função de cálculo.
- Conferir resultados com `assertEqual`, tipos de retorno com `assertIsInstance` e exceções com `assertRaises`.
- Introduzir `subTest` nos novos grupos para verificar várias entradas sem repetir um método para cada valor e identificar a tentativa que falhar.
- Testar consumo e custos zero quando permitidos; exigir cotação maior que zero.
- Preservar as diferenças de contrato: volumes aceitam `int` ou `float`, preços e custos exigem `Decimal`, e cotação aceita os três tipos.
- Cobrir tipos inválidos, negativos, infinito e NaN nos argumentos das quatro funções de cálculo restantes, além dos resultados didáticos e estimativas fracionárias permitidas.

**Contribuição para o projeto:** o repositório passou a conter uma suíte reproduzível com 59 métodos de teste, distribuídos em seis classes. Parte dos métodos executa vários subtestes, que não aumentam a contagem exibida em `Ran 59 tests`. A execução completa passou; a auxiliar de validação também é exercitada indiretamente. Os roteiros temporários de 110 e 232 casos, mencionados nos marcos anteriores, continuam sendo registros históricos distintos dessa suíte.

**Marco deste registro:** documentação atualizada em 2026-10-27, até os testes automatizados das seis funções de cálculo, sem dependências externas ou chamadas reais à API.

## 12. Custos fixos de infraestrutura e total com IA

**Etapa:** ampliação da calculadora básica para incluir backend e banco de dados.

**Objetivo dos pedidos:** compreender a cobrança de hospedagem e PostgreSQL, calcular mensalidades fixas e somá-las ao custo variável de IA, com valores didáticos e testes.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Explicar o que representam as cobranças de backend e banco de dados. Criar calcular_custo_servico e seus testes, reutilizando a auxiliar de validação. Usar a função no cenário principal com preços inventados para aprendizado, converter os custos para reais e apresentar infraestrutura, IA e totais mensais e anuais. Explicar cada alteração e como conferir os resultados, incluindo o comportamento com zero usuários. Atualizar README e registro de prompts antes de fazer um novo commit.

**Participação e aprendizado:** o autor executou os testes da nova função e o cenário integrado e confirmou os resultados. As explicações distinguiram preço por unidade, quantidade contratada, custo fixo de infraestrutura e custo variável de IA.

**Decisões registradas:**

- Criar `calcular_custo_servico(preco_mensal_por_unidade, quantidade)`, retornando preço mensal multiplicado pela quantidade, na mesma moeda do preço.
- Exigir preço `Decimal`, finito e não negativo, e quantidade `int` não negativa; recusar booleanos e quantidades como `2.0`.
- Permitir preço gratuito e zero unidades.
- Adotar backend a US$ 5,00 por unidade, com duas unidades, e banco a US$ 3,00 por unidade, com uma unidade. São preços didáticos, sem fonte comercial ou comprovação de capacidade.
- Converter os custos com a cotação didática de R$ 5,00 por dólar e somar apenas valores na mesma moeda.
- Preservar a projeção anual de 12 meses constantes, sem arredondar etapas intermediárias.
- Manter a infraestrutura contratada mesmo quando o consumo de IA for zero.
- Registrar serviços incluídos em um mesmo pacote para evitar duplicar cobranças quando forem pesquisados planos reais.

**Contribuição para o projeto:** a calculadora passou a incluir sete funções de cálculo. O cenário apresenta infraestrutura de US$ 13,00 ou R$ 65,00 mensais e IA de US$ 0,44 ou R$ 2,20 mensais. O total é US$ 13,44 ou R$ 67,20 por mês e US$ 161,28 ou R$ 806,40 por ano, sob as hipóteses registradas.

Foram acrescentados oito métodos de teste para o serviço, levando a suíte a 67 métodos em sete classes. A execução completa passou. Uma conferência adicional do cenário principal, realizada em memória e não salva como teste na suíte, confirmou os totais com 100 usuários e, com zero usuários, IA zero e infraestrutura de US$ 13,00 ou R$ 65,00 mensais. O autor também confirmou a execução no terminal.

**Marco deste registro:** documentação atualizada em 2026-10-28, até a integração de infraestrutura e IA, sem novas dependências ou chamadas reais à API.

## 13. Pesquisa de hospedagem e Firebase como alternativa

**Etapa:** pesquisa de infraestrutura e avaliação de alternativas, antes de alterar o cenário da calculadora.

**Objetivo dos pedidos:** comparar opções gratuitas e pagas em fontes oficiais e compreender se o Firebase pode atender ao LiteArt, aproveitando o aprendizado da faculdade sem substituir antecipadamente a arquitetura planejada.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Pesquisar três opções de hospedagem para backend e PostgreSQL, priorizando baixo custo e incluindo pelo menos uma combinação gratuita. Explicar preços, limites e condições aos poucos e registrar a comparação no planejamento antes de alterar o código. Verificar o Firebase, apresentado na disciplina de programação de dispositivos móveis, especialmente para login com Google e possível centralização de backend e banco. Explicar sua hospedagem, os produtos envolvidos e os custos e limitações. Registrar o Firebase como alternativa, mantendo NestJS e PostgreSQL como referência. Atualizar README e registro de prompts para salvar esse marco em um commit.

**Participação e aprendizado:** o autor trouxe a experiência com Firebase na faculdade e pediu uma avaliação antes de decidir sobre a arquitetura. A orientação distinguiu autenticação, execução de backend, hospedagem de frontend e armazenamento de dados, além de mensalidade fixa, consumo, franquia e teste gratuito temporário.

**Decisões registradas:**

- Comparar Render + Neon, Railway e Koyeb + Neon, registrando fontes e data da consulta de 2026-10-28 no planejamento.
- Distinguir uma combinação gratuita dentro das franquias de créditos limitados e ofertas temporárias; considerar suspensão por inatividade e condições de cadastro.
- Registrar a avaliação do Firebase com consulta de 2026-10-30, incluindo Spark e Blaze e a separação dos serviços e suas cobranças.
- Considerar Firebase Authentication para login com Google no Flutter sem exigir a troca do NestJS ou do PostgreSQL.
- Distinguir Firestore, orientado a documentos, de SQL Connect com PostgreSQL via Cloud SQL; registrar que a gratuidade de teste deste último é temporária.
- Distinguir Hosting tradicional de App Hosting e dos serviços que executam código de backend, como Functions e Cloud Run.
- Manter Flutter, Node.js/NestJS e PostgreSQL como arquitetura de referência; Firebase permanece uma alternativa em estudo.
- Manter os preços didáticos no cenário principal e nos testes. A pesquisa não implementa seleção de provedores, migração ou contratação.
- Preparar hipóteses de operações, armazenamento, processamento e tráfego antes de simular ofertas cobradas por consumo.

**Contribuição para o projeto:** o planejamento passou a registrar três combinações de hospedagem e uma alternativa Firebase com fontes, datas, custos e limitações. O README resume a pesquisa e aponta para os detalhes no planejamento. Nenhum provedor foi escolhido pelo autor para substituir as entradas didáticas, e código e testes permaneceram inalterados neste marco.

**Marco deste registro:** documentação atualizada em 2026-10-31, consolidando a pesquisa de hospedagem e o Firebase como alternativa, com NestJS e PostgreSQL preservados como referência.

## 14. Organização das entradas em dicionários

**Etapa:** organização dos dados da calculadora básica para preparar futuros cenários.

**Objetivo dos pedidos:** separar hipóteses de consumo, preços e cotação, aprendendo dicionários e acesso por chaves sem alterar as fórmulas ou os resultados.

**Síntese dos pedidos relacionados — não é uma citação literal:**

Criar um dicionário com as hipóteses de consumo e adaptar as chamadas das funções, explicando cada parte e como testar se os resultados continuam iguais. Esclarecer se a cotação do dólar poderá ser consultada automaticamente no futuro. Organizar depois os preços de IA, os preços de infraestrutura e a cotação em dicionários separados das hipóteses, explicando a leitura das chaves e a conferência dos cálculos. Atualizar README e registro de prompts antes de fazer um novo commit.

**Participação e aprendizado:** o autor executou o cenário e os testes após cada incremento e confirmou os resultados. As explicações abordaram pares de chave e valor, uso de chaves entre colchetes, preservação de Decimal e a diferença entre testar uma função com entradas próprias e executar o cenário principal.

**Decisões registradas:**

- Criar `hipoteses_consumo` com seis entradas: usuários ativos, respostas por usuário, taxa de acerto, parcela dos acertos com feedback e tokens de entrada e saída por feedback.
- Criar `precos_ia` com as tarifas em USD por milhão de tokens; preservar os comentários de fonte, data e condições.
- Criar `precos_infraestrutura` com os preços didáticos mensais por unidade de backend e banco.
- Criar `cotacao` com a chave `brl_por_usd`, mantendo a taxa manual didática de `Decimal("5.00")`.
- Manter as quantidades contratadas como variáveis separadas, pois representam hipóteses de capacidade.
- Adaptar as chamadas para buscar os valores por chave, mantendo os contratos e as validações das funções.
- Manter os resultados separados das entradas e preservar todos os valores do cenário.
- Considerar futuramente consulta de câmbio por API, registrando fonte e data e mantendo a opção manual. Essa consulta não foi implementada e não prevê o câmbio dos meses futuros.

**Contribuição para o projeto:** quatro dicionários passaram a organizar as entradas no bloco principal. A conferência da última refatoração comparou a saída completa antes e depois e confirmou sua preservação; os 67 métodos de teste passaram. O total permaneceu em US$ 13,44 ou R$ 67,20 por mês e US$ 161,28 ou R$ 806,40 por ano. A organização prepara comparações futuras, mas ainda não implementa uma função de cenário completo nem importação de dados.

**Marco deste registro:** documentação atualizada em 2026-10-31, até a organização de hipóteses, preços e cotação em dicionários, sem novas dependências ou consulta automática de câmbio.