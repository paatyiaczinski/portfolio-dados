from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from datetime import date

# ✅ Forçar a leitura do .env antes de tudo
load_dotenv()

DB_USER = os.getenv("SUPABASE_USER", "postgres.ythuecrhhusaybbcdrjt")
DB_PASSWORD = os.getenv("SUPABASE_PASSWORD")
DB_HOST = os.getenv("SUPABASE_HOST", "aws-0-sa-east-1.pooler.supabase.com")
DB_NAME = os.getenv("SUPABASE_DBNAME", "postgres")
DB_PORT = int(os.getenv("SUPABASE_PORT", "6543"))

class SupabaseUploader:
    def __init__(self):
        if not DB_PASSWORD:
            raise ValueError("❌ SUPABASE_PASSWORD is missing in the .env file")
        
        self.connection_string = (f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        self.engine = create_engine(self.connection_string)

    def clear_all_data_of_source(self, source):
        query = text("""
            DELETE FROM produtos_cafe
            WHERE source = :source
        """)
        with self.engine.begin() as conn:
            conn.execute(query, {"source": source})
        print(f"🧹 All records removed for source: {source}")

    def clear_data_of_day(self, source):
        query = text("""
            DELETE FROM produtos_cafe
            WHERE data_coleta = CURRENT_DATE AND source = :source
        """)
        with self.engine.begin() as conn:
            conn.execute(query, {"source": source})
        print(f"🧹 Today's records removed for source: {source}")

    def upload(self, df, source):
        df['source'] = source
        df['data_coleta'] = date.today()
        self.clear_all_data_of_source(source)
        print(df.head())
        df.to_sql('produtos_cafe', con=self.engine, if_exists='append', index=False)
        print(f"✅ {len(df)} records successfully uploaded to Supabase for source: {source}")
