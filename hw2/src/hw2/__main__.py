import os
import stat
from os.path import dirname
from typing import Any

from pdflatex import PDFLaTeX  #  type: ignore

from . import create_latex_table, create_latex_document, create_latex_image
import hw1.ast_

file_dir = dirname(__file__)
artifacts_dir = os.path.join(dirname(dirname(file_dir)), "artifacts")  # ../../artifacts

table: list[list[Any]] = [[1, 2, 3], ["foo", "bar", "baz"]]

if not os.path.isdir(artifacts_dir):
    os.mkdir(artifacts_dir, mode=0o775)

# ------------------------ Easy begin -------------------------

with open(os.path.join(artifacts_dir, "table.tex"), "w") as f:
    f.write(create_latex_document(create_latex_table(table)))

# ------------------------- Easy end --------------------------

# ----------------------- Medium begin ------------------------

png_file = os.path.join(artifacts_dir, "ast.png")
hw1.ast_.save_ast_png(png_file)

tex = f"""
    {create_latex_table(table)}

    {create_latex_image(png_file)}
"""

tex_file = "for-pdf.tex"

with open(tex_file, "w") as f:
    f.write(create_latex_document(tex))

pdfl = PDFLaTeX.from_texfile(os.path.join(tex_file))
pdf, log, process = pdfl.create_pdf()

with open(os.path.join(artifacts_dir, "tex.pdf"), "wb") as f:
    f.write(pdf)

os.remove(tex_file)

# ------------------------ Medium end -------------------------
