# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for f, t, c in edges:
            self.graph[f].append((c, t))
    
    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[2], edge[1]))
    
    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        best = {node1: 0}
        
        while heap:
            dist, node = heappop(heap)
            
            if node == node2:
                return dist
            
            for ndist, ngh in self.graph[node]:
                nex_dist = dist + ndist
                if nex_dist < best.get(ngh, inf):
                    heappush(heap, (nex_dist, ngh))
                    best[ngh] = nex_dist
            
        return -1
    
