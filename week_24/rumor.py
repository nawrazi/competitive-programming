class DisjointSet:
    def __init__(self, np):
        self.parents = [-1 for _ in range(np + 1)]
        self.extras = 0
        self.costs = [0]

    def find(self, node):
        if self.parents[node] < 0:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)

        if self.costs[parent1] > self.costs[parent2]:
            parent1, parent2 = parent2, parent1

        if parent1 != parent2:
            self.parents[parent1] += self.parents[parent2]
            self.parents[parent2] = parent1

    def solve(self):
        total = 0
        for i in range(1, len(self.parents)):
            if self.parents[i] < 0:
                total += self.costs[i]

        print(total)


np, f = [int(i) for i in input().split()]
costs = [int(i) for i in input().split()]
dj = DisjointSet(np)
dj.costs += costs

for _ in range(f):
    f1, f2 = [int(i) for i in input().split()]
    dj.union(f1, f2)

dj.solve()
