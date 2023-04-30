# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parents = [[-1] * (n + 1) for _ in range(2)]
        
        def find(node, person):
            if parents[person][node] < 0:
                return node
            parents[person][node] = find(parents[person][node], person)
            return parents[person][node]
        
        def union(node1, node2, person):
            parent1, parent2 = find(node1, person), find(node2, person)
            
            if parents[person][parent1] > parents[person][parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                parents[person][parent1] += parents[person][parent2]
                parents[person][parent2] = parent1
                return True
            
        remove = 0
        for t, u, v in edges:
            if t == 3:
                a, b = union(u, v, 0), union(u, v, 1)
                if not a and not b:
                    remove += 1
                    
        for t, u, v in edges:
            if t == 1 and not union(u, v, 0):
                remove += 1
            if t == 2 and not union(u, v, 1):
                remove += 1
                
        if not min(parents[0]) == min(parents[1]) == -n:
            return -1
        
        return remove
    
