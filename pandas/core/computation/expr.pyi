# Stubs for pandas.core.computation.expr (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import ast
from pandas.core.base import StringMixin
from typing import Any, Optional

def tokenize_string(source: Any) -> None: ...
def disallow(nodes: Any): ...
def add_ops(op_classes: Any): ...

class BaseExprVisitor(ast.NodeVisitor):
    const_type: Any = ...
    term_type: Any = ...
    binary_ops: Any = ...
    binary_op_nodes: Any = ...
    binary_op_nodes_map: Any = ...
    unary_ops: Any = ...
    unary_op_nodes: Any = ...
    unary_op_nodes_map: Any = ...
    rewrite_map: Any = ...
    env: Any = ...
    engine: Any = ...
    parser: Any = ...
    preparser: Any = ...
    assigner: Any = ...
    def __init__(
        self, env: Any, engine: Any, parser: Any, preparser: Any = ...
    ) -> None: ...
    def visit(self, node: Any, **kwargs: Any): ...
    def visit_Module(self, node: Any, **kwargs: Any): ...
    def visit_Expr(self, node: Any, **kwargs: Any): ...
    def visit_BinOp(self, node: Any, **kwargs: Any): ...
    def visit_Div(self, node: Any, **kwargs: Any): ...
    def visit_UnaryOp(self, node: Any, **kwargs: Any): ...
    def visit_Name(self, node: Any, **kwargs: Any): ...
    def visit_NameConstant(self, node: Any, **kwargs: Any): ...
    def visit_Num(self, node: Any, **kwargs: Any): ...
    def visit_Str(self, node: Any, **kwargs: Any): ...
    def visit_List(self, node: Any, **kwargs: Any): ...
    visit_Tuple: Any = ...
    def visit_Index(self, node: Any, **kwargs: Any): ...
    def visit_Subscript(self, node: Any, **kwargs: Any): ...
    def visit_Slice(self, node: Any, **kwargs: Any): ...
    def visit_Assign(self, node: Any, **kwargs: Any): ...
    def visit_Attribute(self, node: Any, **kwargs: Any): ...
    def visit_Call_35(self, node: Any, side: Optional[Any] = ..., **kwargs: Any): ...
    def visit_Call_legacy(
        self, node: Any, side: Optional[Any] = ..., **kwargs: Any
    ): ...
    def translate_In(self, op: Any): ...
    def visit_Compare(self, node: Any, **kwargs: Any): ...
    def visit_BoolOp(self, node: Any, **kwargs: Any): ...

class PandasExprVisitor(BaseExprVisitor):
    def __init__(
        self, env: Any, engine: Any, parser: Any, preparser: Any = ...
    ) -> None: ...

class PythonExprVisitor(BaseExprVisitor):
    def __init__(
        self, env: Any, engine: Any, parser: Any, preparser: Any = ...
    ) -> None: ...

class Expr(StringMixin):
    expr: Any = ...
    env: Any = ...
    engine: Any = ...
    parser: Any = ...
    terms: Any = ...
    def __init__(
        self,
        expr: Any,
        engine: str = ...,
        parser: str = ...,
        env: Optional[Any] = ...,
        truediv: bool = ...,
        level: int = ...,
    ) -> None: ...
    @property
    def assigner(self): ...
    def __call__(self): ...
    def __unicode__(self): ...
    def __len__(self): ...
    def parse(self): ...
    @property
    def names(self): ...
