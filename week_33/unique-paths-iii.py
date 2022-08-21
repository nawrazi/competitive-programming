# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        inBound = lambda r, c : 0 <= r < len(grid) and 0 <= c < len(grid[r])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        empty = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 0:
                    empty += 1
                if cell == 1:
                    start = (r, c)
        
        def backtrack(row, col, steps):
            if grid[row][col] == 2:
                self.ways += 1 if steps == empty + 1 else 0
                return
            
            for x, y in directions:
                r, c = row + x, col + y
                if not inBound(r, c) or (r, c) in seen or grid[r][c] == -1:
                    continue
                seen.add((r, c))
                backtrack(r, c, steps + 1)
                seen.remove((r, c))
        
        self.ways = 0
        seen = {start}
        backtrack(*start, 0)
        
        return self.ways
    
