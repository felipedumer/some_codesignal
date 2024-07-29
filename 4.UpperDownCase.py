def transform_char(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    else:
        return char

def transform_string(input_string):
    result = []
    for char in input_string:
        result.append(transform_char(char))

    result_string = ""
    for char in result:
        result_string += char
    
    return result_string

print(transform_string("HelLo WoRld 123"))