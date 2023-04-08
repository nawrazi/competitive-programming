# https://codeforces.com/problemset/problem/1020/B

n = int(input())
graph = [int(n) - 1 for n in input().split()]

def search(node):
    while node not in seen:
        seen.add(node)
        node = graph[node]
    return node

res = []
for i in range(n):
    seen = set()
    res.append(search(i) + 1)
    
print(*res)
