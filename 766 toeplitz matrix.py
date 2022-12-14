#https://leetcode.com/problems/toeplitz-matrix/

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

def isToeplitzMatrix(matrix):
    toeplitz_condition = None
    if matrix:
        for row in range(len(matrix)):
            if toeplitz_condition is None or matrix[row][1:] == toeplitz_condition:
                toeplitz_condition = matrix[row][:-1]
                continue
            else:
                return False
        return True

isToeplitzMatrix(matrix)



