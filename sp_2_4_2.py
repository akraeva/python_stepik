dnk = input()
result = ''

while len(dnk) != 0:
    j = 1
    while j < len(dnk) and dnk[0] == dnk[j]:
        j += 1
    result += dnk[0] + str(j)
    dnk = dnk[j:]
print(result)
