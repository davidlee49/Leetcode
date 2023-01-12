# https://leetcode.com/problems/happy-number/

def isHappy(n):
    known_sum = set()
    sum = 0
    while True:
        while n != 0:
            sum += (n % 10)**2
            n = n//10
        if sum == 1:
            return True
        else:
            if sum in known_sum:
                return False
            known_sum.add(sum)
            n = sum
            sum = 0


print(isHappy(2))