# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def search(node):
            if not node:
                return None
            
            left, right = node.left, node.right
            node.left = None
            node.right = search(left)
            
            temp = node
            while temp.right:
                temp = temp.right
                
            temp.right = search(right)
            
            return node
        
        search(root)
        
