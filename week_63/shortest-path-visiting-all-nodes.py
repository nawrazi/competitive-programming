# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def shortestPath(start):
            queue = deque([(start, 1 << start, 0)])
            seen = {(start, 1 << start)}
            
            while queue:
                node, mask, dist = queue.popleft()
                
                if mask == pow(2, n) - 1:
                    return dist
                
                for ngh in graph[node]:
                    new_mask = mask | 1 << ngh
                    if (ngh, new_mask) not in seen:
                        queue.append((ngh, new_mask, dist + 1))
                        seen.add((ngh, new_mask))
                        
        n = len(graph)
        shortest = inf
        for node in range(n):
            shortest = min(shortest, shortestPath(node))
            
        return shortest
    
