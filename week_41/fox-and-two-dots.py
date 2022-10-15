# https://codeforces.com/gym/404077/problem/C

from collections import defaultdict, deque

def solve():
    m, n = [int(n) for n in input().split()]
    grid = []
    for _ in range(m):
        grid.append(list(input()))

    def bfs(ri, ci):
        isl = []
        color = grid[ri][ci]
        q = deque([(ri, ci)])

        while q:
            r, c = q.popleft()
            if (r, c) not in seen:
                seen.add((r, c))
                isl.append((r, c))
            else:
                continue

            for x, y in dxn:
                nr, nc = r + x, c + y
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if (nr, nc) not in seen and grid[nr][nc] == color:
                    q.append((nr, nc))

        return isl

    def topsort(isl):
        size = 0
        q = deque()
        cur_seen = set()

        for r, c in isl:
            if indeg[(r, c)] <= 1:
                q.append((r, c))

        while q:
            r, c = q.popleft()
            size += 1
            
            for nr, nc in graph[(r, c)]:
                indeg[(nr, nc)] -= 1
                if indeg[(nr, nc)] == 1 and (nr, nc) not in cur_seen:
                    q.append((nr, nc))
                    cur_seen.add((nr, nc))

        return size

    seen = set()
    dxn = [(0,1), (0,-1), (1,0), (-1,0)]
    graph = defaultdict(list)
    indeg = defaultdict(int)

    for r in range(m):
        for c in range(n):
            for x, y in dxn:
                nr, nc = r + x, c + y
                if 0 <= nr < m and 0 <= nc < n and grid[r][c] == grid[nr][nc]:
                    graph[(r, c)].append((nr, nc))
                    indeg[(r, c)] += 1

    total = 0
    for r in range(m):
        for c in range(n):
            if (r, c) not in seen and indeg[(r, c)] <= 1:
                isl = bfs(r, c)
                t = topsort(isl)
                if len(isl) != t:
                    print('Yes')
                    return
                total += t

    print('No' if total == m * n else 'Yes')

solve()
