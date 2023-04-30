# https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        queue = deque()
        seen = set()
        full = 0
        
        for row in range(m):
            for col in range(n):
                cell = grid[row][col]
                if cell == '@':
                    queue.append((row, col, 0, 0))
                    seen.add((row, col, 0))
                if cell.islower():
                    full |= 1 << (ord(cell) - ord('a'))
                    
        while queue:
            row, col, keys, moves = queue.popleft()
            
            if keys == full:
                return moves
            
            for x, y in directions:
                r, c = row + x, col + y
                if not (0 <= r < m and 0 <= c < n) or grid[r][c] == '#':
                    continue
                    
                cell = grid[r][c]
                if cell.isupper() and not keys & 1 << (ord(cell) - ord('A')):
                    continue
                    
                new_keys = keys
                if cell.islower():
                    new_keys |= 1 << (ord(cell) - ord('a'))
                    
                if (r, c, new_keys) not in seen:
                    queue.append((r, c, new_keys, moves + 1))
                    seen.add((r, c, new_keys))
                    
        return -1
    
