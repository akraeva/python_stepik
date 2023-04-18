NUMS = '0123456789'
res = ''
file_name = 'sp_3_4_1.txt'
with open(file_name) as ex:
    string = ex.readline()
    let = ''
    count = 0
    for i in string:
        if i not in NUMS:
            res += let * count
            let = i
            count = 0
        elif i in NUMS:
            count = count * 10 + int(i)
    res += let * count

with open(file_name, 'w') as ex:
    ex.write(res)
