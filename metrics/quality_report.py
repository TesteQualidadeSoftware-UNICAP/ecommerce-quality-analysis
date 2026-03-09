import subprocess
import re


def get_loc():
    result = subprocess.run(
        ["python", "-m", "radon", "raw", "src"],
        capture_output=True,
        text=True
    )

    loc_values = re.findall(r"LOC:\s+(\d+)", result.stdout)
    return sum(int(x) for x in loc_values)


def get_complexity():
    result = subprocess.run(
        ["python", "-m", "radon", "cc", "src", "-a"],
        capture_output=True,
        text=True
    )

    match = re.search(r"Average complexity: (\w)", result.stdout)

    if match:
        return match.group(1)

    return "N/A"


def get_coverage():
    result = subprocess.run(
        ["pytest", "--cov=src"],
        capture_output=True,
        text=True
    )

    match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", result.stdout)

    if match:
        return int(match.group(1))

    return 0


def get_duplication():
    result = subprocess.run(
        ["npx", "jscpd", "src"],
        capture_output=True,
        text=True
    )

    match = re.search(r"(\d+\.\d+)%", result.stdout)

    if match:
        return float(match.group(1))

    return 0


def defect_density(defects, loc):
    if loc == 0:
        return 0

    return (defects / loc) * 1000


def generate_diagnosis(complexity, coverage, density, duplication):

    diagnosis = []

    # Complexidade
    if complexity in ["D", "E", "F"]:
        diagnosis.append("Complexidade elevada. Recomenda-se refatoração.")
    elif complexity == "C":
        diagnosis.append("Complexidade moderada. Avaliar simplificação de funções.")
    else:
        diagnosis.append("Complexidade baixa. Código de fácil manutenção.")

    # Cobertura
    if coverage < 60:
        diagnosis.append("Cobertura de testes baixa. Necessário aumentar testes automatizados.")
    elif coverage < 80:
        diagnosis.append("Cobertura moderada de testes.")
    else:
        diagnosis.append("Cobertura de testes adequada.")

    # Densidade
    if density > 10:
        diagnosis.append("Alta densidade de defeitos detectada.")
    elif density > 5:
        diagnosis.append("Densidade de defeitos moderada.")
    else:
        diagnosis.append("Baixa densidade de defeitos.")

    # Duplicação
    if duplication > 10:
        diagnosis.append("Alta duplicação de código. Refatoração recomendada.")
    elif duplication > 5:
        diagnosis.append("Duplicação moderada de código.")
    else:
        diagnosis.append("Baixa duplicação de código.")

    return diagnosis


def main():

    defects = 4

    loc = get_loc()
    complexity = get_complexity()
    coverage = get_coverage()
    duplication = get_duplication()

    density = defect_density(defects, loc)

    diagnosis = generate_diagnosis(complexity, coverage, density, duplication)

    print("\n📊 Relatório de Qualidade do Código")
    print("-----------------------------------")
    print(f"LOC total: {loc}")
    print(f"Complexidade média: {complexity}")
    print(f"Cobertura de testes: {coverage}%")
    print(f"Defeitos conhecidos: {defects}")
    print(f"Densidade de defeitos: {density:.2f} defeitos/KLOC")
    print(f"Duplicação de código: {duplication}%")

    print("\n🔎 Diagnóstico")
    print("--------------")

    for d in diagnosis:
        print(f"- {d}")


if __name__ == "__main__":
    main()