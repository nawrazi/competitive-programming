# https://leetcode.com/problems/binary-tree-pruning/

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def search(node):
            if not node.left and not node.right:
                return node.val == 1
            
            left_has = search(node.left) if node.left else False
            right_has = search(node.right) if node.right else False
            
            if not left_has and not right_has:
                if node.val == 1:
                    node.left = None
                    node.right = None
                    return True
                else:
                    return False
            
            elif not left_has:
                node.left = None
                return True
            
            elif not right_has:
                node.right = None
                return True
            
            else:
                return True
            
        return root if search(root) else None
    
