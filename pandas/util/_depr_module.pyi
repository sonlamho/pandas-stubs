# Stubs for pandas.util._depr_module (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class _DeprecatedModule:
    deprmod: Any = ...
    deprmodto: Any = ...
    removals: Any = ...
    moved: Any = ...
    self_dir: Any = ...
    def __init__(
        self,
        deprmod: Any,
        deprmodto: Optional[Any] = ...,
        removals: Optional[Any] = ...,
        moved: Optional[Any] = ...,
    ) -> None: ...
    def __dir__(self): ...
    def __getattr__(self, name: Any): ...
