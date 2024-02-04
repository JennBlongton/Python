# Reverse by 1

def arrayrotation(nums):
    temp = nums[0]
    for i in range(len(nums)-1):
        nums[i] = nums[i+1]
        # print(nums[i], nums[i+1])

    nums[-1] = temp
    print(nums)


arrayrotation([1, 2, 3, 4, 5, 6, 7, 8])

# Reverse by k 
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    print("Reverse ", nums)


def rotate_array(nums, k):
    n = len(nums)

    k = k % n
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    reverse(nums, 0, n-1)

    return nums

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 2))


