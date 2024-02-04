# Recursive

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Iterative

def iterFactorial(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 0):
            fact *= n
            n -= 1
        return fact
    
print(iterFactorial(5))