# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node):
            if node.val == startValue:
                q.append((node, '', None))
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        
        q = deque()
        parent = {}
        dfs(root)
        
        while q:
            node, path, source = q.popleft()
            
            if node.val == destValue:
                return path
            
            if node != root and parent[node] != source:
                q.append((parent[node], path + 'U', node))
            if node.left and node.left != source:
                q.append((node.left, path + 'L', node))
            if node.right and node.right != source:
                q.append((node.right, path + 'R', node))
            
