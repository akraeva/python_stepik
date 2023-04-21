n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]
num = 1  # число от 1 до n
d = 1  # изменение координаты
i = 0  # первая строка
j = 0  # первый столбец

while num <= n**2:
    while j > -1 and j < n and matrix[i][j] == 0:
        matrix[i][j] = num
        num += 1
        j += d
    j -= d
    i += d

    while i > 0 and i < n and matrix[i][j] == 0:
        matrix[i][j] = num
        num += 1
        i += d
    i -= d
    j -= d

    d *= (-1)

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
