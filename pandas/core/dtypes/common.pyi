# Stubs for pandas.core.dtypes.common (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

ensure_float64: Any
ensure_float32: Any

def ensure_float(arr: Any): ...

ensure_uint64: Any
ensure_int64: Any
ensure_int32: Any
ensure_int16: Any
ensure_int8: Any
ensure_platform_int: Any
ensure_object: Any

def ensure_categorical(arr: Any): ...
def ensure_int64_or_float64(arr: Any, copy: bool = ...): ...
def classes(*klasses: Any): ...
def classes_and_not_datetimelike(*klasses: Any): ...
def is_object_dtype(arr_or_dtype: Any): ...
def is_sparse(arr: Any): ...
def is_scipy_sparse(arr: Any): ...
def is_categorical(arr: Any): ...
def is_datetimetz(arr: Any): ...
def is_offsetlike(arr_or_obj: Any): ...
def is_period(arr: Any): ...
def is_datetime64_dtype(arr_or_dtype: Any): ...
def is_datetime64tz_dtype(arr_or_dtype: Any): ...
def is_timedelta64_dtype(arr_or_dtype: Any): ...
def is_period_dtype(arr_or_dtype: Any): ...
def is_interval_dtype(arr_or_dtype: Any): ...
def is_categorical_dtype(arr_or_dtype: Any): ...
def is_string_dtype(arr_or_dtype: Any): ...
def is_period_arraylike(arr: Any): ...
def is_datetime_arraylike(arr: Any): ...
def is_datetimelike(arr: Any): ...
def is_dtype_equal(source: Any, target: Any): ...
def is_dtype_union_equal(source: Any, target: Any): ...
def is_any_int_dtype(arr_or_dtype: Any): ...
def is_integer_dtype(arr_or_dtype: Any): ...
def is_signed_integer_dtype(arr_or_dtype: Any): ...
def is_unsigned_integer_dtype(arr_or_dtype: Any): ...
def is_int64_dtype(arr_or_dtype: Any): ...
def is_datetime64_any_dtype(arr_or_dtype: Any): ...
def is_datetime64_ns_dtype(arr_or_dtype: Any): ...
def is_timedelta64_ns_dtype(arr_or_dtype: Any): ...
def is_datetime_or_timedelta_dtype(arr_or_dtype: Any): ...
def is_numeric_v_string_like(a: Any, b: Any): ...
def is_datetimelike_v_numeric(a: Any, b: Any): ...
def is_datetimelike_v_object(a: Any, b: Any): ...
def needs_i8_conversion(arr_or_dtype: Any): ...
def is_numeric_dtype(arr_or_dtype: Any): ...
def is_string_like_dtype(arr_or_dtype: Any): ...
def is_float_dtype(arr_or_dtype: Any): ...
def is_bool_dtype(arr_or_dtype: Any): ...
def is_extension_type(arr: Any): ...
def is_extension_array_dtype(arr_or_dtype: Any): ...
def is_complex_dtype(arr_or_dtype: Any): ...
def infer_dtype_from_object(dtype: Any): ...
def pandas_dtype(dtype: Any): ...
