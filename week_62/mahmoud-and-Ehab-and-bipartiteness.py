# https://codeforces.com/problemset/problem/862/b

n = int(input())
colors = [-1 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = [int(n) for n in input().split()]
    graph[u].append(v)
    graph[v].append(u)
    
stack = [(1, 1)]
while stack:
    node, col = stack.pop()
    if colors[node] == -1:
        colors[node] = col
        for ngh in graph[node]:
            stack.append((ngh, 1 - col))
            
print(colors.count(1) * colors.count(0) - (n - 1))
