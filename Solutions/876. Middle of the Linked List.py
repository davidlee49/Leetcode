#https://leetcode.com/problems/middle-of-the-linked-list/

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    node = head
    nodes = []
    while node is not None:
        nodes.append(node)
        node = node.next

    return nodes[len(nodes) // 2]