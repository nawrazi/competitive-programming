# https://leetcode.com/problems/number-of-ways-to-earn-points/description/

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        @cache
        def getWays(idx, target):
            if idx >= len(types):
                return target == 0
            
            count, marks = types[idx]
            ways = 0
            while target >= 0 and count >= 0:
                ways += getWays(idx + 1, target)
                target -= marks
                count -= 1
                
            return ways % mod
        
        mod = pow(10, 9) + 7
        return getWays(0, target)
    
