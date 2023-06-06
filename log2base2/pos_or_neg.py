"""
Problem text
You will be given a number 'num'.
Your task is to find whether 'num'
is a positive number, negative number or zero
"""

def pos_or_neg(n: int):
    """
    This function returns positive, negative, or
    "neither positive nor negative" depending on the number
    :param n: int number to evaluate
    :return: string of the number state
    """
    return "Positive" if n > 0 else "Negative" \
    if n < 0 else "Neither positive nor negative"

try:
    n = float(input("Please input a number:"))
    print(pos_or_neg(n))
except ValueError:
    print("Expected a number")