# https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        inBound = lambda r, c: 0 <= r < n and 0 <= c < n
        heap = []
        best = {}
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    heappush(heap, (0, row, col))
        
        while heap:
            dist, row, col = heappop(heap)
            
            for x, y in directions:
                nr, nc = row + x, col + y
                if inBound(nr, nc) and grid[nr][nc] == 0 and dist + 1 < best.get((nr, nc), inf):
                    heappush(heap, (dist + 1, nr, nc))
                    best[(nr, nc)] = dist + 1
        
        return max(best.values()) if best else -1
    
