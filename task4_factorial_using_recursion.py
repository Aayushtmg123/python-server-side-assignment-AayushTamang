# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n - 1)  

# Input from user
num = int(input("Enter a number to find its factorial: "))

# Validation and result
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")
