import ast
import itertools
import os
from typing import Optional, cast

import matplotlib.pyplot as plt  # type: ignore
import networkx as nx  # type: ignore


class NxGraphVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.g = nx.DiGraph()
        self.__counter = itertools.count(0)

    def __node_name(self, node: ast.AST) -> Optional[str]:
        match type(node):
            case ast.FunctionDef:
                name = f"FunctionDef: {cast(ast.FunctionDef, node).name}"
            case ast.Constant:
                name = f"Const: {ast.unparse(node)}"
            case ast.Name:
                name = f"Name: {ast.unparse(node)}"
            case ast.arg:
                name = f"Arg: {ast.unparse(node)}"
            case ast.Subscript:
                name = f"Subscript: {ast.unparse(node)}"
            case ast.Assign:
                name = f"Assign: {ast.unparse(node)}"
            case ast.Store | ast.Load | ast.Del:
                return None
            case _:
                name = f"{node.__class__.__name__}"

        return f"{next(self.__counter)}. {name}"

    def visit(self, node: ast.AST) -> Optional[str]:
        node_name = self.__node_name(node)

        if node_name is None:
            return None

        self.g.add_node(node_name)

        child_nodes_names = filter(
            lambda x: x is not None, [self.visit(c) for c in ast.iter_child_nodes(node)]
        )
        self.g.add_edges_from(
            [(node_name, child_node_name) for child_node_name in child_nodes_names]
        )

        return node_name


def save_ast_png(path: str) -> None:
    out_dir = os.path.dirname(path)
    script_dir = os.path.dirname(__file__)

    with open(os.path.join(script_dir, "_fib.py"), "r") as f:
        tree = ast.parse("\n".join(f.readlines()))

    visitor = NxGraphVisitor()
    visitor.visit(tree)
    plt.figure(figsize=(24, 24), dpi=100)
    nx.draw(visitor.g, with_labels=True)

    if not os.path.isdir(out_dir):
        os.makedirs(path)

    plt.savefig(path)


__all__ = ["save_ast_png"]
