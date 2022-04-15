# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        node = head
        while node:
            nodes.append(node)
            prev = node
            node = node.next
            prev.next = None
            
        i = 0
        while i + 1 < len(nodes):
            nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
            i += 2

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        return nodes[0] if nodes else None
