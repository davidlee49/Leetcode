def arrangeCoins(n: int) -> int:
    count, row_len = 0, 0

    while count < n:
        count += row_len
        row_len += 1

    if count == n:
        return row_len
    else:
        return row_len - 1
