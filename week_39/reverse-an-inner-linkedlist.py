# https://binarysearch.com/room/How-do-I-Java-CK7pAOMFwT?questionsetIndex=1

class Solution:
    def solve(self, node, i, j):
        idx = -1
        head = LLNode(-1, next=node)
        cur = head

        def reverse(start):
            prev, cur, nex = None, start, start.next
            for _ in range(j - i):
                cur.next, prev, cur, nex = prev, cur, nex, nex.next
            cur.next = prev
            return cur
            
        end = None
        while cur:
            if idx == i - 1:
                start = cur
            if idx == j + 1:
                end = cur
            cur = cur.next
            idx += 1

        start.next = reverse(start.next)
        temp = start

        while temp.next:
            temp = temp.next
        temp.next = end

        return head.next
    
