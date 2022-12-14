#https://leetcode.com/problems/rectangle-area/

#find the area of both rectangles
    #find area of rect 1 and 2
    #problem 1: if rectangles overlap they take up the same space, find how to subtract the overlap from total area
        #another way to say this would be

ax1 = -3
ay1 = -3
ax2 = 3
ay2 = 3
bx1 = 4
by1 = -5
bx2 = 5
by2 = 0


def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    rect1 = 0
    rect2 = 0
    overlap = 0

    rect1 = (ax2 - ax1) * (ay2 - ay1)
    rect2 = (bx2 - bx1) * (by2 - by1)

    max_x_length = (ax2 - ax1) + (bx2 - bx1)
    max_y_length = (ay2 - ay1) + (by2 - by1)

    if max(ax2, bx2) - min(ax1, bx1) >= max_x_length:
        return rect1 + rect2
    if max(ay2, by2) - min(ay1, by1) >= max_y_length:
        return rect1 + rect2

    overlap_x = min(ax2, bx2) - max(ax1, bx1)
    overlap_y = min(ay2, by2) - max(ay1, by1)

    overlap = overlap_x * overlap_y
    if overlap == rect1 or overlap == rect2:
        return max(rect1, rect2)
    return rect1 + rect2 - overlap


print(computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))