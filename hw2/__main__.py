import os
from typing import Any

from hw2 import gen_latex_table

file_dir = os.path.abspath(os.path.dirname(__file__))
artifacts_dir = os.path.join(file_dir, "artifacts")

table: list[list[Any]] = [[1, 2, 3], ["foo", "bar", "baz"]]

if not os.path.isdir(artifacts_dir):
    os.mkdir(artifacts_dir)

with open(os.path.join(artifacts_dir, "table.tex"), "w") as f:
    f.write(gen_latex_table(table))

