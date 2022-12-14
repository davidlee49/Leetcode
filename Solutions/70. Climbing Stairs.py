#https://leetcode.com/problems/climbing-stairs/

n = 5


def climbStairs(n: int) -> int:
    # there are a couple different things we need to check:
    # if there is a perfect amount of times 1 goes into n
    # if there is a perfect amount of times 2 goes into n
    # find out how many times 2 can go into n to find permutations

    permutations = 0
    step_num = 0
    dp = {}

    def add_steps(permutations, step_num, n):
        if step_num == n:
            return 1
        elif step_num > n:
            return 0

        if step_num in dp:
            permutations += dp[step_num]
        else:
            permutations += add_steps(permutations, step_num + 1, n) + add_steps(permutations, step_num + 2, n)

        dp[step_num] = permutations
        return permutations




    return add_steps(permutations, step_num, n)

print(climbStairs(n))