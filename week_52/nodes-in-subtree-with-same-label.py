# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        result = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def search(node, parent):
            letters = Counter()
            letters[labels[node]] = 1
            
            for child in graph[node]:
                if child != parent:
                    letters += search(child, node)
                    
            result[node] += letters[labels[node]]
            return letters
        
        search(0, -1)
        return result
    
