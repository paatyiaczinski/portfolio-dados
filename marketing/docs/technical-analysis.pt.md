# 📊 Análise Técnica – Projeto de Marketing

## 1. 📥 Origem dos Dados

Os dados utilizados neste projeto são fictícios e foram fornecidos em um arquivo `.csv` chamado `dados_marketing.csv`.  
Eles representam informações de clientes, histórico de compras, respostas a campanhas e hábitos de consumo entre os anos de 2022 e 2023.

---

## 2. 🧾 Dicionário de Dados e Estrutura das Tabelas

### Tabelas do Modelo

O modelo de dados inclui as seguintes tabelas:

- **DadosMarketing**: Tabela principal com informações do cliente, comportamento de compra e gastos.

| Coluna                          | Tipo de Dado | Descrição                                                                 |
|--------------------------------|--------------|---------------------------------------------------------------------------|
| ID                             | Inteiro      | Identificador único do cliente                                            |
| Ano Nascimento                 | Inteiro      | Ano de nascimento do cliente                                              |
| Escolaridade                   | Texto        | Grau de escolaridade do cliente                                           |
| Estado Civil                   | Texto        | Estado civil do cliente                                                   |
| Salario Anual                  | Numérico     | Faixa de salário anual (pode conter valores nulos)                        |
| Filhos em Casa                 | Inteiro      | Quantidade de filhos que moram com o cliente                              |
| Dias Desde Ultima Compra       | Inteiro      | Quantidade de dias desde a última compra realizada                        |
| Gasto com Alimentos            | Numérico     | Valor gasto em alimentos                                                  |
| Gasto com Brinquedos           | Numérico     | Valor gasto em brinquedos                                                 |
| Gasto com Eletrônicos          | Numérico     | Valor gasto em eletrônicos                                                |
| Gasto com Móveis               | Numérico     | Valor gasto em móveis                                                     |
| Gasto com Utilidades           | Numérico     | Valor gasto em utilidades domésticas                                      |
| Gasto com Vestuário            | Numérico     | Valor gasto em vestuário                                                  |
| Numero de Compras na Loja      | Inteiro      | Compras feitas em loja física                                             |
| Numero de Compras via Catálogo | Inteiro      | Compras feitas via catálogo                                               |
| Numero de Compras na Web       | Inteiro      | Compras feitas pela internet                                              |
| Numero de Compras com Desconto | Inteiro      | Compras realizadas com cupons/descontos                                   |
| Comprou                        | Texto        | Indica se realizou compra após a campanha ("Sim" ou "Não")                |
| Compra na Campanha 1 a 5       | Texto        | Indica se comprou em cada campanha específica ("Sim" ou "Não")            |
| RFM_Score                      | Texto        | CALCULADO Score RFM (Recência, Frequência e Monetário)                    |
| Idade                          | Inteiro      | Coluna calculada com base no ano atual - ano de nascimento                |
| Faixa Etária                   | Texto        | Coluna categorizando a idade por faixa (18-30, 31-40, etc.)               |

---

- **CustosCampanhas**: Tabela auxiliar criada para simular os custos de cada campanha de marketing.

| Campanha     | Custo   |
|--------------|---------|
| Campanha 1   | 10.000  |
| Campanha 2   | 8.000   |
| Campanha 3   | 5.000   |
| Campanha 4   | 3.000   |
| Campanha 5   | 2.000   |

Essa tabela é utilizada no cálculo de ROI e CAC de forma dinâmica por campanha.

---

- **RFM_Segmentos**: Tabela auxiliar que traduz os scores da coluna `RFM_Score` em perfis de cliente.

| RFM_Score | Segmento                     |
|-----------|------------------------------|
| 333       | Cliente VIP                  |
| 332       | Cliente Leal                 |
| 331       | Cliente Potencial            |
| 221       | Cliente Promissor            |
| 211       | Novo Cliente                 |
| 111       | Cliente Inativo              |
| 311       | Cliente em Recuperação       |
| 133       | Cliente Impulsivo            |
| 123       | Cliente com Baixo Engajamento|

---

## 3. 🧹 Tratamento e Preparação dos Dados

Durante o processo de limpeza e transformação dos dados, foram aplicadas as seguintes ações:

- Preenchimento de valores nulos da coluna **Salario Anual** com a média da coluna.
- Criação da coluna **Idade** a partir do ano atual e ano de nascimento.
- Criação da coluna **Faixa Etária** com base na idade.
- Criação da coluna **RFM_Score** para segmentação de clientes com base em Recência, Frequência e Monetário.
- Criação da tabela **CustosCampanhas** para possibilitar cálculo de ROI e CAC.
- Criação da tabela **RFM_Segmentos** para análise qualitativa dos perfis.
- Verificação de **outliers** com gráficos de dispersão; mantivemos os dados por representarem perfis extremos relevantes.

---

## 4. 🧠 Principais Fórmulas DAX Criadas

[As fórmulas DAX estão detalhadas separadamente no arquivo `formulas.dax`.]

## 📐 Métrica: Taxa de Conversão

**Conceito de Negócio**  
A taxa de conversão representa o percentual de clientes que realizaram uma compra. É um dos principais indicadores de sucesso das campanhas e estratégias de marketing.

**Fórmula Padrão**  
Taxa de Conversão = Total de Clientes que Compraram / Total de Clientes

**DAX no projeto**
```DAX
.TaxaDeConversao = 
DIVIDE(
    COUNTROWS(FILTER(DadosMarketing, DadosMarketing[Comprou] = "Sim")),
    COUNTROWS(DadosMarketing)
)
```

**Justificativa**  
O campo `Comprou` contém o valor "Sim" como texto, indicando uma compra realizada. Aplicamos esse filtro e dividimos pelo total de clientes para obter a taxa geral. A fórmula também pode ser adaptada por segmento (estado civil, campanha, país, etc.).

---

## 📐 Métrica: ROI (Retorno sobre o Investimento)

**Conceito de Negócio**  
O ROI mede o retorno gerado para cada unidade de valor investido em uma campanha de marketing. Quanto maior o ROI, mais rentável foi a ação.

**Fórmula Padrão**  
ROI = (Receita - Custo) / Custo

**DAX no projeto (exemplo da Campanha 1)**
```DAX
.ROICampanha1 = 
VAR ClientesCampanha = 
    FILTER(DadosMarketing, DadosMarketing[Compra na Campanha 1] = 1)

VAR ReceitaCampanha = 
    CALCULATE([.TotalGasto], ClientesCampanha)

VAR CustoCampanha = 
    LOOKUPVALUE(
        'CustosCampanhas'[Custo],
        'CustosCampanhas'[Campanha],
        "Campanha 1"
    )

RETURN
DIVIDE(ReceitaCampanha - CustoCampanha, CustoCampanha)
```

**Justificativa**  
Utilizamos uma tabela auxiliar simulada (`CustosCampanhas`) para viabilizar comparações e reaproveitamento da lógica entre as campanhas. O resultado é apresentado como número decimal (ex: 2.8 = 280%).

---

## 📐 Métrica: CAC (Custo de Aquisição de Cliente)

**Conceito de Negócio**  
O CAC representa o custo médio para adquirir um cliente durante uma campanha de marketing.

**Fórmula Padrão**  
CAC = Custo da Campanha / Número de Clientes Adquiridos

**DAX no projeto (exemplo da Campanha 1)**
```DAX
.CACCampanha1 = 
VAR Compradores = 
    COUNTROWS(FILTER(DadosMarketing, DadosMarketing[Compra na Campanha 1] = "Sim"))

VAR CustoCampanha = 
    LOOKUPVALUE(
        'CustosCampanhas'[Custo],
        'CustosCampanhas'[Campanha],
        "Campanha 1"
    )

RETURN
DIVIDE(CustoCampanha, Compradores)
```

**Justificativa**  
O uso da tabela de custos das campanhas (`CustosCampanhas`) permite simulações e comparações dinâmicas do CAC entre diferentes ações.

---

## 📐 Segmentação RFM (Recência, Frequência e Valor Monetário)

**Conceito de Negócio**  
O modelo RFM classifica os clientes com base em:

- **Recência**: quanto tempo passou desde a última compra.
- **Frequência**: quantas compras o cliente realizou.
- **Monetário**: quanto o cliente gastou no total.

**DAX no projeto (coluna única)**
```DAX
RFM_Score = 
VAR RecenciaScore = 
    SWITCH(
        TRUE(),
        DadosMarketing[Dias Desde Ultima Compra] <= 30, 3,
        DadosMarketing[Dias Desde Ultima Compra] <= 90, 2,
        1
    )

VAR FreqTotal = 
    DadosMarketing[Numero de Compras na Loja] +
    DadosMarketing[Numero de Compras via Catalogo] +
    DadosMarketing[Numero de Compras na Web] +
    DadosMarketing[Numero de Compras com Desconto]

VAR FrequenciaScore = 
    SWITCH(
        TRUE(),
        FreqTotal >= 15, 3,
        FreqTotal >= 8, 2,
        1
    )

VAR ValorTotal = 
    DadosMarketing[Gasto com Eletronicos] +
    DadosMarketing[Gasto com Brinquedos] +
    DadosMarketing[Gasto com Moveis] +
    DadosMarketing[Gasto com Utilidades] +
    DadosMarketing[Gasto com Alimentos] +
    DadosMarketing[Gasto com Vestuario]

VAR MonetarioScore = 
    SWITCH(
        TRUE(),
        ValorTotal >= 2000, 3,
        ValorTotal >= 1000, 2,
        1
    )

RETURN
FORMAT(RecenciaScore, "0") & FORMAT(FrequenciaScore, "0") & FORMAT(MonetarioScore, "0")
```

**Justificativa**  
Concentrar os scores de Recência, Frequência e Monetário em uma única coluna simplifica os filtros e a análise visual. Isso permite representar rapidamente o perfil de valor e atividade do cliente.

---

## 🔭 Melhorias Futuras

- Criar métricas de Lifetime Value (CLV).
- Aplicar clustering com base no score RFM.
- Aprofundar análise por canal de compra.
- Avaliar sazonalidade nas campanhas.
- Adicionar explicações visuais de cada métrica (tooltips ou imagens).
