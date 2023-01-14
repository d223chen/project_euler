import itertools

import numpy as np
import pandas as pd


def DFS(grid: np.array, x: int, y: int, path_length: int, acc: int, xd: int, yd: int) -> int:
    """Returns product path starting at x,y in grid moving in direction (xd, yd). path_length and acc are accumulator variables which should be initialized to 0 and 1 respectively at top level."""
    print(x, y, path_length, acc)
    if x < 0 or x >= grid.shape[0] or y < 0 or y >= grid.shape[0]:
        return -1

    if path_length == 3:
        return acc * grid[y][x]

    val = grid[y][x]
    search = DFS(grid, x + xd, y + yd, path_length + 1, acc * val, xd, yd)

    return search


def solve(grid: np.array) -> int:
    result = 0
    for y in range(grid.shape[1]):
        for x in range(grid.shape[0]):
            searches = max(
                [
                    DFS(grid, x, y, 0, 1, xd, yd)
                    for xd, yd in itertools.product((-1, 0, 1), (-1, 0, 1))
                    if not (xd == 0 and yd == 0)
                ]
            )
            result = max(result, searches)

    return result


def load_grid(path: str) -> np.array:
    df = pd.read_csv(path, delimiter=" ", header=None)
    grid = df.values
    return grid


if __name__ == "__main__":
    grid = load_grid("11.txt")
    result = solve(grid)
    print(result)

### pytests, run with


def test_DFS():
    grid = load_grid("11_test.txt")
    result = DFS(
        grid, 3, 0, 0, 1, 0, 1
    )  # start from top right corner and going straight down should yield maximal path.
    assert result == 16


def test_solve():
    grid = load_grid("11_test.txt")
    result = solve(grid)
    assert result == 16
