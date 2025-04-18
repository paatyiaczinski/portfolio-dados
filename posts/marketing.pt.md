# 📢 Estudo de Caso – Análise de Campanhas de Marketing

## 1. Introdução

Este projeto foi desenvolvido como parte de um portfólio pessoal de análise de dados, com foco em estratégias de marketing, comportamento do consumidor e análise de performance.

O objetivo foi **transformar dados simulados em insights reais** que pudessem guiar decisões de negócio. Utilizamos um conjunto de dados fictício contendo informações de clientes, respostas a campanhas de marketing e hábitos de compra. O resultado final é um dashboard em Power BI dividido em quatro abas temáticas.

---

## 2. Desafio

O desafio consistia em responder perguntas comuns do universo de marketing:

- Quem são os clientes mais valiosos?
- Quais campanhas tiveram melhor desempenho?
- Qual é o custo médio para adquirir um cliente?
- Como os padrões de compra variam entre países e canais?
- Como transformar os dados em ações estratégicas?

Para isso, construímos um pipeline completo: desde o entendimento dos dados até a geração de métricas personalizadas em DAX e storytelling visual com foco em resultados.

---

## 3. Abordagem

O dashboard foi estruturado em quatro seções:

- **Visão Geral do Cliente**: perfil demográfico, comportamento de compra, filhos em casa e canais preferidos.
- **Comportamento de Compra**: análise RFM com segmentação de clientes e variações de gasto.
- **Performance de Campanhas**: comparação entre campanhas com métricas como ROI, CAC e Taxa de Conversão.
- **Padrões de Compra por Ponto de Venda**: análise geográfica e por canal de compra.

Além das visualizações principais, foi criado um painel de **filtros retrátil** para uma navegação mais fluida, com variáveis como faixa etária, país e canal de compra. A lógica dos filtros foi registrada no blog como melhoria de UX.

---

## 4. Técnicas Utilizadas

- 🧠 **Segmentação RFM**: Criamos uma tabela auxiliar `RFM_Segmentos`, com 9 grupos baseados nos níveis Recência, Frequência e Monetário (valores de 1 a 3), mapeando mais de 20 combinações possíveis.
- 💸 **Modelagem de Campanhas**: Criamos uma tabela `CampanhasDesempenho` consolidando ROI, CAC, Taxa de Conversão e número de clientes por campanha.
- 💡 **Métricas de Negócio**: Todas as fórmulas foram desenvolvidas em DAX com explicações bilíngues no arquivo `formulas.dax`. Entre os destaques:

  - `.ROIMedio`, `.CACMedio`, `.TaxaDeConversao`, `.TotalClientesImpactados`
  - Segmentações como `.ClientesEmRisco`, `.ClientesVIP`, `.ClientesNovos`

- 📦 **Simulação de Custos**: A tabela `CustosCampanhas` foi ajustada durante o projeto para representar valores mais realistas de mercado. O histórico original foi mantido na documentação com destaque de atualização.

---

## 5. Limitações

Apesar da riqueza do dataset, não havia **datas associadas às compras ou campanhas**, apenas “dias desde a última compra” e “ano de nascimento”. Isso impediu análises temporais mais precisas, sendo um dos pontos mais limitantes do estudo.

---

## 6. Melhoria Implementada

Como parte da experiência do usuário, criamos um **painel de filtros retrátil** em Power BI, que aparece quando clicado e desaparece para liberar o espaço do dashboard. Isso foi uma solução criativa para manter o layout limpo sem perder interatividade.

---

## 7. Conclusão

Este projeto foi uma simulação realista de como dados de marketing podem ser utilizados para tomada de decisão. Combinamos boas práticas de visualização, modelagem de dados e storytelling.

A análise permitiu identificar:

- O perfil ideal de cliente (VIP, Promissor, Em Risco)
- As campanhas mais eficazes (com ROI e Conversão altos)
- Os países com maior retorno financeiro
- Oportunidades de segmentação avançada por comportamento

---

## 🔗 Acesse o Dashboard

🖥️ [Clique aqui para visualizar o projeto no Power BI](https://app.powerbi.com/view?r=eyJrIjoiYWMwYzZkYTctMDlkNi00ZGEzLTg0MDktODcwMDI2YzFlZmNiIiwidCI6IjkwNzZiMjlhLWNmZGMtNGMyNC1iNjJmLTBiMTBiOWViMDhmYiIsImMiOjl9)

---

> Este case reforça a importância de unir conhecimento de negócio com domínio técnico. Os dados podem ser simulados, mas os insights são reais. 🌟
