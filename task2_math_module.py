# Task 2: Using the Math Module for Calculations

import math

try:
    number = float(input("Enter a number: "))

    sqrt_value = math.sqrt(number)
    log_value = math.log(number)
    sine_value = math.sin(number)  # number is in radians

    print(f"Square root of {number} is: {sqrt_value}")
    print(f"Natural logarithm (ln) of {number} is: {log_value}")
    print(f"Sine of {number} radians is: {sine_value}")

except ValueError as ve:
    print("Invalid input! Please enter a positive number for log and sqrt.")

except Exception as e:
    print(f"An error occurred: {e}")
