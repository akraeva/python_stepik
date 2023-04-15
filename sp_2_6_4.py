matrix = []
string = ''
while string!= 'end':
    string = input()
    if string not in ['', 'end'] :
        matrix.append([int(i) for i in string.split()])

str_count = len(matrix)
for i in range(str_count) :
    col_count = len(matrix[i])
    for j in range(col_count):
        up = matrix[i-1][j] if i-1 >= 0 else matrix[str_count-1][j]
        down = matrix[i+1][j] if i+1 < str_count else matrix[0][j]
        left = matrix[i][j-1] if j-1 >=0 else matrix[i][col_count-1]
        right = matrix[i][j+1] if j+1 < col_count else matrix[i][0]
        sum_elem = up + down + left + right
        print (sum_elem, end = ' ')
    print()  

    