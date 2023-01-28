# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/

class SummaryRanges:

    def __init__(self):
        self.parents = [-1 for _ in range(10001)]
        self.range = {i: (i, i) for i in range(10001)}
        self.added = set()

    def find(self, node):
        if self.parents[node] < 0:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        
        if parent1 == parent2:
            return
        
        if self.parents[parent1] > self.parents[parent2]:
            parent1, parent2 = parent2, parent1
            
        min1, max1 = self.range[parent1]
        min2, max2 = self.range[parent2]
        self.range[parent1] = (min(min1, min2), max(max1, max2))
        
        self.parents[parent1] += self.parents[parent2]
        self.parents[parent2] = parent1

    def addNum(self, value: int) -> None:
        self.added.add(value)
        if value + 1 in self.added:
            self.union(value, value + 1)
            
        if value - 1 in self.added:
            self.union(value, value - 1)

    def getIntervals(self) -> List[List[int]]:
        intervals = set()
        for value in self.added:
            intervals.add(self.range[self.find(value)])
            
        return sorted(intervals)
    
