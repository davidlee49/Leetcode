# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        LL = []

        if not root:
            return root

        def recur(LL, node):
            if not node:
                return

            LL.append(node)
            recur(LL, node.left)
            recur(LL, node.right)

        recur(LL, root)

        for i, node in enumerate(LL):
            if i == len(LL) - 1:
                node.right = None
                node.left = None
                break
            node.right = LL[i + 1]
            node.left = None

        return LL[0]
