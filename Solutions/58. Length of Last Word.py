def lengthOfLastWord(self, s: str) -> int:
    char = len(s) - 1
    count = 0

    while s[char] == " ":
        char -= 1

    while char >= 0 and s[char] != " ":
        count += 1
        char -= 1

    return count