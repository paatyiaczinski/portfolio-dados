import re
import pandas as pd

class CafeDataProcessor:
    def __init__(self):
        pass

    def clean_price(self, value):
        if pd.isna(value):
            return None
        try:
            cleaned = float(str(value).replace('.', '').replace(',', '.'))
            return round(cleaned, 2)
        except:
            return None

    def extract_weight(self, text):
        if pd.isna(text):
            return None
        text = text.lower()
        match_kg = re.search(r'(\d+)\s?kg', text)
        match_g = re.search(r'(\d+)\s?g', text)
        if match_kg:
            return int(match_kg.group(1)) * 1000
        elif match_g:
            return int(match_g.group(1))
        return None

    def calculate_price_per_100g(self, price, weight):
        if price is not None and weight:
            try:
                return round(price / (weight / 100), 2)
            except ZeroDivisionError:
                return None
        return None

    def categorize_product(self, name):
        if pd.isna(name):
            return "Outros"
        name = name.lower()
        if 'cappuccino' in name:
            return 'Cappuccino'
        elif any(term in name for term in ['filtro', 'coador', 'cápsula', 'cafeteira', 'prensa']):
            return 'Acessórios'
        elif 'café' in name or 'cafe' in name:
            return 'Café'
        return 'Outros'

    def process(self, df):
        df['preco_raw'] = df['preco_raw'].apply(self.clean_price)
        df['peso_g'] = df['produto'].apply(self.extract_weight)

        df['preco_100g'] = df.apply(
            lambda row: self.calculate_price_per_100g(row['preco_raw'], row['peso_g']),
            axis=1
        )

        df['categoria'] = df['produto'].apply(self.categorize_product)
        df = df[df["categoria"].isin(["Café", "Cappuccino"])]

        if 'imagem_url' not in df.columns:
            df['imagem_url'] = None
        if 'rating' not in df.columns:
            df['rating'] = None

        df = df.rename(columns={'preco_raw': 'preco_real'})

        # Aplicar refinamentos finais
        df = self.refine_dataset(df)
        
        print("✅ Process finalizado",df.head(2))

        return df

    def refine_dataset(self, df):
        # Remover produtos sem peso detectado
        df = df[df["peso_g"].notnull()]

        # Remover duplicatas por nome e valor
        df = df.drop_duplicates(subset=["produto", "preco_real"])

        #Retorna preço para xx,xx
        print("✅ Refine finalizado",df.head(2))
        return df