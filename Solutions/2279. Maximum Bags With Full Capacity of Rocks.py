#https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

def maximumBags(self, capacity, rocks, additionalRocks):
    fullest_bags = []
    for i in range(len(capacity)):
        difference = capacity[i] - rocks[i]
        fullest_bags.append(difference)

    fullest_bags.sort()

    filled_bags = 0
    for difference in fullest_bags:
        additionalRocks -= difference
        if additionalRocks < 0:
            break
        filled_bags += 1

    return filled_bags