def max_product_subarray(lst):
    if len(lst) == 0:
        return 0
    
    max_product = float("-inf")
    start = end = 0
    current_product = 1

    for i in range(len(lst)):
        current_product *= lst[i]

        if current_product == 0:
            current_product = 1
            start = end = i + 1
        else:
            if current_product < 0:
                end = i
        max_product = max(max_product, current_product)

    return max_product

arr1 = [6, -3, -10, 0, 2]
print("Output for arr1:", max_product_subarray(arr1))