a = int(input())
b = int(input())
h = int(input())
if h >= a:
    if h <= b:
        print('Это нормально')
    else:
        print('Пересып')
else:
    print('Недосып')

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Високосный')
else:
    print('Обычный')
