# https://leetcode.com/problems/maximum-star-sum-of-a-graph/description/

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges:
            return max(vals)
        
        graph = [[] for _ in vals]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def getSum(node):
            arms = []
            for ngh in graph[node]:
                if vals[ngh] > 0:
                    arms.append(vals[ngh])
            arms.sort(reverse=True)
            while len(arms) > k:
                arms.pop()
                
            self.max_star = max(vals[node] + sum(arms), self.max_star)
            
            for ngh in graph[node]:
                if ngh not in visited:
                    visited.add(ngh)
                    getSum(ngh)
                    
        self.max_star = 0
        visited = set()
        for i in range(len(vals)):
            if i not in visited:
                visited.add(i)
                getSum(i)
                
        return self.max_star
    
