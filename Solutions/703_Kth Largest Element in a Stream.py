import heapq

k = 3
nums = [10, 4, 5, 8, 2, 4, 6, 1, 10, 9]
add = [3, 5, 10, 9, 4]


class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)        #create heap(roughly smallest to largest)

        while len(self.heap) > k:
            heapq.heappop(self.heap)    #pops off the first index and reorganizes array if needed, then returns array


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

obj = KthLargest(k, nums)
print(obj.heap)
# for i in add:
#     obj.add(i)
#     print(obj.heap)

# print(type(obj))