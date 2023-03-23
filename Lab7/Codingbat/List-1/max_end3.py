def max_end3(nums):
    l = []
    if nums[0] > nums[len(nums)-1]:
       for i in range(len(nums)):
           l.append(nums[0])
    else:
       for i in range(len(nums)):
           l.append(nums[len(nums)-1])
           
    return l