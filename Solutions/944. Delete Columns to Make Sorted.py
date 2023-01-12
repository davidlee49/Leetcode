class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col_to_del = 0
        if len(strs) == 1:
            return col_to_del

        for i in range(len(strs[0])):
            prev_char = strs[0][i]
            for letters in strs[1:]:
                if letters[i] < prev_char:
                    col_to_del += 1
                    break
                prev_char = letters[i]

        return col_to_del