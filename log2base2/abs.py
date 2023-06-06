"""
You will be given a number 'num'.
Your task is to print the absolute value of 'num'
"""

def abs_value(n: int):
    """
    :param n: int to find abs value
    :return: int absolute value of n
    """
    return n if n>= 0 else -n


try:
    n = float(input("Please input a number:"))
    print(f"The asolute value of {n} is {abs_value(n)}")
except ValueError:
    print("Expected a number")