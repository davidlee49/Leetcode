#https://leetcode.com/problems/perfect-squares/
import math
n = 13


class Solution:
    def __init__(self):
        self.dp = {
        }
        self.squares = []

        num = 1
        while num**2 <= 10**4:
            self.squares.append(num**2)
            self.dp[num**2] = 1
            num += 1

    def numSquares(self, n):
        if n in self.dp:
            return self.dp[n]

        closest_square = int(math.sqrt(n))
        for square in range(closest_square, 0, -1):
            total_addens = 1
            sum = n - closest_square**2
            if sum not in self.dp:
                self.numSquares(sum)

            total_addens += self.dp[sum]
            if n not in self.dp or self.dp[n] > total_addens:
                self.dp[n] = total_addens

            if closest_square == 1 or (n // (closest_square - 1)**2) > self.dp[n]:
                break

            closest_square -= 1

        return self.dp[n]


    # def add_DP_num(self, n):
    #     closest_square = int(math.sqrt(n))
    #
    #
    #     for square in range(closest_square, 0, -1):
    #         total_addens = 1
    #         sum = n - closest_square**2
    #         if sum not in self.dp:
    #             self.add_DP_num(sum)
    #
    #         total_addens += self.dp[sum]
    #         if n not in self.dp or self.dp[n] > total_addens:
    #             self.dp[n] = total_addens
    #
    #         if closest_square == 1 or (n // (closest_square - 1)**2) > self.dp[n]:
    #             break
    #
    #         closest_square -= 1












question = Solution()
print(question.numSquares(n))