from time import time, sleep
"""
Returns the fibonacci series up to the given integer
"""

def fibo(n: int):
    """
    Returns the fibonacci of n
    :param n: int >= 0
    :return: list
    """
    assert isinstance(n, int)
    assert n >= 0
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibonacci_series(n):
    res = [fibo(i) for i in range(n)]
    return res


def fibonacci_series2(n):
    res = [0, 1]
    for i in range(2, n):
        temp = res[i - 1] + res[i - 2]
        res.append(temp)
    return res

def fibonacci_series3(n):
    a, b, temp = 0, 1, 0
    for i in range(1, n+1):
        print(a)
        temp = a + b
        a, b = b, temp

print(fibonacci_series(1))
print(fibonacci_series2(1))
fibonacci_series3(4)