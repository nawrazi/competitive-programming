# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = [-1 for _ in edges]
        for start, end in enumerate(edges):
            graph[start] = end
            
        distance = Counter()
        seen = {node1, -1}
        def record(node, dist):
            distance[node] = dist
            if graph[node] not in seen:
                seen.add(graph[node])
                record(graph[node], dist + 1)
        
        closest = (inf, -1)
        def search(node, dist):
            nonlocal closest
            if node in distance:
                curr = max(distance[node], dist)
                closest = min(closest, (curr, node))
                
            if graph[node] not in seen:
                seen.add(graph[node])
                search(graph[node], dist + 1)
        
        record(node1, 0)
        seen = {node2, -1}
        search(node2, 0)
        return closest[1]
    
