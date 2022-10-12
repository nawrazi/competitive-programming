# https://codeforces.com/gym/403303/problem/E

from collections import deque

n, m, k = [int(n) for n in input().split()]
grid = []
for _ in range(n):
    grid.append(list(input()))

q = deque()
seen = set()
d = [(0,1), (0,-1), (1,0), (-1,0)]
e = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            if not q:
                q.append((i, j))
                seen.add((i, j))
            e += 1

while q:
    r, c = q.popleft()
    if e == k:
        break
    grid[r][c] = 'X'
    e -= 1

    for x, y in d:
        nr, nc = r + x, c + y
        if (nr, nc) not in seen and 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.':
            q.append((nr, nc))
            seen.add((nr, nc))

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            grid[i][j] = 'X'
        elif grid[i][j] == 'X':
            grid[i][j] = '.'

for i in range(n):
    print(''.join(grid[i]))
    
