# https://leetcode.com/problems/insertion-sort-list/

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        node = head
        while node:
            nodes.append(node)
            prev = node
            node = node.next
            prev.next = None

        for i in range(1, len(nodes)):
            cur = nodes[i]
            j = i - 1
            while j >= 0 and cur.val < nodes[j].val:
                nodes[j+1] = nodes[j]
                j -= 1
            nodes[j+1] = cur

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        return nodes[0]
