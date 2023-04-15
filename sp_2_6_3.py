lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
else:
    while x in lst:
        i = lst.index(x)
        print(i, end = ' ')
        lst[i] = x-1
    print()