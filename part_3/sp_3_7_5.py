result = {}

file_name = 'sp_7_5_data.txt'
with open(file_name) as text:
    data = text.readlines()

for i in data:
    row = i.strip().split('\t')
    class_number = int(row[0])
    student_height = int(row[2])
    if class_number in result:
        result[class_number]['count'] += 1
        result[class_number]['hight'] += student_height
    else:
        result[class_number] = {'count': 1, 'hight': student_height}

file_name = 'sp_7_5_result.txt'
with open(file_name, 'w') as text:
    for i in range(1, 12):
        if i in result:
            row = result[i]
            middle_hight = row['hight'] / row['count']
        else:
            middle_hight = '-'

        text.write(f'{i} {middle_hight}\n')
