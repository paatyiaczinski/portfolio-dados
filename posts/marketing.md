
# 📣 Case Study – Marketing Campaigns Analysis

## 1. Introduction

This post presents a data analysis project focused on customer behavior and marketing campaign performance, developed as part of a personal portfolio. It uses simulated data to replicate a realistic business environment and explores patterns in spending, customer segmentation, and campaign effectiveness.

The main goal was to build dashboards that deliver actionable insights for marketing teams, covering customer profiles, campaign ROI, and purchasing behavior across points of sale.

---

## 2. Problem

The simulated business team requested an analytical study to address the following key questions:

- What are the profiles of the most valuable customers?
- Which marketing campaigns had the best performance?
- How effective were campaigns in converting and acquiring new clients?
- What patterns exist in how and where customers shop?
- What recommendations can be drawn from customer segments?

Two main datasets were provided:

1. **Customer marketing dataset**, containing:
   - Customer profiles and purchase history
   - Household information (e.g., age, income, children at home)
   - Interactions with 5 marketing campaigns

2. **Campaign cost table**, created to calculate ROI and CAC

---

## 3. Solution

The solution was developed in **Power BI** and divided into four analytical dashboards:

- **Customer Overview** – demographic and behavioral profiles  
- **Purchase Behavior** – segmentation using RFM logic  
- **Campaign Performance** – comparison of CAC, ROI, and conversions  
- **Point of Sale** – channel and geographic behavior  

We also created a **Home** page with a dynamic last-updated date and navigation highlights.

### 📌 Filter Panel: Usability Improvement

To enhance usability across pages, we implemented a **retractable filter panel** that controls slicers like:

- Age group  
- Country  
- Customer gender  
- Has children at home  
- Store type  
- Income group  

This pattern allows for a clean dashboard layout while preserving full interactivity.

---

## 4. Technical Details

### 📁 Tables and Models

- **CustosCampanhas**: Table simulating the marketing investment cost per campaign.

```diff
- | Campaign    | Cost    |
- |-------------|---------|
- | Campaign 1  | 10,000  |
- | Campaign 2  | 8,000   |
- | Campaign 3  | 5,000   |
- | Campaign 4  | 3,000   |
- | Campaign 5  | 2,000   |
```

✅ Updated to more realistic values based on revenue analysis:

| Campaign     | Cost (BRL) |
|--------------|------------|
| Campaign 1   | 21,500     |
| Campaign 2   | 42,200     |
| Campaign 3   | 93,000     |
| Campaign 4   | 98,500     |
| Campaign 5   | 30,000     |

This update was essential to generate more accurate **ROI** and **CAC** metrics.

---

- **RFM_Segmentos**: Lookup table that maps RFM scores into meaningful segments. Extended to include levels of **Recency**, **Frequency**, and **Monetary**:

```diff
- | RFM_Score | Segment          |
- |-----------|------------------|
- | 333       | VIP Customer     |
- | 332       | Loyal Customer   |
```

✅ Updated with full RFM structure:

| RFM_Score | Segment               | Recency | Frequency | Monetary |
|-----------|------------------------|---------|-----------|-----------|
| 111       | Inactive               | 1       | 1         | 1         |
| 123       | At Risk                | 1       | 2         | 3         |
| 211       | New Customer           | 2       | 1         | 1         |
| 221       | Promising              | 2       | 2         | 1         |
| 231       | Potential              | 2       | 3         | 1         |
| 311       | Needs Recovery         | 3       | 1         | 1         |
| 331       | Revenue Champion       | 3       | 3         | 1         |
| 333       | VIP                    | 3       | 3         | 3         |

*(Other combinations were also mapped.)*

The score from 1 to 3 in each RFM dimension allowed us to customize the classification based on purchase behavior, enabling segmentation visuals and KPIs.

---

- **CampanhasDesempenho**: New dynamic table combining ROI, CAC, and conversion rate across all 5 campaigns:

| Campaign     | ROI     | CAC     | Conversion Rate |
|--------------|---------|---------|------------------|
| Campaign 1   | 3.2     | 25.30   | 0.85             |
| Campaign 2   | 1.6     | 41.10   | 0.72             |
| ...          | ...     | ...     | ...              |

This unified table made possible the visual comparison through bar charts, matrix tables, and scatter plots.

---

## 5. Challenges

Some technical and data constraints were addressed during the project:

- 🗓️ **Missing time variables**: the dataset only contained subscription and last purchase dates. Therefore, no time series or seasonality analysis was performed — this was explicitly stated in the documentation and blog.  
- 🛠️ **Need for simulated campaign costs**: realistic ROI/CAC required manual creation and adjustment of costs.  
- 🎯 **No campaign segmentation**: customers were not linked to segments in campaigns, preventing segment-based effectiveness analysis (future improvement).  
- 🎛️ **Dashboard usability**: slicers were grouped into a **side panel activated via bookmarks**, to improve readability and flexibility.

---

## 6. Results and Insights

The dashboards allowed us to:

- Identify high-value and at-risk customers using RFM segmentation  
- Evaluate the effectiveness of each campaign across ROI, CAC, and conversion  
- Track customer preferences by country, age group, and channel  
- Discover that nearly half of all purchases still occur in **physical stores**  
- Show that **Campaign 4** had the best overall performance (highest ROI and lowest CAC)  
- Suggest improvements like tailoring future campaigns to specific RFM segments  

---

## 7. Access the Dashboard

🔗 [Click here to view the dashboard on Power BI](https://app.powerbi.com/view?r=eyJrIjoiYWMwYzZkYTctMDlkNi00ZGEzLTg0MDktODcwMDI2YzFlZmNiIiwidCI6IjkwNzZiMjlhLWNmZGMtNGMyNC1iNjJmLTBiMTBiOWViMDhmYiIsImMiOjl9)
