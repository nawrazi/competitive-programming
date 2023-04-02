# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        mod = pow(10, 9) + 7
        
        def appleInRange(r1, c1, r2, c2):
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if pizza[r][c] == 'A':
                        return True
        
        @cache
        def countWays(row, col, k):
            if k == 1:
                return 1 if appleInRange(row, col, rows, cols) else 0
            
            count = 0
            found = False
            for r in range(row + 1, rows):
                found = found or appleInRange(row, col, r, cols)
                if found:
                    count += countWays(r, col, k - 1)
                    
            found = False
            for c in range(col + 1, cols):
                found = found or appleInRange(row, col, rows, c)
                if found:
                    count += countWays(row, c, k - 1)
                    
            return count % mod
        
        return countWays(0, 0, k)
    
