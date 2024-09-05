class Solution(object):
    def missingRolls(self, rolls, mean, n):
        # find total number of rolls
        total_rolls = len(rolls) + n
        # calculate current sum
        cur_sum=sum(rolls)
        # calculate number needed for mean
        target = (mean*total_rolls) - cur_sum
        # determine if it fits within the boundaries of possible rolls
        if (n <= target <= n*6):
            # calculate the rolls
            answer = [target//n] * n
            for i in range(target % n):
                answer[i] += 1
            return answer
        else:
            return []