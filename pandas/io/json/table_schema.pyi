# Stubs for pandas.io.json.table_schema (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

loads: Any

def as_json_table_type(x: Any): ...
def set_default_names(data: Any): ...
def convert_pandas_type_to_json_field(arr: Any, dtype: Optional[Any] = ...): ...
def convert_json_field_to_pandas_type(field: Any): ...
def build_table_schema(
    data: Any, index: bool = ..., primary_key: Optional[Any] = ..., version: bool = ...
): ...
def parse_table_schema(json: Any, precise_float: Any): ...
