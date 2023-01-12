#https://leetcode.com/problems/jump-game-ii/description/

def jump(self, nums):
    cur_jumps = 0
    pos = 0
    end = len(nums) - 1

    if len(nums) == 1:
        return 0

    while pos <= end:
        max_range = nums[pos]

        if pos + max_range >= end:
            return cur_jumps + 1

        next_max_dist = 0
        new_pos = 0
        for i in range(1, nums[pos] + 1):
            if nums[pos + i] + (i + pos) >= next_max_dist:
                next_max_dist = nums[pos + i] + (i + pos)
                new_pos = pos + i

        pos = new_pos
        cur_jumps += 1