
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        large, small = [], []
        dummy = ListNode(None, head)
        cur_node = dummy
        while cur_node.next:
            if cur_node.next.val >= x:
                large.append(cur_node.next)
            else:
                small.append(cur_node.next)

            cur_node = cur_node.next

        nodes = small + large
        head = nodes[0]

        for i, node in enumerate(nodes):
            if i == len(nodes) - 1:
                node.next = None
            else:
                node.next = nodes[i + 1]

        return head


