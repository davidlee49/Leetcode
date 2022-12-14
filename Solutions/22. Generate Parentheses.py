#https://leetcode.com/problems/generate-parentheses/



def generateParenthesis(n):
    valid = []
    cur_string = ""
    total_char = n * 2

    def add_brackets(total_char, cur_string, n, close_brackets = 1):
        if n == 0:
            return
        new_string = cur_string + "("
        add_brackets(total_char, new_string, n-1, close_brackets + 1)
        new_string += ")" * close_brackets
        if len(new_string) != total_char:
            add_brackets(total_char, new_string, n-1)
        else:
            valid.append(new_string)



    add_brackets(total_char, cur_string, n)
    return valid

print(generateParenthesis(3))