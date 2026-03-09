import subprocess
import re


def get_duplication(path="src"):
    """
    Obtém o percentual de duplicação de código
    usando a ferramenta jscpd.
    """

    result = subprocess.run(
        ["npx", "jscpd", path],
        capture_output=True,
        text=True
    )

    match = re.search(r"(\d+\.\d+)%", result.stdout)

    if match:
        return float(match.group(1))

    return 0.0