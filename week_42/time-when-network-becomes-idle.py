# https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        distance = [0 for _ in range(len(patience))]
        graph = [[] for _ in range(len(patience))]
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        q = deque([(0, 0)])
        seen = {0}
        while q:
            dist, node = q.popleft()
            distance[node] = dist
            
            for ngh in graph[node]:
                if ngh not in seen:
                    q.append((dist + 1, ngh))
                    seen.add(ngh)
                    
        max_idle = 0
        for dist, pat in zip(distance[1:], patience[1:]):
            idle = (2 * dist) + (pat * ((2 * dist - 1) // pat))
            max_idle = max(max_idle, idle + 1)
            
        return max_idle
    
