class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #we need to explore every number because a large number may give access to a lot of smaller numbers O(n)
        #we can do this recursively
            #find the base case
            #take min of the two paths for all nums available
        dp = {}
        def recur(triangle, cur_row, i, dp):
            if cur_row == len(triangle) - 1:
                return triangle[cur_row][i]

            if (cur_row, i) in dp:
                return dp[(cur_row, i)]

            sums = []
            sums.append(triangle[cur_row][i] + recur(triangle, cur_row + 1, i, dp))
            sums.append(triangle[cur_row][i] + recur(triangle, cur_row + 1, i + 1, dp))

            dp[(cur_row, i)] = min(sums)
            return dp[(cur_row, i)]

        return recur(triangle, 0, 0, dp)