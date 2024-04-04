from math import ceil, sqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    def check_all_factors(factor: int):
        if factor == 1:
            return True

        return n % factor != 0 and check_all_factors(factor - 1)

    return check_all_factors(ceil(sqrt(n)))
