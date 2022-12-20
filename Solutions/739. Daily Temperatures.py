
def dailyTemperatures(temperatures):
    # go through temps
    # we can immediately add to answers if the next day is greater
    # if the next day is cooler, then we can make a stack until we reach a hotter day than the last element in the stack
    prev_temps = []
    cur_day = 1
    answer = [0] * len(temperatures)



    prev_temps.append((temperatures[0], 0))


    while cur_day < len(temperatures):
        while prev_temps and temperatures[cur_day] > prev_temps[-1][0]:
            position = prev_temps.pop()[1]
            days_waited = cur_day - position
            answer[position] = days_waited

            # prev_temps.append((temperatures[cur_day], cur_day))
        prev_temps.append((temperatures[cur_day], cur_day))

        cur_day += 1

    return answer