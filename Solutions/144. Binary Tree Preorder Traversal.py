# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # store values in array
        nums = []
        stack = []

        cur_node = root

        while cur_node or stack:
            while cur_node:
                nums.append(cur_node.val)
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop().right

        return nums
