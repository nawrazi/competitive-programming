# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        heap = [(0, 0, 0)]
        seen = {(0, 0): 0}
        
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        
        while heap:
            time, row, col = heappop(heap)
            
            if row == m - 1 and col == n - 1:
                return time
            
            for x, y in directions:
                r, c = row + x, col + y
                if not inBound(r, c):
                    continue
                    
                # moving to a cell with a lower value
                new_time = time + 1
                if grid[r][c] <= new_time and new_time < seen.get((r, c), inf):
                    heappush(heap, (new_time, r, c))
                    seen[(r, c)] = new_time
                    
                # waiting and then moving to a cell with a higher value
                new_time = grid[r][c] + 1 - ((grid[r][c] - time) % 2)
                if grid[r][c] > time + 1 and new_time < seen.get((r, c), inf):
                    heappush(heap, (new_time, r, c))
                    seen[(r, c)] = new_time
                    
        return -1
    
