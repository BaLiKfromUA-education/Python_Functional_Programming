from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def fibonacci(num: int, prev_val: int = 0, next_val: int = 1, step: int = 0) -> int:
        if step == num:
            return prev_val

        return fibonacci(num, next_val, prev_val + next_val, step + 1)

    return fibonacci
