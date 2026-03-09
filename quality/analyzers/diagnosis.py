def generate_diagnosis(coverage, duplication, density):
    """
    Gera um diagnóstico automático da qualidade do sistema
    com base nas métricas coletadas.
    """

    diagnosis = []

    # --------------------------------------------
    # Cobertura de testes
    # --------------------------------------------

    if coverage >= 90:
        diagnosis.append(
            "✔ Cobertura de testes excelente (Test Coverage is excellent)."
        )

    elif coverage >= 80:
        diagnosis.append(
            "✔ Cobertura de testes adequada (Test Coverage is adequate)."
        )

    elif coverage >= 60:
        diagnosis.append(
            "⚠ Cobertura de testes moderada. Recomenda-se aumentar os testes automatizados (Test Coverage is moderate)."
        )

    else:
        diagnosis.append(
            "❌ Cobertura de testes baixa. Aumentar significativamente os testes automatizados (Low Test Coverage)."
        )

    # --------------------------------------------
    # Duplicação de código
    # --------------------------------------------

    if duplication < 5:
        diagnosis.append(
            "✔ Baixa duplicação de código (Low Code Duplication)."
        )

    elif duplication < 10:
        diagnosis.append(
            "⚠ Duplicação de código moderada. Avaliar oportunidades de refatoração (Moderate Code Duplication)."
        )

    else:
        diagnosis.append(
            "❌ Alta duplicação de código. Refatoração recomendada (High Code Duplication)."
        )

    # --------------------------------------------
    # Densidade de defeitos
    # --------------------------------------------

    if density < 5:
        diagnosis.append(
            "✔ Baixa densidade de defeitos (Low Defect Density)."
        )

    elif density < 10:
        diagnosis.append(
            "⚠ Densidade de defeitos moderada (Moderate Defect Density)."
        )

    else:
        diagnosis.append(
            "⚠ Densidade de defeitos elevada, possivelmente influenciada pelo tamanho reduzido do sistema analisado (High Defect Density)."
        )

    return diagnosis