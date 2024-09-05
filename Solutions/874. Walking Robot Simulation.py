# https://leetcode.com/problems/walking-robot-simulation/?submissionId=1379252150

class Solution(object):
    def robotSim(self, commands, obstacles):
        cur_pos = [0, 0]
        obstacles = set([tuple(i) for i in obstacles])
        cardinal = ['north', 'east', 'south', 'west']
        cur_card = 0
        cardinal_trav = {
            'north': [0, 1], 'south': [0, -1], 'east': [1, 0], 'west': [-1, 0]
        }
        max_dist = 0

        # iterate through the commands O(n)
        for command in commands:
            # calculate direction or...
            if command < 0:
                if command == -1:
                    cur_card = (cur_card + 1) % 4
                else:
                    cur_card = (cur_card - 1) % 4

            # iterate through the movement and check if it intersects with an obstable, stopping if it does
            else:
                for i in range(command):
                    x, y = cur_pos
                    next_pos = x + cardinal_trav[cardinal[cur_card]][0], y + cardinal_trav[cardinal[cur_card]][1]

                    if next_pos in obstacles:
                        break

                    cur_pos = next_pos
                    max_dist = max(max_dist, (cur_pos[0] ** 2) + (cur_pos[1] ** 2))

        return max_dist