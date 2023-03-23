def first_last6(nums):
    for i in range(len(nums)):
        if nums[i] == 6 and i == 0 or nums[i] == 6 and i == len(nums)-1:
           return True
    return False