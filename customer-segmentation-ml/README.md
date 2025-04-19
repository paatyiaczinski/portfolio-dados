# 🧠 Customer Segmentation with Machine Learning

**Course**: Microsoft Power BI for Business Intelligence and Data Science  
**Proposed by**: Data Science Academy

---

## 📌 Challenge

Imagine a company that has historical data on customers who purchased products or services. The dataset includes, for each customer:

- Age  
- Annual income  
- Spending score (indicator of purchasing power)

The company aims to segment these customers into **3 distinct groups**, based on similar characteristics, in order to **personalize marketing campaigns**.

The Marketing manager expects a report with:

- The **3 final segments**  
- The **average age, income, and spending score** of each group  
- Clear and comparative visualizations  

We'll be working with **simulated data**.

---

## 🧪 Methodology

To achieve this goal, we'll apply an **unsupervised Machine Learning pipeline** with the following steps:

1. 📥 Data import and exploration  
2. 🧼 Preprocessing and normalization  
3. 📊 Exploratory analysis and clustering visualization  
4. 🧠 K-Means clustering  
5. 🧩 Cluster interpretation and labeling  
6. 📈 Report generation and visual dashboards  

---

## 💼 Technologies Used

- `Python` (via Jupyter Notebook in VS Code)  
- `Pandas` and `NumPy` for data handling  
- `Matplotlib` and `Seaborn` for visualization  
- `Scikit-learn` for clustering (KMeans)  
- `PowerBI` for interactive visualizations  

---

## 📁 Project Structure

```plaintext
customer-segmentation-ml/
│
├── docs/
│   ├── insights.md
│   ├── insights.pt.md
│   ├── technical-analysis.md
│   └── technical-analysis.pt.md
│
├── img/
│
├── src/
│   └── 01-exploracao.ipynb
│
├── formulas.dax
├── README.md
└── README.pt.md
```

---

📊 Expected Outcome
🔍 Segmentation of customers into 3 distinct clusters

📊 Comparative dashboard showing average characteristics of each group

🎯 Strategic support for personalized marketing campaigns

---

🔜 Next Steps
Apply alternative clustering models (DBSCAN, Hierarchical)

Test impact of normalization with different scales

Automate the pipeline with task scheduling

---

>Project developed as part of a personal portfolio.
> All data used is **fictional** and for educational purposes only.