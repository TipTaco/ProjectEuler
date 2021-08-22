# Project Euler 215. wall stacking problem
# Adrian Shedley 7/8/21

from typing import List
import numpy as np


class Row:
    two_block = "01"
    three_block = "001"

    def __init__(self):
        self.contents: str = ""
        self.width: int = 0
        self.array: np.array = []
        self.neighbours: List['Row'] = []

        self.levels: List[int] = []

    def setup_levels(self, num_levels):
        self.levels = [0] * num_levels

    def get_level(self, level):
        return self.levels[level]

    def run_level(self, level: int):
        if level == 0:
            self.levels[0] = 1
        elif level == 1:
            self.levels[1] = len(self.neighbours)
        else:
            self.levels[level] = int(np.sum([n.levels[level - 1] for n in self.neighbours]))

    def append(self, block: str):
        self.contents += block
        self.array = np.array([int(ss) for ss in self.contents[:-1]])
        self.width += len(block)

    def copy(self) -> 'Row':
        row = Row()
        row.width = self.width
        row.contents = self.contents
        self.array = np.array([int(ss) for ss in self.contents[:-1]])
        return row

    def __str__(self):
        return f"({self.width}){self.contents}"

    @staticmethod
    def grow_tree(tree: List['Row']) -> List['Row']:
        new_tree: List['Row'] = []

        for node in tree:
            new_tree += Row.branch_tree(node)

        return new_tree

    @staticmethod
    def branch_tree(base: 'Row') -> List['Row']:
        left: Row = base.copy()
        left.append(Row.two_block)
        right: Row = base.copy()
        right.append(Row.three_block)

        return [left, right]

    @staticmethod
    def trim_tree(tree: List['Row'], max_length) -> (List['Row'], List['Row']):
        too_short = [t for t in tree if t.width < max_length]
        correct = [t for t in tree if t.width == max_length]
        return too_short, correct

    @staticmethod
    def get_all_rows(max_width) -> List['Row']:

        too_short = [Row()]
        correct = []

        while len(too_short) > 0:
            possibles = Row.grow_tree(too_short)
            too_short, new_confirmed = Row.trim_tree(possibles, max_width)
            correct += new_confirmed

        return correct


if __name__ == "__main__":

    width = 32
    height = 8

    # we are going to represent a wall as a
    base_rows = Row.get_all_rows(width)

    print(base_rows[0])

    good_rows = 0

    matches = np.zeros(len(base_rows))
    for i, row in enumerate(base_rows):
        print(f"Done row {i+1}/{len(base_rows)} {row}")
        for j, r in enumerate(base_rows):
            if np.max(r.array + row.array) == 1:
                row.neighbours.append(r)

    print("Generated rows")

    [row.setup_levels(height) for row in base_rows]

    for i in range(height):
        print(i)
        [row.run_level(i) for row in base_rows]

    print(f"Ans {np.sum([row.get_level(height-1) for row in base_rows])}")




    # def depth_first(row, depth):
    #     good_rows = 0
    #
    #     if depth == height:
    #         good_rows += 1
    #     else:
    #         for r in base_rows:
    #             if np.max(r.array + row.array) == 1:
    #                 good_rows += depth_first(r, depth+1)
    #
    #     return good_rows
    #
    # for i, r in enumerate(base_rows):
    #     good_rows += depth_first(r, 1)
    #     print(f"Done {i}/{len(base_rows)}")

    # print(good_rows)
