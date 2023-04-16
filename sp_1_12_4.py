figure = input()

if figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    s = (p * (p-a) * (p-b) * (p-c))**(1/2)
    print(s)
elif figure == 'прямоугольник':
    a = float(input())
    b = float(input())
    s = a * b
    print(s)
elif figure == 'круг':
    pi = 3.14
    r = float(input())
    s = pi * r ** 2
    print(s)
