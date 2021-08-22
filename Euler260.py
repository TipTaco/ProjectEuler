# Project Euler Question 260:
# Stones Game. Find and Sum all the Losing positions (n, n, n)
# Adrian Shedley, 22 August 2021
import numpy as np


EMPTY = 0
WIN = 1
LOSS = 2


def fill_game_board(size):

    # Start with two dimensions

    board = np.zeros((size, size, size), dtype=np.uint8)

    # Initial Conditions
    board[(0, 0, 0)] = LOSS
    fill_vectors((0, 0, 0), board, WIN)

    for shell_size in range(1, size):
        if shell_size % 10 == 0:
            print(shell_size)

        # Iterate over 3 faces of an expanding cube, this does overlap some work at the face intersections..
        for z in range(0, shell_size + 1):
            if z == shell_size:
                for y in range(0, shell_size + 1):
                    for x in range(0, shell_size + 1):
                        check_and_fill_cell(board, (x, y, z))
            else:
                for k in range(0, shell_size + 1):
                    check_and_fill_cell(board, (shell_size, k, z))
                    check_and_fill_cell(board, (k, shell_size, z))

    return board


def check_and_fill_cell(board, position):
    if board[position] == EMPTY:
        board[position] = LOSS
        fill_vectors(position, board, WIN)


def fill_vectors(start, board, val):

    vectors = [(0, 0, 1), (0, 1, 0), (1, 0, 0),
               (0, 1, 1), (1, 1, 0), (1, 0, 1),
               (1, 1, 1)]

    for v in vectors:
        fill_vector(start, board, v, val)


def fill_vector(start, board, vector, val):
    size = board.shape[0]

    x_index = vector[0] == 1
    y_index = vector[1] == 1
    z_index = vector[2] == 1

    xs = np.arange(start[0] + 1, size, 1) if x_index else start[0]
    ys = np.arange(start[1] + 1, size, 1) if y_index else start[1]
    zs = np.arange(start[2] + 1, size, 1) if z_index else start[2]

    slice_max = np.min([len(xs) if x_index else size,
                        len(ys) if y_index else size,
                        len(zs) if z_index else size])

    xs = xs[:slice_max] if x_index else xs
    ys = ys[:slice_max] if y_index else ys
    zs = zs[:slice_max] if z_index else zs

    board[xs, ys, zs] = val


if __name__ == "__main__":

    size = 100 + 1

    board = fill_game_board(size)

    losses = np.argwhere(board == LOSS)
    losses.sort()  # Organise each of the triples

    counts = {}
    for loss in losses:
        key = str(loss)
        current_val = counts.get(key, 0)
        counts[key] = max(np.sum(loss), current_val)

    print(f"Sum of all losing positions {np.sum([v for v in counts.values()])}")

