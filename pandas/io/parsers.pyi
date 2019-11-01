# Stubs for pandas.io.parsers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.io.common import BaseIterator
from typing import Any, Optional

read_csv: Any
read_table: Any

def read_fwf(filepath_or_buffer: Any, colspecs: str = ..., widths: Optional[Any] = ..., infer_nrows: int = ..., **kwds: Any): ...

class TextFileReader(BaseIterator):
    f: Any = ...
    orig_options: Any = ...
    engine: Any = ...
    chunksize: Any = ...
    nrows: Any = ...
    squeeze: Any = ...
    def __init__(self, f: Any, engine: Optional[Any] = ..., **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def __next__(self): ...
    def read(self, nrows: Optional[Any] = ...): ...
    def get_chunk(self, size: Optional[Any] = ...): ...

class ParserBase:
    names: Any = ...
    orig_names: Any = ...
    prefix: Any = ...
    index_col: Any = ...
    unnamed_cols: Any = ...
    index_names: Any = ...
    col_names: Any = ...
    parse_dates: Any = ...
    date_parser: Any = ...
    dayfirst: Any = ...
    keep_date_col: Any = ...
    na_values: Any = ...
    na_fvalues: Any = ...
    na_filter: Any = ...
    keep_default_na: Any = ...
    true_values: Any = ...
    false_values: Any = ...
    tupleize_cols: Any = ...
    mangle_dupe_cols: Any = ...
    infer_datetime_format: Any = ...
    header: Any = ...
    handles: Any = ...
    def __init__(self, kwds: Any) -> None: ...
    def close(self) -> None: ...

class CParserWrapper(ParserBase):
    kwds: Any = ...
    unnamed_cols: Any = ...
    names: Any = ...
    orig_names: Any = ...
    index_names: Any = ...
    def __init__(self, src: Any, **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def set_error_bad_lines(self, status: Any) -> None: ...
    def read(self, nrows: Optional[Any] = ...): ...

def TextParser(*args: Any, **kwds: Any): ...
def count_empty_vals(vals: Any): ...

class PythonParser(ParserBase):
    data: Any = ...
    buf: Any = ...
    pos: int = ...
    line_pos: int = ...
    encoding: Any = ...
    compression: Any = ...
    memory_map: Any = ...
    skiprows: Any = ...
    skipfunc: Any = ...
    skipfooter: Any = ...
    delimiter: Any = ...
    quotechar: Any = ...
    escapechar: Any = ...
    doublequote: Any = ...
    skipinitialspace: Any = ...
    lineterminator: Any = ...
    quoting: Any = ...
    skip_blank_lines: Any = ...
    warn_bad_lines: Any = ...
    error_bad_lines: Any = ...
    names_passed: Any = ...
    has_index_names: bool = ...
    verbose: Any = ...
    converters: Any = ...
    dtype: Any = ...
    thousands: Any = ...
    decimal: Any = ...
    comment: Any = ...
    num_original_columns: Any = ...
    columns: Any = ...
    orig_names: Any = ...
    index_names: Any = ...
    nonnum: Any = ...
    def __init__(self, f: Any, **kwds: Any) -> None: ...
    def read(self, rows: Optional[Any] = ...): ...
    def get_chunk(self, size: Optional[Any] = ...): ...

class FixedWidthReader(BaseIterator):
    f: Any = ...
    buffer: Any = ...
    delimiter: Any = ...
    comment: Any = ...
    colspecs: Any = ...
    def __init__(self, f: Any, colspecs: Any, delimiter: Any, comment: Any, skiprows: Optional[Any] = ..., infer_nrows: int = ...) -> None: ...
    def get_rows(self, infer_nrows: Any, skiprows: Optional[Any] = ...): ...
    def detect_colspecs(self, infer_nrows: int = ..., skiprows: Optional[Any] = ...): ...
    def __next__(self): ...

class FixedWidthFieldParser(PythonParser):
    colspecs: Any = ...
    infer_nrows: Any = ...
    def __init__(self, f: Any, **kwds: Any) -> None: ...
