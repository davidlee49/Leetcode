#https://leetcode.com/problems/determine-if-two-strings-are-close/
import collections

word1 = "abc"
word2 = "bca"

x = "accbbb"


def closeStrings(word1: str, word2: str) -> bool:
    # intuition would be to create two string while traversing word1 and word2 and compare them for each condition
    # string traversal will require O(n) time
    # every swap will take O(n) time to remake the string and another O(n) time to compare
    # every transform will take O(n) time to remake the string and another O(n) time to compare

    # we can optimize by simply evaluating conditions based on the char and char position rather than remaking the string
    # the swap operation allows a lot more flexibility and order no longer matters. we now only need the char and the char count
    # finally transforming allows us to meet the the condition if the two chars counts between word1 and word2 are invserse

    word1_chars = collections.Counter(word1)
    word2_chars = collections.Counter(word2)

    for char in word1:
        if char not in word2:
            return False

    word1_char_count = collections.Counter(word1_chars.values())
    word2_char_count = collections.Counter(word2_chars.values())

    return word1_char_count == word2_char_count




print(closeStrings(word1, word2))