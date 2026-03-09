Software Quality Metrics - E-commerce System

Este repositório demonstra a análise de métricas de qualidade de código
em um sistema simples de e-commerce utilizando Python.

Estrutura do Projeto

src/ cart.py order.py payment.py

tests/ test_cart.py test_order.py test_payment.py

metrics/ defect_density.py

requirements.txt pytest.ini

Métricas Analisadas

-   Complexidade Ciclomática
-   Cobertura de Testes
-   Densidade de Defeitos
-   Linhas de Código (LOC)
-   Duplicação de Código

Instalação

Clone o repositório:

git clone https://github.com/seuusuario/software-quality-metrics.git cd
software-quality-metrics

Instale as dependências:

pip install -r requirements.txt

Executar Testes

pytest

Cobertura de Testes

pytest –cov=src

Complexidade Ciclomática

radon cc src -a

Linhas de Código

radon raw src

Densidade de Defeitos

python metrics/defect_density.py

Ferramentas Utilizadas

-   Python
-   Pytest
-   Pytest-cov
-   Radon

Objetivo

Demonstrar como coletar e analisar métricas de qualidade de software
para identificar:

-   áreas de alta complexidade
-   cobertura insuficiente de testes
-   oportunidades de refatoração
-   possíveis riscos de manutenção no sistema

Este projeto pode ser utilizado como base para estudos de Engenharia de
Software, Qualidade de Software e Testes Automatizados.
