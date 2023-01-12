def removeDuplicates(self, nums):
    l, r = 0, 1
    if len(nums) < 2:
        return r
    while r < len(nums):
        if nums[r] == nums[l]:
            nums[r] = None
            r += 1
            continue
        if nums[l + 1] is None:
            nums[l + 1] = nums[r]
            nums[r] = None
            l += 1
            r += 1
        else:
            r += 1
            l += 1

    l += 1
    return l