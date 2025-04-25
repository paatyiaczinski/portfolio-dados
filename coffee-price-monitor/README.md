# ☕ Coffee Pricing: Web Scraping and Analysis

This project collects daily prices of coffee-related products (ground coffee, beans, cappuccinos, and accessories) from major Brazilian online retailers such as Mercado Livre, Americanas, and Magazine Luiza.

It uses Python-based web scraping techniques to extract, clean, and store data in a cloud PostgreSQL database (Supabase), enabling automated updates and potential integration with dashboards.

---

## 📌 Technologies Used

- Python 3.11+
- BeautifulSoup & Requests (for static scraping)
- Selenium (for dynamic pages)
- Pandas
- SQLAlchemy
- Supabase (PostgreSQL cloud database)
- GitHub Actions (future automation)

---

## 🧱 Project Structure

```bash
coffee-price-monitor/
├── src/
│   ├── scrapers/                 # Scrapers for each store (ML, Magalu, Americanas)
│   ├── processors/               # Data cleaning and transformation
│   ├── upload/                   # Data upload to Supabase
│   ├── main.py                   # Main execution file
│   └── mercado_livre_selenium.py # Alternative version using Selenium
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment config
cp .env.example .env

# Edit the .env with your Supabase credentials
# Then run:
python src/main.py
```

---

## 🔐 Security

- Secrets are managed via `python-dotenv` and are not committed to the repository.
- `.env.example` contains all required variables for setup.

---

## 📈 Next Steps

- Automate daily scraping with GitHub Actions
- Connect to Power BI or Metabase for analysis
- Expand to more categories or regions