# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parents = [-1 for _ in range(n)]
        
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
                return True
            
        cables = 0
        recon = -1
        for a, b in connections:
            if not union(a, b):
                cables += 1
                
        for parent in parents:
            if parent < 0:
                recon += 1
                
        return recon if recon <= cables else -1
    
