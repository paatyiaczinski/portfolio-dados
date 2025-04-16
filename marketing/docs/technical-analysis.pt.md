# 📊 Análise Técnica – Projeto de Marketing

Este documento consolida as principais métricas de negócio, seus fundamentos teóricos e como foram implementadas em DAX na análise de marketing. Também inclui tabelas auxiliares e decisões de modelagem que orientaram o desenvolvimento do dashboard.

---

## 🎯 Objetivos

- Compreender o comportamento do cliente por meio da segmentação RFM.
- Avaliar a eficácia e rentabilidade das campanhas de marketing.
- Acompanhar KPIs como ROI, CAC e Taxa de Conversão.
- Documentar decisões técnicas e de modelagem para futuras evoluções.

---

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

## 📋 Tabela Auxiliar: RFM_Segmentos

Para interpretar os códigos numéricos da coluna `RFM_Score`, foi criada uma tabela auxiliar com segmentações pré-definidas:

| RFM_Score | Segmento           |
|-----------|--------------------|
| 333       | Cliente VIP        |
| 332       | Cliente Leal       |
| 311       | Cliente em Risco   |
| 221       | Cliente Promissor  |
| 111       | Cliente Inativo    |

Essa tabela está relacionada com a coluna `RFM_Score` da base principal e é usada em tooltips, segmentações e visuais categorizados.

---

## 🚧 Melhorias Futuras

- Adicionar a métrica de Lifetime Value (CLV).
- Simular detecção de churn com base na recência.
- Adicionar segmentação visual por país e canal.
- Testar modelos de clusterização ou pontuação por perfil.
- Enriquecer a documentação com diagramas e explicações visuais.
