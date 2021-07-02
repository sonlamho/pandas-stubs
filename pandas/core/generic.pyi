# Stubs for pandas.core.generic (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.core.base import PandasObject, SelectionMixin
from typing import Any, Optional, TypeVar, Iterator
from numpy import ndarray

sentinel: Any

_S = TypeVar("_S")

class NDFrame(PandasObject, SelectionMixin):
    timetuple: Any = ...
    def __init__(
        self,
        data: Any,
        axes: Optional[Any] = ...,
        copy: bool = ...,
        dtype: Optional[Any] = ...,
        fastpath: bool = ...,
    ) -> None: ...
    @property
    def is_copy(self): ...
    @is_copy.setter
    def is_copy(self, msg: Any) -> None: ...
    @property
    def shape(self): ...
    @property
    def axes(self): ...
    @property
    def ndim(self): ...
    @property
    def size(self): ...
    def set_axis(self, labels: Any, axis: int = ..., inplace: Optional[Any] = ...): ...
    def transpose(self, *args: Any, **kwargs: Any): ...
    def swapaxes(self, axis1: Any, axis2: Any, copy: bool = ...): ...
    def droplevel(self, level: Any, axis: int = ...): ...
    def pop(self, item: Any): ...
    def squeeze(self, axis: Optional[Any] = ...): ...
    def rename_axis(self, mapper: Any = ..., **kwargs: Any): ...
    def equals(self, other: Any): ...
    def __neg__(self): ...
    def __pos__(self): ...
    def __invert__(self): ...
    def __nonzero__(self) -> None: ...
    __bool__: Any = ...
    def __abs__(self): ...
    def __round__(self, decimals: int = ...): ...
    def __hash__(self) -> int: ...
    def __iter__(self): ...
    def keys(self): ...
    def iteritems(self) -> Iterator: ...
    def __len__(self): ...
    def __contains__(self, key: Any): ...
    @property
    def empty(self): ...
    __array_priority__: int = ...
    def __array__(self, dtype: Optional[Any] = ...): ...
    def __array_wrap__(self, result: Any, context: Optional[Any] = ...): ...
    def to_dense(self): ...
    def __unicode__(self): ...
    def to_excel(
        self,
        excel_writer: Any,
        sheet_name: str = ...,
        na_rep: str = ...,
        float_format: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        header: bool = ...,
        index: bool = ...,
        index_label: Optional[Any] = ...,
        startrow: int = ...,
        startcol: int = ...,
        engine: Optional[Any] = ...,
        merge_cells: bool = ...,
        encoding: Optional[Any] = ...,
        inf_rep: str = ...,
        verbose: bool = ...,
        freeze_panes: Optional[Any] = ...,
    ) -> None: ...
    def to_json(
        self,
        path_or_buf: Optional[Any] = ...,
        orient: Optional[Any] = ...,
        date_format: Optional[Any] = ...,
        double_precision: int = ...,
        force_ascii: bool = ...,
        date_unit: str = ...,
        default_handler: Optional[Any] = ...,
        lines: bool = ...,
        compression: str = ...,
        index: bool = ...,
    ): ...
    def to_hdf(self, path_or_buf: Any, key: Any, **kwargs: Any): ...
    def to_msgpack(
        self, path_or_buf: Optional[Any] = ..., encoding: str = ..., **kwargs: Any
    ): ...
    def to_sql(
        self,
        name: Any,
        con: Any,
        schema: Optional[Any] = ...,
        if_exists: str = ...,
        index: bool = ...,
        index_label: Optional[Any] = ...,
        chunksize: Optional[Any] = ...,
        dtype: Optional[Any] = ...,
        method: Optional[Any] = ...,
    ) -> None: ...
    def to_pickle(self, path: Any, compression: str = ..., protocol: Any = ...): ...
    def to_clipboard(
        self, excel: bool = ..., sep: Optional[Any] = ..., **kwargs: Any
    ) -> None: ...
    def to_xarray(self): ...
    def to_latex(
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
        bold_rows: bool = ...,
        column_format: Optional[Any] = ...,
        longtable: Optional[Any] = ...,
        escape: Optional[Any] = ...,
        encoding: Optional[Any] = ...,
        decimal: str = ...,
        multicolumn: Optional[Any] = ...,
        multicolumn_format: Optional[Any] = ...,
        multirow: Optional[Any] = ...,
    ): ...
    def to_csv(
        self,
        path_or_buf: Optional[Any] = ...,
        sep: str = ...,
        na_rep: str = ...,
        float_format: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        header: bool = ...,
        index: bool = ...,
        index_label: Optional[Any] = ...,
        mode: str = ...,
        encoding: Optional[Any] = ...,
        compression: str = ...,
        quoting: Optional[Any] = ...,
        quotechar: str = ...,
        line_terminator: Optional[Any] = ...,
        chunksize: Optional[Any] = ...,
        tupleize_cols: Optional[Any] = ...,
        date_format: Optional[Any] = ...,
        doublequote: bool = ...,
        escapechar: Optional[Any] = ...,
        decimal: str = ...,
    ): ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def __getitem__(self, item: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def take(
        self,
        indices: Any,
        axis: int = ...,
        convert: Optional[Any] = ...,
        is_copy: bool = ...,
        **kwargs: Any
    ): ...
    def xs(
        self,
        key: Any,
        axis: int = ...,
        level: Optional[Any] = ...,
        drop_level: bool = ...,
    ): ...
    def select(self, crit: Any, axis: int = ...): ...
    def reindex_like(
        self,
        other: Any,
        method: Optional[Any] = ...,
        copy: bool = ...,
        limit: Optional[Any] = ...,
        tolerance: Optional[Any] = ...,
    ): ...
    def drop(
        self,
        labels: Optional[Any] = ...,
        axis: int = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        level: Optional[Any] = ...,
        inplace: bool = ...,
        errors: str = ...,
    ): ...
    def add_prefix(self: _S, prefix: Any) -> _S: ...
    def add_suffix(self: _S, suffix: Any) -> _S: ...
    # def sort_values(self, by: Optional[Any] = ..., axis: int = ..., ascending: bool = ..., inplace: bool = ..., kind: str = ..., na_position: str = ...) -> None: ...
    def sort_index(
        self,
        axis: int = ...,
        level: Optional[Any] = ...,
        ascending: bool = ...,
        inplace: bool = ...,
        kind: str = ...,
        na_position: str = ...,
        sort_remaining: bool = ...,
    ): ...
    # def reindex(self, *args: Any, **kwargs: Any): ...
    def reindex_axis(
        self,
        labels: Any,
        axis: int = ...,
        method: Optional[Any] = ...,
        level: Optional[Any] = ...,
        copy: bool = ...,
        limit: Optional[Any] = ...,
        fill_value: Optional[Any] = ...,
    ): ...
    def filter(
        self,
        items: Optional[Any] = ...,
        like: Optional[Any] = ...,
        regex: Optional[Any] = ...,
        axis: Optional[Any] = ...,
    ): ...
    def head(self, n: int = ...): ...
    def tail(self, n: int = ...): ...
    def sample(
        self: _S,
        n: Optional[int] = ...,
        frac: Optional[float] = ...,
        replace: bool = ...,
        weights: Optional[Any] = ...,
        random_state: Optional[Any] = ...,
        axis: Optional[int] = ...,
    ) -> _S: ...
    def pipe(self, func: Any, *args: Any, **kwargs: Any): ...
    def __finalize__(self, other: Any, method: Optional[Any] = ..., **kwargs: Any): ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any): ...
    def as_matrix(self, columns: Optional[Any] = ...): ...
    @property
    def values(self) -> ndarray: ...
    def get_values(self) -> ndarray: ...
    def get_dtype_counts(self): ...
    def get_ftype_counts(self): ...
    @property
    def dtypes(self): ...
    @property
    def ftypes(self): ...
    def as_blocks(self, copy: bool = ...): ...
    @property
    def blocks(self): ...
    def astype(
        self, dtype: Any, copy: bool = ..., errors: str = ..., **kwargs: Any
    ): ...
    def copy(self: _S, deep: bool = ...) -> _S: ...
    def __copy__(self, deep: bool = ...): ...
    def __deepcopy__(self, memo: Optional[Any] = ...): ...
    def convert_objects(
        self,
        convert_dates: bool = ...,
        convert_numeric: bool = ...,
        convert_timedeltas: bool = ...,
        copy: bool = ...,
    ): ...
    def infer_objects(self): ...
    def fillna(
        self,
        value: Optional[Any] = ...,
        method: Optional[Any] = ...,
        axis: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        downcast: Optional[Any] = ...,
    ): ...
    def ffill(
        self,
        axis: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        downcast: Optional[Any] = ...,
    ): ...
    def bfill(
        self,
        axis: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        downcast: Optional[Any] = ...,
    ): ...
    def replace(
        self,
        to_replace: Optional[Any] = ...,
        value: Optional[Any] = ...,
        inplace: bool = ...,
        limit: Optional[Any] = ...,
        regex: bool = ...,
        method: str = ...,
    ): ...
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
    def asof(self, where: Any, subset: Optional[Any] = ...): ...
    def isna(self): ...
    def isnull(self): ...
    def notna(self): ...
    def notnull(self): ...
    def clip(
        self,
        lower: Optional[Any] = ...,
        upper: Optional[Any] = ...,
        axis: Optional[Any] = ...,
        inplace: bool = ...,
        *args: Any,
        **kwargs: Any
    ): ...
    def clip_upper(
        self, threshold: Any, axis: Optional[Any] = ..., inplace: bool = ...
    ): ...
    def clip_lower(
        self, threshold: Any, axis: Optional[Any] = ..., inplace: bool = ...
    ): ...
    def groupby(
        self,
        by: Optional[Any] = ...,
        axis: int = ...,
        level: Optional[Any] = ...,
        as_index: bool = ...,
        sort: bool = ...,
        group_keys: bool = ...,
        squeeze: bool = ...,
        observed: bool = ...,
        **kwargs: Any
    ): ...
    def asfreq(
        self,
        freq: Any,
        method: Optional[Any] = ...,
        how: Optional[Any] = ...,
        normalize: bool = ...,
        fill_value: Optional[Any] = ...,
    ): ...
    def at_time(self, time: Any, asof: bool = ..., axis: Optional[Any] = ...): ...
    def between_time(
        self,
        start_time: Any,
        end_time: Any,
        include_start: bool = ...,
        include_end: bool = ...,
        axis: Optional[Any] = ...,
    ): ...
    def resample(
        self,
        rule: Any,
        how: Optional[Any] = ...,
        axis: int = ...,
        fill_method: Optional[Any] = ...,
        closed: Optional[Any] = ...,
        label: Optional[Any] = ...,
        convention: str = ...,
        kind: Optional[Any] = ...,
        loffset: Optional[Any] = ...,
        limit: Optional[Any] = ...,
        base: int = ...,
        on: Optional[Any] = ...,
        level: Optional[Any] = ...,
    ): ...
    def first(self, offset: Any): ...
    def last(self, offset: Any): ...
    def rank(
        self,
        axis: int = ...,
        method: str = ...,
        numeric_only: Optional[Any] = ...,
        na_option: str = ...,
        ascending: bool = ...,
        pct: bool = ...,
    ): ...
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
    def where(
        self,
        cond: Any,
        other: Any = ...,
        inplace: bool = ...,
        axis: Optional[Any] = ...,
        level: Optional[Any] = ...,
        errors: str = ...,
        try_cast: bool = ...,
        raise_on_error: Optional[Any] = ...,
    ): ...
    def mask(
        self,
        cond: Any,
        other: Any = ...,
        inplace: bool = ...,
        axis: Optional[Any] = ...,
        level: Optional[Any] = ...,
        errors: str = ...,
        try_cast: bool = ...,
        raise_on_error: Optional[Any] = ...,
    ): ...
    def shift(
        self,
        periods: int = ...,
        freq: Optional[Any] = ...,
        axis: int = ...,
        fill_value: Optional[Any] = ...,
    ): ...
    def slice_shift(self, periods: int = ..., axis: int = ...): ...
    def tshift(
        self, periods: int = ..., freq: Optional[Any] = ..., axis: int = ...
    ): ...
    def truncate(
        self,
        before: Optional[Any] = ...,
        after: Optional[Any] = ...,
        axis: Optional[Any] = ...,
        copy: bool = ...,
    ): ...
    def tz_convert(
        self, tz: Any, axis: int = ..., level: Optional[Any] = ..., copy: bool = ...
    ): ...
    def tz_localize(
        self,
        tz: Any,
        axis: int = ...,
        level: Optional[Any] = ...,
        copy: bool = ...,
        ambiguous: str = ...,
        nonexistent: str = ...,
    ): ...
    def abs(self): ...
    def describe(
        self,
        percentiles: Optional[Any] = ...,
        include: Optional[Any] = ...,
        exclude: Optional[Any] = ...,
    ): ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: str = ...,
        limit: Optional[Any] = ...,
        freq: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    def transform(self, func: Any, *args: Any, **kwargs: Any): ...
    def first_valid_index(self): ...
    def last_valid_index(self): ...
