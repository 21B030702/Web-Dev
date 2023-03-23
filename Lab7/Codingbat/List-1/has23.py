def has23(nums):
    for i in range(len(nums)):
        if nums[i] == 2 or nums[i] == 3:
           return True
    return False