#https://leetcode.com/problems/maximum-profit-in-job-scheduling/

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]


def jobScheduling(startTime, endTime, profit):
    max_profit = 0
    # find all combinations of times that do not overlap
    # need to sort times

    jobs = zip(startTime, endTime)
    # grouped_jobs_time = [[]] * 10**9
    grouped_jobs_time = [[None]]*10

    for job in jobs:
        if grouped_jobs_time[job[0]][0] == None:
            grouped_jobs_time[job[0]] = [job]
        else:
            grouped_jobs_time[job[0]].append(job)

    # for combo in grouped_jobs_time:
    #





    print(grouped_jobs_time)

    # calculate profits for each combination
    # probably will need to do some dynamic programming


jobScheduling(startTime,endTime,profit)