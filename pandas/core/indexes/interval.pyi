# Stubs for pandas.core.indexes.interval (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas._libs.interval import IntervalMixin
from pandas.core.indexes.base import Index
from typing import Any, Optional

class IntervalIndex(IntervalMixin, Index):
    def __new__(
        cls,
        data: Any,
        closed: Optional[Any] = ...,
        dtype: Optional[Any] = ...,
        copy: bool = ...,
        name: Optional[Any] = ...,
        verify_integrity: bool = ...,
    ): ...
    @classmethod
    def from_breaks(
        cls,
        breaks: Any,
        closed: str = ...,
        name: Optional[Any] = ...,
        copy: bool = ...,
        dtype: Optional[Any] = ...,
    ): ...
    @classmethod
    def from_arrays(
        cls,
        left: Any,
        right: Any,
        closed: str = ...,
        name: Optional[Any] = ...,
        copy: bool = ...,
        dtype: Optional[Any] = ...,
    ): ...
    @classmethod
    def from_intervals(
        cls,
        data: Any,
        closed: Optional[Any] = ...,
        name: Optional[Any] = ...,
        copy: bool = ...,
        dtype: Optional[Any] = ...,
    ): ...
    @classmethod
    def from_tuples(
        cls,
        data: Any,
        closed: str = ...,
        name: Optional[Any] = ...,
        copy: bool = ...,
        dtype: Optional[Any] = ...,
    ): ...
    def __contains__(self, key: Any): ...
    def contains(self, key: Any): ...
    def to_tuples(self, na_tuple: bool = ...): ...
    @property
    def left(self): ...
    @property
    def right(self): ...
    @property
    def closed(self): ...
    def set_closed(self, closed: Any): ...
    @property
    def length(self): ...
    @property
    def size(self): ...
    @property
    def shape(self): ...
    @property
    def itemsize(self): ...
    def __len__(self): ...
    def values(self): ...
    def __array__(self, result: Optional[Any] = ...): ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...): ...
    def __reduce__(self): ...
    def copy(self, deep: bool = ..., name: Optional[Any] = ...): ...
    def astype(self, dtype: Any, copy: bool = ...): ...
    def dtype(self): ...
    @property
    def inferred_type(self): ...
    def memory_usage(self, deep: bool = ...): ...
    def mid(self): ...
    def is_monotonic(self): ...
    def is_monotonic_increasing(self): ...
    def is_monotonic_decreasing(self): ...
    def is_unique(self): ...
    def is_non_overlapping_monotonic(self): ...
    @property
    def is_overlapping(self): ...
    def get_loc(self, key: Any, method: Optional[Any] = ...): ...
    def get_value(self, series: Any, key: Any): ...
    def get_indexer(
        self,
        target: Any,
        method: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        tolerance: Optional[Any] = ...,
    ): ...
    def get_indexer_non_unique(self, target: Any): ...
    def where(self, cond: Any, other: Optional[Any] = ...): ...
    def delete(self, loc: Any): ...
    def insert(self, loc: Any, item: Any): ...
    def take(
        self,
        indices: Any,
        axis: int = ...,
        allow_fill: bool = ...,
        fill_value: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    def __getitem__(self, value: Any): ...
    def argsort(self, *args: Any, **kwargs: Any): ...
    def equals(self, other: Any): ...
    def overlaps(self, other: Any): ...
    @property
    def is_all_dates(self): ...
    union: Any = ...
    intersection: Any = ...
    difference: Any = ...
    symmetric_difference: Any = ...

def interval_range(
    start: Optional[Any] = ...,
    end: Optional[Any] = ...,
    periods: Optional[Any] = ...,
    freq: Optional[Any] = ...,
    name: Optional[Any] = ...,
    closed: str = ...,
): ...
