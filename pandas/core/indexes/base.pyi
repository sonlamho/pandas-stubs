# Stubs for pandas.core.indexes.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.core.base import IndexOpsMixin, PandasObject
from typing import Any, Optional

class InvalidIndexError(Exception): ...

class Index(IndexOpsMixin, PandasObject):
    name: Any = ...
    asi8: Any = ...
    str: Any = ...
    def __new__(
        cls,
        data: Optional[Any] = ...,
        dtype: Optional[Any] = ...,
        copy: bool = ...,
        name: Optional[Any] = ...,
        fastpath: Optional[Any] = ...,
        tupleize_cols: bool = ...,
        **kwargs: Any
    ): ...
    def is_(self, other: Any): ...
    def __len__(self): ...
    def __array__(self, dtype: Optional[Any] = ...): ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...): ...
    def dtype(self): ...
    def dtype_str(self): ...
    def ravel(self, order: str = ...): ...
    def view(self, cls: Optional[Any] = ...): ...
    def astype(self, dtype: Any, copy: bool = ...): ...
    def take(
        self,
        indices: Any,
        axis: int = ...,
        allow_fill: bool = ...,
        fill_value: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    def repeat(self, repeats: Any, axis: Optional[Any] = ...): ...
    def copy(
        self,
        name: Optional[Any] = ...,
        deep: bool = ...,
        dtype: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    def __copy__(self, **kwargs: Any): ...
    def __deepcopy__(self, memo: Optional[Any] = ...): ...
    def __unicode__(self): ...
    def format(
        self, name: bool = ..., formatter: Optional[Any] = ..., **kwargs: Any
    ): ...
    def to_native_types(self, slicer: Optional[Any] = ..., **kwargs: Any): ...
    def summary(self, name: Optional[Any] = ...): ...
    def to_flat_index(self): ...
    def to_series(self, index: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def to_frame(self, index: bool = ..., name: Optional[Any] = ...): ...
    names: Any = ...
    def set_names(
        self, names: Any, level: Optional[Any] = ..., inplace: bool = ...
    ): ...
    def rename(self, name: Any, inplace: bool = ...): ...
    @property
    def nlevels(self): ...
    def sortlevel(
        self,
        level: Optional[Any] = ...,
        ascending: bool = ...,
        sort_remaining: Optional[Any] = ...,
    ): ...
    get_level_values: Any = ...
    def droplevel(self, level: int = ...): ...
    @property
    def is_monotonic(self): ...
    @property
    def is_monotonic_increasing(self): ...
    @property
    def is_monotonic_decreasing(self): ...
    def is_lexsorted_for_tuple(self, tup: Any): ...
    def is_unique(self): ...
    @property
    def has_duplicates(self): ...
    def is_boolean(self): ...
    def is_integer(self): ...
    def is_floating(self): ...
    def is_numeric(self): ...
    def is_object(self): ...
    def is_categorical(self): ...
    def is_interval(self): ...
    def is_mixed(self): ...
    def holds_integer(self): ...
    def inferred_type(self): ...
    def is_all_dates(self): ...
    def __reduce__(self): ...
    def hasnans(self): ...
    def isna(self): ...
    isnull: Any = ...
    def notna(self): ...
    notnull: Any = ...
    def fillna(self, value: Optional[Any] = ..., downcast: Optional[Any] = ...): ...
    def dropna(self, how: str = ...): ...
    def unique(self, level: Optional[Any] = ...): ...
    def drop_duplicates(self, keep: str = ...): ...
    def duplicated(self, keep: str = ...): ...
    def get_duplicates(self): ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __iadd__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __rsub__(self, other: Any): ...
    def __and__(self, other: Any): ...
    def __or__(self, other: Any): ...
    def __xor__(self, other: Any): ...
    def __nonzero__(self) -> None: ...
    __bool__: Any = ...
    def union(self, other: Any, sort: Optional[Any] = ...): ...
    def intersection(self, other: Any, sort: bool = ...): ...
    def difference(self, other: Any, sort: Optional[Any] = ...): ...
    def symmetric_difference(
        self, other: Any, result_name: Optional[Any] = ..., sort: Optional[Any] = ...
    ): ...
    def get_loc(
        self, key: Any, method: Optional[Any] = ..., tolerance: Optional[Any] = ...
    ): ...
    def get_indexer(
        self,
        target: Any,
        method: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        tolerance: Optional[Any] = ...,
    ): ...
    def reindex(
        self,
        target: Any,
        method: Optional[Any] = ...,
        level: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        tolerance: Optional[Any] = ...,
    ): ...
    def join(
        self,
        other: Any,
        how: str = ...,
        level: Optional[Any] = ...,
        return_indexers: bool = ...,
        sort: bool = ...,
    ): ...
    @property
    def values(self): ...
    def get_values(self): ...
    def memory_usage(self, deep: bool = ...): ...
    def where(self, cond: Any, other: Optional[Any] = ...): ...
    def is_type_compatible(self, kind: Any): ...
    def __contains__(self, key: Any): ...
    def contains(self, key: Any): ...
    def __hash__(self) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def append(self, other: Any): ...
    def putmask(self, mask: Any, value: Any): ...
    def equals(self, other: Any): ...
    def identical(self, other: Any): ...
    def asof(self, label: Any): ...
    def asof_locs(self, where: Any, mask: Any): ...
    def sort_values(self, return_indexer: bool = ..., ascending: bool = ...): ...
    def sort(self, *args: Any, **kwargs: Any) -> None: ...
    def shift(self, periods: int = ..., freq: Optional[Any] = ...) -> None: ...
    def argsort(self, *args: Any, **kwargs: Any): ...
    def get_value(self, series: Any, key: Any): ...
    def set_value(self, arr: Any, key: Any, value: Any) -> None: ...
    def get_indexer_non_unique(self, target: Any): ...
    def get_indexer_for(self, target: Any, **kwargs: Any): ...
    def groupby(self, values: Any): ...
    def map(self, mapper: Any, na_action: Optional[Any] = ...): ...
    def isin(self, values: Any, level: Optional[Any] = ...): ...
    def slice_indexer(
        self,
        start: Optional[Any] = ...,
        end: Optional[Any] = ...,
        step: Optional[Any] = ...,
        kind: Optional[Any] = ...,
    ): ...
    def get_slice_bound(self, label: Any, side: Any, kind: Any): ...
    def slice_locs(
        self,
        start: Optional[Any] = ...,
        end: Optional[Any] = ...,
        step: Optional[Any] = ...,
        kind: Optional[Any] = ...,
    ): ...
    def delete(self, loc: Any): ...
    def insert(self, loc: Any, item: Any): ...
    def drop(self, labels: Any, errors: str = ...): ...
