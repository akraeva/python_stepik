num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 :
    num_max = num1
    num_min = num2
else :
    num_max = num2
    num_min = num1

if num3 >= num_max :
    num_mid = num_max
    num_max = num3
elif num3 <= num_min :
    num_mid = num_min
    num_min = num3
else :
    num_mid = num3

print(num_max)
print(num_min)
print(num_mid)