def calculate_defect_density(defects, loc):
    """
    Calcula a densidade de defeitos (defeitos por 1000 linhas de código).
    """

    if loc == 0:
        return 0

    return (defects / loc) * 1000


def classify_density(density):
    """
    Classifica a qualidade com base na densidade de defeitos.
    """

    if density < 1:
        return "Excelente"
    elif density < 5:
        return "Boa"
    elif density < 10:
        return "Média"
    else:
        return "Baixa"