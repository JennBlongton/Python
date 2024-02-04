# First Method
def primenumber_interval(start, end):
    result = []
    flag = 0
    for i in range(start, end):
        for j in range(2, i):
            if (i % j == 0):
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            result.append(i)
    return result

print(primenumber_interval(2, 7))

# Second Method
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_in_interval(start, end):
    result = []
    for num in range(start, end+1):
        if isPrime(num):
            result.append(num)
    return result

print(prime_in_interval(2, 5))