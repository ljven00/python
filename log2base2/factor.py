"""
Given two integers,
print "Yes" if the second one is a
factor of the first and "No" otherwise
"""

def factor(num1: int, num2: int):
    """
    return true if num2 is a factor num1 else false
    :param num1: int first number
    :param num2: int second number
    :return: string result of the test
    """
    return True if num1 % num2 == 0 else False

factor2 = lambda x, y: x % y == 0