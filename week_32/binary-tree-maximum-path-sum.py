# https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -inf
        
        def getSum(node):
            if not node:
                return 0
            
            left_sum = getSum(node.left)
            right_sum = getSum(node.right)
            cur_sum = node.val + max(left_sum, right_sum, left_sum + right_sum, 0)
            self.max_sum = max(self.max_sum, cur_sum)
            
            return node.val + max(left_sum, right_sum, 0)
        
        getSum(root)
        return self.max_sum
    
