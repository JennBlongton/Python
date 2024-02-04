from collections import Counter

def removeduplicate(nums):
    if len(nums) == 0:
        return
    nums_dict = Counter(nums)

    res = []

    for k in nums_dict.keys():
        res.append(k)

    return res


nums = [2, 2, 2, 2, 2]
print(removeduplicate(nums))
    