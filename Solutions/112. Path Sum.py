#https://leetcode.com/problems/path-sum/

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    cur_sum = 0

    def DFS(node, cur_sum, targetSum):
        if not node:
            return

        if node.right is None and node.left is None:
            return targetSum == cur_sum + node.val

        return DFS(node.left, cur_sum + node.val, targetSum) or DFS(node.right, cur_sum + node.val, targetSum)

    if root:
        return DFS(root, cur_sum, targetSum)

    return False

