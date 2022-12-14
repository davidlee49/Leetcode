#https://leetcode.com/problems/valid-parentheses/


s = "("
def isValid(s):
    stack = []
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
            continue

        if not stack or brackets[stack.pop()] != char:
            return False

    if stack:
        return False

    return True
print(isValid(s))