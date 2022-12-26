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


LL = create_LL([7,9,6,6,7,8,3,0,9,5])
print_LL(LL)
k=5

def swapNodes(head, k):
    if not head.next:
        return head
    else:
        node = head.next
        lag_node = node

    for i in range(k-1):
        node.next = node



swapNodes(LL, k)