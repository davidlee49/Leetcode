#https://leetcode.com/problems/partition-list/


def partition(head, x):
    small_nodes = head
    large_nodes = None
    #one pointer traverse linked list until end or node.next >= x
    if not head:
        return head

    while small_nodes.next



    #2nd pointer starts at node.next and traverses until end or
        #if node.next is < x do the partition
        #update pos of pointer 1


