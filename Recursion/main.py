

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
