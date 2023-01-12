#https://leetcode.com/problems/climbing-stairs/

nums = [1, 3]
target = 3


def searchInsert(nums, target):
    l, r = 0, len(nums) - 1
    mid = (l + r) // 2

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            r = mid - 1

        else:
            l = mid + 1

    if nums[mid] < target:
        return mid + 1
    else:
        return mid


print(searchInsert(nums, target))