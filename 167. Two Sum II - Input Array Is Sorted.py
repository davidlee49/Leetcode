#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


numbers = [2,7,11,15]
target = 9
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l != r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        if numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1


twoSum(numbers, target)