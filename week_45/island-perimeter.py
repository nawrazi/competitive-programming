# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[row])
        neighbors = lambda r, c: [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]
        perimeter = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    for r, c in neighbors(row, col):
                        if not inBound(r, c) or grid[r][c] == 0:
                            perimeter += 1
                            
        return perimeter
    
