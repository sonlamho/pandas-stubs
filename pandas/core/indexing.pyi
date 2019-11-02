# Stubs for pandas.core.indexing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas._libs.indexing import _NDFrameIndexerBase
from typing import Any, Optional

def get_indexers_list(): ...

class _IndexSlice:
    def __getitem__(self, arg: Any): ...

IndexSlice: Any

class IndexingError(Exception): ...

class _NDFrameIndexer(_NDFrameIndexerBase):
    axis: Any = ...
    def __call__(self, axis: Optional[Any] = ...): ...
    def __iter__(self) -> None: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...

class _IXIndexer(_NDFrameIndexer):
    def __init__(self, name: Any, obj: Any) -> None: ...

class _LocationIndexer(_NDFrameIndexer):
    def __getitem__(self, key: Any): ...

class _LocIndexer(_LocationIndexer): ...
class _iLocIndexer(_LocationIndexer): ...

class _ScalarAccessIndexer(_NDFrameIndexer):
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...

class _AtIndexer(_ScalarAccessIndexer): ...
class _iAtIndexer(_ScalarAccessIndexer): ...

def length_of_indexer(indexer: Any, target: Optional[Any] = ...): ...
def convert_to_index_sliceable(obj: Any, key: Any): ...
def check_bool_indexer(ax: Any, key: Any): ...
def check_setitem_lengths(indexer: Any, value: Any, values: Any) -> None: ...
def convert_missing_indexer(indexer: Any): ...
def convert_from_missing_indexer_tuple(indexer: Any, axes: Any): ...
def maybe_convert_indices(indices: Any, n: Any): ...
def validate_indices(indices: Any, n: Any) -> None: ...
def maybe_convert_ix(*args: Any): ...
def is_nested_tuple(tup: Any, labels: Any): ...
def is_list_like_indexer(key: Any): ...
def is_label_like(key: Any): ...
def need_slice(obj: Any): ...
def maybe_droplevels(index: Any, key: Any): ...