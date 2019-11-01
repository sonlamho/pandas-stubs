
from typing import overload
from pandas import Timestamp
from datetime import datetime

class BaseOffset:

  def __init__(self, n:int=..., normalize:bool=...): ...

  @overload
  def __add__(self, other: Timestamp) -> Timestamp: ...

  @overload
  def __add__(self, other: datetime) -> Timestamp: ...

  @overload
  def __rsub__(self, other: Timestamp) -> Timestamp: ...

  @overload
  def __rsub__(self, other: datetime) -> Timestamp: ...

  def __mul__(self, other: float) -> BaseOffset: ...

class _Tick(object):
  ...
