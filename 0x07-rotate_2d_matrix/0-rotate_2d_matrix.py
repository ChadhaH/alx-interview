#!/usr/bin/python3
"""n x n 2D matrix rotation module
"""


def rotate_2d_matrix(matrix):
    """edits a n x n 2D matrix  in-place
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    row = len(matrix)
    col = len(matrix[0])
    if not all(map(lambda x: len(x) == col, matrix)):
        return
    cols, rows = 0, row - 1
    for i in range(col * row):
        if i % row == 0:
            matrix.append([])
        if rows == -1:
            rows = row - 1
            cols += 1
        matrix[-1].append(matrix[rows][cols])
        if cols == col - 1 and rows >= -1:
            matrix.pop(rows)
        rows -= 1
