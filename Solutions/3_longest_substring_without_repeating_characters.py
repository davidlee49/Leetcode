# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

s = "abcgabcbb"

def lengthOfLongestSubstring(s):
# need to eval all characters O(n)
# since we only need to find the longest length, we dont need to store the actual characters and can use a window approach
    r, l = 0, 0
    string = set()
    count = 0
    max = 0
    while r < len(s):
        if s[r] not in string:
            string.add(s[r])
            count += 1
            r += 1
            max = count if count > max else max
        else:
            string.remove(s[l])
            l += 1
            count -= 1
    return max

print(lengthOfLongestSubstring(s))
