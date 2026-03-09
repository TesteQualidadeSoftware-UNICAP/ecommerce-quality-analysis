# metrics/defect_density.py

def calculate_defect_density(defects, loc):
    """
    Calcula a densidade de defeitos por KLOC (1000 linhas de código)

    :param defects: número de defeitos encontrados
    :param loc: linhas de código do sistema
    :return: densidade de defeitos
    """
    if loc <= 0:
        raise ValueError("LOC deve ser maior que zero")

    density = (defects / loc) * 1000
    return density


def quality_classification(density):
    """
    Classifica a qualidade do software com base na densidade de defeitos
    """

    if density < 1:
        return "Excelente"
    elif density < 5:
        return "Boa"
    elif density < 10:
        return "Média"
    else:
        return "Baixa"


if __name__ == "__main__":
    LOC = 15450
    defects = 23

    density = calculate_defect_density(defects, LOC)
    quality = quality_classification(density)

    print("📊 Relatório de Qualidade")
    print("-----------------------")
    print(f"Linhas de código (LOC): {LOC}")
    print(f"Defeitos encontrados: {defects}")
    print(f"Densidade de defeitos: {density:.2f} defeitos/KLOC")
    print(f"Classificação da qualidade: {quality}")
