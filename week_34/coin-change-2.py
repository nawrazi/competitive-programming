# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def getWays(base, needed):
            if needed == 0:
                return 1
            
            ways = 0
            for i in range(base, len(coins)):
                if needed - coins[i] >= 0:
                    ways += getWays(i, needed - coins[i])
                
            return ways
        
        return getWays(0, amount)
    
