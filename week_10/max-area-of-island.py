# https://leetcode.com/problems/max-area-of-island/submissions/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def getArea(row,col):
            area = 1
            visited.add((row,col))
            for x,y in directions:
                new_row, new_col = row+x, col+y
                if inBound(new_row,new_col) and unseenLand(new_row,new_col):
                    area+=getArea(new_row,new_col)

            return area

        max_area = 0
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        inBound = lambda r, c : 0<=r<len(grid) and 0<=c<len(grid[0])
        unseenLand = lambda r, c : grid[r][c] == 1 and (r,c) not in visited

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    area = getArea(row,col)
                    max_area = max(max_area, area)

        return max_area
