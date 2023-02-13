# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        inBound = lambda r, c: 0 <= r < n and 0 <= c < n
        queue = deque([(0, 0, 1)])
        seen = {(0, 0)}
        
        while queue:
            row, col, length = queue.popleft()
            
            if row == col == n - 1:
                return length
            
            for x, y in directions:
                nr, nc = row + x, col + y
                if (nr, nc) not in seen and inBound(nr, nc) and grid[nr][nc] == 0:
                    queue.append((nr, nc, length + 1))
                    seen.add((nr, nc))
                    
        return -1
    
