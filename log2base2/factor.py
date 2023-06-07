"""
Given two integers,
print "Yes" if the second one is a
factor of the first and "No" otherwise
"""

def factor(num1: int, num2: int):
    """
    return "Yes" if num2 is a factor num1 else "No"
    :param num1: int first number
    :param num2: int second number
    :return: string result of the test
    """
    return "Yes" if num1 % num2 == 0 else "No"

print(factor(10, 5))