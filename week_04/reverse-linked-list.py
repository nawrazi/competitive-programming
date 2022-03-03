# https://leetcode.com/problems/reverse-linked-list/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        prev, cur, nex = None, head, head.next

        while nex:
            cur.next, prev, cur, nex = prev, cur, nex, nex.next

        cur.next = prev

        return cur
