
from typing import overload, Union
from pandas import Timestamp
from datetime import datetime

_ANYDATETIME = Union[datetime, Timestamp]

class BaseOffset(object):

  def __init__(self, n:int=..., normalize:bool=...): ...

  def __add__(self, other: _ANYDATETIME) -> Timestamp: ...

  def __rsub__(self, other: _ANYDATETIME) -> Timestamp: ...

  def __mul__(self, other: float) -> BaseOffset: ...

class _Tick(object):
  ...
