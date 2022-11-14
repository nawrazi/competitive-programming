# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        group = [-1 for _ in stones]
        
        def find(node):
            if group[node] < 0:
                return node
            group[node] = find(group[node])
            return group[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if group[parent1] > group[parent2]:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                group[parent1] += group[parent2]
                group[parent2] = parent1
                
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for idx, (row, col) in enumerate(stones):
            rows[row].append(idx)
            cols[col].append(idx)
            
        for row in rows.values():
            for i in range(len(row) - 1):
                union(row[i], row[i + 1])
                
        for col in cols.values():
            for i in range(len(col) - 1):
                union(col[i], col[i + 1])
                
        removed = 0
        for member in group:
            if member < 0:
                removed += abs(member) - 1
                
        return removed
    
