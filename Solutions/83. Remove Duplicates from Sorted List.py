def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(101, head)
    prev_node = dummy
    cur_node = head

    while cur_node:
        if prev_node.val == cur_node.val:
            prev_node.next = cur_node.next
            cur_node = cur_node.next
            continue

        prev_node = cur_node
        cur_node = cur_node.next

    return dummy.next
