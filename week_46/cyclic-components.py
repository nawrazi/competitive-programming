# https://codeforces.com/gym/411140/problem/B

n, e = [int(i) for i in input().split()]
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

indeg = [0 for _ in range(n + 1)]
edges = []

for _ in range(e):
    edges.append([int(i) for i in input().split()])
    
for n1, n2 in edges:
    union(n1, n2)
    indeg[n1] += 1
    indeg[n2] += 1
    
count = [0 for _ in range(n + 1)]
for n1, n2 in edges:
    parent = find(n1)
    count[parent] += 1
    
acyclic = set()
for i in range(1, n + 1):
    if indeg[i] <= 1:
        parent = find(i)
        acyclic.add(parent)
        
cyclic = 0
for i, p in enumerate(parents[1:], 1):
    if p < 0 and i not in acyclic and count[i] == -p:
        cyclic += 1
        
print(cyclic)
