"""
Given an integer n
print the sum of the natural numbers
up to n inclusive
"""


def sum_of_natural_num(n: int):
    """
    prints the sum of natural nums up to n
    :param n: int
    :return: int sum
    """
    assert isinstance(n, int)
    if n > 0:
        sum = 0
        for i in range(1, n + 1):
            sum += i
    return sum


def sum_of_natural_num2(n: int):
    if n <= 1:
        return n
    return n + sum_of_natural_num2(n - 1)

def sum_of_natural_num3(n: int):
    return n * (n + 1) / 2

print(sum_of_natural_num(5))
print(sum_of_natural_num2(5))
print(sum_of_natural_num3(5))
