# Stubs for pandas.core.algorithms (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def match(to_match: Any, values: Any, na_sentinel: int = ...): ...
def unique(values: Any): ...

unique1d = unique

def isin(comps: Any, values: Any): ...
def factorize(
    values: Any,
    sort: bool = ...,
    order: Optional[Any] = ...,
    na_sentinel: int = ...,
    size_hint: Optional[Any] = ...,
): ...
def value_counts(
    values: Any,
    sort: bool = ...,
    ascending: bool = ...,
    normalize: bool = ...,
    bins: Optional[Any] = ...,
    dropna: bool = ...,
): ...
def duplicated(values: Any, keep: str = ...): ...
def mode(values: Any, dropna: bool = ...): ...
def rank(
    values: Any,
    axis: int = ...,
    method: str = ...,
    na_option: str = ...,
    ascending: bool = ...,
    pct: bool = ...,
): ...
def checked_add_with_arr(
    arr: Any, b: Any, arr_mask: Optional[Any] = ..., b_mask: Optional[Any] = ...
): ...
def quantile(x: Any, q: Any, interpolation_method: str = ...): ...

class SelectN:
    obj: Any = ...
    n: Any = ...
    keep: Any = ...
    def __init__(self, obj: Any, n: Any, keep: Any) -> None: ...
    def nlargest(self): ...
    def nsmallest(self): ...
    @staticmethod
    def is_valid_dtype_n_method(dtype: Any): ...

class SelectNSeries(SelectN):
    def compute(self, method: Any): ...

class SelectNFrame(SelectN):
    columns: Any = ...
    def __init__(self, obj: Any, n: Any, keep: Any, columns: Any) -> None: ...
    def compute(self, method: Any): ...

def take(
    arr: Any,
    indices: Any,
    axis: int = ...,
    allow_fill: bool = ...,
    fill_value: Optional[Any] = ...,
): ...
def take_nd(
    arr: Any,
    indexer: Any,
    axis: int = ...,
    out: Optional[Any] = ...,
    fill_value: Any = ...,
    mask_info: Optional[Any] = ...,
    allow_fill: bool = ...,
): ...

take_1d = take_nd

def take_2d_multi(
    arr: Any,
    indexer: Any,
    out: Optional[Any] = ...,
    fill_value: Any = ...,
    mask_info: Optional[Any] = ...,
    allow_fill: bool = ...,
): ...
def diff(arr: Any, n: Any, axis: int = ...): ...
