# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for start, end, cost in flights:
            graph[start].append((end, cost))
            
        heap = [(0, 0, src)]
        best = defaultdict(lambda : (inf, inf))
        
        while heap:
            cur_cost, cur_stops, cur_node = heappop(heap)

            if cur_node == dst:
                return cur_cost

            for nex, nc in graph[cur_node]:
                next_cost = cur_cost + nc
                next_stops = cur_stops + 1
                if next_stops > k + 1:
                    continue
                if next_cost < best[nex][0] or next_stops < best[nex][1]:
                    heappush(heap, (next_cost, next_stops, nex))
                    best[nex] = (next_cost, next_stops)

        return -1
    
