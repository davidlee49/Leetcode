#https://leetcode.com/problems/same-tree/



def isSameTree(p, q):
    p_node, q_node = p, q
    if not p_node and not q_node:
        return True
    if not p_node or not q_node or p_node.val != q_node.val:
        return False
    return self.isSameTree(p_node.right, q_node.right) and self.isSameTree(p_node.left, q_node.left)