file_name = 'sp_3_4_3.txt'
students = []

with open(file_name) as text:
    for line in text:
        students.append(line.strip().split(';'))

file_name = 'sp_3_4_3_res.txt'
with open(file_name, 'w') as result:
    aver = [0.0, 0.0, 0.0]
    for i in students:
        summ = 0
        for j in range(1, 4):
            summ += int(i[j])
            aver[j-1] += int(i[j])
        result.write(str(summ / 3) + '\n')
    for i in range(0, 3):
        aver[i] /= len(students)
        result.write(str(aver[i]) + ' ')
