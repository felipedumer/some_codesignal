def is_palindrome(s):
    # Initialize an empty list to hold the normalized characters
    normalized = []
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the character is a letter
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            # Convert to lowercase manually
            if 'A' <= char <= 'Z':
                normalized.append(chr(ord(char) + 32))
            else:
                normalized.append(char)
    
    # Compare the normalized list with its reverse
    n = len(normalized)
    for i in range(n // 2):
        if normalized[i] != normalized[n - 1 - i]:
            return False
    
    return True

# Example usage
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))                        # Output: True
print(is_palindrome("hello"))                          # Output: False