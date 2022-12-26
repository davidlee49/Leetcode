# https://leetcode.com/problems/longest-common-prefix/

strs = ["ab", "a"]


def longestCommonPrefix(strs):
    letter_index = 0
    prefix = ""
    if not strs[0]:
        return ""
    while letter_index < len(strs[0]):
        for word in strs[1:]:
            if not word or letter_index + 1 > len(word) or word[letter_index] != strs[0][letter_index]:
                return prefix
            else:
                pass
        prefix += strs[0][letter_index]
        letter_index += 1
    return prefix

print(longestCommonPrefix(strs))