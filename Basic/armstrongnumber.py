def armstrong(num):
    n = len(str(num))
    temp_sum = 0
    for c in str(num):
        temp_sum += int(c) ** n

    return temp_sum == num


print(armstrong(120))