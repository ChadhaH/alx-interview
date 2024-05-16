#!/usr/bin/python3
"""N queens
"""
import sys


slts = []
"""The list of solutions to the N queens problem.
"""
n = 0
"""The size
"""
possib = None
"""The list of possible positions on the chessboard.
"""


def get_input():
    """Validates the program's argument.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(possib0, possib1):
    """Checks if the positions of two queens are in an attacking mode.
    """
    if (possib0[0] == possib1[0]) or (possib0[1] == possib1[1]):
        return True
    return abs(possib0[0] - possib1[0]) == abs(possib0[1] - possib1[1])


def group_exists(group):
    """Checks if a group exists in the list of solutions.
    """
    global slts
    for stn in slts:
        i = 0
        for stn_possib in stn:
            for grp_possib in group:
                if stn_possib[0] == grp_possib[0]
                and stn_possib[1] == grp_possib[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the n queens problem.
    """
    global slts
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            slts.append(tmp0)
    else:
        for colum in range(n):
            b = (row * n) + colum
            matches = zip(list([possib[b]]) * len(group), group)
            used_possibitions =
            map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(possib[b].copy())
            if not any(used_possibitions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_slts():
    """Gets the solutions for the given size.
    """
    global possib, n
    possib = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    b = 0
    group = []
    build_solution(b, group)


n = get_input()
get_slts()
for solution in slts:
    print(solution)
