# https://leetcode.com/problems/delete-node-in-a-bst/

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def smallest(node):
            if not node.left:
                return node
            return smallest(node.left)
        
        def search(node, parent):
            if not node:
                return
            
            if node.val > key:
                search(node.left, node)
            elif node.val < key:
                search(node.right, node)
            elif node == parent.left:
                if node.right:
                    parent.left = node.right
                    smallest(parent.left).left = node.left
                else:
                    parent.left = node.left
            elif node == parent.right:
                if node.right:
                    parent.right = node.right
                    smallest(parent.right).left = node.left
                else:
                    parent.right = node.left
                    
        pseudo = TreeNode(left=root)
        search(root, pseudo)
        return pseudo.left
    
