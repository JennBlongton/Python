def isMonotonic(nums):
    return (all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i+1] for i in range(len(nums) - 1)))

print(isMonotonic([6, 5, 4, 4]))



def is_monotonic(nums):
    l, r = 0, len(nums) - 1

    increasing = decreasing = True

    while l < len(nums) - 1:
        if nums[l] > nums[l+1]:
            increasing = False
            break
        l += 1

    while r > 0:
        if nums[r] > nums[r-1]:
            decreasing = False
            break
        r -= 1

    return increasing or decreasing

print(is_monotonic([6, 5, 4, 4]))
