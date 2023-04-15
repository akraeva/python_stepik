nums = [int(i) for i in input().split(' ')]
nums = sorted(nums)

while len(nums) > 1:
    num = nums[0]
    nums = nums[1:]
    if num in nums:
        print(num, end = ' ')
        while num in nums:
            nums = nums[1:]
print()