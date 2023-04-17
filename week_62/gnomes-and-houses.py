# https://www.eolymp.com/en/contests/21097/problems/229737

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    row = input().split()
    for j in range(i, n):
        if row[j] == '1':
            graph[i].append(j)
            graph[j].append(i)
            
visited = [False] * n
def dfs(node):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            
ans = 0
for node in range(n):
    if not visited[node]:
        dfs(node)
        ans += 1
        
print(ans)
