# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def getWays(idx):
            if idx >= len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx == len(s) - 1:
                return 1
            
            ways = getWays(idx + 1)
            if int(s[idx] + s[idx + 1]) <= 26:
                ways += getWays(idx + 2)
                
            return ways
        
        return getWays(0)
    
