# Stubs for pandas.core.arrays.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import numpy as np
from typing import Any, Optional

class ExtensionArray:
    def __getitem__(self, item: Any) -> None: ...
    def __setitem__(self, key: Union[int, np.ndarray], value: Any) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> None: ...
    @property
    def dtype(self) -> ExtensionDtype: ...
    @property
    def shape(self) -> Tuple[int, ...]: ...
    @property
    def ndim(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    def astype(self, dtype: Any, copy: bool = ...): ...
    def isna(self) -> Union[ExtensionArray, np.ndarray]: ...
    def argsort(self, ascending: bool = ..., kind: str = ..., *args: Any, **kwargs: Any): ...
    def fillna(self, value: Optional[Any] = ..., method: Optional[Any] = ..., limit: Optional[Any] = ...): ...
    def dropna(self): ...
    def shift(self, periods: int=..., fill_value: object=...) -> ExtensionArray: ...
    def unique(self): ...
    def searchsorted(self, value: Any, side: str = ..., sorter: Optional[Any] = ...): ...
    def factorize(self, na_sentinel: int=...) -> Tuple[ndarray, ExtensionArray]: ...
    def repeat(self, repeats: Any, axis: Optional[Any] = ...): ...
    def take(self, indices: Sequence[int], allow_fill: bool=..., fill_value: Optional[Any]=...) -> ExtensionArray: ...
    def copy(self, deep: bool=...) -> ExtensionArray: ...

class ExtensionOpsMixin: ...
class ExtensionScalarOpsMixin(ExtensionOpsMixin): ...