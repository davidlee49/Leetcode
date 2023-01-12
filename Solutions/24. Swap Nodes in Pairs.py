#https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = None
nums = [1,2,3,4]
last_node = None
for i in range(len(nums)):
    if head is None:
        head = ListNode(nums[i])
        last_node = head
        continue
    last_node.next = ListNode(nums[i])
    last_node = last_node.next





def swapPairs(head):
    if not head or head.next is None:
        return head

    first = head
    head = first.next

    #swap current node with next node
    while first:
        if first.next is None:
            break
        second = first.next
        temp = second.next
        second.next = first
        first.next = temp
        first = temp


    return head
swapPairs(head)

last_node = head
while last_node:
    print(last_node.val)
    last_node = last_node.next