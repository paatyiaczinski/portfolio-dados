

from scrapers.sites.mercado_livre import ScraperMercadoLivre
from processors.cafe_data_processor import CafeDataProcessor
from scrapers.sites.mercado_livre_dynamic import ScraperMercadoLivreSelenium
from upload.uploader import SupabaseUploader


scraper =ScraperMercadoLivre("https://lista.mercadolivre.com.br/alimentos-bebidas/mercearia/infusoes/cafe/cafe_NoIndex_True?sb=all_mercadolibre#applied_filter_id%3Dcategory%26applied_filter_name%3DCategorias%26applied_filter_order%3D3%26applied_value_id%3DMLB247520%26applied_value_name%3DCaf%C3%A9%26applied_value_order%3D1%26applied_value_results%3D29824%26is_custom%3Dfalse")
df_mercado_livre = scraper.run()
print(df_mercado_livre.head(10))

processor = CafeDataProcessor()
df_mercado_livre = processor.process(df_mercado_livre)

#Temporário: hardcode no uploader, senha injetada
uploader = SupabaseUploader()
uploader.upload(df_mercado_livre, source="Mercado Livre")
