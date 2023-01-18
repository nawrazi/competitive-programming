# https://leetcode.com/problems/increment-submatrices-by-one/description/

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        
        for r1, c1, r2, c2 in queries:
            matrix[r1][c1][1] += 1
            matrix[r2 + 1][c1][1] -= 1
            matrix[r1][c2 + 1][1] -= 1
            matrix[r2 + 1][c2 + 1][1] += 1
            
        for col in range(n):
            prefix = 0
            for row in range(n):
                prefix += matrix[row][col][1]
                matrix[row][col][0] += prefix
                
        for row in range(n):
            prefix = 0
            for col in range(n):
                prefix += matrix[row][col][0]
                matrix[row][col] = prefix
            matrix[row].pop()
            
        return matrix[:-1]
    
