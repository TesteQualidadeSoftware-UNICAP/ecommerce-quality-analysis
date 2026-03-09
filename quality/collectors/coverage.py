import subprocess
import re


def get_coverage():
    """
    Executa pytest com cobertura e retorna o percentual
    de cobertura total do projeto.
    """

    result = subprocess.run(
        ["pytest", "--cov=src"],
        capture_output=True,
        text=True
    )

    match = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", result.stdout)

    if match:
        return int(match.group(1))

    return 0