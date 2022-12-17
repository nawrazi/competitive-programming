# https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        max_sum = 0
        
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                cur_sum = grid[row][col]
                for x, y in directions:
                    cur_sum += grid[row + x][col + y]
                max_sum = max(max_sum, cur_sum)
                
        return max_sum
    
