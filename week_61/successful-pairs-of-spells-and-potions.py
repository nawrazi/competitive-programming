# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        
        for spell in spells:
            pairs.append(len(potions) - bisect_left(potions, success / spell))
            
        return pairs
    
