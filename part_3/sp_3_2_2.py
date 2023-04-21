words = [i for i in input().lower().split(' ')]
result = {}
for i in words:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for i in result:
    print(i, result[i])
