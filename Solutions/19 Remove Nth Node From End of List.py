# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_LL(leetcodeLLarray):
    LL_head = ListNode(leetcodeLLarray[0])
    LL_temp = LL_head
    for i in leetcodeLLarray[1:]:
        LL_temp.next = ListNode(i)
        LL_temp = LL_temp.next
    return LL_head


def print_LL(linked_list):
    print_array = []
    while linked_list:
        print_array.append(linked_list.val)
        linked_list = linked_list.next
    print(print_array)


LL = create_LL([1, 2, 3, 4, 5])
print_LL(LL)

#
# def removeNthFromEnd(head, n: int):
#     travel_node = head
#     lag_node = head
#     for i in range(n):
#         travel_node = travel_node.next
#     if travel_node == None:
#         if not head.next:
#             return
#         else:
#              return head.next
#     while travel_node.next:
#         travel_node = travel_node.next
#         lag_node = lag_node.next
#     if n > 1:
#         lag_node.next = lag_node.next.next
#     else:
#         lag_node.next = None
#     return head
#
# x=(removeNthFromEnd(LL, 5))
# print_LL(x)
def removeNthFromEnd(head, n: int):
    array = []

    while True:
        array.append(head.val)

        if not head.next:
            break
        head = head.next
    x = array[n-1]
    array[n-1] = array[-n]
    array[-n] = x

    dummy = ListNode()
    answer = dummy
    for i in array:
        dummy.next = ListNode(i)
        dummy = dummy.next

    return answer.next


head = [1,2,3,4,5]
k = 2
x = removeNthFromEnd(LL, k)
print_LL(x)