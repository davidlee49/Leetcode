# https://leetcode.com/problems/online-stock-span/


class StockSpanner:
    def __init__(self):
        self.price_history = []


    def next(self, price):
        cur = [price, 1]
        while self.price_history and self.price_history[-1][0] <= price:
            cur[1] += self.price_history.pop()[1]

        self.price_history.append(cur)

        return cur[1]








