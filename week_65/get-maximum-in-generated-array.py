# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        @cache
        def getVal(n):
            if n <= 1:
                return n
            
            if n % 2 == 0:
                return getVal(n // 2)
            
            return getVal(n // 2) + getVal((n // 2) + 1)
        
        return max(getVal(i) for i in range(n + 1))
    
