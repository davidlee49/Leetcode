#https://leetcode.com/problems/reverse-nodes-in-k-group




class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur_node = head
        node_list = []

        while cur_node:
            node_list.append(cur_node)
            cur_node = cur_node.next

        for group in range(len(node_list) // k):
            for i in range(k // 2):
                node_list[(group * k) + i], node_list[(group * k) + (k - 1 - i)] = node_list[(group * k) + (k - 1 - i)], \
                                                                                   node_list[(group * k) + i]

        for i in range(len(node_list)):
            if i == len(node_list) - 1:
                node_list[i].next = None
                break

            node_list[i].next = node_list[i + 1]

        return node_list[0]


