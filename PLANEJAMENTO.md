# Planejamento — LiteArt Cost Analytics

Documento inicial da Etapa 1. As decisões e hipóteses serão revisadas conforme o aprendizado e a coleta de informações.

## 1. Pergunta principal

Quanto custa manter o LiteArt durante um mês, considerando infraestrutura fixa e feedbacks pedagógicos de IA?

## 2. Escopo da primeira versão

- Um projeto, um cenário mensal e um modelo da OpenAI, ainda a definir, por execução.
- Planos de backend e PostgreSQL com mensalidades fixas conhecidas, dentro de seus limites.
- Feedbacks de texto por meio da API da OpenAI.
- Conversão de USD para BRL com cotação informada manualmente.
- Detalhamento de infraestrutura e IA, total mensal em reais e projeção anual constante.

A calculadora apenas simulará o custo da API; não precisará fazer chamadas reais para produzir as estimativas.

## 3. Tipos de informação

- **Preço pesquisado:** tarifa de um fornecedor, acompanhada de fonte, data e condições.
- **Hipótese de consumo ou capacidade:** quantidade assumida para o cenário, ainda sem medição real.
- **Configuração:** escolha que identifica ou parametriza a simulação, como modelo e cotação.
- **Resultado estimado:** valor obtido por cálculo, sem representar uma despesa já realizada.

## 4. Regra de negócio dos feedbacks

Cada resposta errada gera um feedback de IA. Respostas corretas geram feedback somente quando essa opção estiver ativada pelo estudante, por meio de um toggle.

Premissas da primeira versão:

- O sistema identifica acerto ou erro pelo gabarito, sem consultar a IA.
- Uma resposta corresponde a uma tentativa avaliada; questões não respondidas não entram na contagem.
- Cada feedback corresponde a uma chamada à API, sem novas tentativas ou geração duplicada.
- A opção do estudante é verificada antes de chamar a API. Apenas ocultar um feedback já gerado não reduz o consumo.
- Feedbacks de acerto e de erro usam a mesma estimativa média de tokens, inicialmente.

Na aplicação, o toggle é individual. Na calculadora, a entrada será a **parcela dos acertos que recebe feedback**, representando o comportamento agregado dos estudantes. Esse percentual não é necessariamente igual ao percentual de usuários com o toggle ligado, pois eles podem responder quantidades diferentes de questões.

A preferência por feedback nos erros é uma hipótese de produto baseada em pesquisa exploratória inicial, ainda a validar.

## 5. Entradas do cenário

| Entrada | Unidade | Tipo | Significado |
|---|---|---|---|
| Nome do cenário | Texto | Configuração | Identifica a simulação |
| Preço mensal do plano de backend | USD/mês ou BRL/mês por unidade | Preço pesquisado | Hospedagem do backend |
| Quantidade de unidades de backend | Quantidade | Hipótese de capacidade | Unidades contratadas; inicialmente uma |
| Preço mensal do plano de banco | USD/mês ou BRL/mês por unidade | Preço pesquisado | Serviço PostgreSQL |
| Quantidade de unidades de banco | Quantidade | Hipótese de capacidade | Unidades contratadas; inicialmente uma |
| Provedor da API | Texto | Configuração | OpenAI na primeira versão; identifica quem fornece a API e define as tarifas |
| Modelo de IA | Identificador | Configuração | Modelo específico da OpenAI na primeira versão, usado para pesquisar as tarifas |
| Preço de tokens de entrada | USD por 1 milhão de tokens | Preço pesquisado | Tarifa de entrada sem desconto de cache |
| Preço de tokens de saída | USD por 1 milhão de tokens | Preço pesquisado | Tarifa da saída faturável |
| Usuários ativos no cenário | Usuários/mês | Hipótese de consumo | Estudantes que respondem questões e estão incluídos na regra de feedback |
| Respostas por usuário | Respostas/usuário/mês | Hipótese de consumo | Média de tentativas avaliadas por estudante |
| Taxa de acerto | Percentual das respostas | Hipótese de consumo | Parcela correta do total de respostas do cenário |
| Acertos com feedback | Percentual dos acertos | Hipótese de consumo | Parcela dos acertos para a qual a opção está ativada |
| Tokens médios de entrada | Tokens/feedback | Hipótese de consumo | Todo o conteúdo enviado para gerar um feedback |
| Tokens médios de saída faturáveis | Tokens/feedback | Hipótese de consumo | Saída cobrada por feedback; verificar as regras do modelo escolhido |
| Cotação | BRL por USD | Configuração | Taxa hipotética informada para a conversão |

Os tokens de entrada devem considerar instruções, enunciado, resposta do estudante e demais conteúdos enviados. A saída faturável pode diferir do texto visível, conforme o modelo escolhido.

## 6. Registro dos preços e suas fontes

Para cada tarifa, registrar:

- Provedor e serviço, plano ou modelo.
- Valor, moeda e unidade de cobrança.
- URL oficial e data da consulta no formato AAAA-MM-DD.
- Região e modalidade de contratação, quando aplicáveis.
- Recursos incluídos, limites, franquias e condições promocionais.
- Se o preço exige pagamento ou compromisso anual.

Nenhum preço foi coletado nesta etapa. Quando o banco estiver incluído no plano de hospedagem, registrar essa condição e não somar uma segunda cobrança pelo mesmo recurso.

## 7. Fórmulas

Para calcular, converter os percentuais em proporções: 60% corresponde a 0,60.

1. **Respostas mensais** = usuários ativos × respostas por usuário.
2. **Acertos estimados** = respostas mensais × taxa de acerto.
3. **Erros estimados** = respostas mensais − acertos estimados.
4. **Feedbacks nos acertos** = acertos estimados × proporção dos acertos com feedback.
5. **Feedbacks mensais** = erros estimados + feedbacks nos acertos.
6. **Tokens mensais de entrada** = feedbacks mensais × tokens médios de entrada.
7. **Tokens mensais de saída** = feedbacks mensais × tokens médios de saída faturáveis.
8. **Custo de IA em USD** = (tokens de entrada ÷ 1.000.000 × preço de entrada) + (tokens de saída ÷ 1.000.000 × preço de saída).
9. **Custo de cada serviço fixo** = preço mensal por unidade × quantidade de unidades.
10. **Total mensal em BRL** = soma dos custos em BRL + (soma dos custos em USD × cotação).
11. **Projeção anual em BRL** = total mensal em BRL × 12.

Manter os valores em suas moedas até a conversão, sem somar USD e BRL diretamente. A projeção anual pressupõe preços, consumo e cotação **constantes**; não representa uma simulação de crescimento.

### Exemplo didático de consumo

Valores fictícios, sem pesquisa de uso real ou tarifas:

- 100 usuários × 40 respostas = 4.000 respostas/mês.
- Taxa de acerto de 60%: 2.400 acertos e 1.600 erros.
- Feedback em 25% dos acertos: 600 feedbacks nos acertos.
- Total: 1.600 + 600 = **2.200 feedbacks/mês**.

São 45% menos chamadas do que gerar feedback nas 4.000 respostas. Esse percentual não representa redução de 45% no custo total da aplicação, que também inclui infraestrutura.

## 8. Validação dos cálculos

- Quantidades e preços não podem ser negativos; a cotação deve ser maior que zero.
- Percentuais devem estar entre 0% e 100%.
- Zero usuários ou zero respostas deve produzir zero feedbacks e custo variável de IA zero; custos fixos permanecem.
- Com feedback em 100% dos acertos, o total de feedbacks deve corresponder ao total de respostas.
- Com feedback em 0% dos acertos, apenas os erros devem gerar chamadas.
- As contas devem reproduzir o exemplo didático antes de receber dados pesquisados.

Médias e proporções podem produzir contagens estimadas fracionárias. Não arredondar cada etapa para inteiros; a política de precisão e apresentação monetária será definida antes da implementação.

## 9. Limitações e funcionalidades posteriores

### Limites da primeira versão

A primeira versão não incluirá cobrança excedente aos planos, impostos, tarifas de pagamento, descontos de cache, processamento em lote, ferramentas adicionais da API, imagens, áudio ou novas tentativas. Essas exclusões devem acompanhar a interpretação do resultado.

As mensalidades não comprovam capacidade para atender ao cenário. A necessidade de mudar de plano dependerá de medições e testes futuros.

### Evoluções futuras

- Organizar preços em CSV e comparar serviços e cenários com Pandas.
- Permitir selecionar e comparar custos de modelos de diferentes provedores, incluindo Claude, Qwen e Gemini, além dos modelos da OpenAI.
- Simular crescimento e evolução mensal das despesas.
- Criar gráficos com Plotly e uma interface com Streamlit.
- Estimar receita Premium, custo por usuário e ponto de equilíbrio.

Para cada nova opção de IA, pesquisar o modelo específico, o provedor que fornece a API, os preços oficiais, a moeda, as unidades e as regras de cobrança. Quando necessário, converter as tarifas para uma unidade comum, preservando o valor e a unidade originais no registro da fonte.

A comparação usará a mesma tarefa pedagógica e o mesmo volume de feedbacks. O consumo médio de tokens deverá ser uma hipótese específica de cada modelo; usar a mesma quantidade para todos será apenas uma simplificação declarada. O menor custo estimado, isoladamente, não comprova qualidade pedagógica equivalente.

Essas comparações continuarão sendo simulações baseadas em dados de preços e hipóteses, sem exigir chamadas reais às APIs. Os campos de provedor e modelo identificam as entradas; não implementaremos integrações com vários provedores nesta etapa.

Testes e documentação acompanharão os primeiros cálculos. A etapa final consolidará a validação e a publicação da aplicação. O versionamento e o envio da documentação ao GitHub podem começar antes de existir um dashboard.

## 10. Próximas definições

1. Escolher um cenário didático de consumo, identificado como hipótese.
2. Escolher um modelo específico da OpenAI e verificar suas regras de cobrança.
3. Pesquisar planos de backend e PostgreSQL, registrando fontes e condições.
4. Definir a precisão dos cálculos e a apresentação dos valores.
5. Implementar e conferir um cálculo de cada vez, começando pela conversão cambial.
