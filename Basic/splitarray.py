def splitarray(nums, k):
    first_part = nums[:k]
    print(nums[k:]+first_part)

splitarray([12, 10, 5, 6, 52, 36], 2)