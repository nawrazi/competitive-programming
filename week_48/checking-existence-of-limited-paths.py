# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
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
                
        queries = sorted((l, n1, n2, i) for i, (n1, n2, l) in enumerate(queries))
        edgeList.sort(key = lambda x: x[2], reverse = True)
        
        result = [True for _ in queries]
        for limit, node1, node2, idx in queries:
            while edgeList and edgeList[-1][2] < limit:
                top1, top2, _ = edgeList.pop()
                union(top1, top2)
                
            result[idx] = find(node1) == find(node2)
            
        return result
    
