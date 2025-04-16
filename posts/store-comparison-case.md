# 🛍️ Case Study – Store Comparison and Product Proposal: Cafés Brasileiros

## 1. Introduction

This post presents a case study developed as part of a technical selection process. The challenge involved analyzing a fictional dataset related to sales from a coffee shop chain operating in various Brazilian cities, comparing performance across 2022 and 2023.

The project’s goal was to understand sales patterns, identify top-performing stores and products, and — based on the data — generate valuable recommendations for the business team. A final proposal was also included: the suggestion of a new product line for the brand.

---

## 2. Problem

The business team requested an analysis that would help answer the following:

- Which stores performed best in terms of revenue and profit?
- Was there growth between 2022 and 2023?
- Which product categories contributed the most to revenue?
- Which regions had the greatest impact on results?
- What actions could be proposed based on the data?

Two datasets were provided:

1. **Sales base per store**, including revenue, quantity, cost, and location
2. **Product hierarchy base**, with product group and subgroup

---

## 3. Solution

The solution was developed in **Power BI**, divided into four analytical pages:

- **Annual Analysis** – year-over-year comparison of key metrics
- **Store Comparison** – detailed view per store: revenue, profit, COGS, margin
- **Product Comparison** – cross-analysis of group, subgroup, state, and store
- **Top Products** – most sold products by volume and value, ranked overall

Key metrics created included:

- `.ReceitaTotal`, `.Lucro`, `.MargemLucro`
- `.LucroLoja` (each store’s contribution to total profit)
- `.VariaçãoReceita` (year-over-year revenue change)
- `.ClassificaçãoReceitaLoja` (based on standard deviation and average)
- `.LojaComDoisAnos` (to filter only stores active in both years)

During the annual analysis, it became clear that **total revenue growth in 2023 was due to the opening of new stores**, while most existing stores **saw revenue decline**. This reinforced the need for new customer retention strategies.

---

## 3.2 Proposed New Product – “Cafés Brasileiros” Line

Based on state-level trends and category preferences, a new branded line was proposed:  
**“Cafés Brasileiros” – Regional Coffee Editions from Brazil**.

Main characteristics of the proposal:

- Each month, a new coffee from a different Brazilian region would be launched
- Customers would receive a **Loyalty Card**, and after 12 consecutive months, would earn an exclusive gift
- The line would be positioned as **premium**, with storytelling about each region’s flavors and origins

Besides driving sales, the campaign would also enable **better customer data collection**, as it would require registration and regular tracking — which were absent from the original dataset.

---

## 4. Challenges

The main challenge was the limited scope of data, such as:

- Lack of customer profiles (age, channel preference, lifetime value)
- Absence of marketing or campaign records
- No info about stock levels or product release dates

Despite these limitations, strong metrics were created from available data, and interactive filters were applied to simulate fair store comparisons and visualize insights from multiple angles.

---

## 5. Conclusion

Even with simulated data, the project demonstrated how to turn raw records into actionable business insights.

Combining strategic metrics with visual storytelling allowed the business team to:

- Identify store strengths and underperformers
- Analyze category and subgroup impact
- Simulate scenarios with stores active in both years
- Receive a product proposal focused on retention and data intelligence

---

## 6. Access the Dashboard

🔗 [Click here to view the dashboard on Power BI](https://app.powerbi.com/view?r=eyJrIjoiMjQ0YzUyMDYtZTE2My00ZmQ4LTg0MWYtZjcwNTc0NTViYThmIiwidCI6IjkwNzZiMjlhLWNmZGMtNGMyNC1iNjJmLTBiMTBiOWViMDhmYiIsImMiOjl9)
