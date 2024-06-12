#!/usr/bin/python3
"""
    a module to compute an island perimeter
"""


def island_perimeter(grid):
    """
        it computes the perimeter of an island
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    p = len(grid)
    for k, row in enumerate(grid):
        p = len(row)
        for v, cell in enumerate(row):
            if cell == 0:
                continue
            edge = (
                k == 0 or (len(grid[k - 1]) > v and grid[k - 1][v] == 0),
                v == m - 1 or (m > v + 1 and row[v + 1] == 0),
                k == p - 1 or (len(grid[k + 1]) > v and grid[k + 1][v] == 0),
                v == 0 or row[v - 1] == 0,
            )
            perimeter += sum(edge)
    return perimeter
