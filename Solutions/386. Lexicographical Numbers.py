# https://leetcode.com/problems/lexicographical-numbers/?envType=daily-question&envId=2024-09-23

def lexicalOrder(self, n):
    result = []
    current = 1
    for _ in range(n):
        result.append(current)
        if current * 10 <= n:
            current *= 10
        elif current % 10 != 9 and current + 1 <= n:
            current += 1
        else:
            while (current // 10) % 10 == 9:
                current //= 10
            current = current // 10 + 1
    return result