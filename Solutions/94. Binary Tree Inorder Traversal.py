
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # find base case
        def dfs(node, values):
            if node:
                dfs(node.left, values)
                values.append(node.val)
                dfs(node.right, values)
                return

            return

        values = []
        dfs(root, values)
        return values
