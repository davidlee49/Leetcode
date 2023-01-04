#https://leetcode.com/problems/remove-stones-to-minimize-the-total/
import heapq

def minStoneSum(piles, k):
    for i in range(len(piles)):
        piles[i] = piles[i] * -1

    heapq.heapify(piles)
    for i in range(k):
        num = heapq.heappop(piles)
        num //= 2
        heapq.heappush(piles, num)

    return sum(piles) * -1

piles = [1391,5916]
k = 3
print(minStoneSum(piles, k))