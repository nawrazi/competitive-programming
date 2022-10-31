# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1 for _ in range(n + 1)]
        graph = [[] for _ in range(n + 1)]
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
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
        
        for node in range(1, n + 1):
            if colors[node] == -1 and not search(node):
                return False
            
        return True
    
