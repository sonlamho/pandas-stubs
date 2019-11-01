# Stubs for pandas.io.msgpack (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.io.msgpack.exceptions import *
from pandas.io.msgpack._unpacker import unpack, unpackb
from typing import Any

class ExtType:
    def __new__(cls, code: Any, data: Any): ...

def pack(o: Any, stream: Any, **kwargs: Any) -> None: ...
def packb(o: Any, **kwargs: Any): ...
load = unpack
loads = unpackb
dump = pack
dumps = packb
