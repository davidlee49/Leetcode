
def construct2DArray(self, original, m, n):
    if m*n != len(original):
        return []
    answer = []
    for i in range(m):
        answer.append(original[i*n: (i+1)*n])
    return answer