"""
give two numbers swap and return them
"""

try:
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(f"You entered {num1} and {num2}")
    num1, num2 = num2, num1
    print(f"After swapping {num1} becomes {num2} and {num2} becomes {num1}")
except ValueError:
    print("Both should be a number")