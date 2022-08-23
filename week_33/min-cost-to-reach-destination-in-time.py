# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        best_edges = defaultdict(lambda: inf)
        for left, right, time in edges:
            if time < best_edges[(left, right)]:
                best_edges[(left, right)] = time
                
        graph = defaultdict(list)
        for (left, right), time in best_edges.items():
            graph[left].append((right, time))
            graph[right].append((left, time))
            
        heap = [(passingFees[0], 0, 0)]
        best = defaultdict(lambda: (inf, inf))
        best[0] = (passingFees[0], 0)
        
        while heap:
            cost, time, node = heappop(heap)
            
            if node == len(passingFees) - 1:
                return cost
            
            for nex, t in graph[node]:
                nex_time = time + t
                nex_cost = cost + passingFees[nex]
                if nex_time > maxTime:
                    continue
                if nex_cost < best[nex][0] or nex_time < best[nex][1]:
                    heappush(heap, (nex_cost, nex_time, nex))
                    best[nex] = (nex_cost, nex_time)
                    
        return -1
    
