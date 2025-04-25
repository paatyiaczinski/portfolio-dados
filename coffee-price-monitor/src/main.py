
import pandas as pd
from scrapers.sites.mercado_livre import ScraperMercadoLivre
from scrapers.sites.mercado_livre_instrumentado import ScraperMercadoLivre2
from processors.cafe_data_processor import CafeDataProcessor
from upload.uploader import SupabaseUploader


scraper =ScraperMercadoLivre2("https://lista.mercadolivre.com.br/cafe")
df_mercado_livre = scraper.run()
print(df_mercado_livre.head(10))

processor = CafeDataProcessor()
df_mercado_livre = processor.process(df_mercado_livre)

output_path = "C:/Users/Utilizador/Desktop/portifolio-dados/coffee-price-monitor/data/output_mercado_livre5.csv"

df_mercado_livre.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"📁 Dados salvos com sucesso em: {output_path}")

#Temporário: hardcode no uploader, senha injetada
#uploader = SupabaseUploader()
#uploader.upload(df_mercado_livre, source="Mercado Livre")
