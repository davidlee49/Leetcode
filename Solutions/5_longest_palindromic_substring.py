# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.
#
# A string is called a palindrome string if the reverse of that string is the same as the original string.
s = "bbb"


def longestPalindrome(s):
    longest_palindrome = s[0]
    if not s:
        return False
    elif len(s) == 1:
        return s
    else:
        for i in range(len(s)):
            temp = ""
            i2 = i + 1
            if i2 < len(s) and s[i] == s[i2]:
                while i >= 0 and i2 < len(s):
                    if s[i] == s[i2]:
                        temp = s[i] + temp + s[i2]
                    i -= 1
                    i2 += 1
                    if len(temp) > len(longest_palindrome):
                        longest_palindrome = temp
            else:
                x = 1
                temp = s[i]
                while i - x >= 0 and i + x < len(s):
                    if s[i-x] == s[i+x]:
                        temp = s[i-x] + temp + s[i+x]
                    if len(temp) > len(longest_palindrome):
                        longest_palindrome = temp

                    x += 1

    return longest_palindrome
print(longestPalindrome(s))

