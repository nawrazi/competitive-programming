# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        inBound = lambda r, c: 0 <= r < len(maze) and 0 <= c < len(maze[r])
        
        queue = deque([(*entrance, 0)])
        seen = {tuple(entrance)}
        
        while queue:
            row, col, dist = queue.popleft()
            
            for x, y in directions:
                nr, nc = row + x, col + y
                if (nr, nc) in seen:
                    continue
                if not inBound(nr, nc):
                    if dist > 0:
                        return dist
                elif maze[nr][nc] == '.':
                    queue.append((nr, nc, dist + 1))
                    seen.add((nr, nc))
                    
        return -1
    
