# https://leetcode.com/problems/domino-and-tromino-tiling/description/

class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def arrange(col, half):
            if col >= n + 1:
                return col == n + 1 and not half
            
            if half:
                return arrange(col + 1, True) + arrange(col + 2, False)
            
            vertical = arrange(col + 1, False)
            horizontal = arrange(col + 2, False)
            tromino = 2 * arrange(col + 1, True)
            
            return (vertical + horizontal + tromino) % mod
        
        mod = pow(10, 9) + 7
        return arrange(1, False)
    
