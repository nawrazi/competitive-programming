# https://codeforces.com/gym/407211/problem/E

from collections import deque

m, n = [int(i) for i in input().split()]
grid = []
for _ in range(m):
    grid.append(list(input()))
    
seen = set()
drn = [(1,0), (-1,0), (0,1), (0,-1)]
in_bound = lambda r, c : 0 <= r < m and 0 <= c < n
size = {}

def bfs(sr, sc, comp):
    q = deque([(sr, sc)])
    cells = 0
    while q:
        r, c = q.popleft()
        cells += 1
        grid[r][c] = comp
        for x, y in drn:
            nr, nc = r + x, c + y
            if in_bound(nr, nc) and grid[nr][nc] != '*' and (nr, nc) not in seen:
                q.append((nr, nc))
                seen.add((nr, nc))
                
    size[comp] = cells
    
comp = 0
for r in range(m):
    for c in range(n):
        if grid[r][c] == '.' and (r, c) not in seen:
            seen.add((r, c))
            bfs(r, c, comp)
            comp += 1
            
seen = set()
for r in range(m):
    for c in range(n):
        a = 1
        if grid[r][c] == '*':
            for x, y in drn:
                nr, nc = r + x, c + y
                if in_bound(nr, nc) and grid[nr][nc] != '*' and grid[nr][nc] not in seen:
                    a += size[grid[nr][nc]]
                    seen.add(grid[nr][nc])
            print(a % 10, end='')
        else:
            print('.', end='')
        seen.clear()
    print()
    
