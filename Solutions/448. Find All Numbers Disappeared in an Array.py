#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    # create set from nums
    n = len(nums)
    nums = set(nums)
    output = []

    # iterate through all potential nums
    for i in range(1, n + 1):
        # check if in set
        # if not add to output
        if i not in nums:
            output.append(i)

    return output