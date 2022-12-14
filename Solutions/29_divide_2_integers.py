# https://leetcode.com/problems/divide-two-integers/

dividend = -1
divisor = 1

def divide(dividend, divisor):
    x = 0
    y = 0
    answer = 0
    negative = True
    if dividend > 0 and divisor > 0:
        negative = False
    elif dividend < 0 and divisor < 0:
        negative = False
    while x < abs(dividend):
        x += 1
        y += 1
        if y == abs(divisor):
            if negative:
                answer -= 1
            else:
                answer += 1
            y = 0

    print(answer)
    return min(2147483647, max(-2147483648, answer))

divide(dividend,divisor)