# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/description/

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        odd = []
        for node in range(1, n + 1):
            if len(graph[node]) % 2 == 1:
                odd.append(node)
                
        if len(odd) == 2:
            for node in range(1, n + 1):
                if node not in graph[odd[0]] and node not in graph[odd[1]]:
                    return True
                
        if len(odd) == 4:
            pairs = [[(0, 1), (2, 3)], [(0, 2), (1, 3)], [(0, 3), (1, 2)]]
            for (node1, node2), (node3, node4) in pairs:
                if odd[node1] not in graph[odd[node2]] and odd[node3] not in graph[odd[node4]]:
                    return True
                
        return len(odd) == 0
    
