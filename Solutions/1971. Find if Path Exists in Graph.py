#https://leetcode.com/problems/find-if-path-exists-in-graph/description/

def validPath(n, edges, source, destination):
    nodes = {}
    for i in range(n):
        nodes[i] = [i]
    for node1, node2 in edges:
        if node1 not in nodes:
            nodes[node1] = [node2]
        else:
            nodes[node1].append(node2)

        if node2 not in nodes:
            nodes[node2] = [node1]
        else:
            nodes[node2].append(node1)



    def node_recur(nodes, cur_node, destination, nodes_to_explore, seen_nodes):
        if destination in nodes[cur_node]:
            return True

        for node in nodes[cur_node]:
            if node not in seen_nodes:
                nodes_to_explore.append(node)
                seen_nodes.add(node)

        while nodes_to_explore:
            return node_recur(nodes, nodes_to_explore.pop(), destination, nodes_to_explore, seen_nodes)

        return False


    nodes_to_explore = [source]
    seen_nodes = {source}
    return node_recur(nodes, nodes_to_explore.pop(), destination, nodes_to_explore, seen_nodes)






print(validPath(n, edges, source, destination))