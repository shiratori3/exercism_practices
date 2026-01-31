import numpy as np


def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    if not matrix:
        return []

    heigth = len(matrix)
    width = len(matrix[0])
    if not all(True if len(row) == width else False for row in matrix):
        raise ValueError("irregular matrix")

    tuple_row, tuple_col = set(), set()
    for h in range(heigth):
        row = matrix[h]
        max_row = max(row)
        for w in range(width):
            if row[w] == max_row:
                tuple_row.add((h + 1, w + 1))
    for w in range(width):
        col = [matrix[_][w] for _ in range(heigth)]
        min_col = min(col)
        for h in range(heigth):
            if col[h] == min_col:
                tuple_col.add((h + 1, w + 1))

    res = tuple_row.intersection(tuple_col)
    if not res:
        return []
    else:
        keys = ["row", "column"]
        return [dict(zip(keys, t)) for t in res]

