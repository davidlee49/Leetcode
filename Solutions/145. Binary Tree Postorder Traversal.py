# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recur(cur_node):
            if cur_node is None:
                return []
            return recur(cur_node.left) + recur(cur_node.right) + [cur_node.val]

        return recur(root)





