#https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target) -> int:
    # binary search through the array
    # problem 1: handle case if mid is not expected
    # establish boundaries of the array
    # in the case of the where mid is not l < mid < r:

    l, r = 0, len(nums) - 1
    mid = (l + r) // 2

    # complete binary search on sorted side

    def binary_search_sorted(nums, l, r, mid):
        while l <= r:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
                mid = (l + r) // 2
            else:
                l = mid + 1
                mid = (l + r) // 2

        return -1

    # complete binary search on jumbled side
    while l <= r:
        if nums[mid] == target:
            return mid
        elif (nums[mid] > target and nums[mid] > target >= nums[l]) or (nums[mid] < target and nums[mid] < target <= nums[r]):
            return binary_search_sorted(nums, l, r, mid)
        elif nums[mid] >= nums[l]:
            l = mid + 1
            mid = (l + r) // 2
        else:
            r = mid - 1
            mid = (l + r) // 2

    return -1


nums = [3,1]
target = 1

print(search(nums, target))
