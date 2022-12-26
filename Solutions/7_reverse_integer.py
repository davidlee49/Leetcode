# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.
x = -2147483648
# def reverse(x):
#     MIN = -2147483648
#     MAX = 2147483647
#     answer = ""
#     x = str(x)
#     pointer = len(x) -1
#     while pointer >= 0:
#
#
# reverse(x)
#

def reverse(x: int):
    is_negative = 1
    temp = x
    if x < 0:
        is_negative = -1
        temp = -1 * x
    temp = str(temp)
    answer = ""
    for char in temp[-1::-1]:
        answer += char
    answer = int(answer) * is_negative
    if answer > 2147483647 or answer < -2147483648:
        return 0
    print(answer)

reverse(x)