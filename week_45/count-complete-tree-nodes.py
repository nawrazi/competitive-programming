# https://leetcode.com/problems/count-complete-tree-nodes/

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getLeftHeight(node):
            return 1 + getLeftHeight(node.left) if node else 0
        
        def getRightHeight(node):
            return 1 + getRightHeight(node.right) if node else 0
        
        height = getLeftHeight(root)
        if height == getRightHeight(root):
            return pow(2, height) - 1
        
        def findLast(node, level):
            if node.right:
                return findLast(node.right, level + 1)
            else:
                return node.left is not None or level != height
            
        depth = 1
        leaves = 0
        node = root
        while node:
            if node.left and findLast(node.left, depth + 1):
                node = node.left
            else:
                if node.left:
                    leaves += pow(2, height - depth - 1)
                node = node.right
            depth += 1
            
        return leaves + pow(2, height - 1) - 1
    
