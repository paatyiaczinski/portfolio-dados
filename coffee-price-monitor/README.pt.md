# ☕ Coffee Pricing: Web Scraping and Analysis

## 🇧🇷 Monitoramento de Preços de Café: Coleta e Análise com Web Scraping

Este projeto realiza a coleta diária de preços de produtos relacionados ao café (moído, em grãos, cappuccinos e acessórios) em grandes varejistas online brasileiros, como Mercado Livre, Americanas e Magazine Luiza.

A aplicação utiliza técnicas de web scraping com Python para extrair, transformar e armazenar os dados em um banco PostgreSQL na nuvem (Supabase), possibilitando análises automatizadas e visualização futura em dashboards.

---

## 📌 Tecnologias Utilizadas

- Python 3.11+
- BeautifulSoup & Requests (para scraping estático)
- Selenium (para scraping dinâmico)
- Pandas
- SQLAlchemy
- Supabase (PostgreSQL na nuvem)
- GitHub Actions (automação futura)

---

## 🧱 Estrutura do Projeto

```bash
coffee-price-monitor/
├── src/
│   ├── scrapers/               # Scrapers por loja (ML, Magalu, Americanas)
│   ├── processors/             # Limpeza e transformação dos dados
│   ├── upload/                 # Envio para Supabase
│   ├── main.py                 # Execução central
│   └── mercado_livre_selenium.py # Versão alternativa usando Selenium
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar

```bash
# Instale as dependências
pip install -r requirements.txt

# Copie o modelo de ambiente
cp .env.example .env

# Edite sua senha e credenciais no .env
# E execute:
python src/main.py
```

---

## 🔐 Segurança

- As credenciais são gerenciadas com `python-dotenv` e não são incluídas no repositório.
- O arquivo `.env.example` contém todas as variáveis necessárias.

---

## 📈 Futuro

- Automatização com GitHub Actions para coleta diária
- Integração com Power BI ou Metabase
- Expansão para mais categorias ou regiões

---