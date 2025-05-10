"""1. Write a Python function called factorial(n) that computes the factorial
of a given positive integer n using recursion.
2. Write a recurrence relation to find the Fibonacci series of n where n>2.
3. Write all the postive odd numbers smaller or equal to 14 using
recursion"""

def factorial(n):
    if n < 0:
        print("Incorrect input")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


"""
Types of Recurrence Relations:

There are various types of Recurrence Relations are:

    Linear Recurrence Relations
    Divide and Conquer Recurrences
    Substitution Recurrences
    Homogeneous Recurrences
    Non-Homogeneous Recurrences

1. Linear Recurrence Relations:
The following is an example of linear recurrence realtion.
T(n) = T(n-1) + n for n > 0 and T(0) = 1
     = T(n-1) + n
     = T(n-2) + (n-1) + n
     = T(n-k) + (n - (k-1)) + ... + (n-1) + n

In the implementation below, we have chosen to demonstrate a linear recurrence relation using recursion.
The code below reflects the structure and growth of T(n) as defined above.
"""

# Recursive Fibonacci function for a given n
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Prints the entire Fibonacci series up to n
def fibonacci_series(n):
    if n < 0:
        print("Incorrect input")
        return
    print(f"Fibonacci series up to n={n}:")
    for i in range(n + 1):
        print(fibonacci(i), end=" ")
    print()

print(fibonacci(9))

# Recursively prints all positive odd numbers less than or equal to n in ascending order
def print_odd_numbers(n):
    if n <= 0:
        return
    if n % 2 == 1:
        print_odd_numbers(n - 2)
        print(n, end=" ")
    else:
        print_odd_numbers(n - 1)


print_odd_numbers(14)