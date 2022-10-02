# https://leetcode.com/problems/integer-replacement/

class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def getSteps(num):
            if num == 1:
                return 0
            
            if num % 2 == 0:
                return 1 + getSteps(num // 2)
            else:
                return 1 + min(getSteps(num + 1), getSteps(num - 1))
            
        return getSteps(n)
    
