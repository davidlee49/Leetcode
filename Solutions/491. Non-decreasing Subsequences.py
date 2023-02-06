class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = []
        output_set = set()
        def backtracking(cur_i, nums):
            combos = []
            if cur_i == len(nums) - 1:
                combos.append([nums[cur_i]])
                return combos

            for sub in backtracking(cur_i + 1, nums):
                if sub[0] >= nums[cur_i] and (nums[cur_i], *sub) not in output_set:
                    combos.append([nums[cur_i]]+sub)
                    output.append([nums[cur_i]]+sub)
                    output_set.add((nums[cur_i], *sub))
                combos.append(sub)
            combos.append([nums[cur_i]])
            return combos

        backtracking(0, nums)
        return output