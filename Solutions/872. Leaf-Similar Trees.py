#https://leetcode.com/problems/leaf-similar-trees/description/

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # check to see if all leafs in in the same orders for 2 BST
        # Intuition: this will take a min of O(n) where n is the total nodes in both trees
        # it will take O(k) space where k is the number of leaf nodes in both trees

        # Algo:  we can recursively travel down the trees and save the leafs
        # do the same for the 2nd tree
        # compare

        tree1_leaves, tree2_leaves = [], []

        def BST_recur(node, leaf_array):
            if not node:
                return

            if not node.right and not node.left:
                leaf_array.append(node.val)

            BST_recur(node.left, leaf_array)
            BST_recur(node.right, leaf_array)

            return leaf_array

        return BST_recur(root1, tree1_leaves) == BST_recur(root2, tree2_leaves)
