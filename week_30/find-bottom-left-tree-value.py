# https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def search(node, level):
            if not node:
                return
            
            if level > self.max_level[0]:
                self.max_level = (level, node.val)
                
            search(node.left, level + 1)
            search(node.right, level + 1)
            
        self.max_level = (-1, -1)
        search(root, 0)
        return self.max_level[1]
    
