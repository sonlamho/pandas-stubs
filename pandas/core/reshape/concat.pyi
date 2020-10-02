# Stubs for pandas.core.reshape.concat (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def concat(
    objs: Any,
    axis: int = ...,
    join: str = ...,
    join_axes: Optional[Any] = ...,
    ignore_index: bool = ...,
    keys: Optional[Any] = ...,
    levels: Optional[Any] = ...,
    names: Optional[Any] = ...,
    verify_integrity: bool = ...,
    sort: Optional[Any] = ...,
    copy: bool = ...,
): ...

class _Concatenator:
    intersect: bool = ...
    objs: Any = ...
    axis: Any = ...
    join_axes: Any = ...
    keys: Any = ...
    names: Any = ...
    levels: Any = ...
    sort: Any = ...
    ignore_index: Any = ...
    verify_integrity: Any = ...
    copy: Any = ...
    new_axes: Any = ...
    def __init__(
        self,
        objs: Any,
        axis: int = ...,
        join: str = ...,
        join_axes: Optional[Any] = ...,
        keys: Optional[Any] = ...,
        levels: Optional[Any] = ...,
        names: Optional[Any] = ...,
        ignore_index: bool = ...,
        verify_integrity: bool = ...,
        copy: bool = ...,
        sort: bool = ...,
    ) -> None: ...
    def get_result(self): ...
