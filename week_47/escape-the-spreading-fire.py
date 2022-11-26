# https://leetcode.com/problems/escape-the-spreading-fire/

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        inBound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        fire = [[inf for _ in range(cols)] for _ in range(rows)]
        
        queue = deque()
        seen = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col, 0))
                    seen.add((row, col))
                    
        while queue:
            row, col, time = queue.popleft()
            fire[row][col] = time
            
            for x, y in directions:
                nr, nc = row + x, col + y
                if inBound(nr, nc) and (nr, nc) not in seen and grid[nr][nc] == 0:
                    queue.append((nr, nc, time + 1))
                    seen.add((nr, nc))
                    
        def canReach(start):
            queue = deque([(0, 0, start)])
            seen = {(0, 0)}
            
            while queue:
                row, col, time = queue.popleft()
                if row == rows - 1 and col == cols - 1 and time <= fire[row][col]:
                    return True
                if time >= fire[row][col]:
                    continue
                
                for x, y in directions:
                    nr, nc = row + x, col + y
                    if inBound(nr, nc) and (nr, nc) not in seen and grid[nr][nc] == 0:
                        queue.append((nr, nc, time + 1))
                        seen.add((nr, nc))
        
        left, right = 0, pow(10, 9)
        best = -1
        while left <= right:
            mid = (left + right) // 2
            
            if canReach(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return best
    
