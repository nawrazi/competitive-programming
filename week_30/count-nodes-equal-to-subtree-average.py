# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class Solution:
    def __init__(self):
        self.count = 0
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def search(node):
            if not node:
                return 0, 0
            
            left_sum, left_count = search(node.left)
            right_sum, right_count = search(node.right)
            
            cur_sum = left_sum + right_sum + node.val
            cur_count = left_count + right_count + 1
            
            if cur_sum // cur_count == node.val:
                self.count += 1
            
            return cur_sum, cur_count
            
        search(root)
        return self.count
    
