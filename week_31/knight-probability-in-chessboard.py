# https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2,-1), (-1,-2), (-1,2), (-2,1), (1,2), (2,1), (1,-2), (2,-1)]
        inBound = lambda r, c : 0 <= r < n and 0 <= c < n
        
        @cache
        def getSafe(r, c, m):
            if not inBound(r, c):
                return 0
            
            if m == k:
                return 1
            
            safe = 0
            for x, y in directions:
                safe += getSafe(r + x, c + y, m + 1)
                
            return safe
        
        return getSafe(row, column, 0) / (8 ** k)
    
