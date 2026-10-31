# LiteArt Cost Analytics

Projeto pessoal de Análise de Dados para simular os custos operacionais de uma aplicação de software, utilizando o LiteArt como estudo de caso.

O LiteArt é uma plataforma educacional em desenvolvimento, voltada à preparação para vestibulares, com questões, simulados, acompanhamento de desempenho e feedbacks pedagógicos personalizados por Inteligência Artificial.

## Objetivos

- Estimar custos mensais e anuais de infraestrutura e APIs de IA.
- Comparar serviços e cenários de utilização.
- Converter custos em dólares para reais com uma cotação informada.
- Desenvolver conhecimentos de Python e Análise de Dados por meio da prática.
- Construir uma ferramenta que possa ser adaptada a outros projetos de software.

## Situação atual

**Etapa 2 — Calculadora básica em desenvolvimento.** O arquivo `calculadora.py` já organiza os cálculos de consumo, custos de IA e mensalidades de infraestrutura em funções, usando GPT-6 Luna como referência inicial. As hipóteses de consumo, preços e cotação são definidos em dicionários no bloco principal; as quantidades de unidades contratadas permanecem em variáveis separadas. Ainda não há entrada interativa.

### Funcionalidades implementadas

- Organização das hipóteses de consumo, preços e cotação em dicionários separados.
- Cálculo do consumo de um cenário a partir das hipóteses, com retorno em um novo dicionário.
- Volume mensal de respostas, acertos, erros e feedbacks.
- Consumo mensal estimado de tokens de entrada e saída.
- Custos mensais de entrada e saída de IA em dólares, com `Decimal`.
- Mensalidades de backend e banco, calculadas por preço por unidade e quantidade contratada.
- Soma de infraestrutura e IA, com totais mensais e anuais em dólares e reais.
- Conversão dos custos para reais com cotação didática informada no código.
- Projeção anual em dólares e reais, mantendo consumo, preços e câmbio constantes.
- Apresentação dos resultados com os símbolos US$ e R$.
- Validação de tipos, valores negativos, taxas fora do intervalo, infinito e NaN nos argumentos das funções.
- Testes automatizados reproduzíveis das sete funções de cálculo e da função coordenadora de consumo, usando `unittest`.

### Organização das entradas em dicionários

Dentro do bloco principal, as entradas estão agrupadas por finalidade:

| Dicionário | Conteúdo | Natureza dos dados |
|---|---|---|
| `hipoteses_consumo` | Usuários, respostas por usuário, taxa de acerto, parcela dos acertos com feedback e tokens por feedback | Hipóteses didáticas de consumo |
| `precos_ia` | Tarifas de entrada e saída em USD por milhão de tokens | Preços pesquisados, com fonte e data nos comentários e no planejamento |
| `precos_infraestrutura` | Preços mensais por unidade de backend e banco em USD | Valores inventados para aprendizado |
| `cotacao` | `brl_por_usd`, com `Decimal("5.00")` | Configuração cambial didática e manual |

Os preços e a cotação mantêm o tipo `Decimal`. As quantidades `quantidade_backend` e `quantidade_banco` continuam como variáveis separadas: são hipóteses de capacidade, não preços.

As funções de cálculo recebem valores individuais. A função coordenadora `calcular_consumo_cenario` recebe o dicionário inteiro de hipóteses, busca os valores pelas chaves e retorna um novo dicionário de resultados. Preços e cotação continuam sendo consultados no bloco principal. Os resultados não são gravados nos dicionários de entrada.

Essa organização prepara a reutilização dos cálculos em diferentes cenários. Ainda não há função que receba um cenário completo, leitura de CSV ou consulta automática de câmbio.

Na última refatoração, a saída completa foi comparada antes e depois e permaneceu idêntica. Os 77 métodos de teste também passaram. Os testes das funções usam entradas próprias; alterações nos dicionários do cenário devem ser conferidas executando também `calculadora.py`.


### Cálculo do consumo de um cenário

A função `calcular_consumo_cenario(hipoteses_consumo)` recebe o dicionário inteiro e coordena as funções de respostas, feedbacks e tokens. Ela não calcula custos nem imprime resultados.

Antes dos cálculos, exige um `dict` e confere as seis chaves obrigatórias: `usuarios_ativos`, `respostas_por_usuario`, `taxa_acerto`, `proporcao_acertos_com_feedback`, `tokens_entrada` e `tokens_saida`.

- Argumento que não seja `dict`: `TypeError`.
- Chave obrigatória ausente: `ValueError` com o nome do campo.
- Valor inválido: a exceção da função de cálculo é propagada.
- Chaves adicionais: permitidas, sem participar do consumo.
- Entrada: preservada, sem acrescentar resultados nem alterar seus valores.

O retorno é um novo dicionário com `respostas_mensais`, `acertos_mensais`, `erros_mensais`, `feedbacks_nos_acertos`, `feedbacks_mensais`, `tokens_entrada_total` e `tokens_saida_total`.

No bloco principal, `consumo_cenario` recebe esse retorno. Seus valores alimentam os cálculos de custos e os `print()` existentes. O cenário permanece com 4.000 respostas, 2.200 feedbacks e 1.100.000/660.000 tokens de entrada/saída. Ainda não há uma função que reúna consumo, preços, infraestrutura e câmbio em um cenário completo.


### Organização das funções

| Função | Responsabilidade |
|---|---|
| `calcular_consumo_cenario` | Coordenar respostas, feedbacks e tokens a partir das hipóteses |
| `calcular_respostas_mensais` | Estimar o volume de respostas |
| `calcular_feedbacks_mensais` | Calcular acertos, erros e feedbacks |
| `calcular_tokens_mensais` | Estimar os totais de tokens de entrada e saída |
| `calcular_custo_tokens` | Calcular custo em USD a partir da tarifa por milhão de tokens |
| `calcular_real` | Converter um custo em USD para BRL |
| `calcular_custo_anual` | Projetar 12 meses de custo constante |
| `calcular_custo_servico` | Calcular mensalidade por preço unitário e quantidade, na moeda informada |
| `validar_numero_nao_negativo` | Centralizar a validação de tipo permitido, valor finito e ausência de negativos |

As funções de cálculo retornam valores; os `print()` apresentam os resultados separadamente. A auxiliar de validação sinaliza erros com exceções; quando a entrada é válida, termina sem retorno explícito (`None`).

### Auxiliar de validação

A função `validar_numero_nao_negativo(valor, nome, tipos_permitidos=(int, float))` centraliza as regras compartilhadas pelas sete funções de cálculo:

- `valor`: dado que será verificado.
- `nome`: rótulo do campo usado nas mensagens de erro, sem participar do cálculo.
- `tipos_permitidos`: parâmetro opcional que aceita `int` e `float` por padrão. Preços e custos informam `(Decimal,)`; a cotação informa `(int, float, Decimal)`.

A auxiliar rejeita tipos não permitidos, infinito, NaN e negativos, sem converter o valor. Para conferir valores finitos, usa `math.isfinite` com `float` e `.is_finite()` com `Decimal`. As mensagens seguem um formato compartilhado e identificam o campo.

Regras específicas permanecem nas funções de cálculo: usuários e quantidades de unidades devem ser inteiros, taxas não podem ultrapassar 1 e a cotação deve ser maior que zero. A auxiliar já garante o limite inferior de zero para as taxas. As fórmulas, os tipos aceitos e os resultados do cenário didático foram preservados.

### Cenário didático de referência

| Entrada | Hipótese |
|---|---:|
| Usuários ativos por mês | 100 |
| Respostas por usuário no mês | 40 |
| Taxa de acerto | 60% |
| Parcela dos acertos com feedback | 25% |
| Tokens de entrada por feedback | 500 |
| Tokens de saída faturáveis por feedback | 300 |
| Cotação didática | R$ 5,00 por US$ 1,00 |

As tarifas pesquisadas do Luna são US$ 0,10 por milhão de tokens de entrada sem cache e US$ 0,50 por milhão de saída, no processamento Standard e nas condições registradas no planejamento. Fontes e data de consulta (2026-10-23) estão no [PLANEJAMENTO.md](PLANEJAMENTO.md).

| Resultado do cenário | Valor |
|---|---:|
| Feedbacks mensais | 2.200 |
| Tokens mensais de entrada | 1.100.000 |
| Tokens mensais de saída | 660.000 |
| Custo mensal estimado de IA em USD | US$ 0,44 |
| Custo mensal estimado de IA em BRL | R$ 2,20 |
| Custo anual estimado de IA em USD | US$ 5,28 |
| Custo anual estimado de IA em BRL | R$ 26,40 |

Esses valores conferem a aritmética do cenário. Não são despesas reais nem medições do consumo de uma API. A calculadora não realiza chamadas à OpenAI.

### Custos de infraestrutura e total do cenário

Os preços de infraestrutura abaixo são inventados para aprendizado, não preços pesquisados. A função `calcular_custo_servico` multiplica o preço mensal por unidade pela quantidade contratada e retorna `Decimal` na moeda do preço, sem conversão automática.

| Serviço | Preço didático por unidade/mês | Quantidade | Mensal em USD | Mensal em BRL |
|---|---:|---:|---:|---:|
| Backend | US$ 5,00 | 2 | US$ 10,00 | R$ 50,00 |
| Banco PostgreSQL | US$ 3,00 | 1 | US$ 3,00 | R$ 15,00 |
| **Infraestrutura** | — | — | **US$ 13,00** | **R$ 65,00** |

A conversão usa R$ 5,00 por dólar, uma cotação didática. O cenário soma apenas custos na mesma moeda, sem arredondar etapas intermediárias.

| Categoria | Mensal em USD | Mensal em BRL | Anual em USD | Anual em BRL |
|---|---:|---:|---:|---:|
| Infraestrutura | US$ 13,00 | R$ 65,00 | US$ 156,00 | R$ 780,00 |
| IA | US$ 0,44 | R$ 2,20 | US$ 5,28 | R$ 26,40 |
| **Total do cenário** | **US$ 13,44** | **R$ 67,20** | **US$ 161,28** | **R$ 806,40** |

A projeção anual mantém serviços, consumo, preços e câmbio constantes. Com zero usuários, o consumo variável de IA fica zero, mas os serviços contratados permanecem em US$ 13,00 ou R$ 65,00 mensais.

A pesquisa inicial de hospedagem já está registrada no planejamento, mas ainda não substituiu os preços didáticos do cenário. Esses valores não demonstram a capacidade de atendimento do LiteArt. Se o banco estiver incluído na hospedagem, seu custo não deve ser contado duas vezes. O total contempla apenas as categorias e condições deste cenário; as exclusões da primeira versão estão no planejamento.


### Pesquisa de hospedagem e alternativas de arquitetura

A pesquisa inicial de 2026-10-28 comparou três combinações para hospedar o backend e o PostgreSQL:

| Combinação pesquisada | Ponto de atenção registrado |
|---|---|
| Render + Neon | Opções gratuitas com franquias e suspensão por inatividade, além de alternativas pagas |
| Railway | Créditos gratuitos limitados e plano pago com consumo incluído; o mínimo cobrado não é uma mensalidade fixa de todos os serviços |
| Koyeb + Neon | Recursos gratuitos e pagos, com atenção ao plano selecionado e à possível cobrança inicial no cadastro |

A avaliação de 2026-10-30 acrescentou o **Firebase como alternativa em estudo**. Foram distinguidos Authentication para login com Google, Hosting para arquivos web, Functions/Cloud Run para execução de backend, Firestore como banco de documentos e SQL Connect com PostgreSQL via Cloud SQL.

**A arquitetura de referência do LiteArt continua sendo Flutter, backend Node.js/NestJS e PostgreSQL.** Usar Firebase Authentication pode preservar essa arquitetura; adotar Firestore e Functions exigiria rever parte do desenho. Nenhuma migração ou contratação foi realizada.

Preços, unidades de cobrança, franquias, condições de cadastro, testes temporários e fontes oficiais estão na seção 6 do [planejamento](PLANEJAMENTO.md). As consultas são registros datados e devem ser revalidadas antes de contratar. Gratuidade de infraestrutura não inclui automaticamente o consumo das APIs de IA.

Os preços pesquisados ainda não foram aplicados ao cenário principal, que permanece didático. Também não há comparação automatizada entre provedores. Ofertas por consumo precisarão de hipóteses adicionais antes de serem representadas pela calculadora.


### Como executar a versão atual

Abra `calculadora.py` e execute o arquivo com seu interpretador Python 3. No ambiente usado durante o desenvolvimento, a execução foi realizada pelo VS Code. Não há dependências externas nesta etapa: `decimal`, `math` e `unittest` fazem parte da biblioteca padrão.

O cenário didático e os `print()` ficam dentro de `if __name__ == "__main__":`. Ao executar o arquivo diretamente, o cenário é calculado e apresentado. Ao importar suas funções, esse bloco não é executado, permitindo reutilizá-las nos testes sem imprimir os resultados do cenário.

### Validação das entradas

As sete funções de cálculo usam a auxiliar compartilhada e verificações específicas antes de calcular. A coordenadora de consumo valida o dicionário e suas chaves e reutiliza as validações numéricas por meio dessas funções. Tipos não permitidos geram `TypeError`; valores fora das regras geram `ValueError`, com mensagens que identificam o argumento inválido.

| Entrada | Tipos aceitos | Regras |
|---|---|---|
| Usuários ativos e quantidade de unidades de serviço | `int` | Maior ou igual a zero; valores fracionários e `100.0` são recusados |
| Média de respostas por usuário e total de respostas mensais | `int` ou `float` | Finitos e maiores ou iguais a zero |
| Taxa de acerto e parcela dos acertos com feedback | `int` ou `float` | Entre 0 e 1, inclusive; a auxiliar rejeita negativos e valores não finitos, e a função verifica o limite superior |
| Tokens por feedback, feedbacks mensais e total de tokens | `int` ou `float` | Finitos e maiores ou iguais a zero; médias e estimativas fracionárias são permitidas |
| Preço por milhão de tokens, preço mensal por unidade e custos monetários | `Decimal` | Finitos e maiores ou iguais a zero |
| Cotação em BRL por USD | `int`, `float` ou `Decimal` | Finita e maior que zero; convertida internamente para `Decimal` |

Textos passados diretamente, `None` e valores booleanos (`True` e `False`) são recusados. As funções não convertem automaticamente textos numéricos. Construir explicitamente `Decimal("5.00")` continua sendo válido.

Zero é permitido para consumo, quantidades, preços e custos. A cotação é a exceção: precisa ser positiva. Valores especiais como infinito e NaN são recusados; para `float`, usamos `math.isfinite`, e para `Decimal`, `.is_finite()`.

As validações são aplicadas aos argumentos das funções, mesmo quando elas são chamadas fora do cenário principal. Elas verificam as regras definidas para as entradas; não demonstram que as hipóteses representam o consumo real do LiteArt.

### Testes automatizados

O arquivo `test_calculadora.py` contém uma suíte reproduzível com `unittest`, da biblioteca padrão do Python. São 77 métodos de teste, distribuídos em oito classes: sete para os cálculos e uma para a função coordenadora de consumo. Parte dos métodos usa `subTest` para verificar várias entradas; essas tentativas não são contadas separadamente no total de métodos.

A suíte verifica:

- Resultados conhecidos do cenário didático: respostas, feedbacks, tokens e custos mensais e anuais.
- Taxas nos limites 0 e 1 e rejeição de taxas fora do intervalo.
- Tipos inválidos, incluindo textos e booleanos, e valores especiais como infinito e NaN.
- Nos cálculos de tokens e custos: negativos, zeros permitidos e estimativas fracionárias válidas.
- Exigência de `Decimal` para preços e custos e manutenção desse tipo nos resultados monetários.
- Cotação positiva nos três tipos permitidos (`int`, `float` e `Decimal`), com rejeição de zero, negativos e valores não finitos.
- Valores especiais de `Decimal`, incluindo `NaN` e `sNaN`, nos campos monetários.
- Oito métodos para serviços: exemplos de backend e banco, zero unidades, preço gratuito e rejeição de tipos e valores inválidos.
- Dez métodos para consumo do cenário: resultados, zeros, estrutura do dicionário, propagação de exceções, preservação da entrada e chaves adicionais.

A auxiliar de validação é exercitada pelas chamadas às funções de cálculo. A suíte cobre os casos descritos; não é uma verificação exaustiva de todas as entradas possíveis nem uma medição de consumo real da API.

No terminal, dentro da pasta do projeto, use seu interpretador Python 3:

```powershell
python -m unittest -v test_calculadora
```

Para executar somente uma classe, por exemplo a conversão cambial:

```powershell
python -m unittest -v test_calculadora.TestCalcularReal
```

Se `python` não estiver disponível no terminal, utilize o caminho do interpretador configurado no VS Code. Também é possível executar `test_calculadora.py` diretamente com esse interpretador.

A última execução retornou `Ran 77 tests` e `OK`. `assertEqual` confere resultados, `assertIsInstance` verifica tipos de retorno e `assertRaises` confirma as exceções esperadas. Uma exceção capturada por `assertRaises` faz parte do comportamento que o teste verifica.

Além da suíte, foi conferida a execução do cenário principal com 100 e zero usuários: os totais mensais foram, respectivamente, US$ 13,44 / R$ 67,20 e US$ 13,00 / R$ 65,00. Essa conferência adicional foi executada em memória durante o desenvolvimento e não está salva como teste automatizado no repositório.

Antes da criação dessa suíte, foram executados roteiros temporários de 110 e 232 casos durante a implementação e a refatoração das validações. Esses números são registros históricos e não representam a quantidade de testes salvos atualmente.

Exceções ainda não são tratadas em uma interface: fora dos testes, uma chamada inválida sem tratamento pode interromper o script com a mensagem do erro.

### Próximos incrementos

Revisar as alternativas pesquisadas e escolher com o autor a próxima configuração de estudo, revalidando preços e condições antes de alterar o cenário. Revisar casos adicionais de limite nas funções de respostas e feedbacks e definir o próximo incremento da calculadora. O tratamento das mensagens de erro na apresentação poderá ser introduzido antes de receber entradas interativas.

Os custos de infraestrutura já são calculados com valores didáticos. Leitura de CSV, comparação automatizada de cenários, gráficos e dashboard ainda serão implementados.


## Primeira versão planejada

A primeira entrega funcional será uma calculadora em Python puro, com um cenário por execução, considerando:

- Mensalidades de backend e banco de dados.
- GPT-6 Luna (`gpt-6-luna`) como modelo de referência da API da OpenAI.
- Consumo de IA estimado a partir das respostas dos estudantes.
- Feedback em cada resposta errada e feedback opcional nos acertos.
- Custos mensais por categoria, total mensal em reais e projeção anual constante.

Os resultados serão estimativas baseadas em preços pesquisados e hipóteses de consumo. Não representarão despesas efetivamente realizadas nem comprovarão a capacidade dos planos escolhidos.

## Tecnologias previstas

| Tecnologia | Aplicação |
|---|---|
| Python | Lógica e cálculos |
| Pandas | Organização dos dados e comparação de cenários |
| CSV | Formato de arquivo para armazenamento inicial dos preços |
| Plotly | Gráficos interativos |
| Streamlit | Interface do dashboard |
| Git e GitHub | Versionamento e hospedagem do repositório |

As tecnologias serão introduzidas gradualmente, conforme a necessidade de cada etapa.

## Etapas de desenvolvimento

1. Planejamento: requisitos, dados, premissas e fórmulas.
2. Calculadora básica: implementação com Python puro.
3. Análise de dados: tabelas e comparação de cenários com Pandas.
4. Visualização: gráficos com Plotly.
5. Dashboard: interface com Streamlit.
6. Validação final e publicação da aplicação: consolidação dos testes, documentação e disponibilização do dashboard.

Testes e documentação acompanharão as implementações desde os primeiros cálculos.

## Evoluções futuras

Permitir selecionar e comparar os custos de modelos de diferentes provedores, incluindo Claude, Qwen e Gemini, além dos modelos da OpenAI. A inclusão de cada opção dependerá da pesquisa de preços oficiais, unidades e regras de cobrança da API escolhida.

A calculadora simulará os custos dessas APIs; não será necessário fazer chamadas reais para comparar os cenários. A primeira versão continuará limitada a um modelo da OpenAI.

## Documentação

Consulte o [planejamento do projeto](PLANEJAMENTO.md) para conhecer as entradas, regras de negócio, fórmulas e limitações da primeira versão.

O [registro de prompts](PROMPTS.md) documenta pedidos e decisões relevantes do desenvolvimento com apoio de IA.

## Aprendizado e uso de IA

O desenvolvimento conta com apoio de IA para orientação técnica, explicação de conceitos e revisão. A proposta é implementar pequenas funcionalidades, compreender os cálculos e validar os resultados ao longo do aprendizado.
