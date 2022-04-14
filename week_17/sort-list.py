# https://leetcode.com/problems/sort-list/

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head)
            head = head.next
            
        nodes.sort(key = lambda node: node.val)
        nodes.append(None)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        return nodes[0]
