#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

def lowestCommonAncestor(root, p, q):
    # will need to look at every node O(n)
    # in order to find a lower ancestor p and q need to be on the same side so thier values must be lower than the value
    # of their parent node

    #if p or q are not both on the right or both on the left we can return the current node
    #if either the val of p or q are the same as the current node, we know that is the lowest common ansestor

    if p.val == root.val or q.val == root.val:
        return root

    if min(p.val, q.val) < root.val <max(p.val, q.val):
        return root

    if p.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return lowestCommonAncestor(root.left, p, q)

