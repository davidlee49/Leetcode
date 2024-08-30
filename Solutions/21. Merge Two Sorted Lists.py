

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        answer = dummy

        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val < list2.val:
                answer.next = list1
                list1 = list1.next
            else:
                answer.next = list2
                list2 = list2.next
            answer = answer.next
        answer.next = list2 if list2 else list1
        return dummy.next
