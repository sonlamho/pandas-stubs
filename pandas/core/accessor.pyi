# Stubs for pandas.core.accessor (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class DirNamesMixin:
    def __dir__(self): ...

class PandasDelegate: ...

def delegate_names(delegate: Any, accessors: Any, typ: Any, overwrite: bool = ...): ...

class CachedAccessor:
    def __init__(self, name: Any, accessor: Any) -> None: ...
    def __get__(self, obj: Any, cls: Any): ...

def register_dataframe_accessor(name: Any): ...
def register_series_accessor(name: Any): ...
def register_index_accessor(name: Any): ...