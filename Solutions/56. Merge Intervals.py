#https://leetcode.com/problems/merge-intervals/


intervals = [[1,4],[2,3]]
def merge(intervals):
    #can start on index 1 as anything less than that will have no overlap
    #ovelap occurs when previous stop is > than current start
    merged_intervals = []
    intervals.sort()
    for interval_num in range(1, len(intervals)):
        if intervals[interval_num][0] <= intervals[interval_num - 1][1]:
            intervals[interval_num][0] = intervals[interval_num - 1][0]
            intervals[interval_num][1] = max(intervals[interval_num][1], intervals[interval_num - 1][1])
        else:
            merged_intervals.append(intervals[interval_num-1])
    merged_intervals.append(intervals[-1])
    print(merged_intervals)


merge(intervals)