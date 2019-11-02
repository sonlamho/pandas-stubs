# Stubs for pandas.core.dtypes.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class _DtypeOpsMixin:
    na_value: Any = ...
    def __eq__(self, other: Any): ...
    def __hash__(self): ...
    def __ne__(self, other: Any): ...
    @property
    def names(self) -> Optional[List[str]]: ...
    @classmethod
    def is_dtype(cls, dtype: Any): ...

class ExtensionDtype(_DtypeOpsMixin):
    @property
    def type(self) -> type: ...
    @property
    def kind(self): ...
    @property
    def name(self) -> str: ...
    @classmethod
    def construct_array_type(cls) -> None: ...
    @classmethod
    def construct_from_string(cls, string: Any) -> None: ...