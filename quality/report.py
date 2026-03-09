from quality.collectors.loc import get_loc
from quality.collectors.coverage import get_coverage
from quality.collectors.duplication import get_duplication
from quality.collectors.complexity import get_complexity

from quality.analyzers.defect_density import calculate_defect_density
from quality.analyzers.diagnosis import generate_diagnosis


def collect_metrics():
    """
    Coleta todas as métricas de qualidade do sistema
    e retorna um dicionário consolidado.
    """

    # ------------------------------------------------
    # Número de defeitos conhecidos
    # (poderia vir de issue tracker futuramente)
    # ------------------------------------------------

    defects = 4

    # ------------------------------------------------
    # Coleta de métricas
    # ------------------------------------------------

    loc = get_loc()

    coverage = get_coverage()

    duplication = get_duplication()

    complexity_df = get_complexity()

    # ------------------------------------------------
    # Análises derivadas
    # ------------------------------------------------

    density = calculate_defect_density(defects, loc)

    diagnosis = generate_diagnosis(
        coverage,
        duplication,
        density
    )

    # ------------------------------------------------
    # Retorno consolidado
    # ------------------------------------------------

    return {
        "loc": loc,
        "coverage": coverage,
        "duplication": duplication,
        "complexity": complexity_df,
        "density": density,
        "defects": defects,
        "diagnosis": diagnosis
    }


# ------------------------------------------------
# Execução via terminal (opcional)
# ------------------------------------------------

if __name__ == "__main__":

    metrics = collect_metrics()

    print("\n📊 Relatório de Qualidade de Código (Code Quality Report)")
    print("---------------------------------------------------------")

    print(f"Linhas de Código (LOC): {metrics['loc']}")
    print(f"Cobertura de Testes (Test Coverage): {metrics['coverage']}%")
    print(f"Duplicação de Código (Code Duplication): {metrics['duplication']}%")
    print(f"Densidade de Defeitos (Defect Density): {metrics['density']:.2f} defeitos/KLOC")

    print("\n🔎 Diagnóstico de Qualidade (Quality Diagnosis)\n")

    for d in metrics["diagnosis"]:
        print(d)