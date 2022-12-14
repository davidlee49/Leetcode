
def isUgly(n: int) -> bool:
    if n == 1:
        return True
    if n > 0:
        while n % 5 == 0:
            n = n // 5
            if n == 1:
                return True
        while n % 2 == 0:
            n = n //2
            if n == 1:
                return True
        while n % 3 == 0:
            n = n // 3
            if n == 1:
                return True
    else:
        return False

n = 8
print(isUgly(n))