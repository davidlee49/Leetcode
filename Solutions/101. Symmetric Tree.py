# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

x = set()
y = TreeNode()
z = TreeNode()
x.add(y)
x.add(z)
print(x)
a = TreeNode()
b = TreeNode()
c = set()
c.add(a)
c.add(b)
print(c)

print(x == c)