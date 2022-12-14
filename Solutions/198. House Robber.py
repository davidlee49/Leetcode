#https://leetcode.com/problems/house-robber/
nums = [2,5,50,60,100,9, 1, 1, 1]
def rob(self, nums: List[int]) -> int:
    # we want the most valuable houses
    # future houses will change the decision of previous houses AND
    # there is no way to know which would be the most valuable house from the starting position
    # because of this we can use DP to keep track of previous calculations

    def next_house_recur(i, cur_sum):
        if i > len(nums) - 1:
            return cur_sum

        if i == len(nums) - 1 or i == len(nums) - 2:
            new_sum = cur_sum + nums[i]
            dp[i] = new_sum
            return new_sum

        if cur_sum + nums[i] <= dp[i]:
            return 0

        new_sum = cur_sum + nums[i]
        dp[i] = new_sum

        return max(next_house_recur(i + 2, new_sum), next_house_recur(i + 3, new_sum))

    cur_sum = 0
    dp = {}
    for i in range(len(nums)):
        dp[i] = 0

    return max(next_house_recur(0, cur_sum), next_house_recur(1, cur_sum))