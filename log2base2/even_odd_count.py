from even_odd import even_odd

"""
Given an array of int
prints the total of odd an even number
"""


def even_odd_count(nums: list):
    even = odd = 0
    for num in nums:
        if even_odd(num):
            even += 1
        else:
            odd += 1
    return even, odd

