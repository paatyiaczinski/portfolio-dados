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

 **CustosCampanhas**: Tabela auxiliar criada para simular os custos de cada campanha de marketing.

<details>
  <summary>🗃️ Versão anterior: <s>CustosCampanhas</s> (obsoleta)</summary>

| Campanha     | <s>Custo (R$)</s> |
|--------------|------------------|
| Campanha 1   | <s>10.000</s>    |
| Campanha 2   | <s>8.000</s>     |
| Campanha 3   | <s>5.000</s>     |
| Campanha 4   | <s>3.000</s>     |
| Campanha 5   | <s>2.000</s>     |

> ⚠️ Essa versão foi utilizada inicialmente, mas substituída durante o projeto para representar melhor os investimentos reais em campanhas.

</details>

| Campanha    | Custo (R$) |
|-------------|------------|
| Campanha 1  | 21.500     |
| Campanha 2  | 42.200     |
| Campanha 3  | 93.000     |
| Campanha 4  | 98.500     |
| Campanha 5  | 30.000     |

Esses custos foram fundamentais para o cálculo realista do **CAC (Custo de Aquisição por Cliente)** e do **ROI (Retorno sobre Investimento)**.

---

- **RFM_Segmentos**: Tabela auxiliar que traduz os scores da coluna `RFM_Score` em perfis de cliente.

<details>
  <summary>🗃️ Versão anterior: <s>RFM_Segmentos</s> (obsoleta)</summary>

| RFM_Score | <s>Segmento</s>              |
|-----------|------------------------------|
| 333       | <s>Cliente VIP</s>           |
| 332       | <s>Cliente Leal</s>          |
| 331       | <s>Cliente Potencial</s>     |
| 221       | <s>Cliente Promissor</s>     |
| 211       | <s>Novo Cliente</s>          |
| 111       | <s>Inativo</s>               |
| 311       | <s>Recuperação</s>           |
| 133       | <s>Impulsivo</s>             |
| 123       | <s>Baixo Engajamento</s>     |

> ⚠️ Inicialmente usada para mapeamento direto. Posteriormente expandida para permitir análises mais refinadas por componente.

</details>

A tabela foi estendida para incluir a decomposição dos componentes de pontuação RFM – **Recência**, **Frequência** e **Monetário** – permitindo análises mais detalhadas.

| RFM_Score | Segmento              | Recência | Frequência | Monetário |
|-----------|------------------------|----------|-------------|------------|
| 111       | Inativo                | 1        | 1           | 1          |
| 123       | Em Risco               | 1        | 2           | 3          |
| 211       | Novo Cliente           | 2        | 1           | 1          |
| 221       | Promissor              | 2        | 2           | 1          |
| 231       | Potencial              | 2        | 3           | 1          |
| 311       | Recuperação            | 3        | 1           | 1          |
| 331       | Campeão de Receita     | 3        | 3           | 1          |
| 333       | VIP                    | 3        | 3           | 3          |

*(Demais combinações intermediárias também foram mapeadas.)*


---

***CampanhasDesempenho** Tabela auxiliar criada para consolidar os principais KPIs por campanha:

| Campanha   | ROI   | CAC     | TaxaConversao | Clientes |
|------------|-------|---------|----------------|----------|
| Campanha 1 | 376%  | R$ 145  | 7,40%          | 148      |
| Campanha 2 | 300%  | R$ 289  | 7,30%          | 146      |
| Campanha 3 | 150%  | R$ 650  | 7,15%          | 143      |
| Campanha 4 | 100%  | R$ 741  | 6,65%          | 133      |
| Campanha 5 | 12%   | R$ 1.154| 1,30%          | 26       |

Essa estrutura viabilizou análises comparativas, visualizações consolidadas e métricas derivadas com maior clareza.

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
- Criação da tabela **CampanhasDesempenho**, centralizando ROI, CAC, Conversão e volume de clientes por campanha.
- Atualização dos valores de custo das campanhas** (`CustosCampanhas`) para maior realismo nos cálculos financeiros.
- Expansão da tabela `RFM_Segmentos`** para incluir as colunas `Recência`, `Frequência` e `Monetário`, permitindo detalhamento nas segmentações.
- 🚀 *Ponto de melhoria futuro*: permitir o detalhamento das campanhas **por segmento RFM**, usando o filtro de segmento no painel. Atualmente isso gera muitos valores em branco, e precisaria de ajustes futuros na modelagem.


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
