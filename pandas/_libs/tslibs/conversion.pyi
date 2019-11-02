

from datetime import datetime, date
from pandas import Timestamp
from typing import Optional, overload, Union

@overload
def localize_pydatetime(dt: datetime, tz: Optional[str]) -> datetime: ...

@overload
def localize_pydatetime(dt: Timestamp, tz: Optional[str]) -> Timestamp: ...

@overload
def normalize_date(dt: Union[datetime,date]) -> datetime: ...

@overload
def normalize_date(df: Timestamp) -> Timestamp: ...

def tz_convert_single(val:int, tz1:str, tz2:str) -> int: ...
