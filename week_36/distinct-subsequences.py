# https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def getWays(cur, targ):
            if cur == len(s):
                return 0
            
            ways = 0
            if s[cur] == t[targ]:
                if targ == len(t) - 1:
                    ways += 1
                else:
                    ways += getWays(cur + 1, targ + 1)
                
            return ways + getWays(cur + 1, targ)
                
        return getWays(0, 0)
    
