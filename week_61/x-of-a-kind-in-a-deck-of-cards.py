# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) > 1
    
