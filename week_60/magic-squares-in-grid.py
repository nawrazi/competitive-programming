# https://leetcode.com/problems/magic-squares-in-grid/description/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pos_diag = lambda r, c: grid[r-1][c-1] + grid[r+1][c+1]
        neg_diag = lambda r, c: grid[r-1][c+1] + grid[r+1][c-1]
        row = lambda r, c: grid[r][c] + grid[r][c-1] + grid[r][c+1]
        col = lambda r, c: grid[r][c] + grid[r-1][c] + grid[r+1][c]
        magic = 0
        
        def unique(r, c):
            nums = {grid[r][c]}
            for x, y in [(-1,-1), (0,-1), (-1,0), (0,1), (1,0), (1,1), (-1,1), (1,-1)]:
                nums.add(grid[r+x][c+y])
            return nums == {i for i in range(1, 10)}
        
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if not row(r, c) == row(r-1, c) == row(r+1, c):
                    continue
                if not col(r, c) == col(r, c-1) == col(r, c+1):
                    continue
                if pos_diag(r, c) == neg_diag(r, c) and unique(r, c):
                    magic += 1
                    
        return magic
    
