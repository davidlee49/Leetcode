# https://leetcode.com/problems/container-with-most-water/

height = [1,1] #[1,8,6,2,5,4,8,3,7]

def maxArea(height):
    l, r = 0, len(height) - 1
    max_volume = 0
    while l != r:
        volume = (r - l) * min(height[l], height[r])
        max_volume = max(volume, max_volume)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return max_volume

maxArea(height)


# we are only given 1 variable, which is the max length of the array
# best case scenario, tallest walls are on the beginning and end, so start with pointers there
# worst case two super tall poles that hold a lot of volume somehwere in betwen
# because we don't know where the tall walls are, then we will have to search each element in the array O(n)
# increment in and compare max volume, if greater replace
# because we already have a max as we go and never need to recalculate older posts, we dont need any extra large data
# structures
