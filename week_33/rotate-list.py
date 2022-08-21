# https://leetcode.com/problems/rotate-list/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = {head: None}
        tail = head
        length = 1
        while tail and tail.next:
            prev[tail.next] = tail
            tail = tail.next
            length += 1
            
        for _ in range(k % length):
            prev[tail].next = None
            tail.next = head
            prev[head] = tail
            head = tail
            tail = prev[tail]
            
        return head
    
