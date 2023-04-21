x = int(input())
h = int(input())
m = int(input())
sleep = h * 60 + m + x
print(sleep // 60)
print(sleep % 60)
