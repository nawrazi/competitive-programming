# https://codeforces.com/gym/403606/problem/B

from collections import defaultdict, deque

n, f = [int(i) for i in input().split()]
costs = [0] + [int(i) for i in input().split()]
graph = defaultdict(list)

for _ in range(f):
    f1, f2 = [int(i) for i in input().split()]
    graph[f1].append(f2)
    graph[f2].append(f1)

def bfs(start):
    chp = float('inf')
    q = deque([start])

    while q:
        cur = q.popleft()
        seen.add(cur)
        chp = min(chp, costs[cur])

        for nex in graph[cur]:
            if nex not in seen:
                q.append(nex)

    return chp

seen = set()
total = 0
for i in range(1, n + 1):
    if i not in seen:
        total += bfs(i)

print(total)
