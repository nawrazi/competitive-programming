# https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s, e in redEdges:
            graph[s].append((e, 0))
        for s, e in blueEdges:
            graph[s].append((e, 1))
            
        def search(target):
            h = [(0, 0, -1)]
            best = defaultdict(lambda: [inf, inf])
            
            while h:
                dist, node, last = heappop(h)
                
                if node == target:
                    return dist
                
                for nex, col in graph[node]:
                    nex_dist = dist + 1
                    if nex_dist > best[nex][col] or col == last:
                        continue
                    heappush(h, (nex_dist, nex, col))
                    best[nex][col] = nex_dist
                    
            return -1
        
        return [search(i) for i in range(n)]
    
