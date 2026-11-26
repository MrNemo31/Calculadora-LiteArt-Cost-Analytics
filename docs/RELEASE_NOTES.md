# v0.1.0 — LiteArt Cost Analytics: MVP de custos de IA no terminal

**Estado atual — 26/11/2026:** MVP v0.1.0 publicado no GitHub, conforme confirmação do responsável,
sem data exata de publicação informada. A tag aponta para
`10cc485cde5d1c00a743611017fac58f226b7458`. O estudo e o relatório foram publicados no mesmo
repositório, separadamente da release do programa de terminal.

Estas notas foram preparadas em **14/11/2026**, antes da publicação posterior. Naquela preparação
não foram criadas tags nem publicada a release. Os registros finais deste documento preservam
esse contexto histórico e não são pendências atuais.

## Finalidade

Calculadora didática para estimar custos mensais e anuais dos feedbacks de IA do LiteArt, com
cenários informados pelo terminal ou CSV. O MVP apoia o aprendizado de Python e Análise de Dados.
A release distribui o programa de terminal e seu código-fonte; não hospeda um dashboard.

## Funcionalidades disponíveis

- Entrada de um cenário pelo terminal ou leitura de vários cenários por CSV, com arquivo de exemplo.
- Validação de campos obrigatórios, usuários inteiros, médias finitas não negativas e taxas de 0 a 1.
- Cálculo de respostas, feedbacks e tokens mensais a partir das hipóteses informadas.
- Custos de IA mensais e anuais em USD e BRL, com preços e conversão em Decimal.
- Cotação manual sem internet ou última cotação diária disponível do Banco Central, SGS série 1,
  dólar americano de venda. A consulta usa HTTPS, timeout de 10 segundos e uma taxa por execução.
- Alternativa manual ou cancelamento quando a consulta falha, sem taxa substituta ou nova tentativa
  automática. Cancelamento e falhas de entrada preservam resultados anteriores.
- Apresentação brasileira com R$ e US$, duas casas nos custos e pelo menos quatro na cotação.
- Uma tabela na ordem dos cenários e resumo dos extremos de IA mensal em BRL com múltiplos cenários.
- Exportação para `resultados/cenarios.csv`, relativa à pasta da calculadora e substituída a cada
  execução concluída, sem duplicar linhas.
- Importação do módulo sem interação, consulta à rede, leitura de cenários ou exportação.

O CSV de resultados mantém UTF-8, vírgula, ponto decimal, cabeçalho, ausência de índice e valores
financeiros completos, sem aplicar os formatadores do terminal. Suas nove colunas são:

1. `cenario`
2. `usuarios_ativos`
3. `feedbacks_mensais`
4. `tokens_entrada_total`
5. `tokens_saida_total`
6. `custo_ia_mensal_usd`
7. `custo_ia_mensal_br`
8. `custo_ia_anual_usd`
9. `custo_ia_anual_br`

Origem e data da cotação aparecem no terminal; não são metadados exportados nesse CSV.

## Como começar

Seguir o [README](../README.md) para obter os arquivos e criar a `.venv-win` com Python convencional.
Na raiz do projeto, com o ambiente criado, usar o PowerShell sem precisar ativá-lo. Os comandos
de reprodução abaixo refletem a organização atual dos testes em `tests/`:

```powershell
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m pip install -r requirements.txt
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m pip check
& '.\.venv-win\Scripts\python.exe' -X utf8 -B -m unittest discover -s tests -t . -v
& '.\.venv-win\Scripts\python.exe' -X utf8 -B calculadora.py
```

Para reproduzir os exemplos, escolher CSV no primeiro menu, cotação manual no segundo e informar
`5.00` BRL por USD. Os cenários de 100 e 500 usuários produzem IA mensal de R$ 2,20 e R$ 11,00 e
anual de R$ 26,40 e R$ 132,00. Essa taxa é didática, não uma cotação permanentemente atual.

A instalação pode precisar de internet. Depois dela, o modo com cotação manual funciona sem rede;
a consulta automática ao BCB exige conexão. Não há chamadas às APIs dos modelos de IA.

## Ambiente e verificação — registros históricos de 14/11/2026

- Ambiente efetivamente validado: Python convencional 3.14.10 x64, `win-amd64`, Windows 11,
  build 26300. Outras versões, sistemas e computadores não foram validados.
- Dependências fixadas: Pandas 3.1.0, NumPy 2.5.4, python-dateutil 4.0.0 e tzdata 2026.6.
- Em 14/11/2026, instalação por requirements em ambiente virtual novo, isolado dos pacotes globais
  e do usuário, com wheels e sem compilação. A pasta temporária foi removida após a validação.
- `pip check`: nenhum requisito quebrado, tanto na validação anterior quanto na revisão final.
- Suíte: **188 métodos de teste em 17 classes aprovados**, incluindo a execução da revisão final
  na `.venv-win`. Os testes do BCB usam respostas simuladas, sem depender da internet ou da
  taxa do dia.
- Conferências anteriores da cópia limpa: fluxos manual e CSV, resolução de caminhos de outra pasta,
  apresentação, nove campos exportados, precisão e importação silenciosa. Essas verificações pontuais
  não representam métodos adicionais de teste.
- A instalação limpa não foi repetida nesta revisão; código e dependências não foram alterados.
- Markdownlint executado nos documentos e nestas notas, sem problemas de formatação.

O requirements fixa o conjunto validado, mas não é lock completo nem garantia universal de reprodução.

## Limitações conhecidas

- Estimativas exclusivamente de IA: infraestrutura, orçamento e demais custos operacionais estão
  fora do fluxo principal. As funções de infraestrutura e cenário completo e seus testes permanecem.
- Modelo de referência único, GPT-6 Luna (`gpt-6-luna`), sem seleção de modelos. Tarifas e fonte
  registradas com consulta em 23/10/2026; esta revisão não atualiza preços comerciais.
- Hipóteses de tokens e feedbacks são didáticas, sem medição real ou validação de qualidade pedagógica.
- O anual pressupõe 12 meses com consumo, preços e câmbio constantes, sem simular crescimento.
- A cotação diária do BCB pode ter data anterior à execução; não é câmbio em tempo real nem inclui
  necessariamente adicionais do meio de pagamento.
- Entradas usam ponto decimal, sem milhares; taxas são proporções de 0 a 1, não percentuais de 0 a 100.
- CSV não preserva tipos Python. Recuperar campos financeiros como texto e converter diretamente
  para Decimal, sem float intermediário. Não há exportação de metadados cambiais nesta versão.

Preços pesquisados, configurações, hipóteses e resultados estimados continuam distintos.
As fontes, datas e ressalvas estão no README e no [planejamento](PLANEJAMENTO.md).

## Licença

O código do projeto é disponibilizado sob a [licença MIT](../LICENSE), autorizada explicitamente em
14/11/2026. O arquivo contém o texto integral e os avisos de direitos autorais. Uso, modificação e
distribuição, inclusive comercial, são permitidos, mantendo os avisos exigidos.
Dependências e fontes de dados mantêm suas próprias licenças e condições; não são relicenciadas
pela adoção da MIT neste projeto.

## Evoluções futuras

Catálogo e seleção de modelos, comparação de provedores, novos gráficos e dashboard, retomada de
infraestrutura e orçamento e análises avançadas permanecem futuras. Não são funcionalidades
obrigatórias para fechar esta versão e não estão disponíveis no menu atual.
Os dois gráficos do estudo foram produzidos posteriormente e integram o relatório publicado;
isso não altera retroativamente as funcionalidades da v0.1.0.

## Histórico da preparação em 14/11/2026

O registro e o roteiro abaixo descrevem a preparação anterior à publicação confirmada no topo.
Expressões como “sem commit” e “versão proposta” referem-se àquele momento.

Branch revisada: `main`. Commit base conferido:
`3ebf7f745e6389fa239f7a4dc43057f6e07af11e`.

Não havia alterações pendentes no início desta preparação. Estas notas e os pequenos ajustes
documentais ainda estão sem commit e precisam ser incorporados antes da publicação.
O commit definitivo da release será o que incluir os materiais finais; não presumir que o commit
base acima já os contém. Não foram encontradas tags locais ou remotas na consulta de 14/11/2026;
**v0.1.0 é a proposta**, sem criação ou substituição de tags.

Sequência para finalizar, em uma etapa posterior:

1. Revisar e aprovar os materiais finais, incluindo as referências ao arquivo LICENSE já concluído.
2. Fazer o commit das alterações finais e enviá-lo ao GitHub. Conferir seu identificador no remoto.
3. Em **Releases → Draft a new release**, propor a tag `v0.1.0` e selecionar como destino a branch
   que contenha o commit final, conferindo que esse é o commit pretendido antes de publicar.
4. Usar o título e o conteúdo destas notas, revisados para o estado final. Não anexar ambientes
   virtuais, resultados pessoais ou pacotes binários; os arquivos-fonte virão do commit escolhido.
5. Revisar a prévia e publicar somente quando os materiais estiverem aprovados. Salvar como draft
   caso a revisão de publicação ainda não tenha terminado.

Referência: [publicação de releases no GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
Nenhum commit, push, tag, release ou outra alteração remota foi realizado nesta preparação.
