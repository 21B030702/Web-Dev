def centered_average(nums):
    nums.sort()
    nums.pop()
    nums.pop(0)
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        
    return sum // len(nums)
