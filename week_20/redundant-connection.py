# https://leetcode.com/problems/redundant-connection/

class DisjointSet:
    def __init__(self, n):
        self.parents = [-1 for _ in range(n + 1)]
        
    def find(self, node):
        if self.parents[node] < 0:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        
        if self.parents[parent1] > self.parents[parent2]:
            parent1, parent2 = parent2, parent1
        
        if parent1 != parent2:
            self.parents[parent1] += self.parents[parent2]
            self.parents[parent2] = parent1
            return True
        
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dj = DisjointSet(len(edges))
        
        for node1, node2 in edges:
            if not dj.union(node1, node2):
                redundant = [node1, node2]
                
        return redundant
      
