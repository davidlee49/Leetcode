class Solution(object):
    def shuffle(self, nums, n):
        #find x and y staring pos
        x_i = 0
        y_i = len(nums) // 2
        new_nums = []

        #append x and y
        while y_i < len(nums):
            new_nums.extend([nums[x_i], nums[y_i]])

            # increment to the x and y pos
            x_i += 1
            y_i += 1



        return new_nums
