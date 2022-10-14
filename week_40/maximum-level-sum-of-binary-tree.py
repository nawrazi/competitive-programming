# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        levels = defaultdict(int)
        
        while q:
            node, level = q.popleft()
            levels[level] += node.val
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            
        best = -inf, 0
        for i in range(1, len(levels) + 1):
            if levels[i] > best[0]:
                best = levels[i], i
                
        return best[1]
    
