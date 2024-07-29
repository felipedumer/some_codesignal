def swap_adjacent_characters(s):
    result = []
    i = 0
    while i < len(s) - 1:
        # Swap the adjacent characters
        result.append(s[i + 1])
        result.append(s[i])
        i += 2
    
    # If the length of the string is odd, append the last character
    if len(s) % 2 != 0:
        result.append(s[-1])
    
    # Manually concatenate the list of characters into a single string
    result_string = ""
    for char in result:
        result_string += char
    
    return result_string

# Example usage
print(swap_adjacent_characters("abcdef"))  # Output: "badcfe"
print(swap_adjacent_characters("hello"))   # Output: "ehllo"