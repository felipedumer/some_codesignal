def find_min(nums):
    if not nums:
        return None
    
    minNumber = nums[0]
    
    for num in nums:
        if minNumber > num:
            minNumber = num
    
    return minNumber

print(find_min([1, 2, 3, 5, -1]))