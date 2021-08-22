# Project Euler Question 13:
# First 10 Digits of the sum of 100x 50 digit numbers
# Adrian Shedley, 22 August 2021
from typing import List
import pandas as pd
import numpy as np


def load_numbers() -> List[str]:
    # Import all the data as strings so we can sum the digits
    return pd.read_csv("./Euler13.csv")["Data"].values


def first_n_digit_sum(numbers: List[str], n: int = 10) -> str:
    # This could be considered cheating, but python will handle these numbers as a whole
    # The method here will worth without an implementation for arbitrarily long numbers

    digits = []
    remainder = 0

    index = 1
    more_digits = True

    while more_digits:
        partials = [int(num_str[-index]) for num_str in numbers if index <= len(num_str)]
        more_digits = len(partials) != 0 or remainder != 0
        index += 1

        if more_digits:
            partials_sum = np.sum(partials).astype(int) + remainder

            digits.insert(0, str(partials_sum % 10))  # Insert the last of the remainder at the start of the digits list
            remainder = partials_sum // 10

    return ("".join(digits))[0:n]


if __name__ == "__main__":

    real_data = load_numbers()
    test_data = ["1001", "2002", "4004", "8008"]

    print(first_n_digit_sum(real_data, 10))
