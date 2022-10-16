# https://codeforces.com/group/b5GBy1CJ0d/contest/368852/problem/E

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    par = int(input())
    graph[par].append(i + 2)

def dfs(node):
    if not graph[node]:
        return True, 0

    leafs = 0
    depth = 0
    for c in graph[node]:
        val, dep = dfs(c)
        if not val:
            return False, 0
        if dep == 0:
            leafs += 1
        depth = max(depth, dep + 1)
    
    return leafs >= 3, depth

print('Yes' if dfs(1)[0] else 'No')
