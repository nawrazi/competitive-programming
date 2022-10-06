# https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
            
        if not fast or not fast.next:
            return None
        
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        return fast
    
