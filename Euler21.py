# Project Euler Question 21:
# Amicable numbers
# Adrian Shedley, 22 August 2021
from typing import List
import numpy as np


def get_proper_divisors(number: int) -> List[int]:
    divisors = []
    for n in range(1, np.sqrt(number).astype(np.int) + 1):
        if n == 1:
            divisors.append(n)
        else:
            if number % n == 0:
                if number / n == n:
                    divisors.append(n)
                else:
                    divisors += [n, number//n]

    return divisors


def is_amicable(number: int) -> bool:

    sum_divisors = np.sum(get_proper_divisors(number))

    if sum_divisors == number:
        return False
    else:
        return np.sum(get_proper_divisors(sum_divisors)) == number


if __name__ == "__main__":

    amicables = [ia for ia in range(0, 10000) if is_amicable(ia)]
    print(amicables)
    print(np.sum(amicables))