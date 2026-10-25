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

**Etapa 2 — Calculadora básica em desenvolvimento.** O arquivo `calculadora.py` já organiza os cálculos de consumo e custos de IA em funções, usando GPT-6 Luna como referência inicial. Os valores do cenário são definidos diretamente no código; ainda não há entrada interativa.

### Funcionalidades implementadas

- Volume mensal de respostas, acertos, erros e feedbacks.
- Consumo mensal estimado de tokens de entrada e saída.
- Custos mensais de entrada e saída de IA em dólares, com `Decimal`.
- Conversão dos custos para reais com cotação didática informada no código.
- Projeção anual em dólares e reais, mantendo consumo, preços e câmbio constantes.
- Apresentação dos resultados com os símbolos US$ e R$.

### Organização das funções

| Função | Responsabilidade |
|---|---|
| `calcular_respostas_mensais` | Estimar o volume de respostas |
| `calcular_feedbacks_mensais` | Calcular acertos, erros e feedbacks |
| `calcular_tokens_mensais` | Estimar os totais de tokens de entrada e saída |
| `calcular_custo_tokens` | Calcular custo em USD a partir da tarifa por milhão de tokens |
| `calcular_real` | Converter um custo em USD para BRL |
| `calcular_custo_anual` | Projetar 12 meses de custo constante |

As funções retornam valores; os `print()` apresentam os resultados separadamente.

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

### Como executar a versão atual

Abra `calculadora.py` e execute o arquivo com seu interpretador Python 3. No ambiente usado durante o desenvolvimento, a execução foi realizada pelo VS Code. Não há dependências externas nesta etapa: `decimal` faz parte da biblioteca padrão.

### Próximo incremento

Implementar a validação das entradas. As funções atuais pressupõem valores válidos; a conferência de cenários não significa que entradas inválidas já sejam recusadas.

Custos de infraestrutura, leitura de CSV, comparação automatizada de cenários, gráficos e dashboard ainda serão implementados.

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
