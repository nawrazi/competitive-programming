# https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = [[]]
        count = 0

        node = head
        while node:
            if count == k:
                nodes.append([])
                count = 0

            nodes[-1].append(node)
            count += 1
            prev = node
            node = node.next
            prev.next = None

        final = []
        for sub in nodes:
            if len(sub) == k:
                sub.reverse()
            final += sub

        for i in range(len(final) - 1):
            final[i].next = final[i+1]

        return final[0]
