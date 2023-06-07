from factor import factor
"""
Given an integer, checks if it is
a perfect number.
That is the sum of its factor up to it exclusive
is equal to the number
"""

def perfect_num(n):
    factors = list(filter(lambda x: factor(n, x), [i for i in range(1, n)]))
    return n == sum(factors)


print(perfect_num(6))