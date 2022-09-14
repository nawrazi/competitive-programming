# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.paths = 0
        counts = defaultdict(int)
        
        def dfs(node):
            counts[node.val] += 1
            
            if not node.left and not node.right:
                odds = [c for c in counts.values() if c % 2 == 1]
                if len(odds) <= 1:
                    self.paths += 1
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
            counts[node.val] -= 1
            
        dfs(root)
        return self.paths
    
