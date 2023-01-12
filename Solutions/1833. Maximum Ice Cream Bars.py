class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        cur_total = 0
        bars = 0

        for cost in costs:
            if cost + cur_total <= coins:
                cur_total += cost
                bars += 1
            else:
                break
        return bars