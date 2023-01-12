# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    possible_solutions = {}
    first_num = 0
    while first_num < len(nums):
        second_num = target - nums[first_num]
        if second_num not in possible_solutions:
            possible_solutions[nums[first_num]] = first_num
            first_num += 1
        else:
            print([first_num, possible_solutions[second_num]])
            return [first_num, possible_solutions[second_num]]

twoSum(nums, target)