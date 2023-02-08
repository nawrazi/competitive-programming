# https://leetcode.com/problems/bus-routes/description/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
                
        q = deque([(source, 0)])
        seen_station = {source}
        seen_bus = set()
        while q:
            station, dist = q.popleft()
            if station == target:
                return dist
            
            for bus in graph[station]:
                if bus in seen_bus:
                    continue
                for nex in routes[bus]:
                    if nex not in seen_station:
                        q.append((nex, dist + 1))
                        seen_station.add(nex)
                seen_bus.add(bus)
                
        return -1
    
