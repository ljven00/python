"""
Given an integer n
print an n x n box of starts
"""

def nxn_box(n: int):
    """
    print n x n box
    :param n:
    """
    assert n >= 1
    for i in range(1, n+1):
        for j in range(1, n + 1):
            print("*", end=" ")
        print("")


nxn_box(5)