# https://leetcode.com/problems/similar-string-groups/description/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parents = [-1 for _ in range(len(strs))]
        
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
        
        def similar(word1, word2):
            diff = 0
            for c1, c2 in zip(word1, word2):
                diff += c1 != c2
            return diff == 0 or diff == 2
        
        for idx1, word1 in enumerate(strs):
            for idx2, word2 in enumerate(strs):
                if similar(word1, word2):
                    union(idx1, idx2)
        
        return sum(1 for p in parents if p < 0)
    
