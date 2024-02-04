def interchange(lst):
    tmp1, tmp2 = lst[0], lst[-1]
    lst[-1], lst[0] = tmp1, tmp2

    return lst

lst = [12, 35, 9, 56, 24]
print(interchange(lst))