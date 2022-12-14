#https://leetcode.com/problems/minimum-average-difference/
import sys

nums = [0]
def minimumAverageDifference(nums) -> int:
    min_avg_diffs_index = None
    min_average = sys.maxsize
    divisor = sum(nums)
    dividend = 0

    # find the average difference for all elements in nums
    for i in range(len(nums)):
        divisor -= nums[i]
        dividend += nums[i]

        if i == len(nums) - 1:
            avg_diff = abs(dividend // (i + 1))
        else:
            avg_diff = abs((dividend // (i + 1)) - (divisor // (len(nums) - (i + 1))))


        if avg_diff < min_average:
            min_average = avg_diff
            min_avg_diffs_index = i

    return min_avg_diffs_index

print(minimumAverageDifference(nums))