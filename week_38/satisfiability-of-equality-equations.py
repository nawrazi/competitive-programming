# https://leetcode.com/problems/satisfiability-of-equality-equations/

class DisjointSet:
    def __init__(self, total):
        self.parents = [-1 for _ in range(total)]

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

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        idx = {}
        i = 0
        for eq in equations:
            a, b = max(eq.split('=='), eq.split('!='), key = lambda x: len(x))
            if a not in idx:
                idx[a] = i
                i += 1
            if b not in idx:
                idx[b] = i
                i += 1
                
        dj = DisjointSet(i)
        opp = []
        
        for eq in equations:
            if '==' in eq:
                a, b = eq.split('==')
                dj.union(idx[a], idx[b])
            else:
                a, b = eq.split('!=')
                opp.append((idx[a], idx[b]))
                
        for a, b in opp:
            if dj.find(a) == dj.find(b):
                return False
            
        return True
    
