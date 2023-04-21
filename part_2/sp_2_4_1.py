genom = input().lower()
c = genom.count('c')
g = genom.count('g')
c = c if c > 0 else 0
g = g if g > 0 else 0
cg = (c + g) / len(genom) * 100
print(cg)
