# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        mask = 1
        
        for _ in range(32):
            av, bv, cv = a & mask, b & mask, c & mask
            flips += (1 + (av & bv != 0)) * (cv == 0) if av | bv else cv != 0
            mask <<= 1
        
        return flips
    
