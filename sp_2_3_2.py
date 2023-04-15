a = int(input())
b = int(input())
sum_num = 0
count = 0

for i in range(a, b+1):
    if i % 3 == 0:
        sum_num +=i
        count +=1

res = sum_num / count if count !=0 else 0

print(res)