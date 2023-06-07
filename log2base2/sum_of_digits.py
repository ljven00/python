"""
Given an integer, return the sum of all
its digits
"""

def sum_of_digits(n: int):
    """
    return the sum of all n's digits
    :param n: int
    :return: sum of the digits
    """
    return sum([int(x) for x in str(n)])

print(sum_of_digits(123))