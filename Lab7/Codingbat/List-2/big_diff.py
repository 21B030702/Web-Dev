def big_diff(nums):
    k = nums[0]
    h = nums[0]
    for i in range(len(nums)):
        k = min(k, nums[i])
        h = max(h, nums[i])
    
    return h - k
    