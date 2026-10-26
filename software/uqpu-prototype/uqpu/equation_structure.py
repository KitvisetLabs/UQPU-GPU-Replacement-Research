"""Transparent symbolic-structure diagnostics for equation-discovery benchmarks.

This is a small, deterministic baseline inspired by structural-verification
work in symbolic regression. It is NOT a learned verifier, a reproduction of
L2G-SR, or a test of physical truth. Ground-truth structure is suitable only
for evaluating frozen synthetic/known-law fixtures, never for selecting
candidates when the target law is unknown.
"""

from __future__ import annotations

import ast
import math

Node = tuple[str, tuple["Node", ...]]

_ALLOWED_FUNCTIONS = {"abs", "cos", "exp", "log", "sin", "sqrt", "tan"}


def canonical_expression_tree(
    expression: str, *, abstract_numeric_constants: bool = True
) -> Node:
    """Parse a restricted expression and canonicalize commutative structure.

    Addition and multiplication are flattened and sorted, so associative and
    commutative rewrites share a representation. Numeric constants are
    abstracted by default to focus on expression shape; set the flag to False
    when coefficient/exponent values are part of the benchmark target.

    Calls are limited to a small whitelist of unary mathematical functions.
    The expression is parsed, never evaluated.
    """
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("expression must be a non-empty string")
    try:
        root = ast.parse(expression, mode="eval").body
    except (SyntaxError, ValueError) as exc:
        raise ValueError("expression is not valid supported syntax") from exc

    def build(node: ast.AST) -> Node:
        if isinstance(node, ast.Name):
            return (f"var:{node.id}", ())
        if isinstance(node, ast.Constant):
            value = node.value
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("only real numeric constants are supported")
            if not math.isfinite(float(value)):
                raise ValueError("numeric constants must be finite")
            label = "const" if abstract_numeric_constants else f"const:{value!r}"
            return (label, ())
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            label = "pos" if isinstance(node.op, ast.UAdd) else "neg"
            return (label, (build(node.operand),))
        if isinstance(node, ast.BinOp):
            labels = {
                ast.Add: "add",
                ast.Sub: "sub",
                ast.Mult: "mul",
                ast.Div: "div",
                ast.Pow: "pow",
            }
            label = labels.get(type(node.op))
            if label is None:
                raise ValueError("unsupported binary operator")
            children = [build(node.left), build(node.right)]
            if label in {"add", "mul"}:
                flattened: list[Node] = []
                for child in children:
                    if child[0] == label:
                        flattened.extend(child[1])
                    else:
                        flattened.append(child)
                children = sorted(flattened, key=repr)
            return (label, tuple(children))
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in _ALLOWED_FUNCTIONS:
                raise ValueError("unsupported function call")
            if node.keywords:
                raise ValueError("keyword arguments are not supported")
            return (f"call:{node.func.id}", tuple(build(arg) for arg in node.args))
        raise ValueError(f"unsupported syntax: {type(node).__name__}")

    return build(root)


def _tree_size(tree: Node) -> int:
    return 1 + sum(_tree_size(child) for child in tree[1])


def _distance(left: Node, right: Node) -> int:
    """Root-preserving ordered-tree edit metric with subtree insert/delete."""
    root_cost = 0 if left[0] == right[0] else 1
    left_children, right_children = left[1], right[1]
    rows, cols = len(left_children), len(right_children)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        dp[i][0] = dp[i - 1][0] + _tree_size(left_children[i - 1])
    for j in range(1, cols + 1):
        dp[0][j] = dp[0][j - 1] + _tree_size(right_children[j - 1])

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            delete_cost = dp[i - 1][j] + _tree_size(left_children[i - 1])
            insert_cost = dp[i][j - 1] + _tree_size(right_children[j - 1])
            replace_cost = dp[i - 1][j - 1] + _distance(
                left_children[i - 1], right_children[j - 1]
            )
            dp[i][j] = min(delete_cost, insert_cost, replace_cost)
    return root_cost + dp[rows][cols]


def canonical_structure_distance(
    left: str,
    right: str,
    *,
    abstract_numeric_constants: bool = True,
) -> int:
    """Return the integer edit cost between canonical expression trees.

    This project-defined metric is a transparent baseline, not the exact tree
    edit-distance implementation used by any external paper.
    """
    left_tree = canonical_expression_tree(
        left, abstract_numeric_constants=abstract_numeric_constants
    )
    right_tree = canonical_expression_tree(
        right, abstract_numeric_constants=abstract_numeric_constants
    )
    return _distance(left_tree, right_tree)


def normalized_structure_distance(
    left: str,
    right: str,
    *,
    abstract_numeric_constants: bool = True,
) -> float:
    """Normalize the project-defined edit cost to [0, 1] by total tree size."""
    left_tree = canonical_expression_tree(
        left, abstract_numeric_constants=abstract_numeric_constants
    )
    right_tree = canonical_expression_tree(
        right, abstract_numeric_constants=abstract_numeric_constants
    )
    denominator = _tree_size(left_tree) + _tree_size(right_tree)
    return _distance(left_tree, right_tree) / denominator
