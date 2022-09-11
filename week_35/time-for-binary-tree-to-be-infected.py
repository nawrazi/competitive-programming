# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {root: None}
        q = deque()
        seen = set()
        
        def dfs(node):
            if node.val == start:
                q.append((node, 0))
                seen.add(node)
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
            
        dfs(root)
        total = 0
        while q:
            node, time = q.popleft()
            total = time
            
            for nex in [node.left, node.right, parent[node]]:
                if nex not in seen and nex is not None:
                    q.append((nex, time + 1))
                    seen.add(nex)
                
        return total
    
