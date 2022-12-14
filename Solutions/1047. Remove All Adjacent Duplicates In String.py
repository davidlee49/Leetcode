#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


s = "abbaca"

def removeDuplicates(s: str):
    letters = [0]
    new_word = ""
    for char in s:
        if char == letters[-1]:
            letters.pop()
        else:
            letters.append(char)
    for char in letters[1:]:
        new_word = new_word + char

    print(new_word)
    return new_word



removeDuplicates(s)

