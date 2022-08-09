# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[r])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        heap = [(0, 0, 0)]
        best_cost = {(0,0): 0}
        
        while heap:
            cost, row, col = heappop(heap)
            
            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                return cost
            
            for x, y in directions:
                r, c = row + x, col + y
                if not inBound(r, c):
                    continue
                nex_cost = cost + grid[r][c]
                if (r, c) not in best_cost or nex_cost < best_cost[(r, c)]:
                    heappush(heap, (nex_cost, r, c))
                    best_cost[(r, c)] = nex_cost
                    
