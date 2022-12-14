
haystack = "abc"
needle = "c"

def strStr(haystack, needle):
    if haystack == needle:
        return 0
    for letter in range(0, len(haystack) - len(needle)+1):
        if haystack[letter:letter + len(needle)] == needle:
            return letter
    return -1

print(strStr(haystack, needle))