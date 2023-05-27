# https://leetcode.com/problems/tallest-billboard/description/

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @cache
        def tallest(idx, diff):
            if idx >= len(rods):
                return 0 if diff == 0 else -inf
            
            pickL = rods[idx] + tallest(idx + 1, diff + rods[idx])
            pickR = tallest(idx + 1, diff - rods[idx])
            dont = tallest(idx + 1, diff)
            
            return max(pickL, pickR, dont)
        
        return tallest(0, 0)
    
