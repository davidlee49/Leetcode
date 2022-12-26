# https://leetcode.com/problems/roman-to-integer/
s = "III"

def romanToInt(s: str):
    answer = 0
    pointer = 0
    roman_num_conversion = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    while pointer < len(s):
        if pointer + 1 < len(s) and roman_num_conversion[s[pointer + 1]] > roman_num_conversion[s[pointer]]:
            answer += roman_num_conversion[s[pointer + 1]]
            answer -= roman_num_conversion[s[pointer]]
            pointer += 2
        else:
            answer += roman_num_conversion[s[pointer]]
            pointer += 1

    return answer
romanToInt(s)