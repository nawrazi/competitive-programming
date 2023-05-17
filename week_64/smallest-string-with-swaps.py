# https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parents = [-1 for _ in range(len(s))]
        
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
                
        for a, b in pairs:
            union(a, b)
            
        groups = defaultdict(list)
        for idx in range(len(s)):
            groups[find(idx)].append(s[idx])
            
        for parent in groups:
            groups[parent].sort(reverse=True)
            
        result = []
        for idx in range(len(s)):
            par = find(idx)
            result.append(groups[par].pop())
            
        return ''.join(result)
    
