# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from populate_linked_list import *
l1 = create_LL([2, 4, 3])
l2 = create_LL(([5, 6, 4, 9, 4, 6]))


def addTwoNumbers(l1, l2):
    carry_over = 0
    starter_node = ListNode()
    temp_node = starter_node
    while l1 or l2 or carry_over != 0:
        v1 = l1.val if l1 else 0            # amazing
        v2 = l2.val if l2 else 0            # amazing
        v3 = v1 + v2 + carry_over
        carry_over = 0
        if v3 > 9:
            carry_over += 1
            v3 -= 10
        temp_node.next = ListNode(v3)
        temp_node = temp_node.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return starter_node.next


test = addTwoNumbers(l1, l2)
print_LL(test)