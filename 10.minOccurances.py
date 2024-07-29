def count_min_occurrences(nums):
    if not nums:
        return 0
    
    min_value = nums[0]
    min_count = 1
    
    for num in nums[1:]:
        if num < min_value:
            min_value = num
            min_count = 1
        elif num == min_value:
            min_count += 1
    
    return min_count

# Example usage
print(count_min_occurrences([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: 2
print(count_min_occurrences([10, 20, 30, 40, 50]))              # Output: 1
print(count_min_occurrences([-5, -10, 0, -10, 5, 10]))          # Output: 2
print(count_min_occurrences([]))                                # Output: 0