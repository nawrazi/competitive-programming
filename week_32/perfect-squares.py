# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, ceil(sqrt(n + 1)))]
        
        @lru_cache(None)
        def getSquares(amount):
            if amount == 0:
                return 0
            
            min_squares = inf
            for num in squares:
                if amount < num:
                    break
                min_squares = min(min_squares, 1 + getSquares(amount - num))
            
            return min_squares
        
        return getSquares(n)
    
