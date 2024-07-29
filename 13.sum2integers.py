def solution(n):
    # Convert the integer to a string to access each digit
    digits = str(n)
    
    # Convert each character back to an integer and sum them
    digit_sum = sum(int(digit) for digit in digits)
    
    return digit_sum

# Example usage
n = 29
print(solution(n))  # Output: 11