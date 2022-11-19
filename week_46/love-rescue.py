# https://codeforces.com/gym/411140/problem/C

parents = [-1 for i in range(26)]

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

input()
s1 = input()
s2 = input()

spells = []
for c1, c2 in zip(s1, s2):
    if union(ord(c1) - ord('a'), ord(c2) - ord('a')):
        spells.append([c1, c2])
        
print(len(spells))
for s in spells:
    print(*s)
    
