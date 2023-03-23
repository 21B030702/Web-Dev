def rotate_left3(nums):
    nums.append(nums[0])
    nums.pop(0)
    return nums