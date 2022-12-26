# https://leetcode.com/problems/last-stone-weight/
import heapq

stones = [2,7,4,1,8,1]

def lastStoneWeight(stones) -> int:
    for i, s in enumerate(stones):
        stones[i] = -s
    print(stones)
    heapq.heapify(stones)
    while len(stones) >= 2:
        print(stones)
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)
        difference = stone1 - stone2
        if difference < 0:
            heapq.heappush(stones, difference)
    if stones:
        return -stones[0]
    return 0

print(lastStoneWeight(stones))