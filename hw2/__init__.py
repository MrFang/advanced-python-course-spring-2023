from typing import Any


def gen_latex_table(data: list[list[Any]]) -> str:
    n_columns = len(data[0]) if len(data) > 0 else 0

    for row in data:
        assert len(row) == n_columns

    strings: list[str] = []
    strings.append("\\begin{tabular}{ " + ("c " * n_columns) + "}")

    for row in data:
        s = " & ".join([str(x) for x in row])
        strings.append(s + " \\\\")

    strings.append("\\end{tabular}")

    return "\n".join(strings)
