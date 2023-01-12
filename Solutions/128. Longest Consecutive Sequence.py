class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_sub_len = 0

        for num in nums:
            cur_sub_len = 1
            if num - 1 in nums:
                continue
            while num + 1 in nums:
                num += 1
                cur_sub_len += 1
            max_sub_len = max(max_sub_len, cur_sub_len)

        return max_sub_len