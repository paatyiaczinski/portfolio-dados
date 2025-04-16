# 🛍️ Estudo de Caso – Comparação de Lojas e Proposta de Produto: Cafés Brasileiros

## 1. Introdução

Este post apresenta um estudo de caso desenvolvido como parte de um processo seletivo técnico. A proposta envolvia analisar um conjunto de dados fictícios relacionados às vendas de uma rede de cafeterias espalhadas por diferentes cidades do Brasil, comparando o desempenho entre os anos de 2022 e 2023.

O objetivo do projeto foi compreender os padrões de vendas, identificar quais lojas apresentaram melhor performance, quais produtos foram mais relevantes, e — a partir desses dados — gerar recomendações de valor para a área de negócio. Ao final, foi elaborada também uma sugestão estratégica de lançamento de um novo produto da marca.

---

## 2. Problema

A equipe de negócio solicitou uma análise que permitisse:

- Compreender o desempenho das lojas em termos de receita e lucro
- Comparar o crescimento entre os anos de 2022 e 2023
- Identificar quais categorias e produtos mais contribuíram para o faturamento
- Apontar quais regiões têm maior participação nos resultados
- Sugerir ações baseadas nos dados analisados

Foram disponibilizadas duas bases de dados:

1. **Base de vendas por loja**, com receita, quantidade, custo e localização
2. **Base de hierarquia de produtos**, com grupo e subgrupo

---

## 3. Solução

A solução foi desenvolvida no Power BI e dividida em quatro páginas analíticas:

- **Análise Anual** – visão geral da evolução das métricas entre 2022 e 2023
- **Comparativo de Lojas** – análise detalhada por loja: receita, lucro, CMV e margem
- **Comparativo de Produtos** – cruzamento entre grupo, subgrupo, estado e loja
- **Top Produtos** – produtos mais vendidos em volume e valor, com ranking geral

Para apoiar as análises, foram criadas métricas como:

- `.ReceitaTotal`, `.Lucro`, `.MargemLucro`
- `.LucroLoja` (contribuição de cada loja no lucro total)
- `.VariaçãoReceita` (crescimento entre os anos)
- `.ClassificaçãoReceitaLoja` (comparação com a média e desvio padrão)
- `.LojaComDoisAnos` (filtro para análise comparativa justa)

Durante a análise anual, percebeu-se que **o crescimento total da receita da rede só ocorreu por conta da abertura de novas lojas**. A maioria das lojas já existentes **apresentou queda de receita em 2023**, o que reforçou a necessidade de novas estratégias de fidelização.

---

## 3.2 Proposta de Novo Produto – Linha “Cafés Brasileiros”

Com base nos padrões observados por estado e nas preferências por categorias, foi proposta a criação de uma **linha de Cafés Regionais do Brasil**, nomeada internamente como **“Cafés Brasileiros”**.

Essa nova linha teria as seguintes características:

- A cada mês, um café de uma região diferente do Brasil seria apresentado
- O cliente receberia um **Cartão Fidelidade** e, ao completar 12 meses de compra, ganharia um **presente especial da marca**
- A ação teria apelo de **produto premium** e seria acompanhada de storytelling sobre origem e aroma de cada edição

Além de gerar receita, a campanha teria como benefício secundário a **coleta de dados mais detalhados sobre os clientes**, já que envolveria cadastro no programa e acompanhamento mensal — algo ausente nos dados atuais.

---

## 4. Desafios

O principal desafio foi a ausência de dados mais variados, como:

- Perfil de clientes (idade, ticket médio, canal preferido)
- Histórico de campanhas promocionais
- Estoques e datas de lançamento

Essas limitações dificultaram análises mais profundas de comportamento e sazonalidade. Para contornar, focou-se na estruturação de métricas robustas com os dados disponíveis e na criação de filtros dinâmicos para permitir diferentes cortes.

---

## 5. Conclusão

Mesmo com dados simulados e estruturados, o projeto demonstrou a capacidade de transformar dados brutos em insights claros e aplicáveis ao negócio.

A combinação de indicadores estratégicos com storytelling visual permitiu à área de negócio:

- Identificar pontos fortes e gargalos por loja
- Analisar a contribuição de categorias e subgrupos
- Simular cenários com lojas ativas em ambos os anos
- Receber uma proposta de expansão de linha com foco em fidelização e inteligência de dados

---

## 6. Acesse o Dashboard

🔗 [Clique aqui para visualizar o dashboard no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMjQ0YzUyMDYtZTE2My00ZmQ4LTg0MWYtZjcwNTc0NTViYThmIiwidCI6IjkwNzZiMjlhLWNmZGMtNGMyNC1iNjJmLTBiMTBiOWViMDhmYiIsImMiOjl9)
