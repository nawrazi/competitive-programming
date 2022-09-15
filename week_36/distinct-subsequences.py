# https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def getWays(cur, targ):
            if targ == len(t):
                return 1
            if cur == len(s):
                return 0
            
            ways = getWays(cur + 1, targ)
            if s[cur] == t[targ]:
                ways += getWays(cur + 1, targ + 1)
                
            return ways
        
        return getWays(0, 0)
    
