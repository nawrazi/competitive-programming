# https://codeforces.com/gym/404077/problem/D

from collections import defaultdict, deque

n = int(input())
cost = [0] + [int(n) for n in input().split()]
rooms = [int(n) for n in input().split()]

graph = defaultdict(list)
und = defaultdict(set)
indeg = defaultdict(int)
seen = set()
for i, r in enumerate(rooms):
    if i + 1 == r:
        continue
    graph[i+1].append(r)
    und[i+1].add(r)
    und[r].add(i+1)
    indeg[r] += 1

def bfs(start):
    isl = set()
    q = deque([start])

    while q:
        idx = q.popleft()
        isl.add(idx)

        for nex in und[idx]:
            if nex not in seen:
                q.append(nex)
                seen.add(nex)

    return isl

def topsort(isl):
    q = deque()
    cur_seen = set()
    last = [-1, []]
    top = set()

    for i in isl:
        if indeg[i] == 0:
            q.append((i, 0))

    while q:
        idx, lvl = q.popleft()
        top.add(idx)
        if lvl > last[0]:
            last = [lvl, [idx]]
        elif lvl == last[0]:
            last[1].append(idx)

        for nex in graph[idx]:
            indeg[nex] -= 1
            if indeg[nex] == 0 and nex not in cur_seen:
                q.append((nex, lvl + 1))
                cur_seen.add(nex)

    if len(top) == len(isl):
        c = float('inf')
        for l in last[1]:
            c = min(c, cost[l])
        return c
    else:
        cycs = []
        for r in isl:
            if r not in top:
                cycs.append(r)

        c = float('inf')
        for l in cycs:
            c = min(c, cost[l])
        return c

ans = 0
for i, r in enumerate(rooms):
    if i + 1 not in seen:
        isl = bfs(i + 1)
        ans += topsort(isl)

print(ans)
