class Solution(object):
    def findMinArrowShots(self, points):

        points.sort()

        output = 1
        group_l, group_r = points[0]

        for point in points:
            if point[0] > group_r:
                output += 1
                group_l, group_r = point
                continue
            group_l = point[0]
            group_r = min(group_r, point[1])

        return output