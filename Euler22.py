# Project Euler Question 22:
# Alphabetical Name Scoring
# Adrian Shedley, 22 August 2021
from typing import List
import numpy as np


def load_data() -> List[str]:
    with open("./Euler22.txt") as fp:
        data = fp.read()

    data = data.replace('"', "")
    return data.split(",")


def alphabet_value(word: str) -> int:
    return np.sum([ord(letter.upper()) - 64 for letter in word])


if __name__ == "__main__":

    names = load_data()
    names.sort()
    print(names)

    alpha_values = [(i+1) * alphabet_value(name) for i, name in enumerate(names)]

    print(alpha_values)

    print(f"All names worth {np.sum(alpha_values)}")