#https://leetcode.com/problems/jump-game-ii/


nums = [2,3,1,1,4]
def jump(nums):
    # traverse to end of nums
    # evaluate all indexes within your jump range
    # choose the index with the farthest reach
    # there may be an edge case at the end where you dont need to jump as far
    i = 0
    while i != len(nums) - 1:
        min_jumps = 0
        jump_index = 1
        for jump_i in range(nums[i]):
            if nums[i + jump_i + 1] > nums[i]:
                jump_index = i + jump_i + 1
            if i + nums[i + jump_i + 1] >= len(nums) - 1:
                min_jumps += 1
                break

        i = jump_index
        min_jumps += 1

    return min_jumps

jump(nums)