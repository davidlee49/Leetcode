# https://leetcode.com/problems/merge-k-sorted-lists/
from populate_linked_list import *
import heapq


x = create_LL([1,4,5])
y = create_LL([1,3,4])
z = create_LL([2,6])

list = [x, y, z]
for i in list:
    print_LL(i)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap_list = []
    answer = None
    temp = None

    #sort nodes into list O(n)
    for i in lists:
        while i:
            heap_list.append(i.val)
            i = i.next
    print(heap_list)

    #create heap
    heapq.heapify(heap_list)
    print(heap_list)


    answer = ListNode()
    temp = answer
    #pop smallest



    #create new LL
    while heap_list:
        temp.next = ListNode(heapq.heappop(heap_list))
        temp = temp.next

    print_LL(answer.next)
    return answer.next


mergeKLists(list)