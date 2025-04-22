
# 🧠 Segmentação de clientes com aprendizado de máquina

**Curso**: Microsoft Power BI Para Business Intelligence e Data Science  
**Proposto por**: Data Science Academy

---

## 📌 Desafio

Imagine que uma empresa possua dados históricos de clientes que fizeram compras de produtos ou serviços. Os dados incluem, para cada cliente:

- Idade
- Renda anual
- Pontuação de gasto (indicador do poder de compra)

O objetivo da empresa é segmentar esses clientes em **3 grupos distintos**, com base em características semelhantes, a fim de **personalizar campanhas de marketing**.

O gestor da área de Marketing espera receber um relatório com:

- Os **3 segmentos finais**
- A **média de idade, renda e pontuação de gastos** de cada grupo
- Visualizações claras e comparativas

Trabalharemos com **dados fictícios**.

---

## 🧪 Metodologia

Para atingir esse objetivo, aplicaremos um pipeline de **Machine Learning não supervisionado**, com as seguintes etapas:

1. 📥 Importação e exploração dos dados  
2. 🧼 Pré-processamento e normalização  
3. 📊 Análise exploratória e clustering visual  
4. 🧠 Agrupamento com K-Means  
5. 🧩 Interpretação e nomeação dos clusters  
6. 📈 Geração de relatórios e dashboards visuais  

---

## 💼 Tecnologias utilizadas

- `Python` (via Jupyter Notebook no VS Code)  
- `Pandas` e `NumPy` para manipulação de dados  
- `Matplotlib` e `Seaborn` para visualização  
- `Scikit-learn` para clustering (KMeans)  
- `PowerBI`  para visualizações interativas  

---

## 📁 Estrutura do Projeto

```plaintext
customer-segmentation-ml/
│
├── docs/
│   ├── insights.md
│   ├── insights.pt.md
│   ├── technical-analysis.md
│   └── technical-analysis.pt.md
│
├── img/
│
├── src/
│   └── 01-exploracao.ipynb
│
├── formulas.dax
├── README.md
└── README.pt.md
```

---

## 📊 Resultado Esperado

- 🔍 Segmentação de clientes em 3 clusters distintos  
- 📊 Painel comparativo com as características médias de cada grupo  
- 🎯 Suporte estratégico para campanhas personalizadas de marketing  

---

## 🔜 Próximas etapas

- Aplicar modelos alternativos de clusterização (DBSCAN, Hierárquico)  
- Testar impacto da normalização com diferentes escalas  
- Automatizar o pipeline com agendamento de tarefas  

---

> Projeto desenvolvido como parte do portfólio pessoal.  
> Todos os dados utilizados são **fictícios** e utilizados apenas para fins educacionais.
