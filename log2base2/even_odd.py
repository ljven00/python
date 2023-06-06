"""
For any given number, evaluate if
it is odd or even and print the result
"""

def even_odd(n: int):
    """
    return odd or even
    :param n: int number to be verified
    :return: string odd or even
    """
    is_even = lambda n: n % 2 == 0

    return "Even" if is_even(n) else "Odd"

try:
    n = int(input("Please input a number:"))
    print(f"{n} is {even_odd(n)}")
except ValueError:
    print("Expected a number")

