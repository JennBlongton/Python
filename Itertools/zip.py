N, X = list(map(int, input().split()))
marks = []
for _ in range(X):
    marks.append(list(map(float, input().split())))

print(marks)
    
marksList = list(zip(*marks))

print(marksList)

for i in range(len(marksList)):
    print(sum(marksList[i])/X)