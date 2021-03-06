# Stubs for pandas.core.indexes.api (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas._libs import NaT as NaT
from pandas.core.indexes.base import (
    Index as Index,
    InvalidIndexError as InvalidIndexError,
    _new_Index as _new_Index,
    ensure_index as ensure_index,
    ensure_index_from_sequences as ensure_index_from_sequences,
)
from pandas.core.indexes.category import CategoricalIndex as CategoricalIndex
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.interval import IntervalIndex as IntervalIndex
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.numeric import (
    Float64Index as Float64Index,
    Int64Index as Int64Index,
    NumericIndex as NumericIndex,
    UInt64Index as UInt64Index,
)
from pandas.core.indexes.period import PeriodIndex as PeriodIndex
from pandas.core.indexes.range import RangeIndex as RangeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex

# Names in __all__ with no definition:
#   _all_indexes_same
#   _get_combined_index
#   _get_consensus_names
#   _get_objs_combined_axis
#   _union_indexes
