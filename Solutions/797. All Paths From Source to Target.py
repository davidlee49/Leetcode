class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        stack = [[0]]

        while stack:
            cur_path = stack.pop()
            for node in graph[cur_path[-1]]:
                if node == len(graph) - 1:
                    output.append(cur_path + [node])
                else:
                    stack.append(cur_path + [node])

        return output