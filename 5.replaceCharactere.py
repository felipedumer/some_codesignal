def replace_character(input_string, c1, c2):
    result = []
    # Iterate through each character in the input string
    for char in input_string:
        if char == c1:
            result.append(c2)  # Append c2 if the character matches c1
        else:
            result.append(char)  # Append the original character otherwise
    
    # Join the list of characters into a single string
    result_string = ""
    for char in result:
      result_string += char
    
    return result_string

print(replace_character("hello, world", "o", "a"))  
# Output: "hella, warld"