# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for start, end, time in times:
            graph[start].append((end, time))
            
        delay = 0
        heap = [(0, k)]
        best_time = {k: 0}
        
        while heap:
            time, node = heappop(heap)
            if time > best_time[node]:
                continue
            delay = max(delay, time)
            
            for ngh, ngh_time in graph[node]:
                nex_time = time + ngh_time
                if nex_time < best_time.get(ngh, inf):
                    heappush(heap, (nex_time, ngh))
                    best_time[ngh] = nex_time
                    
        if len(best_time) < n:
            return -1
        
        return delay
    
