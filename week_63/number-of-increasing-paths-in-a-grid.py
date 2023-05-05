# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        @cache
        def search(row, col):
            paths = 1
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                r, c = row + x, col + y
                if not inBound(r, c) or grid[row][col] >= grid[r][c]:
                    continue
                paths += search(r, c)
            return paths % mod
        
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[r])
        paths = 0
        mod = pow(10, 9) + 7
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                paths += search(r, c)
                
        return paths % mod
    
