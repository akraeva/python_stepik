i = 0
it = 0
while i <= 10:
    it += 1
    i = i + 1
    if i > 7:
        i = i + 2
print(i)
print(it)

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
