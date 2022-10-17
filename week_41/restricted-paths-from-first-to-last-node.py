# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for left, right, weight in edges:
            graph[left].append((right, weight))
            graph[right].append((left, weight))
            
        distanceToLastNode = [inf for _ in range(n)] + [0]
        heap = [(0, n)]
        
        while heap:
            dist, node = heappop(heap)
            
            for nex_node, nex_dist in graph[node]:
                if nex_dist + dist < distanceToLastNode[nex_node]:
                    heappush(heap, (nex_dist + dist, nex_node))
                    distanceToLastNode[nex_node] = nex_dist + dist
                    
        @cache
        def getPaths(node):
            if node == n:
                return 1
            
            paths = 0
            for neighbor, _ in graph[node]:
                if distanceToLastNode[node] > distanceToLastNode[neighbor]:
                    paths += getPaths(neighbor)
                    
            return paths
        
        mod = (10 ** 9) + 7
        return getPaths(1) % mod
    
