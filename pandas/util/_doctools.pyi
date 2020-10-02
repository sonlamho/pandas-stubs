# Stubs for pandas.util._doctools (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class TablePlotter:
    cell_width: Any = ...
    cell_height: Any = ...
    font_size: Any = ...
    def __init__(
        self, cell_width: float = ..., cell_height: float = ..., font_size: float = ...
    ) -> None: ...
    def plot(
        self, left: Any, right: Any, labels: Optional[Any] = ..., vertical: bool = ...
    ): ...

class _WritableDoc(type): ...
