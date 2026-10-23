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

**Etapa 1 — Planejamento.** O projeto possui documentação inicial, um cenário didático definido e uma pesquisa inicial de preços de IA registrada no planejamento. O GPT-6 Luna foi escolhido como referência inicial de custo. A Etapa 2 foi iniciada com o arquivo `calculadora.py`, que calcula o volume estimado de feedbacks. A execução local ainda está pendente de uma instalação Python utilizável; custos e dashboard ainda não foram implementados.

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

## Aprendizado e uso de IA

O desenvolvimento conta com apoio de IA para orientação técnica, explicação de conceitos e revisão. A proposta é implementar pequenas funcionalidades, compreender os cálculos e validar os resultados ao longo do aprendizado.
