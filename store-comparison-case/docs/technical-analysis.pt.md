# 📊 Análise Técnica – Projeto Store Comparison

Este documento descreve a estrutura dos dados utilizados, decisões de limpeza e modelagem, além de destacar algumas das principais medidas DAX que apoiaram a geração de insights no projeto.

---

## 1. 📥 Origem dos Dados

Os dados foram fornecidos como parte de um case prático para um processo seletivo, simulando transações reais em lojas físicas de uma rede fictícia de cafeterias.

Dois conjuntos de dados foram disponibilizados em formato Excel:

- **Base de Dados**: contém transações por loja, produto, valor, custo e localização (cidade/estado), com mês e ano separados.
- **Base de Dados 2**: contém a hierarquia de produtos, agrupando cada item por grupo e subgrupo.

A coluna `Data` foi criada manualmente unificando as colunas de mês e ano para facilitar a modelagem temporal no Power BI.

---

## 2. 🧾 Dicionário e Estrutura dos Dados

### 📄 Tabela: `Base de Dados`

| Coluna           | Descrição                              |
|------------------|----------------------------------------|
| Loja             | Nome da loja                           |
| codigo_produto   | Código de identificação do produto     |
| produto          | Nome do produto                        |
| quantidade       | Quantidade vendida                     |
| unidade          | Unidade de medida                      |
| valor            | Receita gerada                         |
| preco_venda      | Preço unitário                         |
| custo            | Custo unitário                         |
| custo_total      | Custo total da venda                   |
| modelo           | Tipo de modelo de loja                 |
| estado           | Sigla do estado                        |
| mes              | Mês da transação                       |
| ano              | Ano da transação                       |
| CMV              | Custo da mercadoria vendida            |
| Data*            | Coluna criada para representar a data  |

### 📄 Tabela: `Base de Dados 2`

| Coluna         | Descrição                    |
|----------------|------------------------------|
| grupo          | Grupo principal do produto   |
| subgrupo       | Subgrupo do produto          |
| codigo_produto | Código do produto (chave)    |
| produto        | Nome do produto              |

---

## 3. 🧹 Limpeza e Preparação dos Dados

- A coluna `Data` foi criada unindo `mês` e `ano`, convertida para o formato de data.
- Campos como `custo_total` e `valor` foram verificados e não continham nulos.
- Os dados foram mantidos em nível de granularidade por produto e loja para permitir análise cruzada entre categorias e unidades.

---

## 4. 📐 Métricas DAX Selecionadas

Abaixo estão quatro das principais medidas DAX utilizadas para obtenção de insights:

---

### 📌 `.ClassificaçãoReceitaLoja`

**Objetivo**: Classificar as lojas com base na média e desvio padrão de receita.

**Fórmula DAX**
```DAX
.ClassificaçãoReceitaLoja = 
VAR ReceitaAtual = [.ReceitaTotal]
VAR Media = [.MediaReceitaPorLoja]
VAR Desvio = [.DesvioReceitaPorLoja]
RETURN 
    SWITCH(
        TRUE(),
        ReceitaAtual >= Media + Desvio, "Acima da Média",
        ReceitaAtual <= Media - Desvio, "Abaixo da Média",
        "Regular"
    )
```

**Justificativa**  
Apesar de ter sido criada com o intuito de segmentar lojas por performance, não foi utilizada no dashboard final, pois todos os dados estavam acima da média devido à natureza simulada do case. Ainda assim, a lógica é relevante para cenários reais.

---

### 📌 `.LojaComDoisAnos`

**Objetivo**: Identificar lojas com dados registrados em mais de um ano.

**Fórmula DAX**
```DAX
.LojaComDoisAnos = 
CALCULATE(
    DISTINCTCOUNT(dados[ano]),
    ALLEXCEPT(dados, dados[loja])
)
```

**Justificativa**  
Essa métrica foi fundamental para analisar a performance ano a ano, garantindo que a comparação de receita entre 2022 e 2023 fosse feita apenas para lojas que existiam nos dois períodos.

---

### 📌 `.MargemLucro`

**Objetivo**: Calcular a margem de lucro bruta.

**Fórmula DAX**
```DAX
.MargemLucro = 
DIVIDE([.Lucro],[.ReceitaTotal])
```

**Justificativa**  
A margem de lucro é uma métrica padrão para entender a rentabilidade geral da operação. Foi utilizada para comparar o desempenho de estados e lojas, além de verificar o equilíbrio entre custo e receita.

---

### 📌 `.LucroLoja`

**Objetivo**: Medir a contribuição percentual de cada loja no lucro total da empresa.

**Fórmula DAX**
```DAX
.LucroLoja = 
VAR LucroLoja = CALCULATE([.Lucro])
VAR LucroTotal = CALCULATE([.Lucro], ALL(Dados[loja]))
RETURN
DIVIDE(LucroLoja, LucroTotal)
```

**Justificativa**  
Essa medida permitiu identificar quais lojas mais contribuíram para o resultado total e visualizar oportunidades de expansão, replicando o modelo das unidades com melhor margem e lucro.

---

📌 Para todas as fórmulas utilizadas neste projeto, acesse [`formulas.dax`](../formulas.dax).
