# Stubs for pandas.core.computation.scope (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pandas.core.base import StringMixin
from typing import Any, Optional

class Scope(StringMixin):
    level: Any = ...
    scope: Any = ...
    target: Any = ...
    resolvers: Any = ...
    temps: Any = ...
    def __init__(
        self,
        level: Any,
        global_dict: Optional[Any] = ...,
        local_dict: Optional[Any] = ...,
        resolvers: Any = ...,
        target: Optional[Any] = ...,
    ) -> None: ...
    def __unicode__(self): ...
    @property
    def has_resolvers(self): ...
    def resolve(self, key: Any, is_local: Any): ...
    def swapkey(
        self, old_key: Any, new_key: Any, new_value: Optional[Any] = ...
    ) -> None: ...
    def update(self, level: Any) -> None: ...
    def add_tmp(self, value: Any): ...
    @property
    def ntemps(self): ...
    @property
    def full_scope(self): ...
