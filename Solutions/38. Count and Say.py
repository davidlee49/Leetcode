class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(n)

        say = self.countAndSay(n-1)
        say_array = []
        cur_num = []

        for char in say:
            if not cur_num:
                cur_num.extend((1, char))
                continue

            if char != cur_num[1]:
                cur_num[0] = str(cur_num[0])
                say_array.extend(cur_num)
                cur_num[1], cur_num[0] = char, 1

            else:
                cur_num[0] += 1

        cur_num[0] = str(cur_num[0])
        x = "".join(say_array + cur_num)
        return x