# https://leetcode.com/problems/3sum-closest/
import math
nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2


def threeSumClosest(nums, target):

    nums.sort()
    closest = math.inf
    closest_sum = None

    for index, num in enumerate(nums):
        l, r = index + 1, len(nums) - 1
        while l < r:
            if abs(target - (num + nums[l] + nums[r])) < closest:
                closest = abs(target - (num + nums[l] + nums[r]))
                closest_sum = num + nums[l] + nums[r]

            if nums[l] + nums[r] < target - num:
                l += 1
            else:
                r -= 1

    return closest_sum


print(threeSumClosest(nums, target))