#https://leetcode.com/problems/sort-characters-by-frequency/

s = "tree"

def frequencySort(s: str) -> str:
    # need to add characters and frequency so a dictionary would be great for this
    # go through string and increment char count
    # because lower and uppercase are different chars, we should use ord() to make a distinction between the two

    if not s:
        return s

    chars = {}
    chars_freq = []

    for i in range(len(s)):
        chars_freq.append(set())

    for char in s:
        if char not in chars:
            chars[char] = 0
            chars_freq[0].add(char)

        else:
            chars_freq[chars[char]].remove(char)
            chars[char] += 1
            chars_freq[chars[char]].add(char)

    answer = ""

    for letters in range(len(chars_freq)):
        for letter in chars_freq[letters]:
            answer = letter*(letters + 1) + answer


    print(answer)

frequencySort(s)