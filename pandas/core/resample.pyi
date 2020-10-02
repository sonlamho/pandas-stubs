# Stubs for pandas.core.resample (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.core.groupby.base import GroupByMixin
from pandas.core.groupby.groupby import _GroupBy
from pandas.core.groupby.grouper import Grouper
from typing import Any, Optional

class Resampler(_GroupBy):
    groupby: Any = ...
    keys: Any = ...
    sort: bool = ...
    axis: Any = ...
    kind: Any = ...
    squeeze: bool = ...
    group_keys: bool = ...
    as_index: bool = ...
    exclusions: Any = ...
    binner: Any = ...
    grouper: Any = ...
    def __init__(
        self,
        obj: Any,
        groupby: Optional[Any] = ...,
        axis: int = ...,
        kind: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def __unicode__(self): ...
    def __getattr__(self, attr: Any): ...
    def __iter__(self): ...
    @property
    def obj(self): ...
    @property
    def ax(self): ...
    def pipe(self, func: Any, *args: Any, **kwargs: Any): ...
    def aggregate(self, func: Any, *args: Any, **kwargs: Any): ...
    agg: Any = ...
    apply: Any = ...
    def transform(self, arg: Any, *args: Any, **kwargs: Any): ...
    def pad(self, limit: Optional[Any] = ...): ...
    ffill: Any = ...
    def nearest(self, limit: Optional[Any] = ...): ...
    def backfill(self, limit: Optional[Any] = ...): ...
    bfill: Any = ...
    def fillna(self, method: Any, limit: Optional[Any] = ...): ...
    def interpolate(
        self,
        method: str = ...,
        axis: int = ...,
        limit: Optional[Any] = ...,
        inplace: bool = ...,
        limit_direction: str = ...,
        limit_area: Optional[Any] = ...,
        downcast: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    def asfreq(self, fill_value: Optional[Any] = ...): ...
    def std(self, ddof: int = ..., *args: Any, **kwargs: Any): ...
    def var(self, ddof: int = ..., *args: Any, **kwargs: Any): ...
    def size(self): ...
    def quantile(self, q: float = ..., **kwargs: Any): ...

def f(self, _method: Any = ..., min_count: int = ..., *args: Any, **kwargs: Any): ...

class _GroupByMixin(GroupByMixin):
    groupby: Any = ...
    def __init__(self, obj: Any, *args: Any, **kwargs: Any) -> None: ...

class DatetimeIndexResampler(Resampler): ...
class DatetimeIndexResamplerGroupby(_GroupByMixin, DatetimeIndexResampler): ...
class PeriodIndexResampler(DatetimeIndexResampler): ...
class PeriodIndexResamplerGroupby(_GroupByMixin, PeriodIndexResampler): ...
class TimedeltaIndexResampler(DatetimeIndexResampler): ...
class TimedeltaIndexResamplerGroupby(_GroupByMixin, TimedeltaIndexResampler): ...

def resample(obj: Any, kind: Optional[Any] = ..., **kwds: Any): ...
def get_resampler_for_grouping(
    groupby: Any,
    rule: Any,
    how: Optional[Any] = ...,
    fill_method: Optional[Any] = ...,
    limit: Optional[Any] = ...,
    kind: Optional[Any] = ...,
    **kwargs: Any
): ...

class TimeGrouper(Grouper):
    closed: Any = ...
    label: Any = ...
    kind: Any = ...
    convention: Any = ...
    loffset: Any = ...
    how: Any = ...
    fill_method: Any = ...
    limit: Any = ...
    base: Any = ...
    def __init__(
        self,
        freq: str = ...,
        closed: Optional[Any] = ...,
        label: Optional[Any] = ...,
        how: str = ...,
        axis: int = ...,
        fill_method: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        loffset: Optional[Any] = ...,
        kind: Optional[Any] = ...,
        convention: Optional[Any] = ...,
        base: int = ...,
        **kwargs: Any
    ) -> None: ...

def asfreq(
    obj: Any,
    freq: Any,
    method: Optional[Any] = ...,
    how: Optional[Any] = ...,
    normalize: bool = ...,
    fill_value: Optional[Any] = ...,
): ...
