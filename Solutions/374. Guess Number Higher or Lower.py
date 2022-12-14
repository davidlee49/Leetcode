#https://leetcode.com/problems/guess-number-higher-or-lower/

def guessNumber(self, n: int) -> int:
    low_num, high_num = 0, n
    mid = (low_num + high_num) // 2

    while guess(mid) != 0:
        if guess(mid) == -1:
            high_num = mid - 1
        else:
            low_num = mid + 1
        mid = (low_num + high_num) // 2

    return mid