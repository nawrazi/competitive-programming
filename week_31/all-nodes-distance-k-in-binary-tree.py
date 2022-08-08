# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {root: None}
        def search(node):
            if node.val == target.val:
                self.start = node
                
            for child in [node.left, node.right]:
                if child:
                    parent[child] = node
                    search(child)
                
        search(root)
        ans = []
        q = deque([(self.start, 0)])
        seen = {self.start}
        while q:
            cur, level = q.popleft()
            
            if level == k:
                ans.append(cur.val)
                continue
            
            for nex in [cur.left, cur.right, parent[cur]]:
                if nex and nex not in seen:
                    q.append((nex, level + 1))
                    seen.add(nex)
                
        return ans
    
