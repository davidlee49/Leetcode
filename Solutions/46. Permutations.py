def permute(self, nums: List[int]) -> List[List[int]]:
    output = []

    def recur(output, nums):
        partial_perm = []
        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            copy = nums.copy()
            base = copy.pop(i)
            for partial in recur(output, copy):
                partial_perm.append([base] + partial)

        return partial_perm

    return (recur(output, nums))