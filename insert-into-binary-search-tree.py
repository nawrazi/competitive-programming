# https://leetcode.com/problems/insert-into-a-binary-search-tree/

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, high, low):
            if not node:
                return low < val < high
            
            if node.val > val and search(node.left, min(high, node.val), low):
                node.left = TreeNode(val)
            elif search(node.right, high, max(low, node.val)):
                node.right = TreeNode(val)
                
        search(root, inf, -inf)
        return root if root else TreeNode(val)
    
