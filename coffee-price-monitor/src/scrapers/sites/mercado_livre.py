import requests
from scrapers.static_scraper import StaticScraper

class ScraperMercadoLivre(StaticScraper):
    def fetch(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        return response.text

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

