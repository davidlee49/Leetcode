#https://leetcode.com/problems/generate-parentheses/description/

def generateParenthesis(n):
    parenthesis = []

    def add_brackets(n, cur_str, open, close):
        if open == close == n:
            parenthesis.append(cur_str)
            return

        if open < n:
            add_brackets(n, cur_str + "(", open + 1, close)
        if close < open:
            add_brackets(n, cur_str + ")", open, close + 1)

    add_brackets(n, "", 0, 0)

    return parenthesis

print(generateParenthesis(3))