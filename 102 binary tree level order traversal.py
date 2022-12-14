# https://leetcode.com/problems/binary-tree-level-order-traversal/

def levelOrder(root):
    tree_values = []
    cur_level_nodes = []
    cur_level_nodes.append(root)
    def recur_get_bt_tree_vals(cur_level_nodes, tree_values):
        cur_level_values = []
        next_level_nodes = []
        for node in cur_level_nodes:
            cur_level_values.append(node.val)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        tree_values.append(cur_level_values)
        if next_level_nodes:
            recur_get_bt_tree_vals(next_level_nodes, tree_values)
        else:
            return tree_values

    if root:
        recur_get_bt_tree_vals(cur_level_nodes, tree_values)
    print(tree_values)
    return tree_values

x = None
if x:
    print(x)

