from typing import Callable, Generic, TypeVar
from typing_extensions import ParamSpec, TypeAlias, TypeVarTuple, Unpack, reveal_type

T = TypeVar("T", default=int)
# T2 = TypeVar("T2", default=Callable[[T], int])
T3 = TypeVar("T3", default=T)
# T4 = TypeVar("T4", default=T3 | T)

# class Foop(Generic[T, T3, T4]): ...

# reveal_type(Foop[str]())  # TODO should be Foop[str, T3=str, T4=str] not Foop[str, T3=str, T4=T=int | str]

# reveal_type(Foop())
# A = TypeVar("A")
# B = TypeVar("B")
# C = TypeVar("C", default=dict[A, B])
class Foo(Generic[T]):
    class Bar(Generic[T3]): ...

reveal_type(Foo[bool])
reveal_type(Foo[bool].Bar)
reveal_type(Foo[bool]())
reveal_type(Foo[bool]().Bar)
# reveal_type(Foo().Bar())

# reveal_type(Foo[int]())


# reveal_type(Foo)  # revealed type is type[__main__.Foo[T`1 = builtins.int, T2`2 = def (T`1 = builtins.int) -> builtins.int]]
# reveal_type(Foo[str])  # revealed type is type[__main__.Foo[builtins.str, T2`2 = def (builtins.str) -> builtins.int]]
# reveal_type(Foo[str, int])  # revealed type is type[__main__.Foo[builtins.str, int]]

# PreSpecialised: TypeAlias = Foo[str]
# # reveal_type(PreSpecialised)    # revealed type is type[__main__.Foo[builtins.str, T2`2 = def (builtins.str) -> builtins.int]]
# reveal_type(PreSpecialised[int])  # borked

# P = ParamSpec("P", default=(int, str))
# P2 = ParamSpec("P2", default=P)

# class Bar(Generic[P, P2]): ...

# reveal_type(Bar[(int,)])
# def foo(fn: Callable[P, int]) -> bool: ...
# reveal_type(foo)  # revealed type is def [P = [builtins.int, builtins.str]] (fn: def (*P.args, **P.kwargs) -> builtins.int) -> builtins.bool
# reveal_type(Bar)  # revealed type is type[__main__.Bar[P`3 = [builtins.int, builtins.str], P2`4 = P`3 = [builtins.int, builtins.str]]]
