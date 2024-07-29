def count_even_odd(nums):
    even_count = 0
    odd_count = 0
    
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return (even_count, odd_count)

# Example usage
print(count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: (5, 5)
print(count_even_odd([2, 4, 6, 8, 10]))                # Output: (5, 0)
print(count_even_odd([1, 3, 5, 7, 9]))                 # Output: (0, 5)
print(count_even_odd([]))                              # Output: (0, 0)