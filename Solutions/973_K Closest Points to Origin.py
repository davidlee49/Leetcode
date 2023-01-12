# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
import math

points = [[1,3],[-2,2]]
k = 1

def kClosest(points, k):
    closest_points = []
    for i in range(len(points)):
        points[i] = math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1]), points[i]
    heapq.heapify(points)
    for i in range(k):
        i = heapq.heappop(points)
        closest_points.append(i[1])
    print(points)
    return closest_points

print(kClosest(points, k))
print(points)