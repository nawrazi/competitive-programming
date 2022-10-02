# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def getWays(total, dice):
            if total == target:
                return 1 if dice == n else 0
            elif dice == n:
                return 0
            
            ways = 0
            for i in range(1, k + 1):
                if total + i <= target:
                    ways += getWays(total + i, dice + 1)
                    
            return ways
        
        mod = (10 ** 9) + 7
        return getWays(0, 0) % mod
    
