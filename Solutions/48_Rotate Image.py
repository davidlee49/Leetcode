#https://leetcode.com/problems/rotate-image/


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


def rotate(matrix):
    matrix_layers = len(matrix) // 2

    for i in range(matrix_layers):
        x, y = i, i
        x_temp = i
        row = i
        for col in range(i, len(matrix) - i - 1):
            y = col
            cur_val = matrix[x][y]
            prev_val = matrix[x][y]
            for rotate in range(4):
                prev_val = cur_val
                x_temp = x
                x = y
                y = len(matrix) - 1 - x_temp
                cur_val = matrix[x][y]
                matrix[x][y] = prev_val

rotate(matrix)
