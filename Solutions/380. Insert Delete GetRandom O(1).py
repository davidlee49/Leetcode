#https://leetcode.com/problems/insert-delete-getrandom-o1/


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.nums_loc = {}

    def insert(self, val: int) -> bool:
        if val not in self.nums_loc:
            self.nums.append(val)
            self.nums_loc[val] = len(self.nums) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.nums_loc:
            if self.nums[-1] == val:
                self.nums_loc.pop(self.nums.pop())
                return True

            else:

                swap_loc = self.nums_loc[val]
                swap_val = self.nums[-1]

                self.nums[-1], self.nums[self.nums_loc[val]] = self.nums[self.nums_loc[val]], self.nums[-1]

                self.nums_loc.pop(self.nums.pop())
                self.nums_loc[swap_val] = swap_loc

                return True

        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)

x = RandomizedSet()
print(x.insert(1))
print(x.insert(2))
print(x.insert(3))
print(x.insert(4))
print(x.insert(5))

print(x.remove(0))
print(x.remove(1))
print(x.remove(2))
print(x.remove(3))
print(x.remove(4))
print(x.remove(5))

print(x.insert(0))
print(x.insert(0))