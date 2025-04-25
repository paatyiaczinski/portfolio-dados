from scrapers.base_scraper import BaseScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

class DynamicScraper(BaseScraper):
    def __init__(self, url, headless=False):
        super().__init__(url)
        self.headless = headless

    def get_driver(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        service = Service()
        return webdriver.Chrome(service=service, options=options)

    def get_blocks(self, soup):
        raise NotImplementedError("Subclasses must implement 'get_blocks'")

    def parse_name(self, block):
        raise NotImplementedError("Subclasses must implement 'parse_name'")

    def parse_price(self, block):
        raise NotImplementedError("Subclasses must implement 'parse_price'")

    def parse_image(self, block):
        return None

    def parse_rating(self, block):
        return None

    def build_row(self, block):
        return {
            "produto": self.parse_name(block),
            "preco_raw": self.parse_price(block),
            "imagem_url": self.parse_image(block),
            "rating": self.parse_rating(block),
        }

    def parse(self, raw_html_pages):
        all_data = []
        for i, html in enumerate(raw_html_pages, start=1):
            soup = BeautifulSoup(html, "html.parser")
            blocks = self.get_blocks(soup)
            print(f"📦 Página {i} - Produtos encontrados: {len(blocks)}")
            
            for idx, block in enumerate(blocks):
                if idx == 0:  # Só mostrar para o primeiro bloco (para não lotar o terminal)
                    print("🔍 HTML do primeiro bloco:")
                    print(block.prettify())

                    print("📝 Nome extraído:", self.parse_name(block))
                    print("💰 Preço extraído:", self.parse_price(block))
                    print("🖼️ Imagem extraída:", self.parse_image(block))
                    print("⭐ Rating extraído:", self.parse_rating(block))
                
                all_data.append(self.build_row(block))
                        
        return pd.DataFrame(all_data)