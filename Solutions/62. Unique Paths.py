#https://leetcode.com/problems/unique-paths/

rows = 3
cols = 7

def uniquePaths(m, n):

    def breath_recur(m, n):
        if m == 0 and n == 0:
            return 0
        if n > 0:
            return 1 + breath_recur(m, n-1) + breath_recur(m-1, n)
        if m > 0:
            return 1 + breath_recur(m-1, n)




    path_count = 0
    path_count += breath_recur(m, n)
    print(path_count)
    return path_count

uniquePaths(rows, cols)