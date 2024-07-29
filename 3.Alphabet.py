def shift_char(char):
    if 'a' <= char <= 'z':
        if char == 'z':
            return 'a'
        else:
            return chr(ord(char) + 1)
    elif 'A' <= char <= 'Z':
        if char == 'Z':
            return 'A'
        else:
            return chr(ord(char) + 1)
    else:
        return char

def solution(s):
    result = []
    for char in s:
        result.append(shift_char(char))

    result_string = ""
    for char in result:
        result_string += char
    return result_string

print(solution("abc123XYz!"))