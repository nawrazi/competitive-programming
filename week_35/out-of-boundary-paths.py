# https://leetcode.com/problems/out-of-boundary-paths/

class Solution: 
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n
        mod = (10 ** 9) + 7
        
        @cache
        def move(row, col, moved):
            if not inBound(row, col):
                return 1
            
            if moved == maxMove:
                return 0
            
            ways = 0
            for x, y in directions:
                ways += move(row + x, col + y, moved + 1)
            
            return ways
        
        return move(startRow, startColumn, 0) % mod
    
