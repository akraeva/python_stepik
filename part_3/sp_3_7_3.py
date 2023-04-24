d = int(input())  # количество слов в словаре
dic = []
[dic.append(input().lower()) for i in range(d)]

result = []
lines = int(input())  # количество строк текста
for i in range(lines):
    line = input().lower().split()
    for j in line:
        if j not in dic and j not in result:
            result.append(j)

[print(i) for i in result]
