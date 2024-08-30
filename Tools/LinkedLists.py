
# Takes in an array and creates a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(array):
    prev = None
    for i, val in enumerate(array):
        cur = array[i] = ListNode(val)

        if prev:
            prev.next = cur

        prev = cur

    return array[0]

node1 = ListNode(5)
max_value = max([node1, None], key=lambda x: x.val if x is not None else -11)
print(max_value)