# https://leetcode.com/problems/integer-to-roman/

num = 198
def intToRoman(num):
    roman_num = {
        1: "I",
        11: "V",
        2: "X",
        12: "L",
        3: "C",
        13: "D",
        4: "M"
    }
    answer = ""
    place_value = len(str(num))
    for i in range(place_value):
        temp = 1
        digit = (num//(10**(place_value-1)))
        if digit == 0:
            pass
        elif digit == 9:
            answer += roman_num[place_value]
            answer += roman_num[place_value + 1]
        elif digit < 4:
            answer += roman_num[place_value] * digit
        elif digit == 4:
            answer += roman_num[place_value]
            answer += roman_num[place_value + 10]
        elif digit > 4:
            answer += roman_num[place_value + 10]
            answer += roman_num[place_value] * (digit - 5)
        num = num - (digit * (10**(place_value-1)))
        place_value -= 1

    print(answer)
    return answer



intToRoman(num)

