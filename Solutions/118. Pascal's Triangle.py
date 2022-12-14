#https://leetcode.com/problems/pascals-triangle/

numRows = 5

def generate(numRows: int):
    rows = [[1]]

    if numRows > 1:
        for row in range(numRows - 1):
            prev_row = rows[-1]
            rows.append([1])

            for i in range(len(prev_row) - 1):
                rows[-1].append(prev_row[i] + prev_row[i + 1])

            rows[-1].append(1)

    return rows

print(generate(numRows))