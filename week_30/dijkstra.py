# https://codeforces.com/gym/393453/problem/D

from collections import defaultdict
from heapq import heappop, heappush

graph = defaultdict(set)

n, m = [int(i) for i in input().split()]
for _ in range(m):
    n1, n2, e = [int(i) for i in input().split()]
    graph[n1].add((n2, e))
    graph[n2].add((n1, e))

heap = [(0, 1)]
best = {1: 0}
parent = {1: None}
found = False

while heap:
    dis, node = heappop(heap)

    if node == n:
        path = []
        while parent[node]:
            path.append(node)
            node = parent[node]
        path.append(1)

        print(*reversed(path))
        found = True
        break

    for nex_node, nex_dis in graph[node]:
        tot_dis = dis + nex_dis
        if nex_node not in best or tot_dis < best[nex_node]:
            parent[nex_node] = node
            best[nex_node] = tot_dis
            heappush(heap, (tot_dis, nex_node))

if not found:
    print(-1)
