# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def search(node, num):
            if not node.left and not node.right:
                total[0] += int(num + str(node.val))
                
            if node.left:
                search(node.left, num + str(node.val))
                
            if node.right:
                search(node.right, num + str(node.val))
                
        total = [0]
        search(root, '')
        return total[0]
    
