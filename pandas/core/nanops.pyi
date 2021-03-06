# Stubs for pandas.core.nanops (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

ver: Any

def set_use_bottleneck(v: bool = ...) -> None: ...

class disallow:
    dtypes: Any = ...
    def __init__(self, *dtypes: Any) -> None: ...
    def check(self, obj: Any): ...
    def __call__(self, f: Any): ...

class bottleneck_switch:
    kwargs: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def __call__(self, alt: Any): ...

def nanany(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nanall(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nansum(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    min_count: int = ...,
    mask: Optional[Any] = ...,
): ...
def nanmean(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nanmedian(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nanstd(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    ddof: int = ...,
    mask: Optional[Any] = ...,
): ...
def nanvar(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    ddof: int = ...,
    mask: Optional[Any] = ...,
): ...
def nansem(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    ddof: int = ...,
    mask: Optional[Any] = ...,
): ...

nanmin: Any
nanmax: Any

def nanargmax(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nanargmin(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nanskew(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nankurt(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    mask: Optional[Any] = ...,
): ...
def nanprod(
    values: Any,
    axis: Optional[Any] = ...,
    skipna: bool = ...,
    min_count: int = ...,
    mask: Optional[Any] = ...,
): ...
def nancorr(a: Any, b: Any, method: str = ..., min_periods: Optional[Any] = ...): ...
def get_corr_func(method: Any): ...
def nancov(a: Any, b: Any, min_periods: Optional[Any] = ...): ...
def make_nancomp(op: Any): ...

nangt: Any
nange: Any
nanlt: Any
nanle: Any
naneq: Any
nanne: Any

def nanpercentile(
    values: Any,
    q: Any,
    axis: Any,
    na_value: Any,
    mask: Any,
    ndim: Any,
    interpolation: Any,
): ...
