# https://leetcode.com/problems/add-one-row-to-tree/

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def search(node, level):
            if not node:
                return
            
            if level == depth:
                temp_left, temp_right = node.left, node.right
                node.left = TreeNode(val, left = temp_left)
                node.right = TreeNode(val, right = temp_right)
            else:
                search(node.left, level + 1)
                search(node.right, level + 1)
        
        if depth == 1:
            return TreeNode(val, left = root)
        
        search(root, 2)
        return root
    
