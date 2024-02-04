from itertools import groupby
from collections import defaultdict

# string=input()

# list1=[]
# print(groupby(string))
# for (key, group) in groupby(string):
#     print(key, list(group))

#     list1.append((len(list(group)), int(key)))
  
# print(*list1)

a = ['a', 'a', 'b', 'a', 'b']
b = ['a', 'b']
dict_a = defaultdict(list)

for index, item in enumerate(a):
    if item in dict_a:
        dict_a[item].append(index)
    else:
        dict_a[item] = [index]

print(dict_a)
        
for item in b:
    if item in dict_a:
        print(dict_a[item])
