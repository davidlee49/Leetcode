class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree_nodes = {}
        seen_nodes = set()

        for i in range(len(hasApple)):
            tree_nodes[i] = []

        for parent, child in edges:
            tree_nodes[parent].append(child)
            tree_nodes[child].append(parent)

        def recur(tree_nodes, hasApple, node, seen_nodes):
            seen_nodes.add(node)
            time = 0
            for child in tree_nodes[node]:
                if child in seen_nodes:
                    continue
                time += recur(tree_nodes, hasApple, child, seen_nodes)
            if (hasApple[node] or time > 0) and node != 0:
                time += 2
            return time

        return recur(tree_nodes, hasApple, 0, seen_nodes)


