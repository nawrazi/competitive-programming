# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def findParent(node):
            if node not in parents or parents[node] == node:
                parents[node] = node
                return node
            parent = findParent(parents[node])
            parents[node] = parent
            return parent

        parents = {}
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inBound = lambda r, c : 0 <= r < len(grid) and 0 <= c < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                for x, y in directions:
                    new_row, new_col = i + x, j + y
                    if inBound(new_row, new_col) and grid[new_row][new_col] == "1":
                        parents[findParent((i,j))] = findParent((new_row, new_col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    findParent((i, j))

        return len(set(parents.values()))
