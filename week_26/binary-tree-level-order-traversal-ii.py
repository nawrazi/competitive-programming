# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:        
        def search(node, level):
            if node.left:
                search(node.left, level + 1)
                
            while level >= len(levels):
                levels.append([])
            levels[level].append(node.val)
            
            if node.right:
                search(node.right, level + 1)
                
        levels = []
        if root:
            search(root, 0)
        return reversed(levels)
    
