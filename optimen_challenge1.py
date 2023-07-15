def solveMeFirst(a: int, b: int):
    """return sum of a in b"""
    return a + b

def getInput():
    """returns two integers in the range 1 - 1000 inclusive"""
    while True:
        try:
            a = int(input("Enter first integer (1 - 1000):"))
            b = int(input("Enter second integer (1 - 1000):"))
            assert 1 <= a <= 1000 and 1 <= b <= 1000
            break
        except ValueError:
            print("Integer only integer value like 1, 4, 8")
        except AssertionError:
            print("Value must be in range 1 <= a <= 1000")
    return a, b

a, b = getInput()
res = solveMeFirst(a, b)
print(res)

