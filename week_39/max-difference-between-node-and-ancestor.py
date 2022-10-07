# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = 0
        
        def dfs(node):
            if not node.left and not node.right:
                return node.val, node.val
            
            l_max, l_min = node.val, node.val
            r_max, r_min = node.val, node.val
            if node.left:
                l_max, l_min = dfs(node.left)
            if node.right:
                r_max, r_min = dfs(node.right)
                
            left = max(abs(node.val - l_min), abs(node.val - l_max))
            right = max(abs(node.val - r_min), abs(node.val - r_max))
            self.max_diff = max(self.max_diff, max(left, right))
            
            return max(node.val, l_max, r_max), min(node.val, l_min, r_min)
        
        dfs(root)
        return self.max_diff
    
