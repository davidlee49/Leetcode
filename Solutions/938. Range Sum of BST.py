#https://leetcode.com/problems/range-sum-of-bst/

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        if root is None:
            return root

        # recursively go through BST, adding to sum along the way

        def bst_reccur(node, low, high, total):
            if node is None:
                return total

            print(total)
            if low <= node.val <= high:
                total += node.val
            print(total, node.val)
            total = bst_reccur(node.left, low, high, total)
            total = bst_reccur(node.right, low, high, total)

            return total

        return bst_reccur(root, low, high, total)