# Stubs for pandas.core.ops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def get_op_result_name(left: Any, right: Any): ...
def maybe_upcast_for_op(obj: Any): ...
def radd(left: Any, right: Any): ...
def rsub(left: Any, right: Any): ...
def rmul(left: Any, right: Any): ...
def rdiv(left: Any, right: Any): ...
def rtruediv(left: Any, right: Any): ...
def rfloordiv(left: Any, right: Any): ...
def rmod(left: Any, right: Any): ...
def rdivmod(left: Any, right: Any): ...
def rpow(left: Any, right: Any): ...
def rand_(left: Any, right: Any): ...
def ror_(left: Any, right: Any): ...
def rxor(left: Any, right: Any): ...
def make_invalid_op(name: Any): ...

reverse_op: Any

def fill_binop(left: Any, right: Any, fill_value: Any): ...
def mask_cmp_op(x: Any, y: Any, op: Any, allowed_types: Any): ...
def masked_arith_op(x: Any, y: Any, op: Any): ...
def invalid_comparison(left: Any, right: Any, op: Any): ...
def should_series_dispatch(left: Any, right: Any, op: Any): ...
def dispatch_to_series(left: Any, right: Any, func: Any, str_rep: Optional[Any] = ..., axis: Optional[Any] = ...): ...
def dispatch_to_index_op(op: Any, left: Any, right: Any, index_class: Any): ...
def dispatch_to_extension_op(op: Any, left: Any, right: Any): ...
def add_methods(cls, new_methods: Any) -> None: ...
def add_special_arithmetic_methods(cls): ...
def add_flex_arithmetic_methods(cls) -> None: ...