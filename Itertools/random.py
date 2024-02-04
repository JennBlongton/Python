# nm = input().split()

# n = int(nm[0])

# m = int(nm[1])

# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))

# print(arr)

# k = int(input())

def fibonacci(n):
    numbers = [0, 1]
    for i in range(2, n):
        numbers.append((numbers[i - 1] + numbers[i-2]))
        
    return numbers

print(fibonacci(5))