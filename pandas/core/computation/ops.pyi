# Stubs for pandas.core.computation.ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.core.base import StringMixin
from typing import Any, Optional

class UndefinedVariableError(NameError):
    def __init__(self, name: Any, is_local: Any) -> None: ...

class Term(StringMixin):
    def __new__(cls, name: Any, env: Any, side: Optional[Any] = ..., encoding: Optional[Any] = ...): ...
    env: Any = ...
    side: Any = ...
    is_local: Any = ...
    encoding: Any = ...
    def __init__(self, name: Any, env: Any, side: Optional[Any] = ..., encoding: Optional[Any] = ...) -> None: ...
    @property
    def local_name(self): ...
    def __unicode__(self): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def evaluate(self, *args: Any, **kwargs: Any): ...
    value: Any = ...
    def update(self, value: Any) -> None: ...
    @property
    def is_scalar(self): ...
    @property
    def type(self): ...
    return_type: Any = ...
    @property
    def raw(self): ...
    @property
    def is_datetime(self): ...
    @property
    def value(self): ...
    @value.setter
    def value(self, new_value: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, new_name: Any) -> None: ...
    @property
    def ndim(self): ...

class Constant(Term):
    def __init__(self, value: Any, env: Any, side: Optional[Any] = ..., encoding: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    def __unicode__(self): ...

class Op(StringMixin):
    op: Any = ...
    operands: Any = ...
    encoding: Any = ...
    def __init__(self, op: Any, operands: Any, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self): ...
    def __unicode__(self): ...
    @property
    def return_type(self): ...
    @property
    def has_invalid_return_type(self): ...
    @property
    def operand_types(self): ...
    @property
    def is_scalar(self): ...
    @property
    def is_datetime(self): ...

def is_term(obj: Any): ...

class BinOp(Op):
    lhs: Any = ...
    rhs: Any = ...
    func: Any = ...
    def __init__(self, op: Any, lhs: Any, rhs: Any, **kwargs: Any) -> None: ...
    def __call__(self, env: Any): ...
    def evaluate(self, env: Any, engine: Any, parser: Any, term_type: Any, eval_in_python: Any): ...
    def convert_values(self): ...

def isnumeric(dtype: Any): ...

class Div(BinOp):
    def __init__(self, lhs: Any, rhs: Any, truediv: Any, *args: Any, **kwargs: Any) -> None: ...

class UnaryOp(Op):
    operand: Any = ...
    func: Any = ...
    def __init__(self, op: Any, operand: Any) -> None: ...
    def __call__(self, env: Any): ...
    def __unicode__(self): ...
    @property
    def return_type(self): ...

class MathCall(Op):
    func: Any = ...
    def __init__(self, func: Any, args: Any) -> None: ...
    def __call__(self, env: Any): ...
    def __unicode__(self): ...

class FuncNode:
    name: Any = ...
    func: Any = ...
    def __init__(self, name: Any) -> None: ...
    def __call__(self, *args: Any): ...