#!/usr/bin/python3
""" 0x00. Pascal's Triangle """


def pascal_triangle(n):
    """
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    pas_triangle = []

    if n <= 0:
        return pas_triangle

    for loop1 in range(n):
        row = []
        for loop2 in range(loop2 + 1):
            if loop2 == 0 or loop1 == loop2:
                row.append(1)
            elif loop1 > 0 and loop2 > 0:
                row.append(pas_triangle[loop1 - 1][loop2 - 1]
                           + pas_triangle[loop1 - 1][j])
        pas_triangle.append(row)

    return(pas_triangle)
