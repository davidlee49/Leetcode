# #https://leetcode.com/problems/trapping-rain-water/



#THIS WAS DONE WRONG AND CALCULATES WHICH POOL WOULD BE THE LARGEST NOT THE TOTAL AMOUNT TRAPPED!!!!
#BUT IT TOOK ME FOREVER SO I SAVED IT



height = [0,1,0,2,1,0,1,3,2,1,2,1]
def trap(height):
    max_height = 0
    max_height_index = 0

    max_volume = 0
    l, r = 0, 0

    if len(height) < 3:
        return 0

    while height[l+1] >= height[l]:
        if l == len(height) - 1:
            return 0
        l += 1
    r = l+1
    local_height = height[l]
    local_height_index = l
    max_height = height[l]
    max_height_index = l
    volume_slice = 0

    while volume_slice < len(height):
        local_volume = 0
        while r < len(height) - 1 and height[r + 1] < height[r]:
            r += 1
            if r == len(height) - 1:
                return max_volume

        while r < len(height) - 1 and height[r + 1] > height[r]:
            r += 1



        if height[r] > local_height:
            volume_slice = max_height_index + 1
            while volume_slice != r:
                local_volume += min(max_height, height[r]) - height[volume_slice]
                volume_slice += 1

        else:
            volume_slice = local_height_index + 1
            while volume_slice != r:
                local_volume += min(local_height, height[r]) - height[volume_slice]
                volume_slice += 1

        max_volume = max(max_volume, local_volume)

        if height[r] >= max_height:
            max_height = height[r]
            max_height_index = r
        local_height = height[r]
        local_height_index = r
        if r == len(height)-1:
            break

    return max_volume





print(trap(height))