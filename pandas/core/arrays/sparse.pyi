# Stubs for pandas.core.arrays.sparse (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import numpy as np
from pandas.core.accessor import PandasDelegate
from pandas.core.arrays import ExtensionArray, ExtensionOpsMixin
from pandas.core.base import PandasObject
from pandas.core.dtypes.base import ExtensionDtype
from typing import Any, Optional

class SparseDtype(ExtensionDtype):
    def __init__(self, dtype: Union[str, np.dtype, ExtensionDtype, type]=..., fill_value: Any=...) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other: Any): ...
    @property
    def fill_value(self): ...
    @property
    def kind(self): ...
    @property
    def type(self): ...
    @property
    def subtype(self): ...
    @property
    def name(self): ...
    @classmethod
    def construct_array_type(cls): ...
    @classmethod
    def construct_from_string(cls, string: Any): ...
    @classmethod
    def is_dtype(cls, dtype: Any): ...
    def update_dtype(self, dtype: Any): ...

class SparseArray(PandasObject, ExtensionArray, ExtensionOpsMixin):
    __array_priority__: int = ...
    def __init__(self, data: Any, sparse_index: Optional[Any] = ..., index: Optional[Any] = ..., fill_value: Optional[Any] = ..., kind: str = ..., dtype: Optional[Any] = ..., copy: bool = ...) -> None: ...
    def __array__(self, dtype: Optional[Any] = ..., copy: bool = ...): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    @property
    def sp_index(self): ...
    @property
    def sp_values(self): ...
    @property
    def dtype(self): ...
    @property
    def fill_value(self): ...
    @fill_value.setter
    def fill_value(self, value: Any) -> None: ...
    @property
    def kind(self): ...
    def __len__(self): ...
    @property
    def nbytes(self): ...
    @property
    def density(self): ...
    @property
    def npoints(self): ...
    @property
    def values(self): ...
    def isna(self): ...
    def fillna(self, value: Optional[Any] = ..., method: Optional[Any] = ..., limit: Optional[Any] = ...): ...
    def shift(self, periods: int = ..., fill_value: Optional[Any] = ...): ...
    def unique(self): ...
    def factorize(self, na_sentinel: int = ...): ...
    def value_counts(self, dropna: bool = ...): ...
    def __getitem__(self, key: Any): ...
    def take(self, indices: Any, allow_fill: bool = ..., fill_value: Optional[Any] = ...): ...
    def searchsorted(self, v: Any, side: str = ..., sorter: Optional[Any] = ...): ...
    def copy(self, deep: bool = ...): ...
    def astype(self, dtype: Optional[Any] = ..., copy: bool = ...): ...
    def map(self, mapper: Any): ...
    def to_dense(self): ...
    get_values: Any = ...
    def nonzero(self): ...
    def all(self, axis: Optional[Any] = ..., *args: Any, **kwargs: Any): ...
    def any(self, axis: int = ..., *args: Any, **kwargs: Any): ...
    def sum(self, axis: int = ..., *args: Any, **kwargs: Any): ...
    def cumsum(self, axis: int = ..., *args: Any, **kwargs: Any): ...
    def mean(self, axis: int = ..., *args: Any, **kwargs: Any): ...
    def transpose(self, *axes: Any): ...
    @property
    def T(self): ...
    def __array_wrap__(self, array: Any, context: Optional[Any] = ...): ...
    def __array_ufunc__(self, ufunc: Any, method: Any, *inputs: Any, **kwargs: Any): ...
    def __abs__(self): ...
    def __unicode__(self): ...

def make_sparse(arr: Any, kind: str = ..., fill_value: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ...): ...

class SparseAccessor(PandasDelegate):
    def __init__(self, data: Optional[Any] = ...) -> None: ...
    @classmethod
    def from_coo(cls, A: Any, dense_index: bool = ...): ...
    def to_coo(self, row_levels: Any = ..., column_levels: Any = ..., sort_labels: bool = ...): ...
