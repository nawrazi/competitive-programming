# https://leetcode.com/problems/sum-of-matrix-after-queries/description/

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        seen = [set(), set()]
        total = 0
        
        for kind, index, val in reversed(queries):
            if index not in seen[kind]:
                total += val * (n - len(seen[1 - kind]))
                seen[kind].add(index)
        
        return total
    
