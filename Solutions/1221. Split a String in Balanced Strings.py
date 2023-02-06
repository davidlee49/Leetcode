class Solution(object):
    def balancedStringSplit(self, s):
        output = 0
        s_list = [char for char in s if char == char]
        r_count = 0
        l_count = 0

        while s_list:
            char = s_list.pop()
            if char == "R":
                r_count += 1
            else:
                l_count += 1

            if r_count == l_count:
                output += 1

        return output





