

# 📁 Standard Project Structure

All projects in this portfolio follow a structured process based on common practices in the data field. The process is divided into 4 main stages:

## 1. 🛠️ Initial Setup and Documentation
- Create the project folder
- Define objective, scope, and tools used
- Create the `README.md` and `README.pt.md` with context and goals
- Create folder structure: `/docs`, `/img`, `/posts` (if blog post is planned)

## 2. 🔄 ETL – Extract, Transform, and Load
- Collect data (API, CSV, Excel, manual input, etc.)
- Clean, transform, and format the dataset
- Join datasets and prepare data model (Power BI / Python)
- Normalize columns, handle nulls/outliers, and standardize decimal format
- Document data dictionary (optional)

## 3. 📊 Visualizations, Metrics, and Data Storytelling
- Build dashboards in Power BI (or plots in Python)
- Create KPIs and business metrics using DAX or code
- Apply segmentation (e.g., by age, region, channel)
- Add interactivity with filters and drill-throughs
- Use visual storytelling to highlight patterns and outliers

## 4. 📄 Final Documentation and Publication
- Write `technical-analysis.md` explaining the logic of metrics and models
  - **Sections included**:
    1. Data source and file format
    2. Data dictionary and table structure
    3. Data cleaning and preparation rules
    4. 3–4 key DAX formulas, with objective and explanation
- Write `insights.md` and `insights.pt.md` with main business conclusions
  - Each section of the dashboard is illustrated with an image from `/img`
  - Every insight starts with a bold takeaway sentence, followed by analysis
- Export dashboard visuals to `/img`
- Share Power BI public link (when applicable)
- Create post for LinkedIn/blog under `/posts` folder (optional)
- Commit all files and close the GitHub Project milestone

---
## 5. 🗂️ Repository Folder Structure

Below is the current organization of the folders and files in the `portfolio-dados` repository:


portfolio-dados/
├── README.md                  # main summary (English)
├── README.pt.md               # optional (Portuguese)
│
├── docs/
│   ├── project-structure.md
│   ├── project-structure.pt.md
│   ├── convention-commits.md
│   ├── convention-commits.pt.md
│   ├── insights.md
│   ├── insights.pt.md
│   ├── technical-analysis.md
│   └── technical-analysis.pt.md
│
├── posts/
│   ├── marketing.md
│   └── store-comparison-case.md
│
├── marketing/
│   ├── README.md
│   ├── README.pt.md
│   ├── formulas.dax
│   ├── img/
│   └── docs/
│       ├── insights.md
│       ├── insights.pt.md
│       ├── technical-analysis.md
│       └── technical-analysis.pt.md
│
├── store-comparison-case/
│   ├── README.md
│   ├── README.pt.md
│   ├── formulas.dax
│   ├── img/
│   └── docs/
│       ├── insights.md
│       ├── insights.pt.md
│       ├── technical-analysis.md
│       └── technical-analysis.pt.md
---

📎 This standardized structure helps maintain consistency across all projects and demonstrates technical and analytical skills in a clear and professional way.
