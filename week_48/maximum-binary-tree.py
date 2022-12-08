# https://leetcode.com/problems/maximum-binary-tree/description/

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            if left > right:
                return None
            
            best = [-inf, 0]
            for idx in range(left, right + 1):
                best = max(best, [nums[idx], idx])
                
            return TreeNode(
                val = best[0],
                left = construct(left, best[1] - 1),
                right = construct(best[1] + 1, right)
            )
        
        return construct(0, len(nums) - 1)
    
