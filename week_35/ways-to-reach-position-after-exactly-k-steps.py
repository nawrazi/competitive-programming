# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def getWays(pos, steps):
            if pos == endPos and steps == 0:
                return 1
            
            if abs(pos - endPos) > steps:
                return 0
            
            return getWays(pos + 1, steps - 1) + getWays(pos - 1, steps - 1)
        
        mod = (10 ** 9) + 7
        return getWays(startPos, k) % mod
    
