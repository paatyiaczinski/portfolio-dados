
import pandas as pd
from scrapers.sites.mercado_livre import ScraperMercadoLivre
from scrapers.sites.mercado_livre_instrumentado import ScraperMercadoLivre2
from processors.cafe_data_processor import CafeDataProcessor
from upload.uploader import SupabaseUploader

"""
scraper =ScraperMercadoLivre2("https://lista.mercadolivre.com.br/cafe")
df_mercado_livre = scraper.run()
print(df_mercado_livre.head(10))

processor = CafeDataProcessor()
df_mercado_livre = processor.process(df_mercado_livre)

#output_path = "C:/Users/Utilizador/Desktop/portifolio-dados/coffee-price-monitor/data/output_mercado_livre5.csv"

#df_mercado_livre.to_csv(output_path, index=False, encoding="utf-8-sig")
#print(f"📁 Dados salvos com sucesso em: {output_path}")

#Temporário: hardcode no uploader, senha injetada
uploader = SupabaseUploader()
uploader.upload(df_mercado_livre, source="Mercado Livre")
"""
"""
from scrapers.sites.magazine_luiza import ScraperMagalu
from processors.cafe_data_processor import CafeDataProcessor
from datetime import date

# Instancia o scraper configurando URL e número de páginas
scraper = ScraperMagalu(
    url="https://www.magazineluiza.com.br/busca/cafe",
    headless=False,
    max_pages=1 # Pode aumentar ou diminuir conforme o necessário
)

# Executa o scraping (chama automaticamente fetch() e parse())
df = scraper.run()
print("✅ Scraper finalizado",df.head(2))
# Instancia o processador de dados para limpar e organizar
processor = CafeDataProcessor()
df = processor.process(df)
print("✅ processor finalizado",df.head(2))
# Adiciona a data de coleta
df["data_coleta"] = date.today()

# Salva o resultado em CSV para análise
output_path = "C:/Users/Utilizador/Desktop/portifolio-dados/coffee-price-monitor/data/output_magalu.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"📁 Dados salvos com sucesso em: {output_path}")
"""

from scrapers.sites.americanas import ScraperAmericanas
from scrapers.sites.americanas_teste2 import ScraperAmericanas3
from scrapers.sites.americanas_instrumentado import ScraperAmericanas2
from processors.cafe_data_processor import CafeDataProcessor

# Inicializa o scraper
scraper = ScraperAmericanas3(headless=False)  # deixa visível para debug

# Executa o scraping
df_americanas = scraper.run()
print("\n✅ Scraping finalizado!")
print(df_americanas.head())

# Inicializa o processor de dados
processor = CafeDataProcessor()
df_americanas = processor.process(df_americanas)

"""
uploader = SupabaseUploader()
uploader.upload(df_americanas, source="Americanas")
"""


# Exporta para CSV para validação
output_path = "C:/Users/Utilizador/Desktop/portifolio-dados/coffee-price-monitor/data/cafes_americanas2.csv"
df_americanas.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"\n💾 Arquivo salvo em: {output_path}")


uploader = SupabaseUploader()
uploader.upload(df_americanas, source="Americanas")

