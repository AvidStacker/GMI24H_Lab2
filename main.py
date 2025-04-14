"""1. Write a Python function called factorial(n) that computes the factorial
of a given positive integer n using recursion.
2. Write a recurrence relation to find the Fibonacci series of n where n>2.
3. Write all the postive odd numbers smaller or equal to 14 using
recursion"""

def fibonacci(n):
    # Check if n is less than 0
    if n < 0:
        print("Incorrect input")
    # Check if n is equal to 0
    elif n == 0:
        return 0
    # Check if n is equal to 1
    elif n == 1:    
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))
