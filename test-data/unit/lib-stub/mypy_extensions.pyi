# NOTE: Requires fixtures/dict.pyi
from typing import Dict, Type, TypeVar, Optional, Any, Generic, Mapping, NoReturn
import sys

_T = TypeVar('_T')
_U = TypeVar('_U')


def Arg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def DefaultArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def NamedArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def DefaultNamedArg(type: _T = ..., name: Optional[str] = ...) -> _T: ...

def VarArg(type: _T = ...) -> _T: ...

def KwArg(type: _T = ...) -> _T: ...


# Fallback type for all typed dicts (does not exist at runtime)
class _TypedDict(Mapping[str, object]):
    def copy(self: _T) -> _T: ...
    # Using NoReturn so that only calls using the plugin hook can go through.
    def setdefault(self, k: NoReturn, default: object) -> object: ...
    # Mypy expects that 'default' has a type variable type
    def pop(self, k: NoReturn, default: _T = ...) -> object: ...
    def update(self: _T, __m: _T) -> None: ...
    if sys.version_info < (3, 0):
        def has_key(self, k: str) -> bool: ...
    def __delitem__(self, k: NoReturn) -> None: ...

def TypedDict(typename: str, fields: Dict[str, Type[_T]], *, total: Any = ...) -> Type[dict]: ...

# This is intended as a class decorator, but mypy rejects abstract classes
# when a Type[_T] is expected, so we can't give it the type we want
def trait(cls: Any) -> Any: ...

class NoReturn: pass

class FlexibleAlias(Generic[_T, _U]): ...
