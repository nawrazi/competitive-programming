# https://codeforces.com/gym/419372/problem/D

from collections import deque, defaultdict

b, c = [int(i) for i in input().split()]
graph = [[] for _ in range(b + 1)]
indeg = [0 for _ in graph]

for _ in range(c):
    u, v = [int(i) for i in input().split()]
    graph[u].append(v)
    graph[v].append(u)
    indeg[u] += 1
    indeg[v] += 1
    
q = deque()
for n, i in enumerate(indeg):
    if i == 1:
        q.append((n, 0))
        
levels = defaultdict(list)

while q:
    node, lvl = q.popleft()
    levels[lvl].append(node)
    
    for ngh in graph[node]:
        indeg[ngh] -= 1
        if indeg[ngh] == 1:
            q.append((ngh, lvl + 1))
            
m = (0, 0)
for lvl, nodes in levels.items():
    m = max(m, (lvl, nodes[0]))
    
q.clear()
vis = {m[1]}
cur = 10
for ngh in graph[m[1]]:
    q.append((ngh, cur, 1))
    vis.add(ngh)
    cur += 10
    
l = defaultdict(int)
while q:
    node, grp, lvl = q.popleft()
    l[grp] = max(l[grp], lvl)
    
    for ngh in graph[node]:
        if ngh not in vis:
            q.append((ngh, grp, lvl + 1))
            vis.add(ngh)
            
s = sorted(l.values())
if len(s) <= 1:
    print(1)
else:
    print(s[-1] + s[-2])
    
