# Stubs for pandas.io.clipboard.exceptions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class PyperclipException(RuntimeError): ...

class PyperclipWindowsException(PyperclipException):
    def __init__(self, message: Any) -> None: ...
