# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        @cache
        def getSet(current):
            if current == num:
                return 0
            
            min_set = inf
            for i in range(k, num + 1, 10):
                if current + i <= num and i != 0:
                    min_set = min(min_set, 1 + getSet(current + i))
                    
            return min_set
        
        min_set = getSet(0)
        return min_set if min_set != inf else -1
    
