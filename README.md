# Experimento A/B, Funil de Conversão e SQL

## Descrição do projeto

Projeto de análise de dados desenvolvido para avaliar um experimento A/B, analisar o funil de conversão e aplicar consultas SQL para apoiar a tomada de decisão.

## 1. Objetivo do projeto

Avaliar se a alteração testada em um experimento A/B gerou diferença relevante na conversão dos usuários ao longo do funil, considerando etapas como visualização de produto, carrinho e compra.

## 2. Resultado

Estruturação de análise com cálculo de conversão por grupo, identificação de gargalos no funil e aplicação de teste estatístico para comparação entre os grupos A e B.

## 3. Ferramentas utilizadas

Python, pandas, NumPy, scipy, matplotlib, SQL, Jupyter Notebook e SQLAlchemy.

## 4. O que foi aprendido

Tratamento de bases, análise de funil, teste A/B, teste Z para proporções, interpretação de p-valor, consultas SQL e comunicação de resultados analíticos.

## 5. Melhorias futuras

Adicionar notebook completo com comentários detalhados, incluir visualizações finais em imagens, conectar os resultados a um dashboard e substituir bases simuladas pelas bases finais do projeto, quando permitido.

## Metodologia

Carregamento e inspeção dos dados, tratamento de inconsistências, separação por grupos experimentais, cálculo de conversão por etapa, aplicação de teste estatístico e consolidação dos achados.

## Como executar

```bash
pip install -r requirements.txt
python scripts/ab_funnel_analysis.py
```

## Estrutura

```text
.
├── README.md
├── requirements.txt
├── scripts/
│   ├── ab_funnel_analysis.py
│   └── sql_analysis.sql
├── data/
└── output/
```
