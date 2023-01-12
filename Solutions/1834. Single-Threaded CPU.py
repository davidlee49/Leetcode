class Solution(object):
    def getOrder(self, tasks):
        heap = []
        heapq.heapify(heap)
        cur_time = 0
        task_order = []
        total_tasks = len(tasks)

        for i, task in enumerate(tasks):
            task.append(i)

        tasks.sort(reverse=True)

        while len(task_order) != total_tasks:
            # check heap for available tasks
            if not heap and tasks and cur_time < tasks[-1][0]:
                cur_time = tasks[-1][0]


            while tasks and cur_time >= tasks[-1][0]:
                heapq.heappush(heap, tasks.pop()[1:])



            next_task = heapq.heappop(heap)
            task_order.append(next_task[1])
            cur_time += next_task[0]


        return task_order