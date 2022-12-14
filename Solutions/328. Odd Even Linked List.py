#https://leetcode.com/problems/odd-even-linked-list/

def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    odd_head = head
    odd_last = head
    even_head = None
    even_last = None
    cur_node = None

    # populate starter nodes (since main algo is based on .next logic)
    if head:
        odd_head = head
        odd_last = odd_head

    else:
        return head

    if odd_head.next:
        even_head = odd_head.next
        even_last = even_head
        cur_node = even_last.next

    else:
        return head

        # go through list and find odds
    while cur_node:
        # go through list and find odds
        if cur_node:
            odd_last.next = cur_node
            cur_node = cur_node.next
            odd_last = odd_last.next

        # go through list and find evens
        if cur_node:
            even_last.next = cur_node
            cur_node = cur_node.next
            even_last = even_last.next

    even_last.next = None
    odd_last.next = even_head

    # return head of odd
    return odd_head