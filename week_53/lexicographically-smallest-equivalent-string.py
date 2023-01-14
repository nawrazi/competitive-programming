# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parents = {char: char for char in ascii_lowercase}
        
        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 > parent2:
                parent1, parent2 = parent2, parent1
                
            if parent1 != parent2:
                parents[parent2] = parent1
                
        for a, b in zip(s1, s2):
            union(a, b)
            
        return ''.join(find(char) for char in baseStr)
    
