"""
takes numbers separated by space
and outputs the sum
"""

def procces_num(line: str):
    total = 0
    if line.isspace():
        return None
    nums = line.split()
    try:
        for num in nums:
            total += float(num)
    except ValueError:
        return None
    return total


