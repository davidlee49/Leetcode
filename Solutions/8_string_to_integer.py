# https://leetcode.com/problems/string-to-integer-atoi/
s = "  -42"
def myAtoi(s: str) -> int:
    i = 0
    answer = ""
    is_negative = 1
    string = s.strip()
    if not string:
        return 0
    if string[i] == "-" or string[i] == "+":
        if string[i] == "-":
            is_negative = -1
        i += 1
    while i < len(string):
        if string[i].isdigit():
            answer += string[i]
            i += 1
        else:
            break

    if not answer:
        return 0
    else:
        answer = int(answer) * is_negative
        if answer > 2147483647:
            return 2147483647
        elif answer < -2147483648:
            return -2147483648
        else:
            return answer


print(myAtoi(s))
