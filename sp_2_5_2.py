nums = [int(i) for i in input().split(' ')]
nums_count = len(nums)
if nums_count == 1:
    print(nums[0])
else:
    for i in range(nums_count) :
        i_first = i - 1
        i_last =  i + 1 if i < nums_count-1 else 0
        print (nums[i_first] + nums[i_last], end = ' ')
print()