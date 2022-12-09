# https://leetcode.com/problems/couples-holding-hands/description/

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        parents = [-1 for _ in range(len(row))]
        
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
                return 1
            
            return 0
        
        for i in range(0, len(row), 2):
            union(row[i], row[i + 1])
            
        swaps = 0
        for i in range(0, len(row), 2):
            swaps += union(i, i + 1)
            
        return swaps
    
