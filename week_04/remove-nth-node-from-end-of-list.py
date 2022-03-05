# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None: return None

        temp, node_list = head, []

        while temp:
            node_list.append(temp)
            temp = temp.next

        index = len(node_list)-n-1
        if index<0: return head.next
        node_list[index].next = node_list[index].next.next

        return head
