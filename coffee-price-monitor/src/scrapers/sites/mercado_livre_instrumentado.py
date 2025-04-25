import requests
from bs4 import BeautifulSoup
from scrapers.static_scraper import StaticScraper
import time

class ScraperMercadoLivre2(StaticScraper):
    def fetch(self):
        print("🔍 Iniciando coleta de páginas do Mercado Livre...")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }

        html_pages = []
        page = 1

        while True:
            paginated_url = self.url if page == 1 else f"{self.url}_Desde_{(page - 1) * 50 + 1}"
            print(f"➡️ Acessando página {page}: {paginated_url}")
            response = requests.get(paginated_url, headers=headers)
            if response.status_code != 200:
                print(f"⚠️ Página {page} retornou status {response.status_code}. Encerrando.")
                break

            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            #  Verificar se a página está vazia
            blocks = soup.find_all("li", class_="ui-search-layout__item")
            if not blocks:
                print(f"⚠️ Página {page} retornou 0 produtos. Parando...")
                break

            html_pages.append(html)

            next_button = soup.find("li", class_="andes-pagination__button--next")
            if not next_button or 'andes-pagination__button--disabled' in next_button.get("class", []):
                print(f"✅ Última página detectada: {page}")
                break

            page += 1
            time.sleep(1)

        print(f"✅ Total de páginas coletadas: {len(html_pages)}")
        return html_pages

    def get_blocks(self, soup):
        return soup.find_all("li", class_="ui-search-layout__item")

    def parse_name(self, block):
        img = block.find("img", class_="poly-component__picture")
        return img.get("title") if img else None

    def parse_price(self, block):
        integer = block.find("span", class_="andes-money-amount__fraction")
        cents = block.find("span", class_="andes-money-amount__cents")
        if integer:
            return integer.text.strip() + "," + (cents.text.strip() if cents else "00")
        return None

    def parse_image(self, block):
        img = block.find("img", class_="poly-component__picture")
        return img.get("data-src") or img.get("src")

    def parse_rating(self, block):
        rating_tag = block.find("span", class_="poly-reviews__rating")
        return rating_tag.text.strip() if rating_tag else None

    def run(self):
        print("🚀 Iniciando run()...")
        pages = self.fetch()
        from bs4 import BeautifulSoup
        import pandas as pd

        data = []
        for i, html in enumerate(pages, start=1):
            soup = BeautifulSoup(html, 'html.parser')
            blocks = self.get_blocks(soup)
            print(f"📦 Página {i} - Produtos encontrados: {len(blocks)}")

            for block in blocks:
                data.append({
                    "produto": self.parse_name(block),
                    "preco_raw": self.parse_price(block),
                    "imagem_url": self.parse_image(block),
                    "rating": self.parse_rating(block),
                })

        print(f"✅ Total de produtos coletados: {len(data)}")
        return pd.DataFrame(data)