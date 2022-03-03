# https://leetcode.com/problems/number-of-enclaves/submissions/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def findIslands():
            nonlocal islands
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col]==1:
                        islands+=1

        def findNonIslands(row,col):
            grid[row][col] = 0

            for x,y in directions:
                new_row = row+x
                new_col = col+y

                if inBound(new_row,new_col) and grid[new_row][new_col] == 1:
                    findNonIslands(new_row,new_col)

        islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inBound = lambda r,c : 0 <= r < len(grid) and 0 <= c < len(grid[0])

        for row in range(len(grid)):
            for col in (0,len(grid[0])-1):
                if grid[row][col]==1:
                    findNonIslands(row,col)

        for col in range(len(grid[0])):
            for row in (0,len(grid)-1):
                if grid[row][col]==1:
                    findNonIslands(row,col)

        findIslands()

        return islands
