from typing import Any


def create_latex_table(data: list[list[Any]]) -> str:
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


def create_latex_document(content: str) -> str:
    return f"""
    \\documentclass{{article}}
    \\usepackage{{graphicx}}
    \\begin{{document}}
    {content}
    \\end{{document}}
    """


def create_latex_image(path: str) -> str:
    return f"\\includegraphics[width=1\\columnwidth]{{{path}}}"
