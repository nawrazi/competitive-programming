# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.max = 0
        
        def search(node, path_max):
            if not node:
                return
            
            cur_max = path_max
            if node.val >= path_max:
                self.max += 1
                cur_max = node.val
                
            search(node.left, cur_max)
            search(node.right, cur_max)
            
        search(root, -inf)
        return self.max
    
