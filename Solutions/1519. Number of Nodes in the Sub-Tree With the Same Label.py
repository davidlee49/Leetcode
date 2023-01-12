class Solution(object):
    def countSubTrees(self, n, edges, labels):
        # Intuition:
        # because the quantity of the labels depends on the subtree, it makes sense to start at the bottom and work your way back
        # from the bottom we can check the next level up, if they are the same we can increment the frequency

        # we can preprocess the edges so we dont have to look for them: reduce O(n2) to O(n)
        node_connections = list([] for i in range(n) if i == i)

        for node1, node2 in edges:
            node_connections[node1].append(node2)
            node_connections[node2].append(node1)

        # create a set so that we dont go in a cycle
        seen_nodes = set()
        like_labels_in_subtree = [None] * n

        # recursively find base case (leaf nodes)
        def get_like_labels(node_connections, labels, cur_node, seen_nodes, like_labels_in_subtree):
            # because we are only given edges ie [1,4] we dont know if 1 or 4 is the leaf so we have to check both and there is no base case
            # keep track of the node letter
            label_count = collections.Counter({labels[cur_node]: 1})
            seen_nodes.add(cur_node)
            for node in node_connections[cur_node]:
                if node in seen_nodes:
                    continue
                label_count.update(get_like_labels(node_connections, labels, node, seen_nodes, like_labels_in_subtree))

            like_labels_in_subtree[cur_node] = label_count[labels[cur_node]]
            return label_count

        get_like_labels(node_connections, labels, 0, seen_nodes, like_labels_in_subtree)
        return like_labels_in_subtree






