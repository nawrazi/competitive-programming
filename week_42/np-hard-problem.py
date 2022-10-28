# https://codeforces.com/problemset/problem/687/A

from collections import deque

n, m = [int(i) for i in input().split()]
graph = [set() for _ in range(n + 1)]
for _ in range(m):
    s, e = [int(i) for i in input().split()]
    graph[s].add(e)
    graph[e].add(s)
    
def bfs(start):
    q = deque([(start, 0)])
    color[start] = 0
    
    while q:
        node, col = q.popleft()
        
        for ngh in graph[node]:
            if color[ngh] == col:
                return False
            if ngh not in seen:
                q.append((ngh, 1 - col))
                color[ngh] = 1 - col
                seen.add(ngh)
                
    return True

color = [-1 for _ in range(n + 1)]
seen = set()
for node in range(1, n + 1):
    if color[node] == -1:
        if not bfs(node):
            print(-1)
            exit()
            
group = [[], []]
for node in range(1, n + 1):
    group[color[node]].append(node)
    
for grp in group:
    print(len(grp))
    print(*grp)
    
