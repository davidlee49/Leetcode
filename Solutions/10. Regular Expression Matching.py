#https://leetcode.com/problems/regular-expression-matching/


s = "baaaaaasdiiiialaj"
p = "ba*aasdi*alaj"

def isMatch(s, p) -> bool:
    #traverse string
    #check if it matches p
        #accomodate for edge cases "." and "*"

    s_index = 0
    p_index = 0
    while s_index < len(s):
        char = ""
        if p[p_index] == "*":
            char = p[p_index - 1]

        else:
            char = p[p_index]


        if s[s_index] != char:
            return False

        s_index += 1
        if p[p_index] == "*" and s[s_index] == char:
            continue

        else:
            p_index += 1



    if p_index == len(p):
        return True
    else:
        return False

print(isMatch(s, p))