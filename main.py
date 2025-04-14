"""1. Write a Python function called factorial(n) that computes the factorial
of a given positive integer n using recursion.
2. Write a recurrence relation to find the Fibonacci series of n where n>2.
3. Write all the postive odd numbers smaller or equal to 14 using
recursion"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:    
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))

def print_odd_numbers(n):
 
    if n <= 0:
        return
   
    print_odd_numbers(n-2)
    if n % 2 == 1:
        print(n, end=" ")

print_odd_numbers(14)