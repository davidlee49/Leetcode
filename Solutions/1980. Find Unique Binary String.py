class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        for i in range(len(nums)+1):
            string = format(i, f"0{len(nums)}b")
            if not string in nums:
                return string