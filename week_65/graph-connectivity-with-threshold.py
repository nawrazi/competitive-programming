# https://leetcode.com/problems/graph-connectivity-with-threshold/

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parents = [-1 for _ in range(n + 1)]
        
        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1
                
        for node in range(threshold + 1, n + 1):
            mul = 2
            while node * mul <= n:
                union(node, node * mul)
                mul += 1
                
        for a, b in queries:
            yield find(a) == find(b)
        
