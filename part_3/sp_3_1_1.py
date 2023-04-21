def f(x):
    if x <= -2:
        res = 1 - (x+2)**2
    elif x > 2:
        res = (x-2)**2 + 1
    else:
        res = - x / 2
    return res


print(f(4.5) == 7.25)
print(f(-4.5) == -5.25)
print(f(1) == -0.5)
