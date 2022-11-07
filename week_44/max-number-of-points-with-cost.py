# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def fillRow(self, row, points):
        cols = len(points[row])
        if row > 0:
            for col in range(cols):
                points[row][col] += points[row - 1][col]
                
        cur_best = 0
        for col in range(cols):
            points[row][col] = max(points[row][col], cur_best)
            cur_best = points[row][col] - 1
            
        cur_best = 0
        for col in range(cols - 1, -1, -1):
            points[row][col] = max(points[row][col], cur_best)
            cur_best = points[row][col] - 1
            
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        for row in range(rows):
            self.fillRow(row, points)
        
        return max(points[-1])
    
