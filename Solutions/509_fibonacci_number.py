# https://leetcode.com/problems/fibonacci-number/

n = 5

def fib(n: int) -> int:
    first = 0
    second = 1
    answer = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    while n != 1:
        answer = first + second
        first = second
        second = answer
        n -= 1
    return answer

fib(n)

def recursive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n - 1) + recursive_fib(n - 2)

recursive_fib(n)


