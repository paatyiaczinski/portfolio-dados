# 📄 Documento Técnico – Coleta e Análise de Preços de Café

## 🌟 Objetivo
Coletar dados de preços de diferentes produtos relacionados a café (moído, em grãos, cappuccino e acessórios) em três grandes varejistas online no Brasil, estruturando a base de dados para posterior análise comparativa e visualização em dashboards.

---

## 🧰 Ferramentas Utilizadas
- **Python**
  - `requests`, `BeautifulSoup4`, `Selenium`, `pandas`, `re`, `sqlalchemy`
- **Selenium** (para sites com carregamento dinâmico)
- **ChromeDriver**
- **Supabase** (armazenamento em banco de dados PostgreSQL na nuvem)
- **CSV** (armazenamento temporário local, substituído pela base de dados)

---

## 🎯 Fontes Utilizadas
| Plataforma        | URL Base                                                                                  | Método     |
|-------------------|--------------------------------------------------------------------------------------------|------------|
| Mercado Livre     | `https://lista.mercadolivre.com.br/cafe`                                                  | `requests` |
| Americanas        | `https://www.americanas.com.br/s?q=cafe&...category-1=alimentos-e-bebidas...`             | `Selenium` |
| Magazine Luiza    | `https://www.magazineluiza.com.br/busca/cafe/`                                            | `Selenium` |

---

## 📦 Dados Coletados por Produto
- `produto`: Nome do produto
- `preco_real`: Preço convertido para float (limpo, com 2 casas decimais)
- `peso_g`: Peso estimado do item em gramas (com base no nome e regex)
- `preco_100g`: Valor proporcional por 100g para comparação
- `categoria`: Classificação em `Café`, `Cappuccino`, `Acessórios` ou `Outros`
- `imagem_url`: URL da imagem do produto (quando disponível)
- `rating`: Avaliação do produto (se disponível)
- `source`: Nome da fonte (ex: Mercado Livre)

---

## 🧼 Regras de Tratamento

### 💸 Limpeza e Conversão de Preço (`clean_price`)
Converte valores como "3.499,99" para `float` → `3499.99`
Retorna `preco_real` com `round(2)`

### ⚖️ Extração de Peso (`extract_weight`)
Extrai quantidades como `250g` ou `1kg` e converte para gramas

### 📊 Cálculo de Preço por 100g (`calculate_price_per_100g`)
```python
preco_por_100g = preco_real / (peso_em_gramas / 100)
```

### 🧠 Categorização de Produtos (`categorize_product`)
Com base em palavras-chave presentes no nome do produto:
- `Cappuccino`: contém "cappuccino"
- `Acessórios`: contém "filtro", "cápsula", "cafeteira", etc.
- `Café`: contém "café", "cafe"
- `Outros`: tudo que não se encaixa nas regras anteriores

---

## 🧠 Classe `CafeDataProcessor`

### 📌 Uso
```python
from processors.cafe_data_processor import CafeDataProcessor
processor = CafeDataProcessor()
df = processor.process(df)
```

### 📌 O método `.process(df)` executa:
- Limpeza e conversão da coluna `preco_raw` para `preco_real` (float com 2 casas decimais)
- Extração do peso
- Cálculo do preço por 100g
- Categorização
- Garante que `imagem_url` e `rating` existam (mesmo que `None`)

---

## 🗂️ Estrutura de Projeto

```plaintext
📁 src/
├── scrapers/
│   ├── base_scraper.py
│   ├── static_scraper.py
│   ├── dynamic_scraper.py (em construção)
│   └── sites/
│       ├── mercado_livre.py
│       ├── americanas.py
│       └── magazine_luiza.py
├── processors/
│   └── cafe_data_processor.py
├── upload/
│   └── uploader.py
└── main.py
```

---

## 🔁 Estratégia de Envio para Base de Dados
- Utiliza `SupabaseUploader.upload()` para inserir dados na base
- Antes de cada envio, a função `clear_all_data_of_source()` é chamada automaticamente para apagar os dados da fonte e evitar duplicações
- A função `clear_data_of_day()` também existe e poderá ser usada futuramente para otimizações mais específicas

---

## 📄 Arquivos Gerados (Intermediários, substituídos por inserções no Supabase)
- `cafes_mercado_livre_completo.csv`
- `cafes_americanas_completo.csv`
- `cafes_magalu_completo.csv`

---

## 🧠 Considerações de Projeto
- O `CafeDataProcessor` foi transformado em uma classe, tornando o processamento reutilizável e orientado a fluxo
- O método `.process()` deve ser chamado explicitamente após instanciar a classe, mantendo clareza de uso e separação entre estrutura e execução
- A arquitetura foi desenhada para escalar com novas fontes, novos produtos e evolução de lógica (ex: uso futuro de UPSERT no Supabase)

