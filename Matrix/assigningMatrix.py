test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

res = {test_list[0][ele]: test_list[ele + 1] for ele in range(len(test_list) - 1)}

print(res)

res2 = dict(zip(test_list[0], test_list[1:]))
print(res2)