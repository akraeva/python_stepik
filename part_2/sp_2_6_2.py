count = int(input())
result = []
i = 0
while len(result) < count:
    i += 1
    part = [i] * i
    result += part

result = result[:count]
for i in result:
    print(i, end=' ')
print()
