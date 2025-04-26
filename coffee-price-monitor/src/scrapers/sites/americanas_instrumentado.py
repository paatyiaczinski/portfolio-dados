import requests
from bs4 import BeautifulSoup
from scrapers.dynamic_scraper import DynamicScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

class ScraperAmericanas2(DynamicScraper):
    def __init__(self, headless=False):
        url = "https://www.americanas.com.br/s?q=caf%C3%A9&fuzzy=0&operator=and&category-1=alimentos-e-bebidas&facets=fuzzy%2Coperator%2Ccategory-1&sort=score_desc&page={page}"
        super().__init__(url=url, headless=headless)
        self.max_pages = None  # ou o número de páginas que quiser coletar




    def fetch(self):
        pages_html = []

        # Primeira página
        self.driver.get(self.url.format(page=0))

        # Esperar o carregamento dos produtos
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'ProductCard_productInfo')]"))
        )

        # Pegar o total de produtos
        total_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Pagination_totalCount__Th3o8"))
        )
        total_text = total_element.text

        # Pegar o número
        
        match = re.search(r'de\s([\d\.]+)', total_text)
        total_produtos = int(match.group(1).replace('.', '')) if match else 0

        # Calcular número de páginas
        self.max_pages = (total_produtos // 24) + 1
        print(f"🔢 Total estimado de páginas: {self.max_pages}")

        # Coletar todas as páginas
        for page in range(1):  #self.max_pages
            paginated_url = self.url.format(page=page)
            print(f"➡️ Acessando página {page + 1}: {paginated_url}")
            self.driver.get(paginated_url)

            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'ProductCard_productInfo')]"))
            )

            html = self.driver.page_source
            pages_html.append(html)

        return pages_html


    def get_blocks(self, soup):
        return soup.find_all('div', attrs={"data-fs-custom-product-card": True})

    def parse_name(self, block):
        name_tag = block.find('h3', class_="ProductCard_productName__mwx7Y")
        return name_tag.get('title') if name_tag else None

    def parse_price(self, block):
        price_tag = block.find('p', class_="ProductCard_productPrice__XFEqu")
        if price_tag:
            return price_tag.text.replace('\xa0', '').replace('R$', '').strip()
        return None

    def parse_image(self, block):
        img_tag = block.find('div', attrs={"data-fs-card-image": True})
        if img_tag and img_tag.img:
            return img_tag.img['src']
        print("parse image-------",block.prettify())
        return None


    def parse_rating(self, block):
        rating_tag = block.find('div', class_="avg-rating")
        if rating_tag:
            return rating_tag.text.strip()
        print("parse rating-------",block.prettify())
        return None



