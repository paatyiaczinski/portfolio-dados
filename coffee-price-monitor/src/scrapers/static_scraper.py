
from scrapers.base_scraper import BaseScraper
from bs4 import BeautifulSoup
import pandas as pd

class StaticScraper(BaseScraper):
    def fetch(self):
        raise NotImplementedError("Subclasses must implement the fetch method.")

    def parse_name(self, block):
        raise NotImplementedError("Subclasses must implement the parse_name method.")

    def parse_price(self, block):
        raise NotImplementedError("Subclasses must implement the parse_price method.")

    def parse_image(self, block):
        return None  # Optional: override in subclass if needed

    def parse_rating(self, block):
        return None  # Optional: override in subclass if needed

    def build_row(self, block):
        return {
            "produto": self.parse_name(block),
            "preco_raw": self.parse_price(block),
            "imagem_url": self.parse_image(block),
            "rating": self.parse_rating(block),
        }

    def parse(self, raw_html):
        soup = BeautifulSoup(raw_html, "html.parser")
        product_blocks = self.get_blocks(soup)
        data = [self.build_row(block) for block in product_blocks]
        return pd.DataFrame(data)

    def get_blocks(self, soup):
        raise NotImplementedError("Subclasses must implement the get_blocks method.")
