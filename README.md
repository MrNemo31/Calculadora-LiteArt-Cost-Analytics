# LiteArt Cost Analytics

Projeto pessoal de Análise de Dados para simular os custos operacionais de uma aplicação de
software, utilizando o LiteArt como estudo de caso.

O LiteArt é uma plataforma educacional em desenvolvimento, voltada à preparação para vestibulares,
com questões, simulados, acompanhamento de desempenho e feedbacks pedagógicos personalizados por
Inteligência Artificial.

## Objetivos

- Estimar custos mensais e anuais de infraestrutura e APIs de IA.
- Comparar serviços e cenários de utilização.
- Converter custos em dólares para reais com uma cotação informada.
- Desenvolver conhecimentos de Python e Análise de Dados por meio da prática.
- Construir uma ferramenta que possa ser adaptada a outros projetos de software.

## Situação atual

**Etapa 3 — Início da análise de dados com Pandas.** O arquivo `calculadora.py` já organiza os
cálculos de consumo, custos de IA e mensalidades de infraestrutura em funções, usando GPT-6 Luna
como referência inicial. As entradas são definidas em cinco dicionários no bloco principal:
hipóteses de consumo e capacidade, preços de IA e infraestrutura e cotação. Ainda não há entrada
interativa. O terminal apresenta a comparação didática de 100 e 500 usuários e o primeiro
DataFrame, criado a partir da lista de resumos dos cenários.

### Funcionalidades implementadas

- Comparação dos cenários didáticos de 100 e 500 usuários no terminal, com lista e laço for.
- Lista de resumos com sete campos por cenário e custos preservados como Decimal.
- Primeiro DataFrame com Pandas: dois cenários, sete colunas e apresentação no terminal.
- Seleção de três colunas e ordenação por custo mensal decrescente em `comparacao_custos`.
- Filtro de cenários por orçamento mensal didático, preservando custos em `Decimal`.
- Coluna calculada de saldo do orçamento, com sobra ou excesso por cenário em `Decimal`.
- Resumo do menor e maior custo mensal e da diferença entre os extremos, preservando `Decimal`.
- Formatação monetária com duas casas decimais nas tabelas e resumos, somente na apresentação.
- Exportação dos dois cenários e sete colunas de `tabela_cenarios` para `resultados/cenarios.csv`.
- Organização das hipóteses de consumo e capacidade, preços e cotação em dicionários separados.
- Cálculo do consumo de um cenário a partir das hipóteses, com retorno em um novo dicionário.
- Volume mensal de respostas, acertos, erros e feedbacks.
- Consumo mensal estimado de tokens de entrada e saída.
- Custos mensais de entrada e saída de IA em dólares, com `Decimal` .
- Coordenação dos custos de IA por cenário, com conversão e projeção anual retornadas em um
  dicionário.
- Mensalidades de backend e banco, calculadas por preço por unidade e quantidade contratada.
- Coordenação dos custos de infraestrutura por cenário, com conversão e projeção anual em um novo
  dicionário.
- Cenário completo com consumo, custos por categoria e totais organizados em um dicionário.
- Soma de infraestrutura e IA, com totais mensais e anuais em dólares e reais.
- Conversão dos custos para reais com cotação didática informada no código.
- Projeção anual em dólares e reais, mantendo consumo, preços e câmbio constantes.
- Apresentação dos resultados com os símbolos US$ e R$.
- Validação de tipos, valores negativos, taxas fora do intervalo, infinito e NaN nos argumentos das
  funções.
- Testes automatizados reproduzíveis das sete funções de cálculo e das três coordenadoras de partes
  do cenário e da função de cenário completo, usando `unittest` .

### Organização das entradas em dicionários

Dentro do bloco principal, as entradas estão agrupadas por finalidade:

| Dicionário | Conteúdo | Natureza dos dados |
| --- | --- | --- |
| `hipoteses_consumo` | Usuários, respostas por usuário, taxa de acerto, parcela dos acertos com feedback e tokens por feedback | Hipóteses didáticas de consumo |
| `hipoteses_capacidade` | Quantidades de unidades de backend e banco | Hipóteses didáticas de capacidade |
| `precos_ia` | Tarifas de entrada e saída em USD por milhão de tokens | Preços pesquisados, com fonte e data nos comentários e no planejamento |
| `precos_infraestrutura` | Preços mensais por unidade de backend e banco em USD | Valores inventados para aprendizado |
| `cotacao` | `brl_por_usd`, com `Decimal("5.00")` | Configuração cambial didática e manual |

Os preços e a cotação mantêm o tipo `Decimal` . As quantidades `quantidade_backend` e
`quantidade_banco` são chaves de `hipoteses_capacidade` , separadas dos preços e das hipóteses de
consumo.

As funções de cálculo recebem valores individuais. A função coordenadora `calcular_consumo_cenario`
recebe o dicionário inteiro de hipóteses, busca os valores pelas chaves e retorna um novo dicionário
de resultados. A coordenadora de custos de IA recebe consumo, preços e cotação em dicionários; a
coordenadora de infraestrutura recebe preços, capacidade e cotação. Os resultados não são gravados
nos dicionários de entrada.

Essa organização prepara a reutilização dos cálculos em diferentes cenários. O cenário completo já
pode ser calculado por uma função. Leitura de CSV e consulta automática de câmbio ainda não foram
implementadas.

Na última refatoração, a saída completa foi comparada antes e depois e permaneceu idêntica. Os 111
métodos de teste também passaram. Os testes das funções usam entradas próprias; alterações nos
dicionários do cenário devem ser conferidas executando também `calculadora.py` .

### Cálculo do consumo de um cenário

A função `calcular_consumo_cenario(hipoteses_consumo)` recebe o dicionário inteiro e coordena as
funções de respostas, feedbacks e tokens. Ela não calcula custos nem imprime resultados.

Antes dos cálculos, exige um `dict` e confere as seis chaves obrigatórias: `usuarios_ativos` ,
`respostas_por_usuario` , `taxa_acerto` , `proporcao_acertos_com_feedback` , `tokens_entrada` e
`tokens_saida` .

- Argumento que não seja `dict` : `TypeError` .
- Chave obrigatória ausente: `ValueError` com o nome do campo.
- Valor inválido: a exceção da função de cálculo é propagada.
- Chaves adicionais: permitidas, sem participar do consumo.
- Entrada: preservada, sem acrescentar resultados nem alterar seus valores.

O retorno é um novo dicionário com `respostas_mensais` , `acertos_mensais` , `erros_mensais` ,
`feedbacks_nos_acertos` , `feedbacks_mensais` , `tokens_entrada_total` e `tokens_saida_total` .

No bloco principal, `consumo_cenario` recebe esse retorno. Seu retorno alimenta a coordenadora de
custos de IA, e os valores de consumo são usados nos `print()` existentes. O cenário permanece com
4.000 respostas, 2.200 feedbacks e 1.100.000/660.000 tokens de entrada/saída. A função
calcular_cenario reúne consumo, preços, infraestrutura e câmbio.

### Cálculo dos custos de IA de um cenário

A função `calcular_custo_ia_cenario(consumo_cenario, precos_ia, cotacao)` coordena os custos de
tokens, a conversão para reais e a projeção anual. Reutiliza `calcular_custo_tokens` ,
`calcular_real` e `calcular_custo_anual` , sem imprimir resultados ou alterar as entradas.

| Argumento | Chaves obrigatórias |
| --- | --- |
| `consumo_cenario` | `tokens_entrada_total`, `tokens_saida_total` |
| `precos_ia` | `entrada_por_milhao_usd`, `saida_por_milhao_usd` |
| `cotacao` | `brl_por_usd` |

Os três argumentos devem ser `dict` ; outros tipos geram `TypeError` . Uma chave ausente gera
`ValueError` com o campo identificado. As funções existentes validam os números e suas exceções são
propagadas. Chaves adicionais são aceitas, permitindo usar diretamente o retorno completo de
`calcular_consumo_cenario` .

O retorno é um novo dicionário com oito resultados em `Decimal` : custos de entrada, saída e total
mensal em USD e BRL, além dos totais anuais nas duas moedas. No cenário principal,
`custos_ia_cenario` recebe esse dicionário; seus valores alimentam os `print()` e a soma com
infraestrutura.

O cenário preserva US$ 0,44 / R$ 2,20 mensais de IA e US$ 5,28 / R$ 26,40 anuais. A função não
calcula infraestrutura nem consulta câmbio; utiliza os dados recebidos e mantém a projeção de 12
meses constantes.

### Cálculo dos custos de infraestrutura de um cenário

A função `calcular_custo_infra_cenario(precos_infraestrutura, hipoteses_capacidade, cotacao)`
coordena mensalidades de backend e banco, conversão para reais e projeção anual. Reutiliza
`calcular_custo_servico` , `calcular_real` e `calcular_custo_anual` , sem imprimir resultados ou
modificar as entradas.

| Argumento | Chaves obrigatórias |
| --- | --- |
| `precos_infraestrutura` | `backend_mensal_por_unidade_usd`, `banco_mensal_por_unidade_usd` |
| `hipoteses_capacidade` | `quantidade_backend`, `quantidade_banco` |
| `cotacao` | `brl_por_usd` |

Os três argumentos devem ser `dict` ; outros tipos geram `TypeError` . Uma chave obrigatória ausente
gera `ValueError` com o campo identificado. As validações numéricas das funções existentes são
preservadas: preços em `Decimal` finitos e não negativos, quantidades `int` não negativas e cotação
finita e positiva. Chaves adicionais são permitidas sem participar dos cálculos.

O retorno é um novo dicionário com oito resultados em `Decimal` : backend, banco e total mensal em
USD e BRL, mais os totais anuais de infraestrutura nas duas moedas. No bloco principal,
`custos_infra_cenario` recebe esse retorno, que alimenta a soma com IA e os `print()` .

A função utiliza os serviços contratados, independentemente da quantidade de estudantes. Com os
valores didáticos, mantém US$ 13,00 / R$ 65,00 mensais e US$ 156,00 / R$ 780,00 anuais. A projeção
pressupõe 12 meses com preços, quantidades e câmbio constantes; a capacidade de atendimento não foi
validada.

### Cálculo do cenário completo

A função
`calcular_cenario(hipoteses_consumo, hipoteses_capacidade, precos_ia, precos_infraestrutura, cotacao)`
reúne as três coordenadoras e calcula os totais. As verificações de tipos, chaves e valores são
feitas pelas funções chamadas, que propagam suas exceções.

O retorno é um novo dicionário com quatro grupos:

| Chave | Conteúdo |
| --- | --- |
| `consumo` | Respostas, acertos, erros, feedbacks e tokens |
| `custos_ia` | Custos mensais e anuais de IA em USD e BRL |
| `custos_infraestrutura` | Custos de backend, banco e infraestrutura em USD e BRL |
| `totais` | Totais mensais e anuais de infraestrutura e IA em USD e BRL |

O acesso utiliza duas chaves, como `resultado_cenario["totais"]["custo_total_mensal_br"]` . A função
não imprime resultados nem modifica os cinco dicionários recebidos. Cada execução produz seus
próprios resultados; chaves adicionais nas entradas são permitidas pelas coordenadoras.

No bloco principal, uma chamada a `calcular_cenario` substitui a sequência de cálculos. Os grupos
são recuperados para manter os `print()` existentes. O total continua em US$ 13,44 / R$ 67,20 por
mês e US$ 161,28 / R$ 806,40 por ano, com as hipóteses didáticas e 12 meses constantes.

### Organização das funções

| Função | Responsabilidade |
| --- | --- |
| `calcular_cenario` | Reunir consumo, custos por categoria e totais do cenário |
| `calcular_consumo_cenario` | Coordenar respostas, feedbacks e tokens a partir das hipóteses |
| `calcular_custo_ia_cenario` | Coordenar custos mensais e anuais de IA em USD e BRL |
| `calcular_custo_infra_cenario` | Coordenar custos mensais e anuais de infraestrutura em USD e BRL |
| `calcular_respostas_mensais` | Estimar o volume de respostas |
| `calcular_feedbacks_mensais` | Calcular acertos, erros e feedbacks |
| `calcular_tokens_mensais` | Estimar os totais de tokens de entrada e saída |
| `calcular_custo_tokens` | Calcular custo em USD a partir da tarifa por milhão de tokens |
| `calcular_real` | Converter um custo em USD para BRL |
| `calcular_custo_anual` | Projetar 12 meses de custo constante |
| `calcular_custo_servico` | Calcular mensalidade por preço unitário e quantidade, na moeda informada |
| `validar_numero_nao_negativo` | Centralizar a validação de tipo permitido, valor finito e ausência de negativos |

As funções de cálculo retornam valores; os `print()` apresentam os resultados separadamente. A
auxiliar de validação sinaliza erros com exceções; quando a entrada é válida, termina sem retorno
explícito (`None`).

### Auxiliar de validação

A função `validar_numero_nao_negativo(valor, nome, tipos_permitidos=(int, float))` centraliza as
regras compartilhadas pelas sete funções de cálculo:

- `valor` : dado que será verificado.
- `nome` : rótulo do campo usado nas mensagens de erro, sem participar do cálculo.
- `tipos_permitidos` : parâmetro opcional que aceita `int` e `float` por padrão. Preços e custos
  informam `(Decimal,)` ; a cotação informa `(int, float, Decimal)` .

A auxiliar rejeita tipos não permitidos, infinito, NaN e negativos, sem converter o valor. Para
conferir valores finitos, usa `math.isfinite` com `float` e `.is_finite()` com `Decimal` . As
mensagens seguem um formato compartilhado e identificam o campo.

Regras específicas permanecem nas funções de cálculo: usuários e quantidades de unidades devem ser
inteiros, taxas não podem ultrapassar 1 e a cotação deve ser maior que zero. A auxiliar já garante o
limite inferior de zero para as taxas. As fórmulas, os tipos aceitos e os resultados do cenário
didático foram preservados.

### Cenário didático de referência

| Entrada | Hipótese |
| --- | ---: |
| Usuários ativos por mês | 100 |
| Respostas por usuário no mês | 40 |
| Taxa de acerto | 60% |
| Parcela dos acertos com feedback | 25% |
| Tokens de entrada por feedback | 500 |
| Tokens de saída faturáveis por feedback | 300 |
| Cotação didática | R$ 5,00 por US$ 1,00 |

As tarifas pesquisadas do Luna são US$ 0,10 por milhão de tokens de entrada sem cache e US$ 0,50 por
milhão de saída, no processamento Standard e nas condições registradas no planejamento. Fontes e
data de consulta (2026-10-23) estão no [PLANEJAMENTO.md](PLANEJAMENTO.md) .

| Resultado do cenário | Valor |
| --- | ---: |
| Feedbacks mensais | 2.200 |
| Tokens mensais de entrada | 1.100.000 |
| Tokens mensais de saída | 660.000 |
| Custo mensal estimado de IA em USD | US$ 0,44 |
| Custo mensal estimado de IA em BRL | R$ 2,20 |
| Custo anual estimado de IA em USD | US$ 5,28 |
| Custo anual estimado de IA em BRL | R$ 26,40 |

Esses valores conferem a aritmética do cenário. Não são despesas reais nem medições do consumo de
uma API. A calculadora não realiza chamadas à OpenAI.

### Custos de infraestrutura e total do cenário

Os preços de infraestrutura abaixo são inventados para aprendizado, não preços pesquisados. A função
`calcular_custo_servico` multiplica o preço mensal por unidade pela quantidade contratada e retorna
`Decimal` na moeda do preço, sem conversão automática.

| Serviço | Preço didático por unidade/mês | Quantidade | Mensal em USD | Mensal em BRL |
| --- | ---: | ---: | ---: | ---: |
| Backend | US$ 5,00 | 2 | US$ 10,00 | R$ 50,00 |
| Banco PostgreSQL | US$ 3,00 | 1 | US$ 3,00 | R$ 15,00 |
| **Infraestrutura** | — | — | **US$ 13,00** | **R$ 65,00** |

A conversão usa R$ 5,00 por dólar, uma cotação didática. O cenário soma apenas custos na mesma
moeda, sem arredondar etapas intermediárias.

| Categoria | Mensal em USD | Mensal em BRL | Anual em USD | Anual em BRL |
| --- | ---: | ---: | ---: | ---: |
| Infraestrutura | US$ 13,00 | R$ 65,00 | US$ 156,00 | R$ 780,00 |
| IA | US$ 0,44 | R$ 2,20 | US$ 5,28 | R$ 26,40 |
| **Total do cenário** | **US$ 13,44** | **R$ 67,20** | **US$ 161,28** | **R$ 806,40** |

A projeção anual mantém serviços, consumo, preços e câmbio constantes. Com zero usuários, o consumo
variável de IA fica zero, mas os serviços contratados permanecem em US$ 13,00 ou R$ 65,00 mensais.

A pesquisa inicial de hospedagem já está registrada no planejamento, mas ainda não substituiu os
preços didáticos do cenário. Esses valores não demonstram a capacidade de atendimento do LiteArt. Se
o banco estiver incluído na hospedagem, seu custo não deve ser contado duas vezes. O total contempla
apenas as categorias e condições deste cenário; as exclusões da primeira versão estão no
planejamento.

### Comparação inicial de dois cenários didáticos

Ao final da execução, o programa compara 100 e 500 usuários. A lista `cenarios_didaticos` reúne
o nome e as hipóteses de consumo e capacidade de cada cenário. Os dicionários são copiados com
`copy()`, permitindo alterar a quantidade de usuários sem modificar o outro cenário.

O laço `for` chama `calcular_cenario` para cada item, apresenta o resumo no terminal e guarda
nome, usuários e resultado em `comparacao_cenarios`. Os preços e a cotação são compartilhados.

| Resultado | 100 usuários | 500 usuários |
| --- | ---: | ---: |
| Respostas mensais | 4.000 | 20.000 |
| Feedbacks mensais | 2.200 | 11.000 |
| Tokens mensais de entrada | 1.100.000 | 5.500.000 |
| Tokens mensais de saída | 660.000 | 3.300.000 |
| IA mensal | R$ 2,20 | R$ 11,00 |
| Infraestrutura mensal | R$ 65,00 | R$ 65,00 |
| Total mensal | R$ 67,20 | R$ 76,00 |
| Total anual | R$ 806,40 | R$ 912,00 |

Apenas os usuários mudam: respostas por usuário, taxas, tokens por feedback, preços, cotação e
quantidades contratadas permanecem constantes. Assim, consumo e custo de IA crescem cinco vezes,
enquanto a infraestrutura fica igual. Isso não comprova capacidade para atender 500 usuários.

O detalhamento original continua sendo apresentado antes da comparação. Para conferir ambos,
execute `calculadora.py` com seu interpretador Python 3. Os resultados são estimativas didáticas,
com cotação de R$ 5,00 por dólar e projeção de 12 meses constantes, sem chamadas à API.

A última conferência adicional verificou os dois cenários, a preservação das entradas e do
detalhamento anterior e a multiplicação por cinco do consumo e da IA. Esse roteiro foi executado
durante o desenvolvimento e não foi salvo na suíte. Os 111 métodos existentes passaram; a
comparação no bloco principal ainda deve ser conferida executando também a calculadora.

### Lista de resumos e primeiro DataFrame

A lista `resumos_cenarios` organiza os resultados em dois dicionários planos, um por cenário.
Cada registro contém os mesmos sete campos:

| Campo | Conteúdo |
| --- | --- |
| `cenario` | Nome da simulação |
| `usuarios_ativos` | Quantidade de usuários |
| `feedbacks_mensais` | Feedbacks estimados no mês |
| `custo_ia_mensal_br` | Custo mensal de IA em BRL |
| `custo_infra_mensal_br` | Custo mensal de infraestrutura em BRL |
| `custo_total_mensal_br` | Total mensal em BRL |
| `custo_total_anual_br` | Projeção anual em BRL |

O laço percorre `comparacao_cenarios`, seleciona valores já calculados e acrescenta cada resumo
com `append()`. Não refaz as fórmulas. Nos dados de cálculo, os custos permanecem como `Decimal`,
sem símbolos monetários, conversão para texto ou arredondamento intermediário.

O terminal apresenta os resumos antes da tabela. Para cada registro, `resumo_exibicao` reúne os
campos financeiros como textos com duas casas decimais, mantendo os demais campos como recebidos.
A lista `resumos_cenarios` continua com os objetos `Decimal` originais: por exemplo,
`Decimal('67.200000')` é apresentado como `67.20`, sem substituir o valor armazenado.
Cada registro é um dicionário novo, e os resultados completos permanecem na comparação original.

Foram conferidos os dois registros, os sete campos, os valores conhecidos e os tipos monetários,
além da independência entre registros e da preservação dos resultados anteriores. Essa
conferência foi executada durante o desenvolvimento, sem novos métodos na suíte: os 111 testes
existentes passaram. Os totais mensais continuam em R$ 67,20 e R$ 76,00 e os anuais em
R$ 806,40 e R$ 912,00, para 100 e 500 usuários, respectivamente.

Dentro do bloco principal, após montar a lista, a tabela é criada com Pandas:

```python
tabela_cenarios = pd.DataFrame.from_records(resumos_cenarios, coerce_float=False)
```

Cada dicionário de `resumos_cenarios` vira uma linha de `tabela_cenarios`. São duas linhas, para
100 e 500 usuários, e sete colunas, na ordem dos campos acima. A criação não refaz os cálculos.

Nos dados da tabela, os quatro campos financeiros mantêm objetos `Decimal`, sem conversão para
`float` ou texto e sem arredondamento intermediário. `coerce_float=False` evita a conversão para
float na criação da tabela. A apresentação produz textos formatados separadamente.
Essas colunas apresentam `dtype object`, que permite armazenar objetos Python como `Decimal`;
o dtype sozinho não comprova o tipo de cada valor. A conferência usou `isinstance(valor, Decimal)`
individualmente nos oito valores financeiros dos dois cenários.

Na inspeção realizada, `cenario` apresentou tipo `str`, `usuarios_ativos`, `int64`, e
`feedbacks_mensais`, `float64`. Os feedbacks já eram `float` na lista de origem; essa informação
não altera os tipos monetários.

A apresentação usa `to_string()` com `index=False` e formatadores monetários por coluna.
`index=False` oculta a numeração das linhas. A representação textual é usada somente na impressão;
os valores financeiros da tabela continuam sendo objetos `Decimal`.
Os cenários permanecem didáticos, sem despesas reais ou capacidade de atendimento comprovada.
A tabela já é exportada para CSV; a importação de hipóteses de cenários continua planejada.

As verificações pontuais confirmaram o formato `(2, 7)`, a ordem dos campos, a igualdade com a
lista e sua preservação desde antes da criação da tabela, além dos resultados exatos dos dois
cenários. Também confirmaram a importação sem executar o cenário e a manutenção das funções e
saídas anteriores. Esses roteiros não foram adicionados a `test_calculadora.py`; os 111 métodos
existentes passaram com o Python da `.venv-win`.

### Seleção e ordenação dos custos mensais

Dentro do bloco principal, `comparacao_custos` reúne três colunas de `tabela_cenarios`, nesta
ordem: `cenario`, `usuarios_ativos` e `custo_total_mensal_br`. Os cenários são ordenados pelo
custo mensal, do maior para o menor, em outro DataFrame. A tabela original mantém seus valores,
tipos, colunas, índices e ordem das linhas.

A comparação tem duas linhas e três colunas. O cenário de 500 usuários aparece primeiro, com
custo mensal igual a `Decimal("76.00")`; o de 100 usuários vem depois, com `Decimal("67.20")`.
Os índices originais acompanham as linhas: a comparação fica com `[1, 0]`, enquanto
`tabela_cenarios` permanece com `[0, 1]`. O terminal apresenta um título explicativo e
`to_string()` com índices ocultos e formatadores monetários, preservando as saídas anteriores.
Nos dados de cálculo, os custos continuam em `Decimal`, sem conversão ou arredondamento.

As verificações pontuais conferiram o formato `(2, 3)`, a ordem das colunas e dos cenários e os
custos exatos. Cada custo passou por `isinstance(valor, Decimal)`; `dtype object` sozinho não
comprova esse tipo. A comparação com uma cópia anterior de `tabela_cenarios`, usando
`assert_frame_equal` e conferências dos tipos individuais, confirmou sua preservação integral.
Também foram preservadas as funções de cálculo, as saídas e a importação sem executar os cenários.
Essas conferências foram executadas em memória, sem novos testes no repositório. A calculadora
foi executada com a `.venv-win`, e os 111 testes existentes passaram.

### Filtro de cenários por orçamento mensal

O limite didático `orcamento_mensal_br` é definido como `Decimal("70.00")` no bloco principal,
após a seleção e ordenação dos custos. Não representa um orçamento real do LiteArt e não há
entrada interativa para alterá-lo.

A comparação de `custo_total_mensal_br` com o limite usa `<=`, incluindo custos menores ou iguais
ao orçamento. Ela produz a máscara booleana `dentro_do_orcamento`, com um valor `True` ou `False`
por cenário. A seleção com `.loc` mantém apenas as linhas aprovadas em `cenarios_no_orcamento`.
As três colunas, a ordem da comparação e os índices originais são preservados, sem redefinição.

Com R$ 70,00, somente o cenário de 100 usuários é apresentado, com custo mensal de R$ 67,20.
O resultado tem uma linha, três colunas e índice `[0]`. O terminal mostra o orçamento e um título
explicativo; a tabela é apresentada sem os índices, mantendo as saídas anteriores.
Quando `.empty` identifica um resultado sem linhas, a mensagem é:
"Nenhum cenário avaliado cabe no orçamento mensal informado."

Nos dados filtrados, os custos continuam como objetos `Decimal`, sem conversão para float ou texto
e sem arredondamento intermediário. `tabela_cenarios` e `comparacao_custos` permanecem integralmente
iguais, incluindo valores, tipos, colunas, índices e ordem das linhas.

As verificações pontuais em memória confirmaram os seguintes limites, sem mudar os R$ 70,00
definidos no arquivo:

| Orçamento em BRL | Cenários incluídos, na ordem | Índices |
| --- | --- | --- |
| R$ 70,00 | 100 usuários, com R$ 67,20 mensais | `[0]` |
| R$ 67,20 | Somente 100 usuários | `[0]` |
| R$ 76,00 | 500 usuários e depois 100 usuários | `[1, 0]` |
| R$ 60,00 | Nenhum; mensagem de resultado vazio confirmada | `[]` |

Os valores financeiros selecionados foram conferidos com `isinstance(valor, Decimal)`.
Os dois DataFrames de origem foram comparados com cópias anteriores à filtragem, incluindo
conferências dos tipos individuais. A importação silenciosa, as funções de cálculo e as saídas
anteriores foram preservadas. A calculadora e os 111 testes existentes passaram na `.venv-win`;
essas verificações específicas do filtro não foram adicionadas como novos testes ao repositório.

### Saldo do orçamento por cenário

No bloco principal, `analise_orcamento` é criada com uma cópia de `comparacao_custos`, mantendo
os dois cenários na ordem de 500 e depois 100 usuários. A coluna `saldo_orcamento_br` é
acrescentada ao final, com a fórmula: orçamento mensal menos custo total mensal.
A subtração é feita diretamente sobre a coluna de custos, elemento por elemento, sem laço
ou `apply`. A análise tem duas linhas, quatro colunas e índices `[1, 0]`.

O orçamento didático permanece em `Decimal("70.00")`. Saldo positivo indica sobra; negativo
indica excesso sobre o orçamento; zero indica custo igual ao limite. Esse saldo não representa
lucro, pois não considera receitas.

| Usuários | Custo total mensal | Saldo do orçamento |
| ---: | ---: | ---: |
| 500 | R$ 76,00 | −R$ 6,00 |
| 100 | R$ 67,20 | R$ 2,80 |

Nos dados da análise, custos e saldos permanecem como objetos `Decimal`, sem conversão para float
ou texto e sem arredondamento intermediário. A cópia permite acrescentar a coluna sem alterar
`comparacao_custos`. Também são preservados `tabela_cenarios` e `cenarios_no_orcamento`, incluindo
valores, tipos, colunas, índices e ordem das linhas.

O terminal acrescenta a tabela sem índices, com um título que informa o orçamento e uma breve
explicação dos sinais do saldo, mantendo as saídas anteriores. São estimativas didáticas, sem
representar despesas reais ou comprovar a capacidade dos serviços.

As verificações pontuais confirmaram os custos e saldos exatos e conferiram os quatro valores
financeiros com `isinstance(valor, Decimal)`. Uma subtração adicional em memória, com orçamento
de `Decimal("67.20")`, produziu saldo zero para 100 usuários, sem alterar o limite principal ou
os resultados finais. Os três DataFrames anteriores foram comparados com cópias feitas antes da
análise, incluindo conferências dos tipos individuais, e permaneceram integralmente iguais.
As funções, a importação silenciosa e as saídas anteriores também foram preservadas.
A calculadora e os 111 testes existentes passaram na `.venv-win`; as verificações do saldo não
foram adicionadas como novos testes automatizados ao repositório.

### Resumo dos custos mensais

O resumo utiliza a coluna `custo_total_mensal_br` de `comparacao_custos`, com os dois cenários
completos, sem aplicar o filtro de orçamento. As agregações `.min()` e `.max()` retornam um
único valor cada: `menor_custo_mensal_br` e `maior_custo_mensal_br`, respectivamente.
`diferenca_custos_mensais_br` é calculada subtraindo o menor custo do maior.

| Resultado | Valor em BRL |
| --- | ---: |
| Menor custo mensal, para 100 usuários | R$ 67,20 |
| Maior custo mensal, para 500 usuários | R$ 76,00 |
| Diferença entre os extremos | R$ 8,80 |

Os três resultados permanecem como objetos `Decimal`, sem conversão para float ou arredondamento
intermediário. O terminal acrescenta um resumo com rótulos, símbolo R$ e duas casas decimais
somente na exibição, mantendo as saídas anteriores.

Os extremos incluem todos os cenários avaliados; filtrar pelo orçamento antes da agregação
excluiria o cenário de maior custo neste exemplo. A diferença depende das hipóteses atuais:
a infraestrutura permanece em R$ 65,00 nos dois cenários, enquanto a IA passa de R$ 2,20 para
R$ 11,00. Mudanças no consumo, nos preços, no câmbio ou na infraestrutura podem alterar esse
resultado. Os valores são estimativas didáticas, não despesas reais ou custos medidos de uma API.

As verificações pontuais confirmaram igualdade com `Decimal("67.20")`, `Decimal("76.00")` e
`Decimal("8.80")`, além de `isinstance(valor, Decimal)` nos três resultados. Os quatro DataFrames
anteriores foram comparados com cópias anteriores às agregações e permaneceram iguais, incluindo
valores, tipos, colunas, índices e ordem das linhas. As funções de cálculo, a importação silenciosa
e as saídas anteriores também foram preservadas. A calculadora e os 111 testes existentes passaram
na `.venv-win`; as verificações específicas do resumo foram executadas em memória, sem novos
testes automatizados persistentes no repositório.

### Formatação monetária no terminal

Os valores financeiros são apresentados com duas casas decimais no detalhamento, nos resumos e
nas quatro tabelas. Nas mensagens individuais, `:.2f` formata o Decimal em uma representação
textual com duas casas. O terminal usa ponto decimal, como `67.20`; a documentação apresenta
os valores em notação brasileira, como R$ 67,20. Os títulos das tabelas identificam a moeda BRL.

O dicionário `formatadores_monetarios` associa os nomes das colunas de custos e saldo ao
formatador `"{:.2f}".format`. Ele é passado pelo argumento `formatters` de `DataFrame.to_string()`
na tabela completa, na comparação, no filtro e na análise de saldo. `index=False` oculta os
índices somente na impressão.

Para os resumos em dicionários, `resumo_exibicao` contém textos formatados para os valores
financeiros, enquanto `resumos_cenarios` mantém os objetos `Decimal` usados nos cálculos.
Esses textos de apresentação não são atribuídos às colunas dos DataFrames.

A formatação arredonda somente a representação exibida quando necessário: um valor como
`Decimal("1.236")` é apresentado como `1.24`, mas continua armazenado com sua precisão original.
Não há arredondamento ou substituição dos valores dentro dos DataFrames. Cálculos, agregações,
ordenação e filtros continuam usando os objetos `Decimal` com sua precisão completa.
As afirmações de preservação do tipo e ausência de conversão para texto referem-se a esses dados
de cálculo; a impressão necessariamente gera uma representação textual separada.

Uma conferência pontual em memória verificou a apresentação das quatro tabelas e dos resumos,
a separação entre textos e dados, os tipos financeiros e a preservação dos DataFrames e da lista.
Também confirmou a exibição de `1.236` como `1.24` sem alterar o Decimal e a manutenção de
`Decimal('67.200000')` nos dados. Os 111 testes existentes passaram na `.venv-win`.
Essa conferência específica de precisão e apresentação não foi adicionada como teste persistente.

### Exportação da tabela de cenários para CSV

A execução exporta diretamente `tabela_cenarios` para `resultados/cenarios.csv`, com os dois
cenários na ordem original, de 100 e depois 500 usuários, e os sete campos descritos acima.
Não são exportadas a comparação ordenada, a tabela filtrada ou a coluna de saldo.

O caminho usa `Path(__file__).resolve().parent`: o destino é relativo à pasta de `calculadora.py`,
independentemente da pasta em que o terminal foi aberto. A pasta `resultados` é criada
automaticamente quando necessário. Cada execução substitui o CSV anterior, sem acumular linhas,
e apresenta no terminal o caminho completo do arquivo salvo.

O arquivo usa UTF-8, campos separados por vírgula, ponto decimal e cabeçalho. O índice do
DataFrame não é exportado, e os números não recebem símbolos monetários ou separadores de milhares.
Os nomes dos cenários mantêm seus acentos.

O terminal continua apresentando duas casas decimais. O CSV recebe os valores completos dos dados,
sem formatadores de exibição, `:.2f`, `float_format` ou conversão para float. Por exemplo,
o custo exibido como `67.20` é exportado como `67.200000`, preservando a precisão original.

CSV armazena texto e não preserva o tipo Python `Decimal`. Para recuperar a precisão, os campos
financeiros devem ser lidos como texto e convertidos diretamente para `Decimal`, sem passagem
intermediária por float. A leitura feita para conferir o arquivo não constitui uma funcionalidade
de importação de cenários; essa entrada de hipóteses ainda depende de implementação e validação.
Os DataFrames e `resumos_cenarios` mantêm seus valores financeiros como objetos Decimal.

A regra `/resultados/` do `.gitignore` exclui a pasta de arquivos gerados do versionamento.
O CSV pode ser regenerado executando a calculadora; não precisa ser enviado ao Git.

Na conferência da implementação, o arquivo apresentou duas linhas de dados e sete colunas, com
cabeçalhos corretos, sem índice adicional e com acentos preservados. Os oito campos financeiros
foram lidos como texto e reconstruídos como Decimal, iguais aos originais, inclusive nas casas
decimais. Uma escrita e leitura pontual em arquivo temporário preservou `Decimal("1.23456789")`,
sem inserir esse valor nos cenários reais.

Também foram confirmadas a preservação da lista e dos quatro DataFrames, a regeneração sem
duplicatas ao executar de outra pasta e a importação do módulo sem impressão, criação ou alteração
do CSV. Os 111 testes existentes passaram na implementação. Essas conferências específicas foram
roteiros pontuais; não foram adicionados testes persistentes de CSV ao repositório.

### Pesquisa de hospedagem e alternativas de arquitetura

A pesquisa inicial de 2026-10-28 comparou três combinações para hospedar o backend e o PostgreSQL:

| Combinação pesquisada | Ponto de atenção registrado |
| --- | --- |
| Render + Neon | Opções gratuitas com franquias e suspensão por inatividade, além de alternativas pagas |
| Railway | Créditos gratuitos limitados e plano pago com consumo incluído; o mínimo cobrado não é uma mensalidade fixa de todos os serviços |
| Koyeb + Neon | Recursos gratuitos e pagos, com atenção ao plano selecionado e à possível cobrança inicial no cadastro |

A avaliação de 2026-10-30 acrescentou o **Firebase como alternativa em estudo**. Foram distinguidos
Authentication para login com Google, Hosting para arquivos web, Functions/Cloud Run para execução
de backend, Firestore como banco de documentos e SQL Connect com PostgreSQL via Cloud SQL.

**A arquitetura de referência do LiteArt continua sendo Flutter, backend Node.js/NestJS e
PostgreSQL.** Usar Firebase Authentication pode preservar essa arquitetura; adotar Firestore e
Functions exigiria rever parte do desenho. Nenhuma migração ou contratação foi realizada.

Preços, unidades de cobrança, franquias, condições de cadastro, testes temporários e fontes oficiais
estão na seção 6 do [planejamento](PLANEJAMENTO.md) . As consultas são registros datados e devem ser
revalidadas antes de contratar. Gratuidade de infraestrutura não inclui automaticamente o consumo
das APIs de IA.

Os preços pesquisados ainda não foram aplicados ao cenário principal, que permanece didático. Também
não há comparação automatizada entre provedores. Ofertas por consumo precisarão de hipóteses
adicionais antes de serem representadas pela calculadora.

### Como executar a versão atual

Pré-requisitos do ambiente validado: Python convencional 3.14.10 x64 para Windows e Pandas 3.1.0
instalado no ambiente isolado `.venv-win`. `decimal`, `math` e `unittest` continuam fazendo parte
da biblioteca padrão. Pandas é uma dependência externa, importada no início de `calculadora.py`;
por isso, precisa estar disponível também para importar as funções nos testes.

No PowerShell, com a `.venv-win` já preparada, use:

```powershell
Set-Location -LiteralPath 'D:\Natan\LiteArt Cost Analytics'
& '.\.venv-win\Scripts\python.exe' -B -c "import pandas as pd; print(pd.__version__)"
& '.\.venv-win\Scripts\python.exe' -X utf8 -B calculadora.py
```

Ao concluir, o terminal informa o arquivo salvo. Executar novamente substitui esse arquivo com os resultados atuais.

Os comandos conferem a versão do Pandas e executam a calculadora com o interpretador escolhido,
sem precisar ativar o ambiente ou alterar o PATH. `-X utf8` mantém os acentos na saída capturada,
e `-B` evita gerar bytecode. Se Pandas não estiver disponível, prepare essa dependência no ambiente
antes de executar; os comandos acima não instalam nem atualizam pacotes.

No VS Code, use **Python: Select Interpreter** e selecione
`D:\Natan\LiteArt Cost Analytics\.venv-win\Scripts\python.exe`.
A `.venv` anterior, baseada em MSYS2, permanece separada e preservada.

O cenário didático e os `print()` ficam dentro de `if __name__ == "__main__":` . Ao executar o
arquivo diretamente, o cenário é calculado e apresentado. Ao importar suas funções, esse bloco não é
executado, permitindo reutilizá-las nos testes sem imprimir os resultados do cenário nem criar
ou modificar o CSV.

### Validação das entradas

As sete funções de cálculo usam a auxiliar compartilhada e verificações específicas antes de
calcular. As coordenadoras de consumo, custos de IA e infraestrutura validam os respectivos
dicionários e suas chaves e reutilizam as validações numéricas por meio das funções de cálculo.
Tipos não permitidos geram `TypeError` ; valores fora das regras geram `ValueError` , com mensagens
que identificam o argumento inválido.

| Entrada | Tipos aceitos | Regras |
| --- | --- | --- |
| Usuários ativos e quantidade de unidades de serviço | `int` | Maior ou igual a zero; valores fracionários e `100.0` são recusados |
| Média de respostas por usuário e total de respostas mensais | `int` ou `float` | Finitos e maiores ou iguais a zero |
| Taxa de acerto e parcela dos acertos com feedback | `int` ou `float` | Entre 0 e 1, inclusive; a auxiliar rejeita negativos e valores não finitos, e a função verifica o limite superior |
| Tokens por feedback, feedbacks mensais e total de tokens | `int` ou `float` | Finitos e maiores ou iguais a zero; médias e estimativas fracionárias são permitidas |
| Preço por milhão de tokens, preço mensal por unidade e custos monetários | `Decimal` | Finitos e maiores ou iguais a zero |
| Cotação em BRL por USD | `int`, `float` ou `Decimal` | Finita e maior que zero; convertida internamente para `Decimal` |

Textos passados diretamente, `None` e valores booleanos (`True` e `False` ) são recusados. As
funções não convertem automaticamente textos numéricos. Construir explicitamente `Decimal("5.00")`
continua sendo válido.

Zero é permitido para consumo, quantidades, preços e custos. A cotação é a exceção: precisa ser
positiva. Valores especiais como infinito e NaN são recusados; para `float` , usamos `math.isfinite`
, e para `Decimal` , `.is_finite()` .

As validações são aplicadas aos argumentos das funções, mesmo quando elas são chamadas fora do
cenário principal. Elas verificam as regras definidas para as entradas; não demonstram que as
hipóteses representam o consumo real do LiteArt.

### Testes automatizados

O arquivo `test_calculadora.py` contém uma suíte reproduzível com `unittest` , da biblioteca padrão
do Python. São 111 métodos de teste, distribuídos em 11 classes: sete para os cálculos, três para as
coordenadoras de partes do cenário e uma para o cenário completo. Parte dos métodos usa `subTest`
para verificar várias entradas; essas tentativas não são contadas separadamente no total de métodos.

A contagem foi reconferida no arquivo atual. A exportação não acrescentou métodos à suíte;
as verificações específicas de escrita, releitura e precisão do CSV foram pontuais, conforme
descrito na seção de exportação.

A suíte verifica:

- Resultados conhecidos do cenário didático: respostas, feedbacks, tokens e custos mensais e anuais.
- Taxas nos limites 0 e 1 e rejeição de taxas fora do intervalo.
- Tipos inválidos, incluindo textos e booleanos, e valores especiais como infinito e NaN.
- Nos cálculos de tokens e custos: negativos, zeros permitidos e estimativas fracionárias válidas.
- Exigência de `Decimal` para preços e custos e manutenção desse tipo nos resultados monetários.
- Cotação positiva nos três tipos permitidos (`int`, `float` e `Decimal` ), com rejeição de zero,
  negativos e valores não finitos.
- Valores especiais de `Decimal` , incluindo `NaN` e `sNaN` , nos campos monetários.
- Oito métodos para serviços: exemplos de backend e banco, zero unidades, preço gratuito e rejeição
  de tipos e valores inválidos.
- Dez métodos para consumo do cenário: resultados, zeros, estrutura do dicionário, propagação de
  exceções, preservação da entrada e chaves adicionais.
- Doze métodos para custos de IA do cenário: oito resultados em Decimal, zeros, preços gratuitos,
  frações, cotação, estrutura, propagação de erros e preservação das entradas.
- Onze métodos para custos de infraestrutura do cenário: oito resultados em Decimal, zero unidades,
  preços gratuitos, cotação, estrutura, erros dos campos, preservação e chaves adicionais.
- Onze métodos para o cenário completo: resultados dos quatro grupos, zeros, preços gratuitos,
  câmbio, erros propagados, preservação das entradas e independência das execuções.

A auxiliar de validação é exercitada pelas chamadas às funções de cálculo. A suíte cobre os casos
descritos; não é uma verificação exaustiva de todas as entradas possíveis nem uma medição de consumo
real da API.

No terminal, dentro da pasta do projeto, use o Python da `.venv-win`, com Pandas disponível:

```powershell
& '.\.venv-win\Scripts\python.exe' -B -m unittest -v test_calculadora
```

Para executar somente uma classe, por exemplo a conversão cambial:

```powershell
& '.\.venv-win\Scripts\python.exe' -B -m unittest -v test_calculadora.TestCalcularReal
```

Para executar apenas os testes da função de custos de IA do cenário:

```powershell
& '.\.venv-win\Scripts\python.exe' -B -m unittest -v test_calculadora.TestCalcularCustoIaCenario
```

Para executar apenas os testes de infraestrutura do cenário:

```powershell
& '.\.venv-win\Scripts\python.exe' -B -m unittest -v test_calculadora.TestCalcularCustoInfraCenario
```

Para executar apenas os testes do cenário completo:

```powershell
& '.\.venv-win\Scripts\python.exe' -B -m unittest -v test_calculadora.TestCalcularCenario
```

Os comandos usam diretamente o ambiente do projeto, independentemente de `python` no PATH.
Também é possível executar `test_calculadora.py` diretamente com esse mesmo interpretador.

A última execução retornou `Ran 111 tests` e `OK` . `assertEqual` confere resultados,
`assertIsInstance` verifica tipos de retorno e `assertRaises` confirma as exceções esperadas. Uma
exceção capturada por `assertRaises` faz parte do comportamento que o teste verifica.

Além da suíte, foi conferida a execução do cenário principal com 100 e zero usuários: os totais
mensais foram, respectivamente, US$ 13,44 / R$ 67,20 e US$ 13,00 / R$ 65,00. A conferência inicial
foi feita em memória; agora a classe TestCalcularCenario também verifica automaticamente o cenário
didático e zero usuários ou respostas com infraestrutura preservada.

Antes da criação dessa suíte, foram executados roteiros temporários de 110 e 232 casos durante a
implementação e a refatoração das validações. Esses números são registros históricos e não
representam a quantidade de testes salvos atualmente.

Exceções ainda não são tratadas em uma interface: fora dos testes, uma chamada inválida sem
tratamento pode interromper o script com a mensagem do erro.

### Próximos incrementos

O primeiro DataFrame, a seleção e ordenação dos custos, o filtro por orçamento, a coluna de saldo,
o resumo dos extremos mensais e a exportação para CSV já foram implementados na `.venv-win`.
Os próximos incrementos poderão aprofundar a análise dos cenários, preservando as funções
existentes e os tipos monetários.

As alternativas pesquisadas ainda precisam ser revisadas antes da substituição dos preços didáticos.
A importação de hipóteses por CSV continua planejada, com definição do formato de entrada e
validação antes dos cálculos. Catálogo de preços, entrada pelo terminal, novas análises, gráficos
e dashboard dependem de incrementos próprios.

## Primeira versão planejada

A base da primeira entrega funcional já reúne os cálculos e a comparação de dois cenários
didáticos. A etapa de Pandas começou com a tabela de resumos. O escopo considera:

- Mensalidades de backend e banco de dados.
- GPT-6 Luna (`gpt-6-luna`) como modelo de referência da API da OpenAI.
- Consumo de IA estimado a partir das respostas dos estudantes.
- Feedback em cada resposta errada e feedback opcional nos acertos.
- Custos mensais por categoria, total mensal em reais e projeção anual constante.

Os resultados serão estimativas baseadas em preços pesquisados e hipóteses de consumo. Não
representarão despesas efetivamente realizadas nem comprovarão a capacidade dos planos escolhidos.

## Tecnologias utilizadas e previstas

| Tecnologia | Aplicação |
| --- | --- |
| Python | Lógica e cálculos |
| Pandas | DataFrame dos cenários, seleção, ordenação, filtro, saldo e agregações de custos; análises adicionais previstas |
| CSV | Exportação de resultados implementada; importação de cenários e catálogo de preços planejados |
| Plotly | Gráficos interativos |
| Streamlit | Interface do dashboard |
| Git e GitHub | Versionamento e hospedagem do repositório |

Python, Pandas e a exportação CSV já são utilizados. Importação de dados, Plotly e Streamlit
serão introduzidos gradualmente, conforme a necessidade de cada etapa.

## Etapas de desenvolvimento

1. Planejamento: requisitos, dados, premissas e fórmulas.
2. Calculadora básica: implementação com Python puro.
3. Análise de dados: tabelas e comparação de cenários com Pandas.
4. Visualização: gráficos com Plotly.
5. Dashboard: interface com Streamlit.
6. Validação final e publicação da aplicação: consolidação dos testes, documentação e
   disponibilização do dashboard.

Testes e documentação acompanharão as implementações desde os primeiros cálculos.

## Evoluções futuras

Permitir selecionar e comparar os custos de modelos de diferentes provedores, incluindo Claude, Qwen
e Gemini, além dos modelos da OpenAI. A inclusão de cada opção dependerá da pesquisa de preços
oficiais, unidades e regras de cobrança da API escolhida.

A calculadora simulará os custos dessas APIs; não será necessário fazer chamadas reais para comparar
os cenários. A primeira versão continuará limitada a um modelo da OpenAI.

## Formatação da documentação

O projeto usa `.markdownlint.json` para manter uma linha em branco entre blocos, tabelas no estilo
`compact` e texto com até 100 caracteres por linha. Tabelas e blocos de código ficam fora do limite
de comprimento, preservando URLs, células e comandos legíveis. As regras de tabelas e linhas em
branco permanecem ativas.

Com a extensão Markdownlint instalada, `.vscode/settings.json` habilita as correções disponíveis ao
salvar explicitamente um arquivo Markdown. Nem todo aviso tem correção automática; revise o painel
Problemas e mantenha os parágrafos dentro do limite nas próximas edições.

Para conferir os três documentos com a mesma versão usada nesta revisão:

```powershell
npx --yes --package markdownlint-cli2@0.23.2 markdownlint-cli2 README.md PLANEJAMENTO.md PROMPTS.md
```

Esse comando requer Node.js/npm e pode baixar a ferramenta para o cache. Ele é opcional para a
documentação; a execução da calculadora requer Pandas no ambiente Python selecionado.

## Documentação

Consulte o [planejamento do projeto](PLANEJAMENTO.md) para conhecer as entradas, regras de negócio,
fórmulas e limitações da primeira versão.

O [registro de prompts](PROMPTS.md) documenta pedidos e decisões relevantes do desenvolvimento com
apoio de IA.

## Aprendizado e uso de IA

O desenvolvimento conta com apoio de IA para orientação técnica, explicação de conceitos e revisão.
A proposta é implementar pequenas funcionalidades, compreender os cálculos e validar os resultados
ao longo do aprendizado.
