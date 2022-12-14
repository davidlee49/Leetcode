#https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque()
        node_and_depth = (root, 1)
        q.append(node_and_depth)

        while q:
            node, depth = q.popleft()
            if node.right is None and node.left is None:
                return depth

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

