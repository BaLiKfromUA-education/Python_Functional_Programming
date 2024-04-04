from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


def factorial_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def factorial(num: int, result: int = 1):
        if num <= 1:
            return result

        return factorial(num - 1, result * num)

    return factorial
