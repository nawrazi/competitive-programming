# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2: return list2
        elif not list2 and list1: return list1
        elif not list2 and not list1: return None

        if list1.val < list2.val: head, list1 = list1, list1.next
        else: head, list2 = list2, list2.next

        temp = head
        while list1 and list2:
            if list1.val < list2.val: temp.next, list1 = list1, list1.next
            else: temp.next, list2 = list2, list2.next
            temp = temp.next

        if list1: temp.next = list1
        else: temp.next = list2

        return head
