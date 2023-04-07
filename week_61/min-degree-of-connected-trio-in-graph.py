# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/description/

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for _ in range(n + 1)]
        degree = [0 for _ in range(n + 1)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1
            
        min_deg = inf
        for node1 in range(1, n + 1):
            for node2 in graph[node1]:
                for node3 in graph[node1]:
                    if node2 != node3 and node3 in graph[node2]:
                        deg = degree[node1] + degree[node2] + degree[node3] - 6
                        min_deg = min(min_deg, deg)
                        graph[node3].discard(node1)
                        graph[node3].discard(node2)
                        
        return min_deg if min_deg != inf else -1
    
