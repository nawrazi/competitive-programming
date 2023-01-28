# https://codeforces.com/gym/424201/problem/B

from collections import deque

def valid(grid, sr, sc):
    directions = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
    inBound = lambda r,c : 0<=r<len(grid) and 0<=c<len(grid[0])
    area = 0
    minr, maxr = sr, sr
    minc, maxc = sc, sc
    q = deque([(sr, sc)])
    seen = {(sr, sc)}
    
    while q:
        row, col = q.popleft()
        area += 1
        minr = min(minr, row)
        minc = min(minc, col)
        maxr = max(maxr, row)
        maxc = max(maxc, col)
        
        if area > 3:
            return False
        
        for x, y in directions:
            nr, nc = row + x, col + y
            if inBound(nr, nc) and (nr, nc) not in seen and grid[nr][nc] == '*':
                q.append((nr, nc))
                seen.add((nr, nc))
                
    return area == 3 and abs(maxr - minr) == 1 and abs(maxc - minc) == 1

for _ in range(int(input())):
    r, c = [int(i) for i in input().split()]
    grid = []
    
    for _ in range(r):
        grid.append(list(input()))
        
    for row in range(r):
        for col in range(c):
            if grid[row][col] == '*' and not valid(grid, row, col):
                print('NO')
                break
        else:
            continue
        break
    else:
        print('YES')
        
