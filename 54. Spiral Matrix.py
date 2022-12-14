# https://leetcode.com/problems/spiral-matrix/

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def spiralOrder(matrix):
    # eval every element in matrix O(n)
    # because our return array will have every element, we can use the len(of our return answer) to know we are done
    spiral_nums = []
    rows = len(matrix)
    if not matrix[0]:
        return spiral_nums

    cols = len(matrix[0])

    total_layers = min(cols, rows) // 2


    # get nums in full layers
    for layer_num in range(total_layers+1):

        # traverse top row
        spiral_nums.extend(matrix[layer_num][layer_num: cols - layer_num])
        if len(spiral_nums) == rows * cols:
            break

        # traverse down right
        for col_height in range(layer_num + 1, rows - 1 - layer_num):
            spiral_nums.append(matrix[col_height][-1-layer_num])
        if len(spiral_nums) == rows * cols:
            break
        # traverse bottom row in reverse
        spiral_nums.extend(reversed(matrix[-1 - layer_num][layer_num: cols - layer_num]))
        if len(spiral_nums) == rows * cols:
            break
        # traverse up left side
        for col_height in range(rows -2 - layer_num, layer_num, -1):
            spiral_nums.append(matrix[col_height][layer_num])


    return spiral_nums
print(spiralOrder(nums))
#
