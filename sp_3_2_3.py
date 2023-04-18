def f(param):
    return param*100


n = int(input())
res = {}
for i in range(n):
    x = int(input())
    if x not in res:
        res[x] = f(x)
    print(res[x])
