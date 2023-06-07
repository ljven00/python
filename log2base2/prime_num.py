"""
Given an integer check if it is
prime or not
"""

def is_prime(n: int):
    """
    returns true if number is prime
    :param n: int
    :return: bool
    """
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(5))

