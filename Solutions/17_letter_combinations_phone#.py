# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


digits = "243"

def letterCombinations(digits: str):
    answer = []
    number = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def find_combo(i, combo):
        if len(combo) == len(digits):
            return answer.append(combo)
        for c in number[digits[i]]:
            find_combo(i + 1, combo + c)

    if digits:
        find_combo(0, "")

    return answer



print(letterCombinations(digits))

