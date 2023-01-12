class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        output = []

        ordered_sums = []
        cur_total = 0

        for num in nums:
            cur_total += num
            ordered_sums.append(cur_total)

        for index, query in enumerate(queries):
            for i, cur_sum in enumerate(ordered_sums):
                if cur_sum > query:
                    output.append(i)
                    break

            if len(output) - 1 != index:
                output.append(len(ordered_sums))

        return output