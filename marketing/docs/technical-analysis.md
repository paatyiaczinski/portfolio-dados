# 📊 Technical Analysis – Marketing Project

This document consolidates the main business metrics, their theoretical foundations, and how they were implemented using DAX in the marketing analysis. It also includes auxiliary tables and modeling decisions that guided the development of the dashboard.

---

## 🎯 Objectives

- Understand customer behavior through segmentation (RFM).
- Evaluate the effectiveness and profitability of marketing campaigns.
- Track KPIs such as ROI, CAC, and Conversion Rate.
- Document technical and modeling decisions for future evolution.

---

## 📐 Metric: Conversion Rate

**Business Concept**  
The conversion rate represents the percentage of customers who made a purchase. It is a key performance indicator used to evaluate the success of marketing strategies and campaigns in turning potential customers into actual buyers.

**Standard Formula**  
Conversion Rate = Total Buyers / Total Customers

**DAX in the project**
```DAX
.TaxaDeConversao = 
DIVIDE(
    COUNTROWS(FILTER(DadosMarketing, DadosMarketing[Comprou] = "Sim")),
    COUNTROWS(DadosMarketing)
)
```

**Why this approach**  
The field `Comprou` contains the value `"Sim"` as a text value, which indicates a completed purchase. By filtering this value and dividing it by the total number of customers, we obtain the overall conversion rate. This can also be adapted for segmentation by marital status, campaign, country, etc.

---

## 📐 Metric: ROI (Return on Investment)

**Business Concept**  
ROI measures the return generated for each unit of currency invested in a marketing campaign. A high ROI indicates an efficient and profitable campaign.

**Standard Formula**  
ROI = (Revenue - Cost) / Cost

**DAX in the project (Campaign 1 example)**
```DAX
.ROICampanha1 = 
VAR ClientesCampanha = 
    FILTER(DadosMarketing, DadosMarketing[Compra na Campanha 1] = 1)

VAR ReceitaCampanha = 
    CALCULATE([.TotalGasto], ClientesCampanha)

VAR CustoCampanha = 
    LOOKUPVALUE(
        'CustosCampanhas'[Custo],
        'CustosCampanhas'[Campanha],
        "Campanha 1"
    )

RETURN
DIVIDE(ReceitaCampanha - CustoCampanha, CustoCampanha)
```

**Why this approach**  
A simulated cost table (`CustosCampanhas`) was used to allow comparison and replication across multiple campaigns (1 to 5). The formula calculates ROI as a decimal (e.g., 2.8 = 280%).

---

## 📐 Metric: CAC (Customer Acquisition Cost)

**Business Concept**  
CAC represents the average cost required to acquire each customer during a marketing campaign.

**Standard Formula**  
CAC = Campaign Cost / Number of Customers Acquired

**DAX in the project (Campaign 1 example)**
```DAX
.CACCampanha1 = 
VAR Compradores = 
    COUNTROWS(FILTER(DadosMarketing, DadosMarketing[Compra na Campanha 1] = "Sim"))

VAR CustoCampanha = 
    LOOKUPVALUE(
        'CustosCampanhas'[Custo],
        'CustosCampanhas'[Campanha],
        "Campanha 1"
    )

RETURN
DIVIDE(CustoCampanha, Compradores)
```

**Why this approach**  
By using a simulated campaign cost table (`CustosCampanhas`), we enabled dynamic cost simulations and allowed CAC comparisons across all campaigns.

---

## 📐 RFM Segmentation (Recency, Frequency, Monetary Value)

**Business Concept**  
RFM is a method for segmenting customers based on:

- **Recency**: How recently they made a purchase.
- **Frequency**: How often they purchase.
- **Monetary**: How much they spend in total.

**DAX in the project (single-column score)**
```DAX
RFM_Score = 
VAR RecenciaScore = 
    SWITCH(
        TRUE(),
        DadosMarketing[Dias Desde Ultima Compra] <= 30, 3,
        DadosMarketing[Dias Desde Ultima Compra] <= 90, 2,
        1
    )

VAR FreqTotal = 
    DadosMarketing[Numero de Compras na Loja] +
    DadosMarketing[Numero de Compras via Catalogo] +
    DadosMarketing[Numero de Compras na Web] +
    DadosMarketing[Numero de Compras com Desconto]

VAR FrequenciaScore = 
    SWITCH(
        TRUE(),
        FreqTotal >= 15, 3,
        FreqTotal >= 8, 2,
        1
    )

VAR ValorTotal = 
    DadosMarketing[Gasto com Eletronicos] +
    DadosMarketing[Gasto com Brinquedos] +
    DadosMarketing[Gasto com Moveis] +
    DadosMarketing[Gasto com Utilidades] +
    DadosMarketing[Gasto com Alimentos] +
    DadosMarketing[Gasto com Vestuario]

VAR MonetarioScore = 
    SWITCH(
        TRUE(),
        ValorTotal >= 2000, 3,
        ValorTotal >= 1000, 2,
        1
    )

RETURN
FORMAT(RecenciaScore, "0") & FORMAT(FrequenciaScore, "0") & FORMAT(MonetarioScore, "0")
```

**Why this approach**  
Combining the R, F, and M scores into a single column simplifies filtering, analysis, and visual segmentation. It allows a compact representation of customer value and activity.

---

## 📋 Auxiliary Table: RFM_Segmentos

To translate and interpret the numeric `RFM_Score`, a support table was created with predefined classifications:

| RFM_Score | Segment         |
|-----------|------------------|
| 333       | VIP Client       |
| 332       | Loyal Client     |
| 311       | At-Risk Client   |
| 221       | Promising Client |
| 111       | Inactive Client  |

This table was linked to the main table using the `RFM_Score` column and is used in tooltips, slicers, and visual legends.

---

## 🚧 Future Enhancements

- Add Customer Lifetime Value (CLV) metric
- Simulate churn detection based on recency
- Add visual segmentation by country and channel
- Apply clustering or scoring logic for deeper audience analysis
- Improve documentation with diagrams and visual aids
