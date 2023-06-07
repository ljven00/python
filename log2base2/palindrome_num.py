from reverse_num import reverse_num
"""
Given in integer, check if it is
a palindrome number. That is, if reads the
same backward
"""

def palindrome_num(n: int):
    """
    checks if the given input is palindrome
    :param n: int input number
    :return: string "Palindrome" if it is
    """
    return "Palindrome" if n == reverse_num(n) else "Not Palindrome"

print(palindrome_num(123))
