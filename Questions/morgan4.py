def count(n):
    result = 0

    for i in range(1, n+1):
        if (has4(i) == True):
            result += 1

    return result


def has4(x):
    while x:
        if (x % 10 == 4):
            return True
        x = x // 10
    
    return False

n = 328
print ("Count of numbers from 1 to ", n,
        " that have 4 as a digit is ", 
                    count(n)) 


# DP

def contains(i):
    while i:
        if i % 10 == 4:
            return True
        i = i // 10
    return False


def countnumber(n):
    count = 0

    dp = [0 for i in range(n+1)]

    for i in range(1, n+1):
        if dp[i]:
            count += 1
            continue
        if contains(i):
            count += 1
            dp[i] = True
    return count