# https://leetcode.com/problems/next-greater-node-in-linked-list/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        mono_stack, tuples, index = [], [], 0

        while head:
            while mono_stack and head.val > mono_stack[-1][1]:
                tuples.append((*mono_stack.pop(), head.val))

            mono_stack.append((index, head.val))
            index+=1
            head = head.next

        while mono_stack:
            tuples.append((*mono_stack.pop(), 0))

        return [i for (_,_,i) in sorted(tuples)]
