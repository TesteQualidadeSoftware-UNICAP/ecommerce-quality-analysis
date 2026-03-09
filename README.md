E-commerce Quality Analysis

Este repositório demonstra como coletar e analisar métricas de qualidade
de código em um sistema simples de e-commerce desenvolvido em Python.

O projeto utiliza ferramentas comuns do ecossistema de Engenharia de
Software e Qualidade de Software para medir características importantes
do código.

Estrutura do Projeto

src/ - cart.py - order.py - payment.py

tests/ - test_cart.py - test_order.py - test_payment.py

metrics/ - defect_density.py - quality_report.py

Arquivos principais: - requirements.txt - pytest.ini - README.md

Métricas Analisadas

O sistema coleta automaticamente as seguintes métricas:

-   LOC (Lines of Code)
-   Complexidade Ciclomática
-   Cobertura de Testes
-   Densidade de Defeitos
-   Duplicação de Código

Ferramentas Utilizadas

-   Python
-   pytest
-   pytest-cov
-   radon
-   jscpd

Instalação

Clone o repositório:

git clone https://github.com/TesteQualidadeSoftware-UNICAP/ecommerce-quality-analysis.git

Entre na pasta do projeto:

cd ecommerce-quality-analysis

Instale as dependências Python:

pip install -r requirements.txt

Instale o detector de duplicação:

npm install -g jscpd

Executar Testes

pytest

Cobertura de Testes

pytest –cov=src

Complexidade Ciclomática

python -m radon cc src -a

Linhas de Código

python -m radon raw src

Relatório Completo de Qualidade

Execute:

python metrics/quality_report.py

Exemplo de saída:

LOC total: 283 Complexidade média: A Cobertura de testes: 95% Defeitos
conhecidos: 4 Densidade de defeitos: 14.13 defeitos/KLOC Duplicação de
código: 0%

Diagnóstico

O relatório gera automaticamente um diagnóstico baseado nas métricas
coletadas.

Objetivo do Projeto

Demonstrar como realizar análise de qualidade de software utilizando
ferramentas automatizadas.