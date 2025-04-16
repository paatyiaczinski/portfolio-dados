# 📊 Technical Analysis – Store Comparison Project

This document describes the data structure used in the project, cleaning and modeling decisions, and highlights key DAX measures that supported insights.

---

## 1. 📥 Data Source

The data was provided as part of a practical case for a selection process, simulating real transactions in physical stores of a fictional coffee shop chain.

Two datasets were delivered in Excel format:

- **Base de Dados**: includes store-level transactions by product, value, cost, and location (city/state), with separate month and year columns.
- **Base de Dados 2**: contains product hierarchy, grouping each item by group and subgroup.

A new `Date` column was manually created by combining `month` and `year`, enabling better temporal modeling in Power BI.

---

## 2. 🧾 Data Dictionary & Structure

### 📄 Table: `Base de Dados`

| Column           | Description                             |
|------------------|-----------------------------------------|
| Loja             | Store name                              |
| codigo_produto   | Product code                            |
| produto          | Product name                            |
| quantidade       | Quantity sold                           |
| unidade          | Unit of measurement                     |
| valor            | Sale value                              |
| preco_venda      | Unit sale price                         |
| custo            | Unit cost                               |
| custo_total      | Total cost of the sale                  |
| modelo           | Store model type                        |
| estado           | State abbreviation                      |
| mes              | Month of the transaction                |
| ano              | Year of the transaction                 |
| CMV              | Cost of goods sold                      |
| Data*            | Manually created column for full date   |

### 📄 Table: `Base de Dados 2`

| Column         | Description                  |
|----------------|------------------------------|
| grupo          | Product main group           |
| subgrupo       | Product subgroup             |
| codigo_produto | Product code (key)           |
| produto        | Product name                 |

---

## 3. 🧹 Data Cleaning & Preparation

- The `Date` column was created by combining `month` and `year` and converting it to a date format.
- Fields like `custo_total` and `valor` were validated and contained no nulls.
- The data was kept at a granular level (product × store) to enable cross-category and unit analysis.

---

## 4. 📐 Selected DAX Measures

Below are four key DAX measures used to generate insights:

---

### 📌 `.ClassificaçãoReceitaLoja`

**Purpose**: Classify stores based on revenue standard deviation and average.

**DAX Formula**
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

**Explanation**  
Although designed to segment stores by performance, this measure was not included in the final dashboard due to all stores being “above average” in the simulated dataset. However, this logic remains highly relevant in real business scenarios.

---

### 📌 `.LojaComDoisAnos`

**Purpose**: Identify stores with data in both years.

**DAX Formula**
```DAX
.LojaComDoisAnos = 
CALCULATE(
    DISTINCTCOUNT(dados[ano]),
    ALLEXCEPT(dados, dados[loja])
)
```

**Explanation**  
This measure was essential to ensure accurate year-over-year comparisons, isolating stores that were active in both 2022 and 2023.

---

### 📌 `.MargemLucro`

**Purpose**: Calculate gross profit margin.

**DAX Formula**
```DAX
.MargemLucro = 
DIVIDE([.Lucro],[.ReceitaTotal])
```

**Explanation**  
Used to assess overall profitability and compare store and regional performance. A standard financial indicator applied throughout the analysis.

---

### 📌 `.LucroLoja`

**Purpose**: Measure each store's contribution to total profit.

**DAX Formula**
```DAX
.LucroLoja = 
VAR LucroLoja = CALCULATE([.Lucro])
VAR LucroTotal = CALCULATE([.Lucro], ALL(Dados[loja]))
RETURN
DIVIDE(LucroLoja, LucroTotal)
```

**Explanation**  
This metric enabled the identification of the stores that contributed most to overall profit and supported strategic recommendations for expansion.

---

📌 For all formulas used in this project, see [`formulas.dax`](../formulas.dax).
