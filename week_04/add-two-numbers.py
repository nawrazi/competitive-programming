# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, rem = ListNode(), 0
        temp = head

        while l1 and l2:
            if l1.next or l2.next:
                temp.next = ListNode()
            else:
                last = temp

            s = l1.val + l2.val + rem
            temp.val = int(str(s)[-1])

            rem = 1 if len(str(s))==2 else 0

            l1, l2, temp = l1.next, l2.next, temp.next

        l = l1 or l2
        while l:
            if l.next:
                temp.next = ListNode()
            else:
                last = temp

            s = l.val + rem
            temp.val = int(str(s)[-1])

            rem = 1 if len(str(s))==2 else 0

            l, temp = l.next, temp.next

        if rem==1:
            last.next = ListNode(1)

        return head
