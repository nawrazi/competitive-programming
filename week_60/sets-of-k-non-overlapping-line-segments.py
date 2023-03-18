# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/description/

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def getWays(pos, used, line):
            if pos == n - 1:
                return used == k
            
            if used > k:
                return 0
            
            old = getWays(pos + 1, used, True) if line else 0
            new = getWays(pos + 1, used + 1, True)
            skip = getWays(pos + 1, used, False)
            return (old + new + skip) % mod
        
        mod = pow(10, 9) + 7
        return getWays(0, 0, False)
    
