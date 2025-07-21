# Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

# Sample call
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
