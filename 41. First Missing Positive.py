#https://leetcode.com/problems/first-missing-positive/

nums = [1,1]

def firstMissingPositive(nums):

    for i in range(len(nums)):
        if nums[i] == i + 1:
            pass

        while nums[i] != (i + 1):
            if 0 < nums[i] <= len(nums):
                if nums[nums[i]-1] == nums[i]:
                    break
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

            else:
                nums[i] = 0
                break

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1

    return len(nums) + 1


print(firstMissingPositive(nums))