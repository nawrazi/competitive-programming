# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parents = [-1 for _ in range(n + 1)]
        score = [inf for _ in range(n + 1)]
        
        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2, dist):
            parent1, parent2 = find(node1), find(node2)
            
            if parents[parent1] > parents[parent2]:
                parent1, parent2 = parent2, parent1
                
            score[parent1] = min(score[parent1], score[parent2], dist)
            if parent1 != parent2:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1
                
        for path in roads:
            union(*path)
            
        return score[find(1)]
    
