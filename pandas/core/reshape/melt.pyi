# Stubs for pandas.core.reshape.melt (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def melt(
    frame: Any,
    id_vars: Optional[Any] = ...,
    value_vars: Optional[Any] = ...,
    var_name: Optional[Any] = ...,
    value_name: str = ...,
    col_level: Optional[Any] = ...,
): ...
def lreshape(
    data: Any, groups: Any, dropna: bool = ..., label: Optional[Any] = ...
): ...
def wide_to_long(
    df: Any, stubnames: Any, i: Any, j: Any, sep: str = ..., suffix: str = ...
): ...
