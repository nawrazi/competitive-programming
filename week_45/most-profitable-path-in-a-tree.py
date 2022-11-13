# https://leetcode.com/problems/most-profitable-path-in-a-tree/

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        nodes = len(edges) + 1
        graph = [[] for _ in range(nodes)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)
            
        def findParents(node, parent):
            parents[node] = parent
            for child in graph[node]:
                if child != parent:
                    findParents(child, node)
                    
        parents = [-1 for _ in range(nodes)]
        findParents(0, -1)
        
        def moveBob(node, time):
            visited[node] = time
            if node != 0:
                moveBob(parents[node], time + 1)
                
        visited = {}
        moveBob(bob, 0)
        
        self.max_profit = -inf
        def moveAlice(node, parent, profit, time):
            if time < visited.get(node, inf):
                profit += amount[node]
            elif time == visited.get(node, inf):
                profit += amount[node] / 2
                
            leaf = True
            for child in graph[node]:
                if child != parent:
                    leaf = False
                    moveAlice(child, node, profit, time + 1)
                    
            if leaf:
                self.max_profit = max(self.max_profit, profit)
        
        moveAlice(0, -1, 0, 0)
        return int(self.max_profit)
    
