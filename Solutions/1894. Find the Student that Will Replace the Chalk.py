class Solution(object):
    def chalkReplacer(self, chalk, k):
        # find the total number of chalk used in 1 round. we can divide k by this to find which student it will run out on in 1 pass
        sum_used = sum(chalk)
        remainder = k % sum_used
        # iterate through chalk to find the student
        for student, chalk_used in enumerate(chalk):
            if chalk_used > remainder:
                return student

            remainder -= chalk_used


