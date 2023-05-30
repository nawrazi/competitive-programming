# https://leetcode.com/problems/number-of-good-paths/

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        parents = [-1 for _ in range(len(edges) + 1)]
        
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
        
        edges = sorted(((max(vals[a], vals[b]), a, b) for a, b in edges), reverse=True)
        paths = len(edges) + 1
        
        for limit in range(max(vals) + 1):
            added = set()
            while edges and edges[-1][0] <= limit:
                _, a, b = edges.pop()
                union(a, b)
                if vals[a] == limit:
                    added.add(a)
                if vals[b] == limit:
                    added.add(b)
                    
            groups = Counter(find(a) for a in added)
            for n in groups.values():
                paths += (n * (n - 1)) // 2
                
        return paths
    
