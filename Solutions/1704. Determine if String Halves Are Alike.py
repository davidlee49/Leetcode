#https://leetcode.com/problems/determine-if-string-halves-are-alike/

def halvesAreAlike(s: str) -> bool:
    # the fastest we can complete this solution is in O(n) time
    # because we need to know what are vowels, the minimum space required is O(1)

    # traverse the string in O(n) time
    # 1 we can create two strings for each half O(n) time, (O(n) space) and
    # 2 traverse and count the vowels O(n) time, O(1) space
    # we can optimize this by understanding that since the traversal order does not matter and only count
    # we can simply use pointers on each end and cut out step 1, reducing space to O(1)

    # time: O(N), space: O(1)

    right_vowel_count, left_vowel_count = 0, 0
    l_half, r_half = 0, len(s) - 1

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    while l_half < r_half:
        if s[l_half] in vowels:
            left_vowel_count += 1
        if s[r_half] in vowels:
            right_vowel_count += 1

        l_half += 1
        r_half -= 1

    return right_vowel_count == left_vowel_count

s = "book"
print(halvesAreAlike(s))
