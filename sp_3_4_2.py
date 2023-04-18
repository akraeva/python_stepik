file_name = 'sp_3_4_2.txt'

with open(file_name) as text:
    words = {}
    for line in text:
        for i in line.lower().split():
            if i in words:
                words[i] += 1
            else:
                words[i] = 1

max = 0
res = ''
for i in words:
    if words[i] > max:
        max = words[i]
        res = i
    elif words[i] == max and (res == '' or i < res):
        res = i
        
print(res, max)
