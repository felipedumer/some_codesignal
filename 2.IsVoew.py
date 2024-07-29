def is_vowel(char):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return char in vowels

def solution(s):
    voewl_positions = []
    for i in range(len(s)):
        if is_vowel(s[i]):
            voewl_positions.append(i)
    return voewl_positions

print(solution("Hello WORLD"))
    
