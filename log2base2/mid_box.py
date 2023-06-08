"""
Given an integer, prints half of
the n x n box
"""


def mid_box(n: int):
    """
    prints a half n x n box
    :param n:
    """
    assert n >= 1
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print("")


# mid_box(5)
