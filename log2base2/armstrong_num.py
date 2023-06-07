"""
Given an integer, checks if it
is an Armstrong number.
That is the sum of the cube of its digits
should equal the initial number
"""

def amstrong_num(n: int):
    """
    checks if a given input is an armstrong number
    :param n: int input number
    :return: string Armstrong or not
    """
    cube = lambda x: x**3
    digits_cube = [cube(int(x)) for x in str(n)]
    return "Armstrong Number" if sum(digits_cube) == n else "Not Armstrong Number"

print(amstrong_num(153))
