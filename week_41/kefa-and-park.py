# https://codeforces.com/gym/404902/problem/C

from collections import deque

n, m = [int(i) for i in input().split()]
cats = [int(i) for i in input().split()]
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    s, e = [int(i) for i in input().split()]
    graph[s].append(e)
    graph[e].append(s)

q = deque([(1, 0, 0)])
safe = 0
while q:
    node, cur_cats, par = q.popleft()

    if cats[node - 1] == 1:
        nex_cats = cur_cats + 1
    else:
        nex_cats = 0

    if nex_cats > m:
        continue

    if len(graph[node]) == 1 and par != 0:
        safe += 1
        continue

    for ngh in graph[node]:
        if ngh != par:
            q.append((ngh, nex_cats, node))

print(safe)
