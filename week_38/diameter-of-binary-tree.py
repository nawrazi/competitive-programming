# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        
        def search(node):
            if not node:
                return 0
            
            left = search(node.left)
            right = search(node.right)
            
            self.max_len = max(self.max_len, left + right)
            
            return 1 + max(left, right)
        
        search(root)
        return self.max_len
    
