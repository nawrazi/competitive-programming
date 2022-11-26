# https://codeforces.com/gym/412541/problem/C

n, o = [int(i) for i in input().split()]
cost = [int(i) for i in input().split()]

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
        return True
    
    return 0

offers = []
for _ in range(o):
    n1, n2, c = [int(i) for i in input().split()]
    offers.append((c, n1, n2))
    
for i in range(n):
    cost[i] = (cost[i], i + 1)
cost.sort()

for i in range(1, n):
    offers.append((cost[0][0] + cost[i][0], cost[0][1], cost[i][1]))
offers.sort()

total = 0
for c, n1, n2 in offers:
    if union(n1, n2):
        total += c
        
print(total)
