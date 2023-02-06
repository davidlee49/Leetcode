class Solution(object):
    def isPalindrome(self, s):
        s = [char.lower() for char in s if char.isalnum()]
        length = len(s)
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True