# https://leetcode.com/problems/reverse-linked-list-ii/

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(start):
            prev, cur, nex = None, start, start.next
            for _ in range(right - left):
                cur.next, prev, cur, nex = prev, cur, nex, nex.next
            cur.next = prev
            return cur
            
        head = ListNode(-1, head)
        end = None
        node = head
        idx = -1
        while node:
            if idx == left - 2:
                start = node
            if idx == right:
                end = node
            node = node.next
            idx += 1

        start.next = reverse(start.next)
        node = start
        while node.next:
            node = node.next
        node.next = end

        return head.next
    
