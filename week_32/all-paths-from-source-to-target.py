# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        edges = {i: adj for i, adj in enumerate(graph)}
        
        def search(node):
            if node == len(graph) - 1:
                return [[node]]
            
            paths = []
            for adj in edges[node]:
                nex = search(adj)
                if nex:
                    for p in nex:
                        paths.append([node] + p)
            
            return paths
        
        return search(0)
    
