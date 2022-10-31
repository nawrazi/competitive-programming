# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1 for _ in graph]
        
        def search(start):
            q = deque([(start, 0)])
            colors[start] = 0
            
            while q:
                node, color = q.popleft()
                for ngh in graph[node]:
                    if colors[ngh] == color:
                        return False
                    if colors[ngh] == -1:
                        q.append((ngh, 1 - color))
                        colors[ngh] = 1 - color
                        
            return True
        
        for node in range(len(graph)):
            if colors[node] == -1 and not search(node):
                return False
            
        return True
    
