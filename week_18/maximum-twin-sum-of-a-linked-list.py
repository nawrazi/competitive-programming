# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        vals = []
        while node:
            vals.append(node.val)
            node = node.next

        return max([vals[i] + vals[~i] for i in range(len(vals) // 2)])
