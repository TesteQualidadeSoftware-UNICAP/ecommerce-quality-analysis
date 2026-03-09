import subprocess
import re


def get_loc():
    """
    Obtém automaticamente o total de linhas de código (LOC)
    usando radon.
    """

    result = subprocess.run(
        ["python", "-m", "radon", "raw", "src"],
        capture_output=True,
        text=True
    )

    loc_values = re.findall(r"LOC:\s+(\d+)", result.stdout)

    loc_total = sum(int(x) for x in loc_values)

    return loc_total


def calculate_defect_density(defects, loc):
    """
    Calcula a densidade de defeitos por KLOC.
    """
    if loc == 0:
        raise ValueError("LOC deve ser maior que zero")

    density = (defects / loc) * 1000
    return density


def classify_quality(density):
    """
    Classificação da qualidade baseada na densidade.
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

    defects = 4  # número real de defeitos conhecidos

    loc = get_loc()

    density = calculate_defect_density(defects, loc)

    quality = classify_quality(density)

    print("\n📊 Densidade de Defeitos")
    print("------------------------")
    print(f"LOC total: {loc}")
    print(f"Defeitos conhecidos: {defects}")
    print(f"Densidade: {density:.2f} defeitos/KLOC")
    print(f"Qualidade: {quality}")