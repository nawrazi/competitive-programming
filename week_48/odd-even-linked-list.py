# https://leetcode.com/problems/odd-even-linked-list/description/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        parity = [[], []]
        index = 0
        
        while head:
            parity[index].append(head)
            index ^= 1
            head = head.next
        parity[1].append(None)
        
        for group in parity:
            for i in range(len(group) - 1):
                group[i].next = group[i + 1]
        parity[0][-1].next = parity[1][0]
        
        return parity[0][0]
    
