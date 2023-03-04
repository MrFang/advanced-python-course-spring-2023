import os
from os.path import dirname

from .ast_ import save_ast_png

script_dir = dirname(__file__)
artifacts_dir = os.path.join(
    dirname(dirname(script_dir)), "artifacts"
)  # ../../artifacts
save_ast_png(os.path.join(artifacts_dir, "ast.png"))
