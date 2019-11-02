# Stubs for pandas.tseries.offsets (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas._libs.tslibs import offsets as liboffsets
from pandas._libs.tslibs.offsets import BaseOffset
from pandas import Timestamp
from datetime import datetime
from typing import Any, Optional, Union

_ANYDATETIME = Union[datetime, Timestamp]

class DateOffset(BaseOffset):
    normalize: bool = ...
    def __init__(self, n: int = ..., normalize: bool = ..., **kwds: Any) -> None: ...
    def apply(self, other: Any): ...
    def apply_index(self, i: Any): ...
    def isAnchored(self): ...
    @property
    def name(self): ...
    def rollback(self, dt: _ANYDATETIME) -> Timestamp: ...
    def rollforward(self, dt: _ANYDATETIME) -> Timestamp: ...
    def onOffset(self, dt: Any): ...
    @property
    def rule_code(self): ...
    def freqstr(self): ...
    @property
    def nanos(self) -> None: ...

class SingleConstructorOffset(DateOffset): ...

class _CustomMixin:
    def __init__(self, weekmask: Any, holidays: Any, calendar: Any) -> None: ...

class BusinessMixin:
    @property
    def offset(self): ...

class BusinessDay(BusinessMixin, SingleConstructorOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., offset: Any = ...) -> None: ...
    def apply(self, other: Any): ...
    def apply_index(self, i: Any): ...
    def onOffset(self, dt: Any): ...

class BusinessHourMixin(BusinessMixin):
    def __init__(self, start: str = ..., end: str = ..., offset: Any = ...) -> None: ...
    def next_bday(self): ...
    def rollback(self, dt: Any): ...
    def rollforward(self, dt: Any): ...
    def apply(self, other: Any): ...
    def onOffset(self, dt: Any): ...

class BusinessHour(BusinessHourMixin, SingleConstructorOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., start: str = ..., end: str = ..., offset: Any = ...) -> None: ...

class CustomBusinessDay(_CustomMixin, BusinessDay):
    def __init__(self, n: int = ..., normalize: bool = ..., weekmask: str = ..., holidays: Optional[Any] = ..., calendar: Optional[Any] = ..., offset: Any = ...) -> None: ...
    def apply(self, other: Any): ...
    def apply_index(self, i: Any) -> None: ...
    def onOffset(self, dt: Any): ...

class CustomBusinessHour(_CustomMixin, BusinessHourMixin, SingleConstructorOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., weekmask: str = ..., holidays: Optional[Any] = ..., calendar: Optional[Any] = ..., start: str = ..., end: str = ..., offset: Any = ...) -> None: ...

class MonthOffset(SingleConstructorOffset):
    @property
    def name(self): ...
    def onOffset(self, dt: Any): ...
    def apply(self, other: Any): ...
    def apply_index(self, i: Any): ...

class MonthEnd(MonthOffset): ...
class MonthBegin(MonthOffset): ...
class BusinessMonthEnd(MonthOffset): ...
class BusinessMonthBegin(MonthOffset): ...

class _CustomBusinessMonth(_CustomMixin, BusinessMixin, MonthOffset):
    onOffset: Any = ...
    apply_index: Any = ...
    def __init__(self, n: int = ..., normalize: bool = ..., weekmask: str = ..., holidays: Optional[Any] = ..., calendar: Optional[Any] = ..., offset: Any = ...) -> None: ...
    def cbday_roll(self): ...
    def m_offset(self): ...
    def month_roll(self): ...
    def apply(self, other: Any): ...

class CustomBusinessMonthEnd(_CustomBusinessMonth):
    __doc__: Any = ...

class CustomBusinessMonthBegin(_CustomBusinessMonth):
    __doc__: Any = ...

class SemiMonthOffset(DateOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., day_of_month: Optional[Any] = ...) -> None: ...
    @property
    def rule_code(self): ...
    def apply(self, other: Any): ...
    def apply_index(self, i: Any): ...

class SemiMonthEnd(SemiMonthOffset):
    def onOffset(self, dt: Any): ...

class SemiMonthBegin(SemiMonthOffset):
    def onOffset(self, dt: Any): ...

class Week(DateOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., weekday: Optional[Any] = ...) -> None: ...
    def isAnchored(self): ...
    def apply(self, other: Any): ...
    def apply_index(self, i: Any): ...
    def onOffset(self, dt: Any): ...
    @property
    def rule_code(self): ...

class _WeekOfMonthMixin:
    def apply(self, other: Any): ...
    def onOffset(self, dt: Any): ...

class WeekOfMonth(_WeekOfMonthMixin, DateOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., week: int = ..., weekday: int = ...) -> None: ...
    @property
    def rule_code(self): ...

class LastWeekOfMonth(_WeekOfMonthMixin, DateOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., weekday: int = ...) -> None: ...
    @property
    def rule_code(self): ...

class QuarterOffset(DateOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., startingMonth: Optional[Any] = ...) -> None: ...
    def isAnchored(self): ...
    @property
    def rule_code(self): ...
    def apply(self, other: Any): ...
    def onOffset(self, dt: Any): ...
    def apply_index(self, dtindex: Any): ...

class BQuarterEnd(QuarterOffset): ...
class BQuarterBegin(QuarterOffset): ...
class QuarterEnd(QuarterOffset): ...
class QuarterBegin(QuarterOffset): ...

class YearOffset(DateOffset):
    def apply(self, other: Any): ...
    def apply_index(self, dtindex: Any): ...
    def onOffset(self, dt: Any): ...
    def __init__(self, n: int = ..., normalize: bool = ..., month: Optional[Any] = ...) -> None: ...
    @property
    def rule_code(self): ...

class BYearEnd(YearOffset): ...
class BYearBegin(YearOffset): ...
class YearEnd(YearOffset): ...
class YearBegin(YearOffset): ...

class FY5253(DateOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., weekday: int = ..., startingMonth: int = ..., variation: str = ...) -> None: ...
    def isAnchored(self): ...
    def onOffset(self, dt: Any): ...
    def apply(self, other: Any): ...
    def get_year_end(self, dt: Any): ...
    @property
    def rule_code(self): ...
    def get_rule_code_suffix(self): ...

class FY5253Quarter(DateOffset):
    def __init__(self, n: int = ..., normalize: bool = ..., weekday: int = ..., startingMonth: int = ..., qtr_with_extra_week: int = ..., variation: str = ...) -> None: ...
    def isAnchored(self): ...
    def apply(self, other: Any): ...
    def get_weeks(self, dt: Any): ...
    def year_has_extra_week(self, dt: Any): ...
    def onOffset(self, dt: Any): ...
    @property
    def rule_code(self): ...

class Easter(DateOffset):
    def apply(self, other: Any): ...
    def onOffset(self, dt: Any): ...

class Tick(liboffsets._Tick, SingleConstructorOffset):
    def __init__(self, n: int = ..., normalize: bool = ...) -> None: ...
    __gt__: Any = ...
    __ge__: Any = ...
    __lt__: Any = ...
    __le__: Any = ...
    def __add__(self, other: Any): ...
    def __eq__(self, other: Any): ...
    def __hash__(self): ...
    def __ne__(self, other: Any): ...
    @property
    def delta(self): ...
    @property
    def nanos(self): ...
    def apply(self, other: Any): ...
    def isAnchored(self): ...

class Day(Tick): ...
class Hour(Tick): ...
class Minute(Tick): ...
class Second(Tick): ...
class Milli(Tick): ...
class Micro(Tick): ...
class Nano(Tick): ...
BDay = BusinessDay
BMonthEnd = BusinessMonthEnd
BMonthBegin = BusinessMonthBegin
CBMonthEnd = CustomBusinessMonthEnd
CBMonthBegin = CustomBusinessMonthBegin
CDay = CustomBusinessDay