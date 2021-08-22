# Project Euler Question 18:
# Maximum sum down a triangle of integers
# Adrian Shedley, 22 August 2021
from typing import List
import numpy as np


def load_data() -> List[List[int]]:
    with open("./Euler18.csv") as fp:
        data = fp.read()

    return [[int(num) for num in line.split(" ")] for line in data.split("\n")]


def max_sum_down_triangle(input_tri) -> int:
    # In each position of the triangle, save the maximum possible at that point in the triangle
    # Triangle assumed to be increasing as row number increases

    triangle_size = len(data)
    last_layer_max = input_tri[-1]

    # Use the fact that the ith row has i elements
    for i in range(triangle_size - 2, -1, -1):

        layer_max = [input_tri[i][j] + max(last_layer_max[j], last_layer_max[j + 1]) for j in range(i+1)]
        last_layer_max = layer_max

    return last_layer_max[0]


if __name__ == "__main__":

    data = load_data()
    print(max_sum_down_triangle(data))