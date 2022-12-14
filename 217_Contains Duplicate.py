#https://leetcode.com/problems/contains-duplicate/



nums = [1,1,1,3,3,4,3,2,4,2]

def containsDuplicate(nums):
    # traverse lists
    known_nums = set()

    for num in nums:
        if num in known_nums:
            return True

        known_nums.add(num)

    return False




print(containsDuplicate(nums))