# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = Counter()
        
        def search(node, level):
            if not node:
                return
            levels[level] += node.val
            search(node.left, level + 1)
            search(node.right, level + 1)
            
        search(root, 0)
        sums = sorted(list(levels.values()))
        return sums[-k] if k <= len(sums) else -1
    
