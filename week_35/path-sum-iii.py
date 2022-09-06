# https://leetcode.com/problems/path-sum-iii/

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.prefix = defaultdict(int)
        self.prefix[0] = 1
        
        def search(node, past):
            if not node:
                return
            
            cur = past + node.val
            self.paths += self.prefix[cur - targetSum]
            self.prefix[cur] += 1
            
            search(node.left, cur)
            search(node.right, cur)
            
            self.prefix[cur] -= 1
            
        search(root, 0)
        return self.paths
    
