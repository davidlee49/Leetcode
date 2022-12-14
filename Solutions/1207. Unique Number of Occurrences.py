#https://leetcode.com/problems/unique-number-of-occurrences/

def uniqueOccurrences(self, arr: List[int]) -> bool:
    unique_nums = {}
    for num in arr:
        if num in unique_nums:
            unique_nums[num] += 1
        else:
            unique_nums[num] = 1

    if len(set(unique_nums.values())) != len(unique_nums):
        return False
    return True