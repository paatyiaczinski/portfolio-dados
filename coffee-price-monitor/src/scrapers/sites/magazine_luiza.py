from scrapers.dynamic_scraper import DynamicScraper
from bs4 import BeautifulSoup
import time
import re

class ScraperMagalu(DynamicScraper):
    def __init__(self, url, headless=False, max_pages=1):
        super().__init__(url, headless)
        self.max_pages = max_pages

    def get_blocks(self, soup):
         return soup.select('h2[data-testid="product-title"]')

    def parse_name(self, block):
        result =  block.text.strip() if block else None
        print("📝 Nome extraído:", result)
        return result
    

    def parse_price(self, block):
        parent = block.find_parent('div')
        if parent:
            price_tag = parent.find('p', attrs={"data-testid": "price-value"})
            if price_tag:
                price = price_tag.text.replace('R$', '').strip()
                print("💰 Preço encontrado:", price)
                return price
        print("💰 Preço não encontrado.")
        return None
        
    def parse_image(self, block):
        parent = block.find_parent('div')
        if parent:
            img_tag = parent.find('img', attrs={"data-testid": "image"})
            if img_tag:
                img_url = img_tag.get('src')
                print("🖼️ Imagem encontrada:", img_url)
                return img_url
        print("🖼️ Imagem não encontrada.")
        return None

    def parse_rating(self, block):
        parent = block.find_parent('div')
        if parent:
            review_div = parent.find('div', attrs={"data-testid": "review"})
            if review_div:
                rating_tag = review_div.find('span', attrs={"format": "score-count"})
                if rating_tag:
                    rating_value = rating_tag.text.strip().split('(')[0].strip()
                    print("⭐ Rating encontrado:", rating_value)
                    return rating_value
        print("⭐ Rating não encontrado.")
        return None

    def fetch(self):
        # Inicializa o navegador
        driver = self.get_driver()
        html_pages = []

        try:
            for page in range(self.max_pages):
                paginated_url = f"{self.url}&page={page}"
                print(f"➡️ Acessando: {paginated_url}")
                driver.get(paginated_url)
                time.sleep(3)  # Espera simples para o carregamento
                html_pages.append(driver.page_source)
        finally:
            driver.quit()
        print("✅ fetch",html_pages)
        return html_pages