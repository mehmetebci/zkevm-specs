from typing import NewType, Sequence, List, Tuple

U256 = NewType("U256", int)
U8 = NewType("U8", int)


def is_circuit_code(func):
    def wrapper():
        func()
    return wrapper


def u256_to_u8s(x: U256) -> Tuple[U8, ...]:
    assert 0 <= x < 2**256, "expect x is unsigned 256 bits"
    return tuple((x >> 8*i) & 0xff for i in range(32))


def u8s_to_u256(xs: Sequence[U8]) -> U256:
    assert len(xs) == 32
    for u8 in xs:
        assert 0 <= u8 <= 255
    return sum(x * (2**(8*i)) for i, x in enumerate(xs))
