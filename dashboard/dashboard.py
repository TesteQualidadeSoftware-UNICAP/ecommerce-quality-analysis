import sys
import os

# Permitir import da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from quality.report import collect_metrics

st.set_page_config(
    page_title="Painel de Qualidade de Código (Code Quality Dashboard)",
    layout="wide"
)

st.title("📊 Painel de Qualidade de Código (Code Quality Dashboard)")

# ------------------------------------------------
# Coletar métricas
# ------------------------------------------------

metrics = collect_metrics()

loc = metrics["loc"]
coverage = metrics["coverage"]
duplication = metrics["duplication"]
density = metrics["density"]
defects = metrics["defects"]
complexity_df = metrics["complexity"]
diagnosis = metrics["diagnosis"]

# ------------------------------------------------
# KPIs
# ------------------------------------------------

st.subheader("Indicadores de Qualidade (Quality Indicators)")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Linhas de Código (Lines of Code)", loc)

col2.metric(
    "Cobertura de Testes (Test Coverage)",
    f"{coverage}%"
)

col3.metric(
    "Defeitos Conhecidos (Known Defects)",
    defects
)

col4.metric(
    "Duplicação de Código (Code Duplication)",
    f"{duplication}%"
)

col5.metric(
    "Densidade de Defeitos (Defect Density)",
    f"{density:.2f} defeitos/KLOC"
)

st.divider()

# ------------------------------------------------
# SEMÁFORO DE QUALIDADE
# ------------------------------------------------

st.subheader("🚦 Semáforo de Qualidade do Sistema (System Quality Traffic Light)")

coverage_status = (
    "🟢 Excelente" if coverage >= 80
    else "🟡 Moderado" if coverage >= 60
    else "🔴 Baixo"
)

duplication_status = (
    "🟢 Baixa" if duplication < 5
    else "🟡 Moderada" if duplication < 10
    else "🔴 Alta"
)

density_status = (
    "🟢 Baixa" if density < 5
    else "🟡 Moderada" if density < 10
    else "🔴 Alta (Sistema pequeno)"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Cobertura de Testes (Test Coverage)",
    f"{coverage}%",
    coverage_status
)

col2.metric(
    "Duplicação de Código (Code Duplication)",
    f"{duplication}%",
    duplication_status
)

col3.metric(
    "Densidade de Defeitos (Defect Density)",
    f"{density:.2f} defeitos/KLOC",
    density_status
)

st.divider()

# ------------------------------------------------
# GAUGE DE COBERTURA
# ------------------------------------------------

st.subheader("Indicador de Cobertura de Testes (Test Coverage Indicator)")

coverage_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=coverage,
    title={'text': "Cobertura de Testes (Test Coverage)"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "green"},
        'steps': [
            {'range': [0, 60], 'color': "red"},
            {'range': [60, 80], 'color': "orange"},
            {'range': [80, 100], 'color': "lightgreen"}
        ]
    }
))

st.plotly_chart(coverage_gauge, use_container_width=True)

st.divider()

# ------------------------------------------------
# COMPLEXIDADE POR MÓDULO
# ------------------------------------------------

st.subheader(
    "Complexidade Ciclomática do Código por Módulo (Cyclomatic Complexity by Module)"
)

if complexity_df.empty:

    st.warning(
        "Nenhum dado de complexidade encontrado (No complexity data available)"
    )

else:

    fig = px.bar(
        complexity_df,
        x="module",
        y="complexity_score",
        color="complexity_score",
        labels={
            "module": "Módulo (Module)",
            "complexity_score": "Índice de Complexidade (Complexity Score)"
        },
        title="Distribuição de Complexidade do Código (Code Complexity Distribution)"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ------------------------------------------------
# RANKING DAS FUNÇÕES MAIS COMPLEXAS
# ------------------------------------------------

st.subheader(
    "🏆 Ranking das Funções Mais Complexas do Sistema (Most Complex Functions)"
)

try:

    import subprocess
    import json

    result = subprocess.run(
        ["python", "-m", "radon", "cc", "src", "-j"],
        capture_output=True,
        text=True
    )

    data = json.loads(result.stdout)

    functions = []

    for file, items in data.items():
        for item in items:
            functions.append({
                "arquivo": file,
                "função": item["name"],
                "complexidade": item["complexity"]
            })

    df_functions = pd.DataFrame(functions)

    df_functions = df_functions.sort_values(
        by="complexidade",
        ascending=False
    ).head(10)

    df_functions.rename(
        columns={
            "arquivo": "Arquivo (File)",
            "função": "Função (Function)",
            "complexidade": "Complexidade (Complexity)"
        },
        inplace=True
    )

    st.dataframe(df_functions)

except:

    st.info(
        "Não foi possível calcular o ranking de funções (Function ranking unavailable)"
    )

st.divider()

# ------------------------------------------------
# DIAGNÓSTICO AUTOMÁTICO
# ------------------------------------------------

st.subheader("🔎 Diagnóstico Automatizado de Qualidade (Automated Quality Diagnosis)")

for d in diagnosis:
    st.write(d)