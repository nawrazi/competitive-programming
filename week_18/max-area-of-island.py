# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        parents = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    parents[(i,j)] = (i,j)

        def findParent(node):
            if parents[node] == node:
                return node
            parent = findParent(parents[node])
            parents[node] = parent
            return parent

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inBound = lambda r, c : 0 <= r < len(grid) and 0 <= c < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                for x, y in directions:
                    new_row, new_col = i + x, j + y
                    if not inBound(new_row, new_col) or not grid[new_row][new_col]:
                        continue
                    parents[findParent((i, j))] = findParent((new_row, new_col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    findParent((i, j))

        return max(Counter(parents.values()).values()) if parents else 0
