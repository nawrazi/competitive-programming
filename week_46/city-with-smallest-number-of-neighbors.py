# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for left, right, dist in edges:
            graph[left].append((right, dist))
            graph[right].append((left, dist))
            
        def countNeighbors(start):
            heap = [(0, start)]
            best = {start: 0}
            
            while heap:
                dist, node = heappop(heap)
                
                for ngh, path_dist in graph[node]:
                    nex_dist = dist + path_dist
                    if nex_dist > distanceThreshold or nex_dist > best.get(ngh, inf):
                        continue
                    heappush(heap, (nex_dist, ngh))
                    best[ngh] = nex_dist
                    
            return len(best) - 1
        
        best = [-1, inf]
        for node in range(n):
            count = countNeighbors(node)
            if count <= best[1]:
                best = [node, count]
            
        return best[0]
    
