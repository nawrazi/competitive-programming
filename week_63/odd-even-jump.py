# https://leetcode.com/problems/odd-even-jump/description/

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = [[-1 for _ in range(n)], [-1 for _ in range(n)]]
        
        stack = []
        for idx in sorted(range(n), key = lambda i: arr[i]):
            while stack and idx >= stack[-1]:
                graph[1][stack.pop()] = idx
            stack.append(idx)
            
        stack = []
        for idx in sorted(range(n), key = lambda i: arr[i], reverse=True):
            while stack and idx >= stack[-1]:
                graph[0][stack.pop()] = idx
            stack.append(idx)
            
        @cache
        def canReach(idx, par):
            if idx == n - 1:
                return True
            
            nex = graph[par][idx]
            return nex != -1 and canReach(nex, 1 - par)
        
        good = 0
        for start in range(n):
            if canReach(start, 1):
                good += 1
                
        return good
    
