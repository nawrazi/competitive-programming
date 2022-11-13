# https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def getWays(length):
            if length > high:
                return 0
            
            ways = 1 if low <= length <= high else 0
            return (ways + getWays(length + zero) + getWays(length + one)) % mod
        
        mod = (10 ** 9) + 7
        return getWays(0) % mod
    
