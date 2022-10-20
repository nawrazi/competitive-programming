# https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def getCycle(self, start, edges, seen, indegrees, graph):
        component = set()
        q = deque([start])
        while q:
            node = q.popleft()
            component.add(node)
            
            for ngh in graph[node]:
                if ngh not in seen:
                    q.append(ngh)
                    seen.add(ngh)
                    
        q = deque()
        for node in component:
            if indegrees[node] == 0:
                q.append(node)
                
        while q:
            node = q.popleft()
            component.remove(node)
            
            ngh = edges[node]
            if ngh != -1:
                indegrees[ngh] -= 1
                if indegrees[ngh] == 0:
                    q.append(ngh)
                    
        return len(component)
    
    def longestCycle(self, edges: List[int]) -> int:
        indegrees = [0 for _ in edges]
        graph = [[] for _ in edges]
        for start, end in enumerate(edges):
            if end != -1:
                indegrees[end] += 1
                graph[start].append(end)
                graph[end].append(start)
                
        seen = set()
        max_cycle = 0
        for node in range(len(edges)):
            if node not in seen:
                cycle = self.getCycle(node, edges, seen, indegrees, graph)
                max_cycle = max(max_cycle, cycle)
                
        return max_cycle if max_cycle != 0 else -1
    
