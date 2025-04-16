# 📁 Estrutura Padrão dos Projetos

Todos os projetos deste portfólio seguem uma lógica de desenvolvimento dividida em 4 etapas principais, alinhadas com práticas da área de dados:

## 1. 🛠️ Estrutura Inicial e Documentação
- Criação da pasta do projeto
- Definição do objetivo, escopo e ferramentas utilizadas
- Escrita do `README.md` com contexto e metas do projeto

## 2. 🔄 ETL – Extração, Transformação e Carga dos Dados
- Coleta de dados (via API, CSV, Excel, etc.)
- Tratamento, limpeza e transformação dos dados
- Junção de tabelas, padronização e modelagem (quando necessário)
- Organização do modelo relacional no Power BI ou preparação para análise em Python

## 3. 📊 Visualizações, Análises e Storytelling com Dados
- Criação de dashboards (Power BI) ou visualizações (Python)
- Construção de indicadores e métricas de negócio
- Segmentações, destaques e análise exploratória
- Comunicação clara dos resultados por meio de storytelling com dados

## 4. 📄 Documentação Final e Publicação

- Escreva o `technical-analysis.md` explicando a lógica das métricas e da modelagem
  - **Seções incluídas**:
    1. Origem dos dados e formato do arquivo
    2. Dicionário de dados e estrutura das tabelas
    3. Regras de limpeza e preparação dos dados
    4. 3 a 4 fórmulas DAX principais, com objetivo e explicação
- Escreva os arquivos `insights.md` e `insights.pt.md` com as principais conclusões de negócio
  - Cada seção do dashboard é ilustrada com uma imagem da pasta `/img`
  - Todo insight começa com uma frase de destaque em negrito, seguida da análise
- Exporte os visuais do dashboard para a pasta `/img`
- Compartilhe o link público do Power BI (se aplicável)
- Crie um post para LinkedIn/blog dentro da pasta `/posts` (opcional)
- Faça o commit de todos os arquivos e finalize o card correspondente no GitHub Projects
---

## 5. 🗂️ Estrutura de Pastas do Repositório

Abaixo está a organização atual das pastas e arquivos do repositório:

portfolio-dados/
├── README.md                  # main summary (English)
├── README.pt.md               # optional (Portuguese)
│
├── docs/
│   ├── project-structure.md
│   ├── project-structure.pt.md
│   ├── convention-commits.md
│   ├── convention-commits.pt.md
│   ├── insights.md
│   ├── insights.pt.md
│   ├── technical-analysis.md
│   └── technical-analysis.pt.md
│
├── posts/
│   ├── marketing.md
│   └── store-comparison-case.md
│
├── marketing/
│   ├── README.md
│   ├── README.pt.md
│   ├── formulas.dax
│   ├── img/
│   └── docs/
│       ├── insights.md
│       ├── insights.pt.md
│       ├── technical-analysis.md
│       └── technical-analysis.pt.md
│
├── store-comparison-case/
│   ├── README.md
│   ├── README.pt.md
│   ├── formulas.dax
│   ├── img/
│   └── docs/
│       ├── insights.md
│       ├── insights.pt.md
│       ├── technical-analysis.md
│       └── technical-analysis.pt.md
---

📎 Esta estrutura padronizada visa manter a consistência entre os projetos, facilitar a leitura e demonstrar boas práticas profissionais em análise de dados.
