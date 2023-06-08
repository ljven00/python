"""
Given an integer,
prints a diagonal for  the
n x n box
"""


def diagonal_nxn_box(n: int):
    """
    prints the diagonal of n x n box
    :param n: int
    """
    assert n >= 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i == j):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

diagonal_nxn_box(5)