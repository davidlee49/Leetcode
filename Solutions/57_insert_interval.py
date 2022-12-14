intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

def insert(intervals, newInterval):
    if not intervals:
        return []
    new_intervals = []
    while intervals:
        if intervals[interval][0] < newInterval[0] < intervals[interval][1] or intervals[interval][0] < newInterval[1] < intervals[interval][1]:
            intervals[interval][0] = min(intervals[interval][0], newInterval[0])
            intervals[interval][1] = max(intervals[interval][1], newInterval[1])

        # if intervals[interval][1] <= intervals[interval - 1][1]:

        if intervals[interval][0] <= intervals[interval - 1][1]:
            intervals[interval - 1][1] = max(intervals[interval - 1][1], intervals[interval][1])











    return intervals

print(insert(intervals, newInterval))