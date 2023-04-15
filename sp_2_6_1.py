sum_nums = 1
nums = []
while sum_nums != 0 :
    sum_nums = 0
    nums.append(int(input()))
    for i in nums:
        sum_nums += i
for i in nums:
    sum_nums += i ** 2
print(sum_nums)