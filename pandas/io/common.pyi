# Stubs for pandas.io.common (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import zipfile
from pandas.compat import BytesIO
from pandas.errors import ParserError
from typing import Any, Optional

CParserError = ParserError

class BaseIterator:
    def __iter__(self): ...
    def __next__(self) -> None: ...

def is_s3_url(url: Any): ...
def is_gcs_url(url: Any): ...
def get_filepath_or_buffer(filepath_or_buffer: Any, encoding: Optional[Any] = ..., compression: Optional[Any] = ..., mode: Optional[Any] = ...): ...
def file_path_to_url(path: Any): ...

class BytesZipFile(zipfile.ZipFile, BytesIO):
    def __init__(self, file: Any, mode: Any, compression: Any = ..., **kwargs: Any) -> None: ...
    def write(self, data: Any) -> None: ...
    @property
    def closed(self): ...

class MMapWrapper(BaseIterator):
    mmap: Any = ...
    def __init__(self, f: Any) -> None: ...
    def __getattr__(self, name: Any): ...
    def __iter__(self): ...
    def __next__(self): ...

class UTF8Recoder(BaseIterator):
    reader: Any = ...
    def __init__(self, f: Any, encoding: Any) -> None: ...
    def read(self, bytes: int = ...): ...
    def readline(self): ...
    def next(self): ...

def UnicodeReader(f: Any, dialect: Any = ..., encoding: str = ..., **kwds: Any): ...
def UnicodeWriter(f: Any, dialect: Any = ..., encoding: str = ..., **kwds: Any): ...

class UnicodeReader(BaseIterator):
    reader: Any = ...
    def __init__(self, f: Any, dialect: Any = ..., encoding: str = ..., **kwds: Any) -> None: ...
    def __next__(self): ...

class UnicodeWriter:
    queue: Any = ...
    writer: Any = ...
    stream: Any = ...
    encoder: Any = ...
    quoting: Any = ...
    def __init__(self, f: Any, dialect: Any = ..., encoding: str = ..., **kwds: Any) -> None: ...
    def writerow(self, row: Any): ...
    def writerows(self, rows: Any): ...
