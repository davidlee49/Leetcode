#https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    leaf_max_diff = []

    if root is None:
        return root

    max_num = root.val
    min_num = root.val
    max_diff = -1

    def get_max_diff(leaf_max_diff, max_num, min_num, node, max_diff):
        if node is None:
            return

        max_diff = max(abs(min_num - node.val), abs(max_num - node.val), max_diff)

        max_num = max(node.val, max_num)
        min_num = min(node.val, min_num)

        if not node.left and not node.right:
            leaf_max_diff.append(max_diff)
            return

        get_max_diff(leaf_max_diff, max_num, min_num, node.left, max_diff)
        get_max_diff(leaf_max_diff, max_num, min_num, node.right, max_diff)

    get_max_diff(leaf_max_diff, max_num, min_num, root, max_diff)

    return max(leaf_max_diff)