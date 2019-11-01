# Stubs for pandas.errors (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class PerformanceWarning(Warning): ...
class UnsupportedFunctionCall(ValueError): ...
class UnsortedIndexError(KeyError): ...
class ParserError(ValueError): ...
class DtypeWarning(Warning): ...
class EmptyDataError(ValueError): ...
class ParserWarning(Warning): ...
class MergeError(ValueError): ...
class NullFrequencyError(ValueError): ...
class AccessorRegistrationWarning(Warning): ...

class AbstractMethodError(NotImplementedError):
    methodtype: Any = ...
    class_instance: Any = ...
    def __init__(self, class_instance: Any, methodtype: str = ...) -> None: ...
