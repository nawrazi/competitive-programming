# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        inBound = lambda r, c: 0 <= r < n and 0 <= c < n
        
        def search(row, col):
            queue.append((row, col, 0))
            grid[row][col] = 2
            for x, y in directions:
                r, c = row + x, col + y
                if inBound(r, c) and grid[r][c] == 1:
                    search(r, c)
                    
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    search(row, col)
                    break
            else:
                continue
            break
        
        while queue:
            row, col, dist = queue.popleft()
            
            for x, y in directions:
                r, c = row + x, col + y
                if not inBound(r, c):
                    continue
                    
                if grid[r][c] == 1:
                    return dist
                
                if grid[r][c] == 0:
                    queue.append((r, c, dist + 1))
                    grid[r][c] = 2
                    
