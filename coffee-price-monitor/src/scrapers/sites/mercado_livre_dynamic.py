
from scrapers.static_scraper import StaticScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

class ScraperMercadoLivreSelenium(StaticScraper):
    def fetch(self):
        options = Options()
        # options.add_argument('--headless')  # Descomente se quiser rodar em modo invisível
        options.add_argument('--window-size=1920,1080')
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(self.url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ui-search-layout__item"))
        )

        html = driver.page_source
        driver.quit()
        return html

    def get_blocks(self, soup):
        return soup.find_all("li", class_="ui-search-layout__item")

    def parse_name(self, block):
        img = block.find("img", class_="ui-search-result-image__element")
        return img.get("alt") if img else None

    def parse_price(self, block):
        integer = block.find("span", class_="andes-money-amount__fraction")
        cents = block.find("span", class_="andes-money-amount__cents")
        if integer:
            return integer.text.strip() + "," + (cents.text.strip() if cents else "00")
        return None

    def parse_image(self, block):
        img = block.find("img", class_="poly-card__portada")
        return img.get("src") if img else None

    def parse_rating(self, block):
        rating_tag = block.find("span", class_="ui-search-reviews__rating-number")
        return rating_tag.text.strip() if rating_tag else None
