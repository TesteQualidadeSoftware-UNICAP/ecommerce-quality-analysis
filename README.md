📊 Painel de Qualidade de Código (Code Quality Dashboard)

Este projeto demonstra como coletar, analisar e visualizar métricas de
qualidade de software em um sistema Python simples (simulação de
e‑commerce).

O objetivo é mostrar como ferramentas de engenharia de software podem
ser usadas para avaliar a qualidade do código, semelhante a plataformas
como SonarQube.

------------------------------------------------------------------------

🎯 Objetivo do Projeto

Criar um mini sistema de análise de qualidade de código que:

-   coleta métricas automaticamente
-   interpreta os resultados
-   apresenta um dashboard visual
-   gera diagnóstico automático de qualidade

Esse projeto pode ser utilizado em:

-   disciplinas de Engenharia de Software
-   disciplinas de Qualidade de Software
-   atividades práticas com métricas de código

------------------------------------------------------------------------

# 🧱 Estrutura do Projeto

```
ecommerce-quality-analysis
│
├── src
│   ├── cart.py
│   ├── order.py
│   └── payment.py
│
├── tests
│   ├── test_cart.py
│   ├── test_order.py
│   └── test_payment.py
│
├── quality
│   ├── collectors
│   │   ├── loc.py
│   │   ├── coverage.py
│   │   ├── duplication.py
│   │   └── complexity.py
│   │
│   ├── analyzers
│   │   ├── defect_density.py
│   │   └── diagnosis.py
│   │
│   └── report.py
│
├── dashboard
│   └── dashboard.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

------------------------------------------------------------------------

📏 Métricas Coletadas

LOC (Lines of Code)
Cobertura de testes (Test Coverage)
Complexidade ciclomática (Cyclomatic Complexity)
Duplicação de código (Code Duplication)
Densidade de defeitos (Defect Density)

------------------------------------------------------------------------

🧰 Ferramentas Utilizadas

Python
pytest
pytest-cov
radon
jscpd
Streamlit
Plotly

------------------------------------------------------------------------

▶️ Como Executar o Projeto

Instalar dependências:

pip install -r requirements.txt

Instalar detector de duplicação:

npm install -g jscpd

Executar testes:

pytest

Executar análise de cobertura:

pytest –cov=src

Executar relatório de qualidade:

python quality/report.py

Executar o dashboard:

streamlit run dashboard/dashboard.py

------------------------------------------------------------------------

📊 Exemplo de Resultado

Linhas de Código (LOC): 283
Cobertura de Testes: 95%
Duplicação de Código: 0%
Densidade de Defeitos: 14.13 defeitos/KLOC

Diagnóstico automático:

✔ Cobertura de testes excelente
✔ Baixa duplicação de código
⚠ Densidade de defeitos elevada (sistema pequeno)

------------------------------------------------------------------------

🚦 Semáforo de Qualidade

🟢 Verde → boa qualidade
🟡 Amarelo → atenção
🔴 Vermelho → problema de qualidade

------------------------------------------------------------------------

📈 Visualizações do Dashboard

Indicadores de qualidade
Semáforo de qualidade
Complexidade por módulo
Ranking das funções mais complexas
Diagnóstico automático

------------------------------------------------------------------------

📌 Conclusão

Este projeto demonstra como ferramentas simples podem ser combinadas
para criar um sistema automatizado de análise de qualidade de código.