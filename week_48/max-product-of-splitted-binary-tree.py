# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max_product = -inf
        
        def findTotal(node):
            if not node:
                return 0
            return node.val + findTotal(node.left) + findTotal(node.right)
        
        total = findTotal(root)
        
        def search(node):
            if not node:
                return 0
            
            left_sum = search(node.left)
            right_sum = search(node.right)
            
            self.max_product = max(left_sum * (total - left_sum), self.max_product)
            self.max_product = max(right_sum * (total - right_sum), self.max_product)
            
            return left_sum + right_sum + node.val
        
        search(root)
        return self.max_product % (pow(10, 9) + 7)
    
