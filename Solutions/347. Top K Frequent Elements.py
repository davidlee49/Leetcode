#https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
import heapq
# This is turns out to be a O(n log n) solution


def topKFrequent(nums, k):
    # Create a counter to find the frequencies
    # Create a heap (organized by frequencies)
    nums = Counter(nums)
    items = [[count, num] for num, count in dict(nums).items()]

    answer = heapq.nlargest(k, items)
    answer = [val for freq, val in answer]

    return answer


# Realizing that if all numbers are unique in nums and if K was the length of nums, then nlargest would be n log n
# We can use a round about, confusing way to create a "beter" time complexity
# by using bucket sorting after we created a counter and using implicit logic of the array index to match frequency

def topKFrequent(nums, k):
    og = nums
    nums = Counter(nums)

    items = nums.items()
    bucket = [[] for _ in range(len(og) + 1)]
    print(bucket)

    for num, freq in items:
        print(num, freq)
        bucket[freq].append(num)

    answer = []
    for i in bucket[::-1]:
        answer.extend(i)
        if len(answer) == k:
            return answer