# Stubs for pandas.io.parquet (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def get_engine(engine: Any): ...

class BaseImpl:
    api: Any = ...
    @staticmethod
    def validate_dataframe(df: Any) -> None: ...
    def write(self, df: Any, path: Any, compression: Any, **kwargs: Any) -> None: ...
    def read(self, path: Any, columns: Optional[Any] = ..., **kwargs: Any) -> None: ...

class PyArrowImpl(BaseImpl):
    api: Any = ...
    def __init__(self) -> None: ...
    def write(
        self,
        df: Any,
        path: Any,
        compression: str = ...,
        coerce_timestamps: str = ...,
        index: Optional[Any] = ...,
        partition_cols: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def read(self, path: Any, columns: Optional[Any] = ..., **kwargs: Any): ...

class FastParquetImpl(BaseImpl):
    api: Any = ...
    def __init__(self) -> None: ...
    def write(
        self,
        df: Any,
        path: Any,
        compression: str = ...,
        index: Optional[Any] = ...,
        partition_cols: Optional[Any] = ...,
        **kwargs: Any
    ): ...
    def read(self, path: Any, columns: Optional[Any] = ..., **kwargs: Any): ...

def to_parquet(
    df: Any,
    path: Any,
    engine: str = ...,
    compression: str = ...,
    index: Optional[Any] = ...,
    partition_cols: Optional[Any] = ...,
    **kwargs: Any
): ...
def read_parquet(
    path: Any, engine: str = ..., columns: Optional[Any] = ..., **kwargs: Any
): ...
