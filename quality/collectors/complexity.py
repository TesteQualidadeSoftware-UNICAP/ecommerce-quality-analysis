import subprocess
import pandas as pd
import re

grade_map = {
    "A": 2,
    "B": 7,
    "C": 15,
    "D": 25,
    "E": 35,
    "F": 45
}

def get_complexity(path="src"):

    result = subprocess.run(
        ["python", "-m", "radon", "cc", path],
        capture_output=True,
        text=True
    )

    modules = []
    scores = []

    current_file = None

    for line in result.stdout.splitlines():

        file_match = re.match(r"(src/.*\.py)", line)

        if file_match:
            current_file = file_match.group(1)

        grade_match = re.search(r"- ([A-F])$", line)

        if grade_match and current_file:
            grade = grade_match.group(1)

            modules.append(current_file)
            scores.append(grade_map[grade])

    if not modules:
        return pd.DataFrame(columns=["module", "complexity_score"])

    df = pd.DataFrame({
        "module": modules,
        "complexity_score": scores
    })

    df = df.groupby("module").mean().reset_index()

    return df