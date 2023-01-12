#https://leetcode.com/problems/jump-game/

nums = [3,2,1,0,4]

def canJump(nums):
    max_jump = 0
    position = 0
    while position < len(nums) - 1:
        max_jump = max(nums[position], max_jump)
        if max_jump < 1:
            return False
        max_jump -= 1
        position += 1

    return True
print(canJump(nums))