# Stubs for pandas.io.pickle (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def to_pickle(
    obj: Any, path: Any, compression: str = ..., protocol: Any = ...
) -> None: ...
def read_pickle(path: Any, compression: str = ...): ...
