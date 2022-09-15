# https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        dishes = []
        bar = 0
        for d in reversed(sorted(satisfaction)):
            if d >= 0 or bar + d > 0:
                dishes.append(d)
                bar += d
                
        return sum((i + 1) * d for i, d in enumerate(reversed(dishes)))
    
