# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def getChange(needed):
            if needed == 0:
                return 0
            if needed < 0:
                return inf
            
            change = inf
            for coin in coins:
                change = min(change, getChange(needed - coin))
                
            return change + 1
        
        return getChange(amount) if getChange(amount) != inf else -1
    
