# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        
        def search(node):
            if not node:
                return True, -inf, inf, 0
            
            l_bst, l_max, l_min, l_sum = search(node.left)
            r_bst, r_max, r_min, r_sum = search(node.right)
            
            if l_bst and r_bst and l_max < node.val < r_min:
                cur_sum = node.val + l_sum + r_sum
                self.max_sum = max(self.max_sum, cur_sum)
                return True, max(node.val, r_max), min(node.val, l_min), cur_sum
            else:
                return False, 0, 0, 0
            
        search(root)
        return self.max_sum
    
