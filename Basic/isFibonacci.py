# A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square (Source: Wiki). 
import math

def isPerfectsquare(n):
    s = int(math.sqrt(n))
    return s*s == n

def isFibonacci(num):
    return isPerfectsquare(5* num ** 2 + 4) or isPerfectsquare(5 * num**2 - 4)


print(isFibonacci(8))