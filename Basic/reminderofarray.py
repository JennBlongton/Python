# First take a remainder or individual number like arr[i] % n. Then multiply the remainder with current result. After multiplication, again take remainder to avoid overflow. This works because of distributive properties of modular arithmetic. ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c

def findreminder(nums, k):
    n = len(nums)
    mul = 1
    for i in range(n):
        mul = (mul * (nums[i] % k)) % k
    
    print(mul % k)

findreminder([ 100, 10, 5, 25, 35, 14 ], 11)