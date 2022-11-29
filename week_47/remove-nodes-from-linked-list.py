# https://leetcode.com/problems/remove-nodes-from-linked-list/

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [ListNode(inf)]
        
        while head:
            while head.val > stack[-1].val:
                stack.pop()
            stack[-1].next = head
            stack.append(head)
            head = head.next
            
        return stack[0].next
    
