from heapq import *

class DisjointSet:
    def __init__(self, np):
        self.parents = [-1 for _ in range(np + 1)]
        self.extras = 0

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
        else:
            self.extras += 1

        heap = self.parents.copy()
        heapify(heap)

        max_cons = 0
        for i in range(self.extras + 1):
            max_cons += abs(heappop(heap))

        print(max_cons - 1)


np, t = [int(i) for i in input().split()]
dj = DisjointSet(np)
for _ in range(t):
    p1, p2 = [int(i) for i in input().split()]
    dj.union(p1, p2)
