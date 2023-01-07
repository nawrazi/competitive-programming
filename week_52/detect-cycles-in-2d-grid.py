# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def search(start_row, start_col):
            queue = deque([(start_row, start_col, -1)])
            
            while queue:
                row, col, last = queue.popleft()
                
                if (row, col) in visited:
                    return True
                else:
                    visited.add((row, col))
                    
                for i, (x, y) in enumerate(directions):
                    nr, nc = row + x, col + y
                    if i != opposite[last] and inBound(nr, nc) and grid[nr][nc] == grid[row][col]:
                        queue.append((nr, nc, i))
                        
            return False
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        opposite = {0: 3, 3: 0, 1: 2, 2: 1, -1: -1}
        visited = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and search(row, col):
                    return True
                
        return False
    
