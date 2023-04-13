#a, b, c, d, e, f = input()

num = input()

half1 = int(num[0]) + int(num[1]) + int(num[2]) 
half2 = int(num[3]) + int(num[4]) + int(num[5]) 

if half1 == half2 :
    print('Счастливый')
else :
    print('Обычный')
