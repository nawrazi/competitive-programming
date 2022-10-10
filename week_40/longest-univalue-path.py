# https://leetcode.com/problems/longest-univalue-path/

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        
        def search(node, parent):
            if not node:
                return 0
            
            left = search(node.left, node.val)
            right = search(node.right, node.val)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right) if node.val == parent else 0
        
        search(root, None)
        return self.longest
    
