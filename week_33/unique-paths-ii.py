# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        inBound = lambda r, c : 0 <= r < m and 0 <= c < n
        directions = [(0, 1), (1, 0)]
        
        @cache
        def getWays(row, col):
            if obstacleGrid[row][col] == 1:
                return 0
            
            if row == m - 1 and col == n - 1:
                return 1
            
            ways = 0
            for x, y in directions:
                r, c = row + x, col + y
                if inBound(r, c):
                    ways += getWays(r, c)
                
            return ways
            
        return getWays(0, 0)
    
