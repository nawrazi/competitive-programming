# https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
            
        total = 0
        for _ in range(len(grid[0])):
            cur = 0
            for row in grid:
                cur = max(cur, row.pop())
            total += cur
            
        return total
    
