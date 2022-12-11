# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        def construct(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            return TreeNode(
                val = nums[mid],
                left = construct(left, mid - 1),
                right = construct(mid + 1, right)
            )
        
        return construct(0, len(nums) - 1)
    
