# https://leetcode.com/problems/last-stone-weight/description/
import heapq

def lastStoneWeight(stones):
    stones = [-val for val in stones]
    heapq.heapify(stones) #O(n)

    stone1 = heapq.heappop(stones)
    while stones:
        stone2 = heapq.heappop(stones)

        stone1 = abs(stone1-stone2)
        if stone1 == 0 and not stones:
            break

        stone1 = heapq.heappushpop(stones, -stone1)

    return abs(stone1)



stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))