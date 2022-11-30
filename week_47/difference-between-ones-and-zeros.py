# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = [[0, 0] for _ in range(len(grid))]
        cols = [[0, 0] for _ in range(len(grid[0]))]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                val = grid[row][col]
                rows[row][val] += 1
                cols[col][val] += 1
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ones = rows[row][1] + cols[col][1]
                zeros = rows[row][0] + cols[col][0]
                grid[row][col] = ones - zeros
                
        return grid
    
