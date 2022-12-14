#https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

def lenLongestFibSubseq(self, arr: List[int]) -> int:
    longest = 0
    nums = set(arr)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            last_num, target = arr[j], arr[i] + arr[j]
            count = 2

            while target in nums:
                count += 1
                last_num, target = target, last_num + target

            if count >= 3:
                longest = max(longest, count)

    return longest


[].sorted