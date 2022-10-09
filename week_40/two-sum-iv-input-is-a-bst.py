# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = set()
        
        def search(node):
            if not node:
                return False
            
            if node.val in vals:
                return True
            vals.add(k - node.val)
            
            return search(node.left) or search(node.right)
        
        return search(root)
    
