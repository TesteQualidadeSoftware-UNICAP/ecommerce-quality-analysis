import subprocess
import re


def get_loc(path="src"):
    """
    Obtém o total de linhas de código (LOC) do projeto
    utilizando a ferramenta radon.
    """

    result = subprocess.run(
        ["python", "-m", "radon", "raw", path],
        capture_output=True,
        text=True
    )

    loc_values = re.findall(r"LOC:\s+(\d+)", result.stdout)

    total_loc = sum(int(x) for x in loc_values)

    return total_loc