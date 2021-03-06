# Stubs for pandas.io.sas.sas_xport (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.io.common import BaseIterator
from typing import Any, Optional

class XportReader(BaseIterator):
    __doc__: Any = ...
    filepath_or_buffer: Any = ...
    def __init__(
        self,
        filepath_or_buffer: Any,
        index: Optional[Any] = ...,
        encoding: str = ...,
        chunksize: Optional[Any] = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __next__(self): ...
    def get_chunk(self, size: Optional[Any] = ...): ...
    def read(self, nrows: Optional[Any] = ...): ...
