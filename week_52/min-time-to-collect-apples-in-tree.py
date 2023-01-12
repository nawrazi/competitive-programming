# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def getTime(node, parent):
            time = 0
            for child in graph[node]:
                if child != parent:
                    time += getTime(child, node)
                    
            if time == 0:
                return hasApple[node]
            
            return time + 1
        
        time = getTime(0, -1)
        return 2 * (time - 1) if time != 0 else 0
    
