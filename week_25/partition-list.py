# https://leetcode.com/problems/partition-list/

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = []
        more = []
        
        if not head:
            return head
        
        node = head
        while node:
            if node.val < x:
                less.append(node)
            else:
                more.append(node)
                
            node = node.next
            
        for i in range(1, len(less)):
            less[i-1].next = less[i]
        for i in range(1, len(more)):
            more[i-1].next = more[i]
            
        if less:
            less[-1].next = more[0] if more else None
        if more:
            more[-1].next = None
        
        return less[0] if less else more[0]
    
