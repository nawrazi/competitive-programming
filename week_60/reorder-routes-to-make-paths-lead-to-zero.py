# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
            
        changed = 0
        q = deque([0])
        seen = {0}
        
        while q:
            node = q.popleft()
            for nex, cost in graph[node]:
                if nex not in seen:
                    q.append(nex)
                    seen.add(nex)
                    changed += cost
                    
        return changed
    
