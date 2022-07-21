# https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars = 0
        for cost in costs:
            coins -= cost
            if coins < 0:
                break
            bars += 1
            
        return bars
    
