"""
Given an integer,
return its number backward
"""

def reverse_num(n: int):
    """
    :param n: int to be reversed
    :return: int the number reversed
    """
    temp = reversed(list(str(n)))
    return int("".join(temp))

# print(reverse_num(300))