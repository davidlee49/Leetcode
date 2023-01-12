class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def get_answer(operator, num2, num1):
            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "/":
                return math.trunc(num1 / num2)
            elif operator == "*":
                return num1 * num2

        nums = []
        operators = {"+", "-", "/", "*"}
        for char in tokens:
            if char in operators:
                answer = get_answer(char, nums.pop(), nums.pop())
                nums.append(answer)

            else:
                nums.append(int(char))

        return nums[0]

