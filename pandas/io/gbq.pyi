# Stubs for pandas.io.gbq (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def read_gbq(
    query: Any,
    project_id: Optional[Any] = ...,
    index_col: Optional[Any] = ...,
    col_order: Optional[Any] = ...,
    reauth: bool = ...,
    auth_local_webserver: bool = ...,
    dialect: Optional[Any] = ...,
    location: Optional[Any] = ...,
    configuration: Optional[Any] = ...,
    credentials: Optional[Any] = ...,
    private_key: Optional[Any] = ...,
    verbose: Optional[Any] = ...,
): ...
def to_gbq(
    dataframe: Any,
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
