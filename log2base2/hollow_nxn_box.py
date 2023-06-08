"""
Given an integer,
print a hollow box n x n
meaning only the border should be
filled
"""

def hollow_nxn_box(n: int):
    assert n >= 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i == 1 or j == 1) or (i == n or j == n):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("")

hollow_nxn_box(5)