
import re

from bs4 import BeautifulSoup
from scrapers.dynamic_scraper import DynamicScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScraperAmericanas3(DynamicScraper):
    def __init__(self, headless=False):
        url = "https://www.americanas.com.br/s?q=caf%C3%A9&fuzzy=0&operator=and&category-1=alimentos-e-bebidas&facets=fuzzy%2Coperator%2Ccategory-1&sort=score_desc&page={page}"
        super().__init__(url=url, headless=headless)
        self.max_pages = 2  # ou o número de páginas que quiser coletar

    

    def calculate_number_of_pages(self):
        self.driver.get(self.url.format(page=0))  # acessa a primeira página
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Pagination_totalCount__Th3o8"))
        )

        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        total_count_tag = soup.find('span', class_="Pagination_totalCount__Th3o8")
        if total_count_tag:
            texto = total_count_tag.get_text()
            match = re.search(r"de\s+(\d+)", texto)
            if match:
                total_produtos = int(match.group(1))
                return (total_produtos // 24) + 1  # arredondar para cima
        return 1  # fallback caso não ache

    def fetch(self):
        max_pages = self.calculate_number_of_pages()
        print("🔵 Máximo de páginas calculado:", max_pages)
        pages_html = []

        for page in range(max_pages):  # Mantemos 1 para testes, depois voltamos para max_pages
            paginated_url = self.url.format(page=page)
            print(f"➡️ Acessando página {page + 1}: {paginated_url}")
            self.driver.get(paginated_url)

            try:
                print("⏳ Esperando aparecer produtos...")
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'ProductCard_productInfo')]"))
                )
                print("✅ Produtos encontrados!")

                print("⏳ Esperando carregar ratings (avg-rating ou avg-rating.empty)...")
                WebDriverWait(self.driver, 10).until(
                    EC.any_of(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.avg-rating")),
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.avg-rating.empty"))
                    )
                )
                print("✅ Ratings encontrados ou confirmados vazios!")

                print("⏳ Esperando carregar preços...")
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "ProductCard_productPrice__XFEqu"))
                )
                print("✅ Preços encontrados!")

            except Exception as e:
                    print(f"⚠️ Erro ao carregar página {page + 1}: {e}")

            print("📄 Capturando HTML da página...")
            html = self.driver.page_source
            pages_html.append(html)
            print(f"📦 Página {page + 1} capturada e adicionada.")

        print("🏁 Finalizado o processo de fetch!")
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
        
        return None


    def parse_rating(self, block):
        rating_tag = block.find('div', class_="avg-rating")
        if rating_tag:
            return rating_tag.text.strip()
        
        return None


