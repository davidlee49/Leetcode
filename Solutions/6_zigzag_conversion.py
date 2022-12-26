# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
# display this pattern in a fixed font for better legibility)
s = "asfdasb"
numRows = 2
Output: "PAHNAPLSIIGYIR"

def convert(s, numRows):
    if numRows == 1:
        return s
    array = [""] * numRows
    pointer = 0
    i = 1
    pattern_size = numRows + numRows - 2
    while pointer < pattern_size * i and pointer < len(s):
        while pointer < pattern_size * (i-1) + numRows and pointer < len(s):
            array_index = pointer - (pattern_size * (i-1))
            array[array_index] += s[pointer]
            pointer += 1
        while pointer < pattern_size * (i) and pointer < len(s):
            array_index = abs(pointer - pattern_size * i)
            array[array_index] += s[pointer]
            pointer += 1
        i += 1
    return "".join(array)


print(convert(s, numRows))
