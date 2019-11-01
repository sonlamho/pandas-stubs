# Stubs for pandas.core.groupby.generic (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.core.groupby.groupby import GroupBy
from typing import Any, Optional

class NDFrameGroupBy(GroupBy):
    def aggregate(self, arg: Any, *args: Any, **kwargs: Any): ...
    agg: Any = ...
    def transform(self, func: Any, *args: Any, **kwargs: Any): ...
    def filter(self, func: Any, dropna: bool = ..., *args: Any, **kwargs: Any): ...

class SeriesGroupBy(GroupBy):
    def apply(self, func: Any, *args: Any, **kwargs: Any): ...
    def aggregate(self, func_or_funcs: Any, *args: Any, **kwargs: Any): ...
    agg: Any = ...
    def transform(self, func: Any, *args: Any, **kwargs: Any): ...
    def filter(self, func: Any, dropna: bool = ..., *args: Any, **kwargs: Any): ...
    def nunique(self, dropna: bool = ...): ...
    def describe(self, **kwargs: Any): ...
    def value_counts(self, normalize: bool = ..., sort: bool = ..., ascending: bool = ..., bins: Optional[Any] = ..., dropna: bool = ...): ...
    def count(self): ...
    def pct_change(self, periods: int = ..., fill_method: str = ..., limit: Optional[Any] = ..., freq: Optional[Any] = ...): ...

class DataFrameGroupBy(NDFrameGroupBy):
    def aggregate(self, arg: Any, *args: Any, **kwargs: Any): ...
    agg: Any = ...
    def count(self): ...
    def nunique(self, dropna: bool = ...): ...
    boxplot: Any = ...

class PanelGroupBy(NDFrameGroupBy):
    def aggregate(self, arg: Any, *args: Any, **kwargs: Any): ...
    agg: Any = ...
    def aggregate(self, arg: Any, *args: Any, **kwargs: Any): ...
