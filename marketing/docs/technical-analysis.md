# 📊 Technical Analysis – Marketing Project

## 1. 📥 Data Source

The data used in this project is fictitious and provided in a `.csv` file named `dados_marketing.csv`.  
It represents customer information, purchase history, campaign responses, and consumption habits between the years 2022 and 2023.

---

## 2. 🧾 Data Dictionary and Table Structure

### Tables in the Model

The data model includes the following tables:

- **DadosMarketing**: Main table with customer information, purchasing behavior, and spending.

| Column                          | Data Type | Description                                                             |
|--------------------------------|-----------|-------------------------------------------------------------------------|
| ID                             | Integer   | Unique identifier of the customer                                       |
| Year of Birth                  | Integer   | Customer's year of birth                                                |
| Education                      | Text      | Customer's education level                                              |
| Marital Status                 | Text      | Customer's marital status                                               |
| Annual Salary                  | Numeric   | Annual salary range (may contain null values)                           |
| Children at Home              | Integer   | Number of children living with the customer                            |
| Days Since Last Purchase       | Integer   | Number of days since the last purchase                                 |
| Spending on Food               | Numeric   | Amount spent on food                                                   |
| Spending on Toys               | Numeric   | Amount spent on toys                                                   |
| Spending on Electronics        | Numeric   | Amount spent on electronics                                            |
| Spending on Furniture          | Numeric   | Amount spent on furniture                                              |
| Spending on Utilities          | Numeric   | Amount spent on home utilities                                         |
| Spending on Clothing           | Numeric   | Amount spent on clothing                                               |
| In-Store Purchases             | Integer   | Number of purchases in physical stores                                 |
| Catalog Purchases              | Integer   | Number of purchases via catalog                                        |
| Web Purchases                  | Integer   | Number of online purchases                                             |
| Discounted Purchases           | Integer   | Number of purchases made using discounts or coupons                    |
| Purchased                      | Text      | Indicates if the customer made a purchase after the campaign (“Yes”/“No”) |
| Campaign Purchase 1 to 5       | Text      | Indicates if the customer bought during each specific campaign         |
| RFM_Score                      | Text      | Calculated RFM score (Recency, Frequency, Monetary)                    |
| Age                            | Integer   | Calculated column: current year – year of birth                        |
| Age Range                      | Text      | Categorical column based on age (18–30, 31–40, etc.)                   |

---

- **CustosCampanhas**: Auxiliary table created to simulate the cost of each marketing campaign.

| Campaign    | Cost    |
|-------------|---------|
| Campaign 1  | 10,000  |
| Campaign 2  | 8,000   |
| Campaign 3  | 5,000   |
| Campaign 4  | 3,000   |
| Campaign 5  | 2,000   |

This table was used in the ROI and CAC calculations.

---

- **RFM_Segmentos**: Auxiliary table that translates RFM_Score codes into customer segments.

| RFM_Score | Segment                     |
|-----------|-----------------------------|
| 333       | VIP Customer                |
| 332       | Loyal Customer              |
| 331       | Potential Customer          |
| 221       | Promising Customer          |
| 211       | New Customer                |
| 111       | Inactive Customer           |
| 311       | Recovering Customer         |
| 133       | Impulsive Customer          |
| 123       | Low Engagement Customer     |

---

## 3. 🧹 Data Cleaning and Preparation

The following transformations were applied during the ETL process:

- Null values in **Annual Salary** were replaced by the average.
- **Age** column created based on current year – year of birth.
- **Age Range** column created using age categories.
- **RFM_Score** column calculated to segment customers based on Recency, Frequency, and Monetary.
- **CustosCampanhas** table created to simulate campaign costs and enable ROI/CAC metrics.
- **RFM_Segmentos** table created for easier segmentation and insights.
- Outliers were identified using scatter plots. These values were kept, assuming they may represent relevant extreme profiles.

---

## 4. 🧠 Key DAX Formulas

### 📐 Metric: ROI (Return on Investment)

**Business Concept**  
ROI measures how much return was generated for each unit of value invested in a marketing campaign.

**Standard Formula**  
ROI = (Revenue – Cost) / Cost

**DAX Example**
```DAX
.ROICampanha1 = 
VAR ClientesCampanha = 
    FILTER(DadosMarketing, DadosMarketing[Compra na Campanha 1] = "Sim")
VAR ReceitaCampanha = 
    CALCULATE([.TotalGasto], ClientesCampanha)
VAR CustoCampanha = 
    LOOKUPVALUE('CustosCampanhas'[Custo], 'CustosCampanhas'[Campanha], "Campanha 1")
RETURN
DIVIDE(ReceitaCampanha - CustoCampanha, CustoCampanha)
```

**Justification**  
This formula helps evaluate the profitability of each campaign. The `CustosCampanhas` table allows this comparison through fictitious values.

---

### 📐 Metric: RFM Segmentation

**Business Concept**  
The RFM strategy classifies customers based on Recency (last purchase), Frequency (how often they buy), and Monetary (how much they spend).

**DAX**
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

**Justification**  
The formula returns a string (e.g. "321") that allows mapping to the auxiliary table `RFM_Segmentos`, simplifying insights into customer types and behavior.

---

### 📐 Metric: Percentage with Children

**Business Concept**  
Analyzing family profile may reveal different consumption patterns and help personalize campaigns.

**DAX**
```DAX
.PercentualComFilhos = 
DIVIDE(
    COUNTROWS(FILTER(DadosMarketing, DadosMarketing[Filhos em Casa] = 1)),
    COUNTROWS(DadosMarketing)
)
```

**Justification**  
This measure supports other analyses, such as comparing average spending between customers with and without children.

---

## 🔭 Future Improvements

- Add Customer Lifetime Value (CLV) calculation.
- Apply clustering based on RFM score.
- Deepen analysis by channel (e.g., online vs. physical).
- Evaluate seasonality in campaign effectiveness.
- Add visual tooltips or formula breakdowns in the dashboard.
