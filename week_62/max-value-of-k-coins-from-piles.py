# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def maxValue(k, pile):
            if k == 0:
                return 0
            
            if pile >= len(piles):
                return -inf
            
            max_val = maxValue(k, pile + 1)
            for i in range(len(piles[pile])):
                val = piles[pile][i] + maxValue(k - i - 1, pile + 1)
                max_val = max(max_val, val)
                
            return max_val
        
        for pile in piles:
            for i in range(1, len(pile)):
                pile[i] += pile[i - 1]
                
        return maxValue(k, 0)
    
