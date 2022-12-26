# https://leetcode.com/problems/set-mismatch/

#this one was tricky only in that you need to understand that [nums] is not sorted, although the examples look like it

def findErrorNums(nums):
    correct_sum = 0
    given_sum = sum(nums)
    given_set_sum = sum(set(nums))
    for i in range(1, len(nums) + 1):
        correct_sum = correct_sum + i
    answer = [given_sum -given_set_sum, correct_sum - given_set_sum]
    return answer