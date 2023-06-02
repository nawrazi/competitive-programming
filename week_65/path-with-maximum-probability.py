# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            graph[a].append((p, b))
            graph[b].append((p, a))
        
        heap = [(1, start)]
        best = {start: 1}
        
        while heap:
            prob, node = heappop(heap)
            
            if node == end:
                return -prob
            
            for nprob, ngh in graph[node]:
                nex_prob = abs(prob * nprob)
                if nex_prob > best.get(ngh, -inf):
                    heappush(heap, (-nex_prob, ngh))
                    best[ngh] = nex_prob
            
        return 0
    
