class Solution(object):
    def minimumRounds(self, tasks):
        # intuition:
        # we need to sort the tasks by difficulty and difficulty freq
        # from there we can divide parse it out into 2 or 3
        # figure out if we need to use DP to find groups or a find formula
        # formula is if %3 == 1 then there will be two groups of 2
        # edge case is if group only has 1

        output = 0
        # make a counter for tasks O(n)
        task_counter = collections.Counter(tasks)

        # make a fn for the formula
        def get_rounds(freq):
            if freq == 1:
                return -1
            elif freq == 2:
                return 1

            groups_of_3 = 0
            groups_of_2 = 0

            groups_of_3 = freq // 3
            freq %= 3
            if freq == 1:
                groups_of_3 -= 1
                groups_of_2 = 2
            elif freq == 2:
                groups_of_2 = 1

            return groups_of_2 + groups_of_3
            # returns how many rounds

        # iterate through counter to find rounds per task group
        for i in task_counter:
            num_of_rounds = get_rounds(task_counter[i])
            if num_of_rounds == -1:
                return -1
            output += num_of_rounds

        return output