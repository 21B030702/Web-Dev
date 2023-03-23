def sum13(nums):
    sum = 0
    ind = -1
    for i in range(len(nums)):
        if nums[i] == 13:
           ind = i+1
           continue
        if ind == i:
            continue
        else:
           sum += nums[i]
    
    return sum