class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = height[0], height[len(height) - 1]
        max_height = 0
        max_height_idex = 0
        volume = 0
        for get_height in range(len(height)):
            if height[get_height] > max_height:
                max_height_idex = get_height
                max_height = height[get_height]

        for i in range(0, max_height_idex):
            if height[i] > l:
                l = height[i]
            volume += min(max_height, l) - height[i]

        for i in range(len(height) - 1, max_height_idex, -1):
            if height[i] > r:
                r = height[i]
            volume += min(max_height, r) - height[i]

        return volume