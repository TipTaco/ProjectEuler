# Project Euler Question 12:
# Number of factors in a triangular number
# Adrian Shedley, 22 August 2021

from typing import List
import numpy as np


def next_triangular_number(numbers: List[int]) -> List[int]:
    if numbers is None or len(numbers) == 0:
        return [1]
    else:
        numbers.append(numbers[-1] + len(numbers) + 1)
        return numbers


def get_triangular_number(tri_number: int, last_tri: int) -> int:
    return last_tri + tri_number + 1


def get_divisors(number: int) -> List[int]:
    divisors = []
    for n in range(1, np.sqrt(number).astype(np.int) + 1):
        if number % n == 0:
            if number / n == n:
                divisors.append(n)
            else:
                divisors += [n, number//n]

    return divisors

    # return [n+1 for n in range(sqrt(number)) if number % (n+1) == 0 or number % ]


def get_num_divisors(number: int) -> int:
    return len(get_divisors(number))


if __name__ == "__main__":

    target_num_divis = 500 + 1

    last_tri = 0
    num_divis = 0
    index = 0

    while num_divis < target_num_divis:
        last_tri = get_triangular_number(index, last_tri)
        divis = get_divisors(last_tri)
        num_divis = len(divis)

        if num_divis >= target_num_divis:
            print(f"[T:{index+1}] {last_tri} => (#{num_divis}){divis}")
        elif index % 100 == 0:
            print(f"processed: {index}")
        index += 1
