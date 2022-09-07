# https://leetcode.com/problems/construct-string-from-binary-tree/

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        trav = []
        
        def search(node):
            trav.append(str(node.val))
            
            if node.left:
                trav.append('(')
                search(node.left)
                trav.append(')')
            elif node.right:
                trav.extend(['(', ')'])
                
            if node.right:
                trav.append('(')
                search(node.right)
                trav.append(')')
                
        search(root)
        return ''.join(trav)
    
