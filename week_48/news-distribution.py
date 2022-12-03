# https://codeforces.com/gym/413954/problem/A

n, m = [int(i) for i in input().split()]
parents = [-1 for _ in range(n + 1)]

def find(node):
    if parents[node] < 0:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(node1, node2):
    parent1, parent2 = find(node1), find(node2)
    
    if parents[parent1] > parents[parent2]:
        parent1, parent2 = parent2, parent1
        
    if parent1 != parent2:
        parents[parent1] += parents[parent2]
        parents[parent2] = parent1

for _ in range(m):
    g, *grp = [int(i) for i in input().split()]
    for i in range(1, g):
        union(grp[0], grp[i])
        
ans = []
for i in range(1, n + 1):
    ans.append(-parents[find(i)])
    
print(*ans)
