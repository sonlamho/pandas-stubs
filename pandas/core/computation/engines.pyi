# Stubs for pandas.core.computation.engines (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc
from typing import Any

class NumExprClobberingError(NameError): ...

class AbstractEngine(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    has_neg_frac: bool = ...
    expr: Any = ...
    aligned_axes: Any = ...
    result_type: Any = ...
    def __init__(self, expr: Any) -> None: ...
    def convert(self): ...
    def evaluate(self): ...

class NumExprEngine(AbstractEngine):
    has_neg_frac: bool = ...
    def __init__(self, expr: Any) -> None: ...
    def convert(self): ...

class PythonEngine(AbstractEngine):
    has_neg_frac: bool = ...
    def __init__(self, expr: Any) -> None: ...
    def evaluate(self): ...
