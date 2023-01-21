# https://leetcode.com/problems/score-after-flipping-matrix/description/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        score = 0
        
        for row in range(m):
            if grid[row][0] == 0:
                for col in range(n):
                    grid[row][col] ^= 1
        
        for col in range(n):
            ones = 0
            for row in range(m):
                ones += grid[row][col]
            
            if ones < len(grid) / 2:
                for row in range(m):
                    grid[row][col] ^= 1
            
            for row in range(m):
                score += grid[row][col] * pow(2, (n - col - 1))
            
        return score
    
