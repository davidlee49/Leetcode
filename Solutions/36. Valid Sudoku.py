#https://leetcode.com/problems/valid-sudoku/

board = [
    [".","8","7","6","5","4","3","2","1"],
    ["2",".",".",".",".",".",".",".","."],
    ["3",".",".",".",".",".",".",".","."],
    ["4",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".",".","."],
    ["6",".",".",".",".",".",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    ["8",".",".",".",".",".",".",".","."],
    ["9",".",".",".",".",".",".",".","."]]

def isValidSudoku(board):
    valid = {
        "square0": set(),
        "square1": set(),
        "square2": set(),
        "square3": set(),
        "square4": set(),
        "square5": set(),
        "square6": set(),
        "square7": set(),
        "square8": set(),
        "c0": set(),
        "c1": set(),
        "c2": set(),
        "c3": set(),
        "c4": set(),
        "c5": set(),
        "c6": set(),
        "c7": set(),
        "c8": set(),
        "r0": set(),
        "r1": set(),
        "r2": set(),
        "r3": set(),
        "r4": set(),
        "r5": set(),
        "r6": set(),
        "r7": set(),
        "r8": set(), }
    for row in range(len(board)):
        for column, number in enumerate(board[row]):
            if number in valid[f"c{column}"]:
                return False
            elif number == ".":
                pass
            else:
                valid[f"c{column}"].add(number)

            if number in valid[f"r{row}"]:
                return False
            elif number == ".":
                pass
            else:
                valid[f"r{row}"].add(number)

            if number in valid[f"square{row // 3 * 3 + column // 3}"]:
                return False
            elif number == ".":
                pass
            else:
                valid[f"square{row // 3 * 3 + column // 3}"].add(number)

    return True

print(isValidSudoku(board))

