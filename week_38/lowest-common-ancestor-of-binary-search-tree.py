# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def search(node):
            if not node:
                return False
            
            left = search(node.left)
            right = search(node.right)
            
            if left and right and not self.ans:
                self.ans = node
                return True
            
            if (left or right) and (node == p or node == q) and not self.ans:
                self.ans = node
                return True
            
            if node == p or node == q:
                return True
            
            return left or right
        
        search(root)
        return self.ans
    
