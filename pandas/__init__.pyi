# Stubs for pandas (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

# from pandas.core.indexes.datetimes import DatetimeIndex
# from .core.indexes.base import Index
from pandas.core import base
from pandas.core.generic import NDFrame
from pandas.core.dtypes.dtypes import CategoricalDtype
from typing import (
    Dict,
    Any,
    Optional,
    Iterator,
    Union,
    TypeVar,
    overload,
    Sequence,
    List,
    Tuple,
    MutableSequence,
    Type,
    Generic,
    Mapping,
    Sized,
    Iterable,
    Hashable,
    Callable,
)
from typing_extensions import Protocol
from abc import abstractmethod
from datetime import datetime, timedelta, date
from numpy import number, timedelta64, ndarray, generic

__docformat__: str
hard_dependencies: Any
missing_dependencies: Any
module: Any
v: Any

NaT: Any

NoneType = type(None)
_NUMBER = Union[float, generic]
_S = TypeVar("_S")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_C = TypeVar("_C", bound="__Comparable")

class __Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass
    @abstractmethod
    def __lt__(self: _C, other: _C) -> bool:
        pass
    def __gt__(self: _C, other: _C) -> bool:
        return (not self < other) and self != other
    def __le__(self: _C, other: _C) -> bool:
        return self < other or self == other
    def __ge__(self: _C, other: _C) -> bool:
        return not self < other

class __Addable(Protocol):
    def __add__(self: _S, other: _S) -> _S:
        pass

class Series(base.IndexOpsMixin, NDFrame, Sequence, Sized):
    hasnans: Any = ...
    def __init__(
        self,
        data: Any = ...,
        index: Optional[Iterable] = ...,
        dtype: Optional[Union[Type, str]] = ...,
        name: Optional[str] = ...,
        copy: bool = ...,
        fastpath: bool = ...,
    ) -> None: ...
    @property
    def shape(self) -> Tuple[int]: ...
    @classmethod
    def from_array(
        cls,
        arr: Any,
        index: Optional[Any] = ...,
        name: Optional[Any] = ...,
        dtype: Optional[Any] = ...,
        copy: bool = ...,
        fastpath: bool = ...,
    ) -> "Series": ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value: Any) -> None: ...
    @property
    def dtype(self): ...
    @property
    def dtypes(self): ...
    @property
    def ftype(self): ...
    @property
    def ftypes(self): ...
    @property
    def values(self) -> ndarray: ...
    def get_values(self) -> ndarray: ...
    @property
    def asobject(self): ...
    def ravel(self, order: str = ...): ...
    def compress(self, condition: Any, *args: Any, **kwargs: Any): ...
    def nonzero(self): ...
    def put(self, *args: Any, **kwargs: Any) -> None: ...
    def __len__(self) -> int: ...
    def view(self, dtype: Optional[Any] = ...): ...
    def __array__(self, dtype: Optional[Any] = ...): ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...): ...
    def __array_prepare__(self, result: Any, context: Optional[Any] = ...): ...
    @property
    def real(self) -> ndarray: ...
    @real.setter
    def real(self, v: Any) -> None: ...
    @property
    def imag(self) -> ndarray: ...
    @imag.setter
    def imag(self, v: Any) -> None: ...
    __float__: Any = ...
    __long__: Any = ...
    __int__: Any = ...
    @property
    def axes(self): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def repeat(self: _S, repeats: Any, axis: Optional[Any] = ...) -> _S: ...
    def get_value(self, label: Any, takeable: bool = ...): ...
    def set_value(self, label: Any, value: Any, takeable: bool = ...): ...
    index: Any = ...
    def reset_index(
        self: _S,
        level: Optional[Any] = ...,
        drop: bool = ...,
        name: Optional[Any] = ...,
        inplace: bool = ...,
    ) -> _S: ...
    def __unicode__(self): ...
    def to_string(
        self,
        buf: Optional[Any] = ...,
        na_rep: str = ...,
        float_format: Optional[Any] = ...,
        header: bool = ...,
        index: bool = ...,
        length: bool = ...,
        dtype: bool = ...,
        name: bool = ...,
        max_rows: Optional[Any] = ...,
    ) -> str: ...
    def iteritems(self) -> Iterator: ...
    items: Any = ...
    def keys(self): ...
    def to_dict(self, into: Any = ...) -> Dict: ...
    def to_frame(self, name: Optional[Any] = ...) -> "DataFrame": ...
    def to_sparse(self, kind: str = ..., fill_value: Optional[Any] = ...): ...
    def count(self, level: Optional[Any] = ...): ...
    def nunique(self, dropna: bool = ...) -> int: ...
    def mode(self, dropna: bool = ...): ...
    def unique(self) -> ndarray: ...
    def drop_duplicates(self: _S, keep: str = ..., inplace: bool = ...) -> _S: ...
    def duplicated(self, keep: str = ...): ...
    def idxmin(
        self, axis: int = ..., skipna: bool = ..., *args: Any, **kwargs: Any
    ): ...
    def idxmax(
        self, axis: int = ..., skipna: bool = ..., *args: Any, **kwargs: Any
    ): ...
    argmin: Any = ...
    argmax: Any = ...
    def round(self: _S, decimals: int = ..., *args: Any, **kwargs: Any) -> _S: ...
    @overload
    def quantile(self, q: float = ..., interpolation: str = ...) -> Any: ...
    @overload
    def quantile(
        self, q: Union[ndarray, Sequence[float]] = ..., interpolation: str = ...
    ) -> "Series": ...
    def corr(self, other: Any, method: str = ..., min_periods: Optional[Any] = ...): ...
    def cov(self, other: Any, min_periods: Optional[Any] = ...): ...
    def diff(self, periods: int = ...): ...
    def autocorr(self, lag: int = ...): ...
    def dot(self, other: Any): ...
    def __matmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    def searchsorted(
        self, value: Any, side: str = ..., sorter: Optional[Any] = ...
    ): ...
    def append(
        self, to_append: Any, ignore_index: bool = ..., verify_integrity: bool = ...
    ): ...
    def combine(self, other: Any, func: Any, fill_value: Optional[Any] = ...): ...
    def combine_first(self, other: Any): ...
    def update(self, other: Any) -> None: ...
    def sort_values(
        self: _S,
        axis: int = ...,
        ascending: bool = ...,
        inplace: bool = ...,
        kind: str = ...,
        na_position: str = ...,
    ) -> _S: ...
    def sort_index(
        self: _S,
        axis: int = ...,
        level: Optional[Any] = ...,
        ascending: bool = ...,
        inplace: bool = ...,
        kind: str = ...,
        na_position: str = ...,
        sort_remaining: bool = ...,
    ) -> _S: ...
    def argsort(self, axis: int = ..., kind: str = ..., order: Optional[Any] = ...): ...
    def nlargest(self, n: int = ..., keep: str = ...): ...
    def nsmallest(self, n: int = ..., keep: str = ...): ...
    def swaplevel(self, i: int = ..., j: int = ..., copy: bool = ...): ...
    def reorder_levels(self, order: Any): ...
    def unstack(self, level: int = ..., fill_value: Optional[Any] = ...): ...
    def map(self: _S, arg: Any, na_action: Optional[Any] = ...) -> _S: ...
    def aggregate(self, func: Any, axis: int = ..., *args: Any, **kwargs: Any): ...
    agg: Any = ...
    def transform(self, func: Any, axis: int = ..., *args: Any, **kwargs: Any): ...
    def apply(
        self: _S, func: Any, convert_dtype: bool = ..., args: Any = ..., **kwds: Any
    ) -> _S: ...
    def align(
        self,
        other: Any,
        join: str = ...,
        axis: Optional[Any] = ...,
        level: Optional[Any] = ...,
        copy: bool = ...,
        fill_value: Optional[Any] = ...,
        method: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        fill_axis: int = ...,
        broadcast_axis: Optional[Any] = ...,
    ): ...
    def rename(self: _S, index: Optional[Any] = ..., **kwargs: Any) -> _S: ...
    def reindex(self: _S, index: Optional[Any] = ..., **kwargs: Any) -> _S: ...
    def drop(
        self: _S,
        labels: Optional[Any] = ...,
        axis: int = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        level: Optional[Any] = ...,
        inplace: bool = ...,
        errors: str = ...,
    ) -> _S: ...
    def fillna(
        self: _S,
        value: Optional[Any] = ...,
        method: Optional[Any] = ...,
        axis: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        downcast: Optional[Any] = ...,
        **kwargs: Any
    ) -> _S: ...
    def replace(
        self: _S,
        to_replace: Optional[Any] = ...,
        value: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        regex: bool = ...,
        method: str = ...,
    ) -> _S: ...
    def shift(
        self,
        periods: int = ...,
        freq: Optional[Any] = ...,
        axis: int = ...,
        fill_value: Optional[Any] = ...,
    ): ...
    def memory_usage(self, index: bool = ..., deep: bool = ...): ...
    def isin(self: _S, values: Any) -> _S: ...
    def between(self, left: Any, right: Any, inclusive: bool = ...): ...
    @classmethod
    def from_csv(
        cls,
        path: Any,
        sep: str = ...,
        parse_dates: bool = ...,
        header: Optional[Any] = ...,
        index_col: int = ...,
        encoding: Optional[Any] = ...,
        infer_datetime_format: bool = ...,
    ): ...
    def to_csv(self, *args: Any, **kwargs: Any): ...
    def isna(self: _S) -> _S: ...
    def isnull(self: _S) -> _S: ...
    def notna(self: _S) -> _S: ...
    def notnull(self: _S) -> _S: ...
    def dropna(self: _S, axis: int = ..., inplace: bool = ..., **kwargs: Any) -> _S: ...
    def valid(self, inplace: bool = ..., **kwargs: Any): ...
    def to_timestamp(
        self: _S, freq: Optional[Any] = ..., how: str = ..., copy: bool = ...
    ) -> _S: ...
    def to_period(self, freq: Optional[Any] = ..., copy: bool = ...): ...
    str: Any = ...
    dt: Any = ...
    cat: Any = ...
    plot: Any = ...
    sparse: Any = ...
    hist: Any = ...
    def __eq__(self: _S, other: Any) -> _S: ...  # type: ignore[override]
    def __ne__(self: _S, other: Any) -> _S: ...  # type: ignore[override]
    def __lt__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __gt__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __le__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __ge__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __and__(self: _S, other: _S) -> _S: ...
    def __or__(self: _S, other: _S) -> _S: ...
    def __xor__(self: _S, other: _S) -> _S: ...
    def __mul__(self: _S, other: Union[_S, _NUMBER]) -> _S: ...
    def __rmul__(self: _S, other: Union[_S, _NUMBER]) -> _S: ...
    def __rsub__(self: _S, other: Union[_S, _NUMBER]) -> _S: ...
    def __sub__(self: _S, other: Union[_S, _NUMBER]) -> _S: ...
    def __div__(self: _S, other: Union[_S, _NUMBER]) -> _S: ...
    def __truediv__(self: _S, other: Union[_S, _NUMBER]) -> _S: ...
    def __add__(self: _S, other: Union[_S, _NUMBER, __Addable]) -> _S: ...
    @overload  # type: ignore[override]
    def __getitem__(self: _S, key: slice) -> _S: ...
    @overload
    def __getitem__(self, key: Any) -> Any: ...

class DataFrame(NDFrame, Sized):
    def __init__(
        self,
        data: Optional[Iterable] = ...,
        index: Optional[Iterable] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        dtype: Optional[Union[Type, str]] = ...,
        copy: bool = ...,
    ) -> None: ...
    @property
    def axes(self): ...
    @property
    def shape(self) -> Tuple[int, int]: ...
    def __unicode__(self): ...
    def to_string(
        self,
        buf: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        col_space: Optional[Any] = ...,
        header: bool = ...,
        index: bool = ...,
        na_rep: str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[Any] = ...,
        index_names: bool = ...,
        justify: Optional[Any] = ...,
        max_rows: Optional[Any] = ...,
        max_cols: Optional[Any] = ...,
        show_dimensions: bool = ...,
        decimal: str = ...,
        line_width: Optional[Any] = ...,
    ) -> str: ...
    @property
    def style(self): ...
    def iteritems(self) -> Iterator: ...
    def iterrows(self) -> Iterator[Series]: ...
    def itertuples(self, index: bool = ..., name: str = ...) -> Iterator[Tuple]: ...
    items: Any = ...
    def dot(self, other: Any): ...
    def __matmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    @classmethod
    def from_dict(
        cls,
        data: Any,
        orient: str = ...,
        dtype: Optional[Any] = ...,
        columns: Optional[Any] = ...,
    ): ...
    def to_numpy(self, dtype: Optional[Any] = ..., copy: bool = ...): ...
    def to_dict(self, orient: str = ..., into: Any = ...): ...
    def to_gbq(
        self,
        destination_table: Any,
        project_id: Optional[Any] = ...,
        chunksize: Optional[Any] = ...,
        reauth: bool = ...,
        if_exists: str = ...,
        auth_local_webserver: bool = ...,
        table_schema: Optional[Any] = ...,
        location: Optional[Any] = ...,
        progress_bar: bool = ...,
        credentials: Optional[Any] = ...,
        verbose: Optional[Any] = ...,
        private_key: Optional[Any] = ...,
    ): ...
    @classmethod
    def from_records(
        cls,
        data: Any,
        index: Optional[Any] = ...,
        exclude: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        coerce_float: bool = ...,
        nrows: Optional[Any] = ...,
    ): ...
    def to_records(
        self,
        index: bool = ...,
        convert_datetime64: Optional[Any] = ...,
        column_dtypes: Optional[Any] = ...,
        index_dtypes: Optional[Any] = ...,
    ): ...
    @classmethod
    def from_items(
        cls, items: Any, columns: Optional[Any] = ..., orient: str = ...
    ): ...
    @classmethod
    def from_csv(
        cls,
        path: Any,
        header: int = ...,
        sep: str = ...,
        index_col: int = ...,
        parse_dates: bool = ...,
        encoding: Optional[Any] = ...,
        tupleize_cols: Optional[Any] = ...,
        infer_datetime_format: bool = ...,
    ): ...
    def to_sparse(self, fill_value: Optional[Any] = ..., kind: str = ...): ...
    def to_panel(self): ...
    def to_stata(
        self,
        fname: Any,
        convert_dates: Optional[Any] = ...,
        write_index: bool = ...,
        encoding: str = ...,
        byteorder: Optional[Any] = ...,
        time_stamp: Optional[Any] = ...,
        data_label: Optional[Any] = ...,
        variable_labels: Optional[Any] = ...,
        version: int = ...,
        convert_strl: Optional[Any] = ...,
    ) -> None: ...
    def to_feather(self, fname: Any) -> None: ...
    def to_parquet(
        self,
        fname: Any,
        engine: str = ...,
        compression: str = ...,
        index: Optional[Any] = ...,
        partition_cols: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def to_html(
        self,
        buf: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        col_space: Optional[Any] = ...,
        header: bool = ...,
        index: bool = ...,
        na_rep: str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[Any] = ...,
        index_names: bool = ...,
        justify: Optional[Any] = ...,
        max_rows: Optional[Any] = ...,
        max_cols: Optional[Any] = ...,
        show_dimensions: bool = ...,
        decimal: str = ...,
        bold_rows: bool = ...,
        classes: Optional[Any] = ...,
        escape: bool = ...,
        notebook: bool = ...,
        border: Optional[Any] = ...,
        table_id: Optional[Any] = ...,
        render_links: bool = ...,
    ): ...
    def info(
        self,
        verbose: Optional[Any] = ...,
        buf: Optional[Any] = ...,
        max_cols: Optional[Any] = ...,
        memory_usage: Optional[Any] = ...,
        null_counts: Optional[Any] = ...,
    ) -> None: ...
    def memory_usage(self, index: bool = ..., deep: bool = ...) -> Series: ...
    def transpose(self: _S, *args: Any, **kwargs: Any) -> _S: ...
    T: Any = ...
    def get_value(self, index: Any, col: Any, takeable: bool = ...): ...
    def set_value(self, index: Any, col: Any, value: Any, takeable: bool = ...): ...
    @overload
    def __getitem__(self, key: Union[str, int, float, Tuple]) -> Series: ...
    @overload
    def __getitem__(self: _S, key: MutableSequence) -> _S: ...
    @overload
    def __getitem__(self: _S, key: Series) -> _S: ...
    @overload
    def __getitem__(self: _S, key: ndarray) -> _S: ...
    def query(self, expr: str, inplace: bool = ..., **kwargs: Any): ...
    def eval(self, expr: str, inplace: bool = ..., **kwargs: Any): ...
    def select_dtypes(
        self, include: Optional[Any] = ..., exclude: Optional[Any] = ...
    ): ...
    def __setitem__(self, key: Any, value: Any): ...
    def insert(
        self, loc: Any, column: Any, value: Any, allow_duplicates: bool = ...
    ) -> None: ...
    def assign(self, **kwargs: Any): ...
    def lookup(self, row_labels: Any, col_labels: Any): ...
    def align(
        self,
        other: Any,
        join: str = ...,
        axis: Optional[Any] = ...,
        level: Optional[Any] = ...,
        copy: bool = ...,
        fill_value: Optional[Any] = ...,
        method: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        fill_axis: int = ...,
        broadcast_axis: Optional[Any] = ...,
    ): ...
    def reindex(self: _S, *args: Any, **kwargs: Any) -> _S: ...
    def reindex_axis(
        self: _S,
        labels: Any,
        axis: int = ...,
        method: Optional[Any] = ...,
        level: Optional[Any] = ...,
        copy: bool = ...,
        limit: Optional[Any] = ...,
        fill_value: Optional[Any] = ...,
    ) -> _S: ...
    def drop(
        self: _S,
        labels: Optional[Any] = ...,
        axis: int = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        level: Optional[Any] = ...,
        inplace: bool = ...,
        errors: str = ...,
    ) -> _S: ...
    def rename(self, *args: Any, **kwargs: Any): ...
    def fillna(
        self: _S,
        value: Optional[Any] = ...,
        method: Optional[Any] = ...,
        axis: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        downcast: Optional[Any] = ...,
        **kwargs: Any
    ) -> _S: ...
    def replace(
        self: _S,
        to_replace: Optional[Any] = ...,
        value: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        regex: bool = ...,
        method: str = ...,
    ) -> _S: ...
    def shift(
        self,
        periods: int = ...,
        freq: Optional[Any] = ...,
        axis: int = ...,
        fill_value: Optional[Any] = ...,
    ): ...
    def set_index(
        self: _S,
        keys: Any,
        drop: bool = ...,
        append: bool = ...,
        inplace: bool = ...,
        verify_integrity: bool = ...,
    ) -> _S: ...
    def reset_index(
        self: _S,
        level: Optional[Any] = ...,
        drop: bool = ...,
        inplace: bool = ...,
        col_level: int = ...,
        col_fill: str = ...,
    ) -> _S: ...
    def isna(self: _S) -> _S: ...
    def isnull(self: _S) -> _S: ...
    def notna(self: _S) -> _S: ...
    def notnull(self: _S) -> _S: ...
    def dropna(
        self: _S,
        axis: int = ...,
        how: str = ...,
        thresh: Optional[Any] = ...,
        subset: Optional[Any] = ...,
        inplace: bool = ...,
    ) -> _S: ...
    def drop_duplicates(
        self: _S, subset: Optional[Any] = ..., keep: str = ..., inplace: bool = ...
    ) -> _S: ...
    def duplicated(self, subset: Optional[Any] = ..., keep: str = ...): ...
    def sort_values(
        self: _S,
        by: Any,
        axis: int = ...,
        ascending: bool = ...,
        inplace: bool = ...,
        kind: str = ...,
        na_position: str = ...,
    ) -> _S: ...
    def sort_index(
        self: _S,
        axis: int = ...,
        level: Optional[Any] = ...,
        ascending: bool = ...,
        inplace: bool = ...,
        kind: str = ...,
        na_position: str = ...,
        sort_remaining: bool = ...,
        by: Optional[Any] = ...,
    ) -> _S: ...
    def nlargest(self, n: Any, columns: Any, keep: str = ...): ...
    def nsmallest(self, n: Any, columns: Any, keep: str = ...): ...
    def swaplevel(self, i: int = ..., j: int = ..., axis: int = ...): ...
    def reorder_levels(self, order: Any, axis: int = ...): ...
    def combine(
        self,
        other: Any,
        func: Any,
        fill_value: Optional[Any] = ...,
        overwrite: bool = ...,
    ): ...
    def combine_first(self, other: Any): ...
    def update(
        self,
        other: Any,
        join: str = ...,
        overwrite: bool = ...,
        filter_func: Optional[Any] = ...,
        errors: str = ...,
    ) -> None: ...
    def pivot(
        self,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        values: Optional[Any] = ...,
    ): ...
    def pivot_table(
        self,
        values: Optional[Any] = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        aggfunc: str = ...,
        fill_value: Optional[Any] = ...,
        margins: bool = ...,
        dropna: bool = ...,
        margins_name: str = ...,
    ): ...
    def stack(self, level: int = ..., dropna: bool = ...): ...
    def unstack(self, level: int = ..., fill_value: Optional[Any] = ...): ...
    def melt(
        self,
        id_vars: Optional[Any] = ...,
        value_vars: Optional[Any] = ...,
        var_name: Optional[Any] = ...,
        value_name: str = ...,
        col_level: Optional[Any] = ...,
    ): ...
    def diff(self, periods: int = ..., axis: int = ...): ...
    def aggregate(self, func: Any, axis: int = ..., *args: Any, **kwargs: Any): ...
    agg: Any = ...
    def transform(self, func: Any, axis: int = ..., *args: Any, **kwargs: Any): ...
    def apply(
        self,
        func: Any,
        axis: int = ...,
        broadcast: Optional[Any] = ...,
        raw: bool = ...,
        reduce: Optional[Any] = ...,
        result_type: Optional[Any] = ...,
        args: Any = ...,
        **kwds: Any
    ): ...
    def applymap(self, func: Any): ...
    def append(
        self,
        other: Any,
        ignore_index: bool = ...,
        verify_integrity: bool = ...,
        sort: Optional[Any] = ...,
    ): ...
    def join(
        self,
        other: Any,
        on: Optional[Any] = ...,
        how: str = ...,
        lsuffix: str = ...,
        rsuffix: str = ...,
        sort: bool = ...,
    ) -> "DataFrame": ...
    def merge(
        self,
        right: Any,
        how: str = ...,
        on: Optional[Any] = ...,
        left_on: Optional[Any] = ...,
        right_on: Optional[Any] = ...,
        left_index: bool = ...,
        right_index: bool = ...,
        sort: bool = ...,
        suffixes: Any = ...,
        copy: bool = ...,
        indicator: bool = ...,
        validate: Optional[Any] = ...,
    ) -> "DataFrame": ...
    def round(self: _S, decimals: int = ..., *args: Any, **kwargs: Any) -> _S: ...
    def corr(self, method: str = ..., min_periods: int = ...): ...
    def cov(self, min_periods: Optional[Any] = ...): ...
    def corrwith(
        self, other: Any, axis: int = ..., drop: bool = ..., method: str = ...
    ): ...
    def count(
        self, axis: int = ..., level: Optional[Any] = ..., numeric_only: bool = ...
    ): ...
    def nunique(self, axis: int = ..., dropna: bool = ...) -> Series: ...
    def idxmin(self, axis: int = ..., skipna: bool = ...): ...
    def idxmax(self, axis: int = ..., skipna: bool = ...): ...
    def mode(self, axis: int = ..., numeric_only: bool = ..., dropna: bool = ...): ...
    @overload
    def quantile(
        self,
        q: float = ...,
        axis: Union[int, str] = ...,
        numeric_only: bool = ...,
        interpolation: str = ...,
    ) -> Series: ...
    @overload
    def quantile(
        self,
        q: Union[ndarray, Sequence[float]],
        axis: Union[int, str] = ...,
        numeric_only: bool = ...,
        interpolation: str = ...,
    ) -> "DataFrame": ...
    def to_timestamp(
        self: _S,
        freq: Optional[Any] = ...,
        how: str = ...,
        axis: int = ...,
        copy: bool = ...,
    ) -> _S: ...
    def to_period(
        self, freq: Optional[Any] = ..., axis: int = ..., copy: bool = ...
    ): ...
    def isin(self: _S, values: Any) -> _S: ...
    plot: Any = ...
    hist: Any = ...
    boxplot: Any = ...
    def __eq__(self: _S, other: Any) -> _S: ...  # type: ignore[override]
    def __ne__(self: _S, other: Any) -> _S: ...  # type: ignore[override]
    def __lt__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __gt__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __le__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __ge__(self: _S, other: Union[_S, _C]) -> _S: ...
    def __mul__(self: _S, other: _NUMBER) -> _S: ...
    def __rmul__(self: _S, other: _NUMBER) -> _S: ...
    def __add__(self: _S, other: _NUMBER) -> _S: ...
    def __radd__(self: _S, other: _NUMBER) -> _S: ...
    def __sub__(self: _S, other: _NUMBER) -> _S: ...
    def __rsub__(self: _S, other: _NUMBER) -> _S: ...

class Timedelta:
    days: int = ...
    delta: int = ...
    def __init__(
        self: _S,
        value: Union[_S, timedelta, timedelta64, str, int],
        unit: Optional[str] = ...,
        **kwargs
    ): ...
    def __mul__(self: _S, other: _NUMBER) -> _S: ...
    def __rmul__(self: _S, other: _NUMBER) -> _S: ...
    def __add__(self: _S, other: _S) -> _S: ...
    def __sub__(self: _S, other: _S) -> _S: ...
    def __lt__(self: _S, other: _S) -> bool: ...

_TS = TypeVar("_TS", bound="Timestamp")

class Timestamp(object):
    min: "Timestamp" = ...
    max: "Timestamp" = ...
    def __new__(
        cls: Type[_S],
        ts_input: Union[_S, datetime, str, int, float, None] = ...,
        freq: Optional[str] = ...,
        tz: Any = ...,
        unit: Any = ...,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
        hour: Optional[int] = ...,
        minute: Optional[int] = ...,
        second: Optional[int] = ...,
        microsecond: Optional[int] = ...,
        nanosecond: Optional[int] = ...,
        tzinfo: Any = ...,
    ) -> _S: ...
    @property
    def year(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def day(self) -> int: ...
    @property
    def hour(self) -> int: ...
    @property
    def minute(self) -> int: ...
    @property
    def second(self) -> int: ...
    def __add__(self: _TS, other: Timedelta) -> _TS: ...
    def __radd__(self: _TS, other: Timedelta) -> _TS: ...
    @overload
    def __sub__(self: _TS, other: Timedelta) -> _TS: ...
    @overload
    def __sub__(self: _TS, other: _TS) -> Timedelta: ...
    @overload
    def __sub__(self, other: datetime) -> Timedelta: ...
    @overload
    def __rsub__(self: _TS, other: _TS) -> Timedelta: ...
    @overload
    def __rsub__(self, other: datetime) -> Timedelta: ...
    def __le__(self: _S, other: _S) -> bool: ...
    def __ge__(self: _S, other: _S) -> bool: ...
    def __lt__(self: _S, other: _S) -> bool: ...
    def __gt__(self: _S, other: _S) -> bool: ...
    @classmethod
    def now(cls: Type[_S], tz: Any = ...) -> _S: ...
    def to_pydatetime(self) -> datetime: ...
    def strftime(self, str) -> str: ...
    def normalize(self: _S) -> _S: ...
    def date(self) -> date: ...

###
def concat(
    objs: Any,
    axis: int = ...,
    join: str = ...,
    join_axes: Optional[Any] = ...,
    ignore_index: bool = ...,
    keys: Optional[Any] = ...,
    levels: Optional[Any] = ...,
    names: Optional[Any] = ...,
    verify_integrity: bool = ...,
    sort: Optional[Any] = ...,
    copy: bool = ...,
) -> DataFrame: ...
@overload
def notnull(obj: Series) -> Series: ...
@overload
def notnull(obj: DataFrame) -> DataFrame: ...
@overload
def notnull(obj: Union[List, ndarray]) -> ndarray: ...
@overload
def notnull(obj: Union[generic, float, str, bool, None]) -> bool: ...
@overload
def isnull(obj: Series) -> Series: ...
@overload
def isnull(obj: DataFrame) -> DataFrame: ...
@overload
def isnull(obj: Union[List, ndarray]) -> ndarray: ...
@overload
def isnull(obj: Union[generic, float, str, bool, None]) -> bool: ...
@overload
def notna(obj: Series) -> Series: ...
@overload
def notna(obj: DataFrame) -> DataFrame: ...
@overload
def notna(obj: Union[List, ndarray]) -> ndarray: ...
@overload
def notna(obj: Union[generic, float, str, bool, None]) -> bool: ...
@overload
def isna(obj: Series) -> Series: ...
@overload
def isna(obj: DataFrame) -> DataFrame: ...
@overload
def isna(obj: Union[List, ndarray]) -> ndarray: ...
@overload
def isna(obj: Union[generic, float, str, bool, None]) -> bool: ...
def read_csv(
    filepath_or_buffer,
    sep=",",
    delimiter=None,
    header="infer",
    names=None,
    index_col=None,
    usecols=None,
    squeeze=False,
    prefix=None,
    mangle_dupe_cols=True,
    dtype=None,
    engine=None,
    converters=None,
    true_values=None,
    false_values=None,
    skipinitialspace=False,
    skiprows=None,
    skipfooter=0,
    nrows=None,
    na_values=None,
    keep_default_na=True,
    na_filter=True,
    verbose=False,
    skip_blank_lines=True,
    parse_dates=False,
    infer_datetime_format=False,
    keep_date_col=False,
    date_parser=None,
    dayfirst=False,
    iterator=False,
    chunksize=None,
    compression="infer",
    thousands=None,
    decimal=b".",
    lineterminator=None,
    quotechar='"',
    quoting=0,
    doublequote=True,
    escapechar=None,
    comment=None,
    encoding=None,
    dialect=None,
    tupleize_cols=None,
    error_bad_lines=True,
    warn_bad_lines=True,
    delim_whitespace=False,
    low_memory=True,
    memory_map=False,
    float_precision=None,
) -> DataFrame: ...
@overload
def to_numeric(
    args: Series,
    errors: str = ...,
    downcast: Optional[str] = ...,
) -> Series: ...
@overload
def to_numeric(
    args: Union[_NUMBER, List, Tuple, ndarray],
    errors: str = ...,
    downcast: Optional[str] = ...,
) -> ndarray: ...

class Index(Sequence[_VT]):
    @overload
    def map(self: _S, mapping: Mapping[_KT, _VT]) -> Sequence[_VT]: ...
    @overload
    def map(self: _S, mapping: Callable[[_KT], _VT]) -> Sequence[_VT]: ...
    @property
    def values(self) -> ndarray: ...
    def get_values(self) -> ndarray: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: Any): ...

class DatetimeIndex(Sequence[Timestamp]):
    timetuple: Any = ...
    freq: Any = ...
    def __new__(
        cls,
        data: Optional[Any] = ...,
        freq: Optional[Any] = ...,
        start: Optional[Any] = ...,
        end: Optional[Any] = ...,
        periods: Optional[Any] = ...,
        tz: Optional[Any] = ...,
        normalize: bool = ...,
        closed: Optional[Any] = ...,
        ambiguous: str = ...,
        dayfirst: bool = ...,
        yearfirst: bool = ...,
        dtype: Optional[Any] = ...,
        copy: bool = ...,
        name: Optional[Any] = ...,
        verify_integrity: Optional[Any] = ...,
    ): ...
    def __array__(self, dtype: Optional[Any] = ...): ...
    @property
    def dtype(self): ...
    @property
    def tz(self): ...
    @tz.setter
    def tz(self, value: Any) -> None: ...
    tzinfo: Any = ...
    def __reduce__(self): ...
    def union(self, other: Any): ...
    def union_many(self, others: Any): ...
    def intersection(self, other: Any, sort: bool = ...): ...
    def to_series(
        self,
        keep_tz: Optional[Any] = ...,
        index: Optional[Any] = ...,
        name: Optional[Any] = ...,
    ): ...
    def snap(self, freq: str = ...): ...
    def join(
        self,
        other: Any,
        how: str = ...,
        level: Optional[Any] = ...,
        return_indexers: bool = ...,
        sort: bool = ...,
    ): ...
    def get_value(self, series: Any, key: Any): ...
    def get_value_maybe_box(self, series: Any, key: Any): ...
    def get_loc(
        self, key: Any, method: Optional[Any] = ..., tolerance: Optional[Any] = ...
    ): ...
    def slice_indexer(
        self,
        start: Optional[Any] = ...,
        end: Optional[Any] = ...,
        step: Optional[Any] = ...,
        kind: Optional[Any] = ...,
    ): ...
    is_normalized: Any = ...
    strftime: Any = ...
    @property
    def offset(self): ...
    @offset.setter
    def offset(self, value: Any) -> None: ...
    def searchsorted(
        self, value: Any, side: str = ..., sorter: Optional[Any] = ...
    ): ...
    def is_type_compatible(self, typ: Any): ...
    @property
    def inferred_type(self): ...
    @property
    def is_all_dates(self): ...
    def insert(self, loc: Any, item: Any): ...
    def delete(self, loc: Any): ...
    def indexer_at_time(self, time: Any, asof: bool = ...): ...
    def indexer_between_time(
        self,
        start_time: Any,
        end_time: Any,
        include_start: bool = ...,
        include_end: bool = ...,
    ): ...
    @overload
    def map(self, mapping: Mapping[_KT, _VT]) -> Index[_VT]: ...
    @overload
    def map(self, mapping: Callable[[_KT], _VT]) -> Index[_VT]: ...
    @property
    def values(self) -> ndarray: ...
    def get_values(self) -> ndarray: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: int) -> Timestamp: ...
    @overload
    def __getitem__(self: _S, key: slice) -> _S: ...

def date_range(
    start: Optional[Any] = ...,
    end: Optional[Any] = ...,
    periods: Optional[Any] = ...,
    freq: Optional[Any] = ...,
    tz: Optional[Any] = ...,
    normalize: bool = ...,
    name: Optional[Any] = ...,
    closed: Optional[Any] = ...,
    **kwargs: Any
) -> DatetimeIndex: ...
def to_datetime(
    arg: _S,
    errors: str = "raise",
    dayfirst: bool = False,
    yearfirst: bool = False,
    utc: Optional[bool] = None,
    format: Optional[str] = None,
    exact: bool = True,
    unit: Optional[str] = None,
    infer_datetime_format: bool = False,
    origin="unix",
    cache: bool = True,
) -> _S: ...
def pivot_table(
    data: DataFrame,
    values: Union[Hashable, NoneType, Sequence[Union[Hashable, NoneType]]] = ...,
    index: Union[Hashable, NoneType, Sequence[Union[Hashable, NoneType]]] = ...,
    columns: Union[Hashable, NoneType, Sequence[Union[Hashable, NoneType]]] = ...,
    aggfunc: Union[Callable, Dict, str, Iterable[Union[Callable, str]]] = ...,
    fill_value: Optional[float] = ...,
    margins: bool = ...,
    dropna: bool = ...,
    margins_name: str = ...,
    observed: bool = ...,
) -> DataFrame: ...
def pivot(
    data: DataFrame,
    index: Union[Hashable, NoneType, Sequence[Union[Hashable, NoneType]]] = ...,
    columns: Union[Hashable, NoneType, Sequence[Union[Hashable, NoneType]]] = ...,
    values: Union[Hashable, NoneType, Sequence[Union[Hashable, NoneType]]] = ...,
) -> DataFrame: ...
