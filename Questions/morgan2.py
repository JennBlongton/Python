from collections import Counter

def dutchflag(lst):
    res = []
    counter_result = Counter(lst)
    print(counter_result)
    for k, v in counter_result.items():
        print(range(v))
        for _ in range(v):
            print(k)
            res.append(k)
    print(res)

data = [0, 1, 2, 0, 1, 2]
dutchflag(data)