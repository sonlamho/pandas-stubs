# Stubs for pandas.core.reshape.pivot (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def pivot_table(data: Any, values: Optional[Any] = ..., index: Optional[Any] = ..., columns: Optional[Any] = ..., aggfunc: str = ..., fill_value: Optional[Any] = ..., margins: bool = ..., dropna: bool = ..., margins_name: str = ...): ...
def pivot(data: Any, index: Optional[Any] = ..., columns: Optional[Any] = ..., values: Optional[Any] = ...): ...
def crosstab(index: Any, columns: Any, values: Optional[Any] = ..., rownames: Optional[Any] = ..., colnames: Optional[Any] = ..., aggfunc: Optional[Any] = ..., margins: bool = ..., margins_name: str = ..., dropna: bool = ..., normalize: bool = ...): ...
