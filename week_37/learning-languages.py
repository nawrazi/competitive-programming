# https://codeforces.com/gym/400361/problem/D

class DisjointSet:
    def __init__(self, np):
        self.parents = [-1 for _ in range(np + 1)]

    def find(self, node):
        if self.parents[node] < 0:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if self.parents[parent1] > self.parents[parent2]:
            parent1, parent2 = parent2, parent1

        if parent1 != parent2:
            self.parents[parent1] += self.parents[parent2]
            self.parents[parent2] = parent1

    def addZero(self, node):
        self.parents[node] = 0

    def solve(self):
        grps = 0
        zeros = 0
        for par in self.parents[1:]:
            if par == 0:
                zeros += 1
            if par < 0:
                grps += 1

        if grps: grps -= 1
        print(grps + zeros)


emp, l = [int(n) for n in input().split()]
dj = DisjointSet(emp)
lan = {i + 1: set() for i in range(l)}

for e in range(1, emp + 1):
    n, *spk = [int(n) for n in input().split()]
    if n == 0:
        dj.addZero(e)
        continue
    for i in spk:
        lan[i].add(e)
    for i in spk:
        for j in lan[i]:
            dj.union(e, j)
            
dj.solve()
