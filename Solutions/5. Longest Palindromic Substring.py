class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for index, char in enumerate(s):
            end = len(s) - 1
            l, r = index, index
            palindrome_substring = char
            # find palindrome, middle
            while r != end and s[r+1] == char:
                r += 1
                palindrome_substring = palindrome_substring + s[r]


            while l > 0 and r < end:
                r += 1
                l -= 1
                if s[l] != s[r]:
                    break
                palindrome_substring = s[l] + palindrome_substring + s[r]


            if len(palindrome_substring) > len(answer):
                answer = palindrome_substring

        return answer