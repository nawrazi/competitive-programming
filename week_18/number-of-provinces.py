# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = {i : i for i in range(len(isConnected))}

        def findParent(node):
            if parents[node] == node:
                return node
            parent = findParent(parents[node])
            parents[node] = parent
            return parent

        for i in range(len(isConnected)):
            for j in range(i, len(isConnected[0])):
                if isConnected[i][j]:
                    parents[findParent(i)] = findParent(j)
        
        for i in range(len(isConnected)):
            findParent(i)

        return len(set(parents.values()))
