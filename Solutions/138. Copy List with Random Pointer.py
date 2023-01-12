import copy

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

x = Node(3,3,3)
print(x.next)
print(x.val)
print(x.random)

y = x
print(y.next)
print(y.val)
print(y.random)