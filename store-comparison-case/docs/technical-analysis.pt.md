# 📊 Análise Técnica – Projeto Store Comparison

Este documento descreve a estrutura dos dados utilizados, decisões de limpeza e modelagem, além de destacar algumas das principais medidas DAX que apoiaram a geração de insights no projeto.

---

## 1. 📥 Origem dos Dados

Os dados foram fornecidos como parte de um case prático para um processo seletivo, simulando transações reais em lojas físicas de uma rede fictícia de cafeterias.

Dois conjuntos de dados foram disponibilizados em formato Excel:

- **Base de Dados**: contém transações por loja, produto, valor, custo e localização (cidade/estado), com mês e ano separados.
- **Base de Dados 2**: contém a hierarquia de produtos, agrupando cada item por grupo e subgrupo.

A coluna `Data` foi criada manualmente unificando as colunas de mês e ano para facilitar a modelagem temporal no Power BI.

---

## 2. 🧾 Dicionário e Estrutura dos Dados

### 📄 Tabela: `Base de Dados`

| Coluna           | Descrição                              |
|------------------|----------------------------------------|
| Loja             | Nome da loja                           |
| codigo_produto   | Código de identificação do produto     |
| produto          | Nome do produto                        |
| quantidade       | Quantidade vendida                     |
| unidade          | Unidade de medida                      |
| valor            | Receita gerada                         |
| preco_venda      | Preço unitário                         |
| custo            | Custo unitário                         |
| custo_total      | Custo total da venda                   |
| modelo           | Tipo de modelo de loja                 |
| estado           | Sigla do estado                        |
| mes              | Mês da transação                       |
| ano              | Ano da transação                       |
| CMV              | Custo da mercadoria vendida            |
| Data*            | Coluna criada para representar a data  |

### 📄 Tabela: `Base de Dados 2`

| Coluna         | Descrição                    |
|----------------|------------------------------|
| grupo          | Grupo principal do produto   |
| subgrupo       | Subgrupo do produto          |
| codigo_produto | Código do produto (chave)    |
| produto        | Nome do produto              |

---

## 3. 🧹 Tratamento e Preparação dos Dados (ETL com Power Query)

A etapa de Extração, Transformação e Carga (ETL) foi realizada principalmente utilizando o **Power Query** dentro do Power BI:

- **Conexão e Combinação:** Os dados foram importados dos arquivos Excel.
- **Criação da Coluna `Data`:** Foi fundamental unificar as colunas separadas de `mês` e `ano` em uma única coluna `Data` (formato `Date`). Isso foi feito manualmente via Power Query para permitir análises temporais corretas no Power BI (ex: funções Time Intelligence, embora não profundamente usadas neste case específico).
- **Verificação de Qualidade:**
    - **Nulos:** Verificou-se que campos cruciais como `custo_total` e `valor` não continham valores nulos.
    - **Tipos de Dados:** Os tipos de dados de todas as colunas foram revisados e ajustados conforme necessário (ex: colunas de valor para Numérico Decimal, códigos para Texto/Inteiro).
    - **Consistência:** A coluna chave `codigo_produto` foi verificada entre as duas tabelas para garantir a integridade do relacionamento.
- **Manutenção da Granularidade:** Optou-se por manter a granularidade original (nível de transação por produto/loja) para permitir flexibilidade máxima nas análises e agregações no Power BI.

---

## 3.1. 🔗 Modelo de Dados (Power BI)

Foi implementado um modelo estrela simples no Power BI, otimizado para performance e clareza:

* **Tabela Fato:** `Base de Dados` (contendo as métricas de vendas, custos, quantidade).
* **Tabela Dimensão:** `Base de Dados 2` (contendo os atributos dos produtos - grupo, subgrupo).
* **Relacionamento:** As tabelas foram relacionadas através da coluna `codigo_produto` (relacionamento de muitos-para-um da `Base de Dados` para `Base de Dados 2`).
* *(Opcional: Uma Tabela Calendário poderia ser adicionada para análises temporais mais avançadas, mas não foi essencial para este case específico)*.

---

## 4. 📐 Métricas DAX Selecionadas

*Nota: Medidas DAX neste projeto utilizam o prefixo '.' para diferenciação visual e organização.*

Abaixo estão algumas das principais medidas DAX criadas para este projeto
Todas as medidas utilizadas no projeto podem ser encontradas no arquivo `formulas.dax` no repositório. ([[Link para formulas.dax, se disponível online]](https://github.com/paatyiaczinski/portifolio-dados/blob/main/store-comparison-case\formulas.dax))

---

### 📌 `.ClassificaçãoReceitaLoja`

**Objetivo**: Classificar as lojas com base na média e desvio padrão de receita.

**Fórmula DAX**
```DAX
.ClassificaçãoReceitaLoja = 
VAR ReceitaAtual = [.ReceitaTotal]
VAR Media = [.MediaReceitaPorLoja]
VAR Desvio = [.DesvioReceitaPorLoja]
RETURN 
    SWITCH(
        TRUE(),
        ReceitaAtual >= Media + Desvio, "Acima da Média",
        ReceitaAtual <= Media - Desvio, "Abaixo da Média",
        "Regular"
    )
```

**Justificativa**  
Apesar de ter sido criada com o intuito de segmentar lojas por performance, não foi utilizada no dashboard final, pois todos os dados estavam acima da média devido à natureza simulada do case. Ainda assim, a lógica é relevante para cenários reais.

---

### 📌 `.LojaComDoisAnos`

**Objetivo**: Identificar lojas com dados registrados em mais de um ano.

**Fórmula DAX**
```DAX
.LojaComDoisAnos = 
CALCULATE(
    DISTINCTCOUNT(dados[ano]),
    ALLEXCEPT(dados, dados[loja])
)
```

**Justificativa**  
Essa métrica foi fundamental para analisar a performance ano a ano, garantindo que a comparação de receita entre 2022 e 2023 fosse feita apenas para lojas que existiam nos dois períodos.

---

### 📌 `.MargemLucro`

**Objetivo**: Calcular a margem de lucro bruta.

**Fórmula DAX**
```DAX
.MargemLucro = 
DIVIDE([.Lucro],[.ReceitaTotal])
```

**Justificativa**  
A margem de lucro é uma métrica padrão para entender a rentabilidade geral da operação. Foi utilizada para comparar o desempenho de estados e lojas, além de verificar o equilíbrio entre custo e receita.

---

### 📌 `.LucroLoja`

**Objetivo**: Medir a contribuição percentual de cada loja no lucro total da empresa.

**Fórmula DAX**
```DAX
.LucroLoja = 
VAR LucroLoja = CALCULATE([.Lucro])
VAR LucroTotal = CALCULATE([.Lucro], ALL(Dados[loja]))
RETURN
DIVIDE(LucroLoja, LucroTotal)
```

**Justificativa**  
Essa medida permitiu identificar quais lojas mais contribuíram para o resultado total e visualizar oportunidades de expansão, replicando o modelo das unidades com melhor margem e lucro.

---

📌 Para todas as fórmulas utilizadas neste projeto, acesse [`formulas.dax`](../formulas.dax).
