from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    before = Integer(1)
    after_1 = increment_fn(before)
    after_2 = increment_fn(before)
    return before.value == 1 and (after_1 is not after_2) and (after_1.value == after_2.value)
