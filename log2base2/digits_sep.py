"""
Given an int, print the result of reverse spliting it
into digits separated by a space
"""

def digits_sep(num: int):
    """
    return the reverse a number split into digits
    :param num: int to split
    :return: string representation of the number's digits
    """
    temp = list(str(num))
    return " ".join(reversed(temp))

print(digits_sep(12))