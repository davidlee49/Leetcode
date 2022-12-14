# https://leetcode.com/problems/remove-element/
nums = [1]
val = 1

def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
removeElement(nums, val)