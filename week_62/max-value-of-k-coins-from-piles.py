# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def maxValue(k, pile):
            if k == 0:
                return 0
            
            if pile >= len(piles):
                return -inf
            
            val, max_val = 0, maxValue(k, pile + 1)
            for i in range(len(piles[pile])):
                val += piles[pile][i]
                max_val = max(max_val, val + maxValue(k - i - 1, pile + 1))
                
            return max_val
        
        return maxValue(k, 0)
    
