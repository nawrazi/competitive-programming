# https://codeforces.com/gym/404077/problem/B

from collections import defaultdict, deque

def solve():
    t = int(input())
    for _ in range(t):
        input()
        n, k = [int(n) for n in input().split()]
        a = n
        graph = defaultdict(list)
        indeg = [0 for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = [int(n) for n in input().split()]
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1

        q = deque()
        for i, n in enumerate(indeg[1:]):
            if n == 1:
                q.append((i + 1, 1))

        levels = defaultdict(int)
        seen = set()
        while q:
            node, lev = q.popleft()
            levels[lev] += 1

            for nex in graph[node]:
                if nex not in seen:
                    indeg[nex] -= 1
                    if indeg[nex] == 1:
                        q.append((nex, lev + 1))
                        seen.add(nex)

        ams = [0 for _ in range(len(levels) + 1)]
        for l, c in levels.items():
            ams[l] += c

        cur = 0
        for i in range(len(ams)):
            cur += ams[i]
            ams[i] = cur

        print(a - ams[k] if k < len(ams) else 0)

solve()
