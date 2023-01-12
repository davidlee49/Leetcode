# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        answer = ListNode()
        travel = answer
        for i in range(len(array)):
            travel.next = ListNode(array[-1-i])
            travel = travel.next
        return answer.next